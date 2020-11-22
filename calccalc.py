import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from math import factorial


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calc.ui', self)
        self.string = ''
        self.equation = ''
        #self.table.setDigitCount(15)

        self.btn0.clicked.connect(self.nums)
        self.btn1.clicked.connect(self.nums)
        self.btn2.clicked.connect(self.nums)
        self.btn3.clicked.connect(self.nums)
        self.btn4.clicked.connect(self.nums)
        self.btn5.clicked.connect(self.nums)
        self.btn6.clicked.connect(self.nums)
        self.btn7.clicked.connect(self.nums)
        self.btn8.clicked.connect(self.nums)
        self.btn9.clicked.connect(self.nums)
        self.btn_dot.clicked.connect(self.nums)

        self.btn_plus.clicked.connect(self.signs)
        self.btn_minus.clicked.connect(self.signs)
        self.btn_div.clicked.connect(self.signs)
        self.btn_pow.clicked.connect(self.signs)
        self.btn_mult.clicked.connect(self.signs)

        self.btn_clear.clicked.connect(self.reset)

        self.btn_sqrt.clicked.connect(self.result)
        self.btn_fact.clicked.connect(self.result)
        self.btn_eq.clicked.connect(self.result)

    def nums(self):
        if self.sender() == self.btn_dot and self.string.count('.') == 1:
            pass
        else:
            self.string += self.sender().text()
            self.equation += self.sender().text()
            self.table.display(self.string)

    def signs(self):
        if {'-', '+', '/', '*'}.intersection(set(self.equation)):
            if '/0' in self.equation:
                self.reset()
                self.table.display('Error')
                return
            self.equation = str(eval(self.equation))
        if self.sender().text() == '^':
            self.equation += '**'
        else:
            self.equation += self.sender().text()
        self.string = ''

    def reset(self):
        self.string = ''
        self.equation = ''
        self.table.display('0')  # ноль под вопросом, число или строка

    def result(self):
        if '/0' in self.equation:
            self.reset()
            self.table.display('Error')
            return
        self.equation = str(eval(self.equation))
        if self.sender() == self.btn_sqrt:
            if self.equation[0] == '-':
                self.reset()
                self.table.display('Error')
                return
            self.equation = str(float(self.equation) ** 0.5)
        elif self.sender() == self.btn_fact:
            if self.equation[0] == '-' or float(self.equation) == int(self.equation):
                self.reset()
                self.table.display('Error')
                return
            self.equation = str(factorial(int(self.equation)))
        self.table.display(self.equation)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())