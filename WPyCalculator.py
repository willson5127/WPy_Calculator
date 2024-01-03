import sys
from PyQt6.QtWidgets import QApplication
from model.model import Model
from controllers.Calculator_ctrl import CalculatorController
from views.Calculator import CalculatorView


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = Model()
        self.main_controller = CalculatorController(self.model)
        self.main_view = CalculatorView(self.model, self.main_controller)
        self.main_view.show()


if __name__ == "__main__":
    app = App(sys.argv)
    sys.exit(app.exec())
