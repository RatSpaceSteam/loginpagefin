from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager

Builder.load_file('LoginPage.kv')

login_dict = {"us": ["peepee"], "ps": ["poopoo"]}

#registration_req = {}
#requirments for registration go in there ^^^
class LoginPageApp(App):
    def build(self):
        return LoginPageManager()

class LoginPageManager(ScreenManager):
    pass

class BoxLayoutExample(BoxLayout):
    pass

class Credentials(Screen):
    def answer_question(self, text):
        if self.ids.username.text.lower() in login_dict["us"] and self.ids.password.text.lower() in login_dict["ps"]:
            self.manager.current = "welcome"
            self.ids.test.text = ""
        else:
            self.manager.current = "credentials"
            self.ids.test.text = "Invalid Credentials"
            self.ids.test.font_size = 50
    def forward(self):
        self.manager.current = "newacc"

class NewAccount(Screen):
    pass

class Welcome(Screen):
    def forward(self):
        self.manager.current = "credentials"

if __name__ == "__main__":
    LoginPageApp().run()