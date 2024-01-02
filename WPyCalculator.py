from PySide6.QtWidgets import QApplication, QMainWindow

from Ui.Calculator import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication([])
    theMainWindow = MainWindow()
    theMainWindow.show()
    app.exec()
