from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager

Builder.load_file('LoginPage.kv')

class LoginPageApp(App):
    def build(self):
        return LoginPageManager()

class LoginPageManager(ScreenManager):
    pass

class BoxLayoutExample(BoxLayout):
    pass

class Credentials(Screen):
    def answer_question(self, bool):
        if bool:
            self.manager.current = "welcome"
        else:
            self.ids.test.text = "Invalid Credentials"
            self.manager.current = "credentials"
            self.ids.test.font_size = 50
class Welcome(Screen):
    def forward(self):
        self.manager.current = "credentials"

if __name__ == "__main__":
    LoginPageApp().run()