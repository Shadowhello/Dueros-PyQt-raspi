from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QGridLayout,QLabel,QPushButton,QLineEdit
class gpioshow(QtWidgets.QWidget):
    def __init__(self):
        super(gpioshow,self).__init__()
        gridLyout = QGridLayout()
        gridLyout.setSpacing(10)
        gridLyout.setContentsMargins(20,20,20,20)

        title = QLabel("hello")
        gridLyout.addWidget(title,0,1)

        btn = QPushButton("gpio_1")
        gridLyout.addWidget(btn,1,1)

        linedit = QLineEdit()
        gridLyout.addWidget(linedit,2,1)

        self.setLayout(gridLyout)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = gpioshow()
    myshow.show()
    sys.exit(app.exec())