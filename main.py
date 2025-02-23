from PySide6.QtWidgets import QApplication, QMainWindow
from bmidef import bmi
from newui import PyDraculaBMI
from bmidevice import advice


class MyWindow(PyDraculaBMI):
    def __init__(self):
        super().__init__()

        self.start_btn.clicked.connect(self.chang1)




    def chang1(self):
        try:
            b = self.height_input.value()
            a = self.weight_input.value()
            print(a)
            print(b)
            user_bmi=bmi(a,b)
            user_advice=advice(a,b)
            print(user_advice)
            print(user_bmi)
        except ZeroDivisionError:
            self.advice_text.setText("请输入正确的数字")
        except:
            self.advice_text.setText("发生未知的错误")


        self.bmi_label.setText(str(user_bmi))
        self.advice_text.setText(user_advice)





if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()