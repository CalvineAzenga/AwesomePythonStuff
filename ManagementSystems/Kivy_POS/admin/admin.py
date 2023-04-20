from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
# from pymongo import MongoClient


class AdminWindow(BoxLayout):
    bg = (.06, .45, .45, 1)
    bg2 = (.06, .45, .45, 1)
    bg3 = (7 / 255, 1 / 255, 27 / 255, 1)
    color1 = (158 / 255, 200 / 255, 98 / 255)
    btnColor = (32 / 255, 38 / 255, 52 / 255, 1)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class AdminApp(App):
    def build(self):
        return AdminWindow()


if __name__ == "__main__":
    admin = AdminApp()
    admin.run()
