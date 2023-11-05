from kivy.uix.screenmanager import Screen
class AttendanceFilterScreen(Screen):
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
                self.manager.current = "manual_attendance"
            case "send_alert":
                print("Alert is being send")
            case "attendance_percentage":
                print("Going to attendance percentage")
                self.manager.current = "Attendance_percentage"
            case _:
                print("default case")
