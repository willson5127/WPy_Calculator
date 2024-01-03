from PyQt6.QtCore import QObject, pyqtSignal


class Model(QObject):
    display_changed = pyqtSignal(str)

    @property
    def display(self):
        return self._display

    @display.setter
    def display(self, value):
        self._display = value
        self.display_changed.emit(value)

    def __init__(self):
        super().__init__()

        self._display = "0"
