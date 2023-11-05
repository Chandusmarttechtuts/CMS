from kivy.uix.screenmanager import Screen, ScreenManager

class LoginScreen(Screen):
    def login(self):
        username = self.ids.staffID_field.text
        password = self.ids.password_field.text

        # login logic
        if username == "admin" and password == "password":
            self.ids.login_message.text = "Login Successful"
            self.manager.current = "home"
        else:
            self.ids.login_message.text = "Login Failed, invalid details!"