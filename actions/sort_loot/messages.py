import re
from computer_vision.image_text_position import ImageTextPosition, TextMatcher


def messages(image, possible_names):
    bottom_bar_height = 50
    messages_panel_height = 110

    messages_height = messages_panel_height + bottom_bar_height

    hImg, wImg = image.shape

    cropY = hImg - messages_height
    cropX = 0

    cropped = image[cropY:cropY + messages_height, cropX:cropX + wImg].copy()

    image_reader = ImageTextPosition()
    image_reader.process_image(cropped)

    item_names = []
    text_matcher = TextMatcher(possible_names)

    for text, _ in image_reader.flush():
        matches = re.search(
            r"You see ((a|an) )?(((?!that|\()([a-zA-Z]+)| )*)", text)
        if matches is None:
            continue

        text = matches.groups()[2]
        item_names.append(text)

    for item_name in reversed(item_names):
        item_name_match = text_matcher.check_text(item_name)
        print(f'{item_name} {item_name_match}')
        if item_name_match is None:
            continue

        return item_name_match
