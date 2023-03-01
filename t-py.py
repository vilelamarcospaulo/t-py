import rumps

class TPyStatusBarApp(rumps.App):
    def __init__(self):
        super(TPyStatusBarApp, self).__init__("T-Py")
        self.menu = ["Lootbox", "Loot Sort"]

    @rumps.clicked("Lootbox")
    def lootbox_mode(self, _):
        rumps.alert("starting lootbox mode to hunt!")

    @rumps.clicked("Loot Sort")
    def loot_sort_mode(self, _):
        rumps.alert("starting loot sort mode!")


if __name__ == "__main__":
  TPyStatusBarApp().run()