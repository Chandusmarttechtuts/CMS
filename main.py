from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.label import MDLabel
from kivy.metrics import dp




class WelcomeScreen(Screen):
    def on_enter(self):

        Clock.schedule_once(self.switch_to_login, 5)
    def switch_to_login(self, dt):

        self.manager.current = "login"
    def for_chatbot_screen(self):
        self.manager.current="chatbot"


class CMS(MDApp):
    # for Speed dial button

    # for year
    def Year_menu_open(self):
        Year_item = ["1st year", "2nd year", "3rd year", "4th year"]

        Year_menu_items = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.Year_menu_callback(x),
            } for i in Year_item
        ]
        self.Year_menu = MDDropdownMenu(
            caller=self.root.get_screen('attendance_filter').ids.year,
            items=Year_menu_items,
            width_mult=4,
        )
        self.Year_menu.open()

    def Year_menu_callback(self, text_item):
        self.root.get_screen('attendance_filter').ids.year.text = text_item
        self.Year_menu.dismiss()
        print(text_item)

    # for semester
    def Sem_menu_open(self):
        Sem_item = ["1st sem", "2nd sem"]

        Sem_menu_items = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.Sem_menu_callback(x),
            } for i in Sem_item
        ]
        self.Sem_menu = MDDropdownMenu(
            caller=self.root.get_screen('attendance_filter').ids.sem,
            items=Sem_menu_items,
            width_mult=4,
        )
        self.Sem_menu.open()

    def Sem_menu_callback(self, text_item):
        self.root.get_screen('attendance_filter').ids.sem.text = text_item
        self.Sem_menu.dismiss()
        print(text_item)

    # for branch
    def Branch_menu_open(self):
        Branch_item = ["CSE", "IT", "AIML", "CSE-DS", "CSE-CS", "CSE-BS", "ECE", "EEE", "MECH", "ROBOTICS", "CIVIL"]

        Branch_menu_items = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.Branch_menu_callback(x),
            } for i in Branch_item
        ]
        self.Branch_menu = MDDropdownMenu(
            caller=self.root.get_screen('attendance_filter').ids.branch,
            items=Branch_menu_items,
            width_mult=4,
        )
        self.Branch_menu.open()

    def Branch_menu_callback(self, text_item):
        self.root.get_screen('attendance_filter').ids.branch.text = text_item
        self.Branch_menu.dismiss()
        print(text_item)

    # for section
    def Sec_menu_open(self):
        Sec_item = ["A SEC", "B SEC", "C SEC", "D SEC", "E SEC", ]
        Sec_menu_items = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.Sec_menu_callback(x),
            } for i in Sec_item
        ]
        self.Sec_menu = MDDropdownMenu(
            caller=self.root.get_screen('attendance_filter').ids.section,
            items=Sec_menu_items,
            width_mult=4,
        )
        self.Sec_menu.open()

    def Sec_menu_callback(self, text_item):
        self.root.get_screen('attendance_filter').ids.section.text = text_item
        self.Sec_menu.dismiss()
        print(text_item)
    def handle_action(self,action):
        match action:
            case "chatbot":
                self.root.get_screen('home').manager.current = "chatbot"
                print("chatbot is opening")

    data = {}

    def build(self):

        self.theme_cls.theme_style_switch_animation = True

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"

        #for speeddailbutton
        self.data = {
            'Student-report': 'progress-pencil',
            'Student-Attendance': 'checkbox-marked-circle',
            'chatbot': ['chat-question',"on_press",lambda x:self.handle_action("chatbot")]
        }
        menu_item = ["Hey", "feedback", "settings"]
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"{i}",
                "height": 56,
                "on_release": lambda x=f"{i}": self.menu_callback(x),
            } for i in menu_item
        ]
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=4,
        )
        return Builder.load_file("screens/main.kv")
    def callback(self, button):
        self.menu.caller = button
        self.menu.open()

    def menu_callback(self, text_item):
        self.menu.dismiss()
        Snackbar(text=text_item).open()

    def switch_theme(self):
        self.theme_cls.primary_palette = (
            "Indigo" if self.theme_cls.primary_palette == "Red" else "Red"
        )
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )




if __name__ == "__main__":
    CMS().run()
