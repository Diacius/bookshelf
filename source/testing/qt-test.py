import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class Bookmark:
    def __init__(self, name, url, tags):
        self.name = name
        self.url = url
        self.tags = tags
    def summaryString(self):
        return f"{self.name} from {self.url}. tagged as {self.tags}"
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Display demo bookmark!")
        self.text = QtWidgets.QLabel("book mark will appear here :)",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        testbookmark = Bookmark(name="Droppings", url="https://what-if.xkcd.com/11/", tags=["what-if", "nerdiness", "demo"])
        self.text.setText(testbookmark.summaryString())

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(1176, 768)
    widget.show()

    sys.exit(app.exec())