from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager

Builder.load_file('LoginPage.kv')

login_dict = {"us": ["peepee"], "ps": ["poopoo"]}
cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low = "abcdefghijklmnopqrstuvwxyz"
num = "1234567890"
spec = "~!@#$%^&*()?"
class LoginPageApp(App):
    def build(self):
        return LoginPageManager()

class LoginPageManager(ScreenManager):
    pass

class BoxLayoutExample(BoxLayout):
    pass

class Credentials(Screen):
    def answer_question(self, text):
        if self.ids.username.text in login_dict["us"] and self.ids.password.text in login_dict["ps"]:
            self.manager.current = "welcome"
            self.ids.test.text = ""
        else:
            self.manager.current = "credentials"
            self.ids.test.text = "Invalid Credentials"
            self.ids.test.font_size = 50
    def forward(self):
        self.manager.current = "newacc"
        self.ids.test.text = ""

class NewAccount(Screen):
    def reqdetect(self, text, list):
        for i in range(len(list)):
            for j in range(len(self.ids.newps.text)):
                if self.ids.newps.text[j] == list[i]:
                    return True
        return False
    def answer_question(self,text):
        if self.ids.newps.text != self.ids.newpsconf.text:
            self.ids.helper.text = "Passwords do not match"
        else:
            if self.reqdetect(text, cap) == False:
                self.ids.helper.text = "Passwords must include capital letter"
            else:
                if self.reqdetect(text, low) == False:
                    self.ids.helper.text = "Passwords must include lowercase letter"
                else:
                    if self.reqdetect(text, num) == False:
                        self.ids.helper.text = "Passwords must include number"
                    else:
                        if self.reqdetect(text, spec) == False:
                            self.ids.helper.text = "Passwords must include special character"
                        else:
                            login_dict["us"].append(self.ids.newus.text), login_dict["ps"].append(self.ids.newps.text)
                            self.ids.helper.text = ""
                            self.manager.current = "credentials"


class Welcome(Screen):
    def forward(self):
        self.manager.current = "credentials"

if __name__ == "__main__":
    LoginPageApp().run()