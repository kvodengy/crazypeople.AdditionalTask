from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from random import *
def click():
    num = randint(0,9)
    number.setText(str(num))
    num2 = randint(0,9)
    number2.setText(str(num2))
    if num == num2:
        text.setText("Ви виграли! Зіграйте знову")
    else:
        text.setText("Ви програли! Зіграйте знову")


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Лотерея")
main_win.resize(400,400)
main_win.move(500,275)

text = QLabel("Натисни, щоб взяти участь")
number = QLabel("?")
number2 = QLabel("?")
button = QPushButton("Випробувати удачу")

line = QVBoxLayout()
line.addWidget(text, alignment=Qt.AlignCenter)
line.addWidget(number, alignment=Qt.AlignCenter)
line.addWidget(number2, alignment=Qt.AlignCenter)
line.addWidget(button, alignment=Qt.AlignCenter)
main_win.setLayout(line)
button.clicked.connect(click)

main_win.show()
app.exec()