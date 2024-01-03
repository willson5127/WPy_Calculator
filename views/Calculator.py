from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import pyqtSlot
from views.Calculator_ui import Ui_MainWindow
from controllers.Calculator_ctrl import CalculatorController
from model.model import Model


class CalculatorView(QMainWindow):
    def __init__(self, model: type[Model], main_controller: type[CalculatorController]) -> None:
        super().__init__()
        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        self._ui.component_ButtonOne.clicked.connect(
            lambda: self._main_controller.keyin_number("1"))

        self._model.display_changed.connect(self.on_display_changed)

    @pyqtSlot(str)
    def on_display_changed(self, value):
        self._ui.component_CrystalDisplay.setText(value)
