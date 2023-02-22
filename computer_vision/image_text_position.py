import difflib
import re
import pytesseract

class ImageTextPosition():
  def __init__(self, conf = 50):
      self.conf = conf
      self.buffer = _BufferReader()
      
  def process_image(self, image):
    processed_data = pytesseract.image_to_data(image)

    for idx, line in enumerate(processed_data.split('\n')):
      if idx == 0:
        continue
      
      data = line.split()
      if len(data) != 12:
        continue

      conf, content = float(data[10]), data[11]
      if conf < self.conf:
        continue

      page, block, par, line, word = int(data[1]), int(data[2]), int(data[3]), int(data[4]), int(data[5])
      left, top, width, height = int(data[6]), int(data[7]), int(data[8]), int(data[9])

      id = [page, block, par, line, word]
      location = [left, top, width, height]

      self.buffer.process(id, location, content)

  def detect_text_position(self, text_list):
    result = []
    text_matcher = TextMatcher(text_list)

    for [text, loc] in self.buffer.flush():
      text = self._sanitize(text)
      match = text_matcher.check_text(text)
      # print(f'matched text {text} with key {match}')
      if match is None:
        continue
      
      print(f'matched text {text} with key {match}')
      result.append((match, loc))

    return result

  def flush(self): 
    return self.buffer.flush()

  def _sanitize(self, content: str):
    content = content.lower()
    content = re.sub('[^ 0-9a-zA-Z]+', '', content)
    return content.strip()

class _BufferReader:
  def __init__(self):
    self.id = None
    self.loc = None
    self.buffered = None
    self.lines = []

  def process(self, id, location, content):
    if self.id is None:
      self.id = id
      self.loc = location
      self.buffered = content

    elif self._same_block(id):
      self.buffered += ' ' + content

    else:
      self.flush()
      self.loc = location
      self.buffered = content

    self.id = id

  def flush(self):
    if not self.buffered is None:
      self.lines.append((self.buffered.strip(), self.loc))
      self.id = None
      self.loc = None
      self.buffered = None

    return self.lines

  def _same_block(self, id): 
    if self.id is None:
      return True

    return (self.id[0] == id[0] 
      and self.id[1] == id[1] 
      and self.id[2] == id[2] 
      and self.id[3] == id[3])


class TextMatcher:
  def __init__(self, texts, conf = 0.8) -> None:
    self.conf = conf
    self.texts = texts

  def check_text(self, text):
    for s in self.texts:
      ratio = self._calculate_diff_ratio(s, text)
      if ratio > self.conf:
        return s
  
  def _calculate_diff_ratio(self, a, b):
    return difflib.SequenceMatcher(None, a, b).ratio()