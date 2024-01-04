from PyQt6.QtCore import QObject, pyqtSlot
from model.model import Model


class CalculatorController(QObject):
    def __init__(self, model: type[Model]) -> None:
        super().__init__()
        self._model = model

    @pyqtSlot(str)
    def keyin_number(self, value: type[str]):
        if self._model.display == "0" or self._model.is_result == True:
            self._model.display = value
            self._model.is_result = False
        else:
            self._model.display = self._model.display + value

    @pyqtSlot(int)
    def convert_decimal(self):
        if self._model.display.count(".") == 0 and self._model.is_result != True:
            self._model.display = self._model.display + "."

    @pyqtSlot(int)
    def convert_posivite_negative(self):
        if self._model.display != "0" and self._model.is_result != True:
            self._model.display = f"{float(self._model.display) * -1:g}"

    @pyqtSlot(str)
    def keyin_operation(self, value: type[str]):
        self._model.NumberA = float(self._model.display)
        self._model.operation_type = value

        self._model.op_display = f"{self._model.NumberA:g}" + \
            " " + self._model.operation_type

        self._model.display = "0"

    @pyqtSlot(int)
    def calculate_result(self):
        if self._model.is_result == False:
            self._model.NumberB = float(self._model.display)

        match self._model.operation_type:
            case "+":
                self._model.display = f"{self._model.NumberA + self._model.NumberB:g}"
            case "-":
                self._model.display = f"{self._model.NumberA - self._model.NumberB:g}"
            case "*":
                self._model.display = f"{self._model.NumberA * self._model.NumberB:g}"
            case "/":
                self._model.display = f"{self._model.NumberA / self._model.NumberB:g}"
            case _:
                return

        self._model.op_display = f"{self._model.NumberA:g}" + " " + \
            self._model.operation_type + " " + \
            f"{self._model.NumberB:g}" + " ="

        self._model.NumberA = float(self._model.display)
        self._model.is_result = True

    @pyqtSlot(int)
    def clear_empty(self):
        self._model.display = "0"

    @pyqtSlot(int)
    def all_clear(self):
        self._model.display = "0"
        self._model.op_display = ""
        self._model.operation_type = ""
        self._model.NumberA = 0
        self._model.NumberB = 0
