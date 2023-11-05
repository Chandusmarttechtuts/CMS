from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineAvatarIconListItem

class ChatbotScreen(Screen):
    def on_nav_bar_press(self, press_item):
        match press_item:
            case "arrow-left":
                print("back is clicked")
                self.manager.current = "home"
            case "home":
                print("Home is clicked")
                self.manager.current = "home"

    def on_buttontype_press(self,buttontype):
        match buttontype:
            case "manual_attendance":
                print("Going to manual attendance")
            case "send_alert":
                print("Alert is being send")
            case "attendance_percentage":
                print("Going to attendance percentage")
                self.manager.current = "Attendance_percentage"
            case _:
                print("default case")
    def send_message(self):
        user_message = self.ids.message_input.text.strip()
        if user_message:
            user_message_item = UserMessageListItem(text=user_message)
            self.ids.chat_container.add_widget(user_message_item)
            self.ids.message_input.text = ""

            bot_response = self.get_bot_response(user_message)
            bot_message_item = BotMessageListItem(text=bot_response)
            self.ids.chat_container.add_widget(bot_message_item)

    def get_bot_response(self, user_message):
        #logic for chatbot
        return "You said: " + user_message

class UserMessageListItem(OneLineAvatarIconListItem):
    pass

class BotMessageListItem(OneLineAvatarIconListItem):
    pass

