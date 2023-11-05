from kivy.uix.screenmanager import Screen
class AttendancePercentageScreen(Screen):
    def on_nav_bar_press(self, press_item):
        match press_item:
            case "arrow-left":
                print("back is clicked")
                self.manager.current = "attendance_filter"
            case "home":
                print("Home is clicked")
                self.manager.current = "home"
