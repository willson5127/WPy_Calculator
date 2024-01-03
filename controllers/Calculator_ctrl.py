from PyQt6.QtCore import QObject, pyqtSlot


class CalculatorController(QObject):
    def __init__(self, model) -> None:
        super().__init__()
        self._model = model

    @pyqtSlot(str)
    def keyin_number(self, value):
        self._model.display = self._model.display + value
