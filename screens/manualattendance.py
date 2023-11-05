from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivymd.uix.button import MDRoundFlatIconButton
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.label import MDLabel
from kivy.uix.recycleview import RecycleView

# Define a placeholder data
default_data = [
    {"name": "chandra sekhar", "reg_no": "22A21A0520", "state": "Absent"},
    {"name": "chandra sekhar", "reg_no": "22A21A0520", "state": "Absent"},
    {"name": "pavan", "reg_no": "22A21A0517", "state": "Absent"},
    {"name": "nagendhra", "reg_no": "22A21A0519", "state": "Absent"},
    {"name": "chandra sekhar", "reg_no": "22A21A0520", "state": "Absent"},
    {"name": "pavan", "reg_no": "22A21A0517", "state": "Absent"},
    {"name": "nagendhra", "reg_no": "22A21A0519", "state": "Absent"},
    {"name": "chandra sekhar", "reg_no": "22A21A0520", "state": "Absent"},
    {"name": "pavan", "reg_no": "22A21A0517", "state": "Absent"},
    {"name": "nagendhra", "reg_no": "22A21A0519", "state": "Absent"},
    {"name": "chandra sekhar", "reg_no": "22A21A0520", "state": "Absent"},
    {"name": "pavan", "reg_no": "22A21A0517", "state": "Absent"},
    {"name": "nagendhra", "reg_no": "22A21A0519", "state": "Absent"},
    {"name": "chandra sekhar", "reg_no": "22A21A0520", "state": "Absent"},
    {"name": "pavan", "reg_no": "22A21A0517", "state": "Absent"},
    {"name": "nagendhra", "reg_no": "22A21A0519", "state": "Absent"},
]

# Initialize data with the default data
data = default_data

class MyCard(BoxLayout):
    name = StringProperty()
    reg_no = StringProperty()
    state = StringProperty()

    def toggle_state(self):
        # Toggle the state between "Present" and "Absent"
        self.state = "Present" if self.state == "Absent" else "Absent"


class CustomRecycleView(RecycleView):
    def __init__(self, **kwargs):
        super(CustomRecycleView, self).__init__(**kwargs)
        self.data = [{"name": entry["name"], "reg_no": entry["reg_no"], "state": entry["state"]} for entry in data]


class ManualAttendanceScreen(Screen):
    def __init__(self, **kwargs):
        super(ManualAttendanceScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        rv = CustomRecycleView()
        layout.add_widget(rv)
        self.add_widget(layout)