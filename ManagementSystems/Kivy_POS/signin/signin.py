from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class SigninWindow(BoxLayout):
    bg = (158 / 255, 200 / 255, 98 / 255, 1)
    bg2 = (92 / 255, 114 / 255, 61 / 255, 1)
    btnColor = (32 / 255, 38 / 255, 52 / 255, 1)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_user(self):
        userField = self.ids.username_field
        pwdField = self.ids.pwd_field
        info = self.ids.info

        uname = userField.text
        passw = pwdField.text

        if uname == '' or passw == '':
            info.text = '[color=#A7194A]Username and/ or password required[/color]'
        else:
            if uname == 'admin' and passw == 'admin':
                info.text = '[color=#14852B]Authorised to Access System[/color]'

            else:
                info.text = '[color=#A7194A]Invalid Details[/color]'


class SigninApp(App):
    def build(self):
        return SigninWindow()


if __name__ == "__main__":
    sa = SigninApp()
    sa.run()
