from PyQt6.QtCore import QObject, pyqtSignal


class Model(QObject):
    display_changed = pyqtSignal(str)
    op_display_changed = pyqtSignal(str)

    @property
    def display(self):
        return self._display

    @display.setter
    def display(self, value: type[str]):
        self._display = value
        self.display_changed.emit(value)

    @property
    def op_display(self):
        return self._op_display

    @op_display.setter
    def op_display(self, value: type[str]):
        self._op_display = value
        self.op_display_changed.emit(value)

    @property
    def NumberA(self):
        return self._NumberA

    @NumberA.setter
    def NumberA(self, value: type[int]):
        self._NumberA = value

    @property
    def NumberB(self):
        return self._NumberB

    @NumberB.setter
    def NumberB(self, value: type[int]):
        self._NumberB = value

    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value: type[str]):
        self._operation_type = value

    @property
    def is_result(self):
        return self._is_result

    @is_result.setter
    def is_result(self, value: type[bool]):
        self._is_result = value

    def __init__(self):
        super().__init__()

        self._is_result = False
        self._display = "0"
        self._op_display = ""
        self._NumberA = 0
        self._NumberB = 0
        self._operation_type = ""
