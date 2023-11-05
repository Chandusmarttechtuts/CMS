from kivy.uix.screenmanager import Screen, ScreenManager

class HomeScreen(Screen):
    def nav_drawer_press(self, clicked_item, previous_screen):
        match clicked_item:
            case "Home":
                print("Home is clicked")
                self.manager.current = "home"
            case "Attendance":
                print("Attendance is clicked")
                self.manager.current = "attendance_filter"
            case "Academics":
                print("Academics is clicked")
            case "Accounts":
                print("Accounts is clicked")
            case "Time tables":
                print("Time tables is clicked")
            case "Regulations":
                print("Regulations is clicked")
            case _:
                print("default case!")

    def on_nav_bar_press(self, press_item):
        match press_item:
            case "arrow-left":
                print("back is clicked")
                self.manager.current = "home"
            case "Home":
                print("Home is clicked")
                self.manager.current = "home"
