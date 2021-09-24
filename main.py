from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.size = (360, 640)




class Container(GridLayout):
    def calculate(self, calculation):

        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Ошибка"


class CalcApp(App):
    def __init__(self, **kwargs):
        self.title = "Calculator"
        super().__init__(**kwargs)

    def build(self):
        return Container()


if __name__ == "__main__":
    CalcApp().run()
