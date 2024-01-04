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
        self._ui.component_ButtonTwo.clicked.connect(
            lambda: self._main_controller.keyin_number("2"))
        self._ui.component_ButtonThree.clicked.connect(
            lambda: self._main_controller.keyin_number("3"))
        self._ui.component_ButtonFour.clicked.connect(
            lambda: self._main_controller.keyin_number("4"))
        self._ui.component_ButtonFive.clicked.connect(
            lambda: self._main_controller.keyin_number("5"))
        self._ui.component_ButtonSix.clicked.connect(
            lambda: self._main_controller.keyin_number("6"))
        self._ui.component_ButtonSeven.clicked.connect(
            lambda: self._main_controller.keyin_number("7"))
        self._ui.component_ButtonEight.clicked.connect(
            lambda: self._main_controller.keyin_number("8"))
        self._ui.component_ButtonNine.clicked.connect(
            lambda: self._main_controller.keyin_number("9"))
        self._ui.component_ButtonZero.clicked.connect(
            lambda: self._main_controller.keyin_number("0"))
        self._ui.component_ButtonDot.clicked.connect(
            lambda: self._main_controller.convert_decimal())
        self._ui.component_ButtonPosNeg.clicked.connect(
            lambda: self._main_controller.convert_posivite_negative())

        self._ui.component_ButtonAddition.clicked.connect(
            lambda: self._main_controller.keyin_operation("+"))
        self._ui.component_ButtonSubtraction.clicked.connect(
            lambda: self._main_controller.keyin_operation("-"))
        self._ui.component_ButtonMultiplication.clicked.connect(
            lambda: self._main_controller.keyin_operation("*"))
        self._ui.component_ButtonDivision.clicked.connect(
            lambda: self._main_controller.keyin_operation("/"))

        self._ui.component_ButtonAnser.clicked.connect(
            lambda: self._main_controller.calculate_result())
        self._ui.component_ButtonClearEntry.clicked.connect(
            lambda: self._main_controller.clear_empty())
        self._ui.component_ButtonAllClear.clicked.connect(
            lambda: self._main_controller.all_clear())

        self._model.display_changed.connect(self.on_display_changed)
        self._model.op_display_changed.connect(self.on_op_display_changed)

    @pyqtSlot(str)
    def on_display_changed(self, value: type[str]):
        self._ui.component_CrystalDisplay.setText(value)

    @pyqtSlot(str)
    def on_op_display_changed(self, value: type[str]):
        self._ui.component_OperationDisplay.setText(value)
