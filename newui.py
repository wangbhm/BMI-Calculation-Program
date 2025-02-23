from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QHBoxLayout, QLabel, QDoubleSpinBox,
                               QPushButton, QTextEdit)


class PyDraculaBMI(QMainWindow):
    def __init__(self):
        super().__init__()

        # 窗口基本设置
        self.setWindowTitle("BMI Calculator")
        self.setMinimumSize(QSize(480, 640))

        # 主容器
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # 主布局
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(40, 40, 40, 40)
        self.main_layout.setSpacing(25)

        # 应用样式
        self.setup_style()

        # 初始化UI组件
        self.setup_ui()

    def setup_style(self):
        """设置PyDracula风格样式表"""
        self.setStyleSheet("""
            /* 主窗口样式 */
            QMainWindow {
                background-color: #282a36;
            }

            /* 输入框通用样式 */
            QDoubleSpinBox {
                background-color: #44475a;
                color: #f8f8f2;
                border: 2px solid #6272a4;
                border-radius: 5px;
                padding: 12px 15px;
                font-size: 16px;
                min-width: 120px;
            }
            QDoubleSpinBox:hover {
                border-color: #bd93f9;
            }
            QDoubleSpinBox:focus {
                border-color: #ff79c6;
            }

            /* 按钮样式 */
            QPushButton {
                background-color: #6272a4;
                color: #f8f8f2;
                border: none;
                border-radius: 8px;
                padding: 15px 30px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #bd93f9;
            }
            QPushButton:pressed {
                background-color: #ff79c6;
            }

            /* 结果标签样式 */
            #output1 {
                background-color: #44475a;
                color: #50fa7b;
                border-radius: 8px;
                padding: 15px;
                font-size: 28px;
                font-weight: bold;
            }

            /* 建议文本框样式 */
            QTextEdit {
                background-color: #44475a;
                color: #f8f8f2;
                border: 2px solid #6272a4;
                border-radius: 8px;
                padding: 15px;
                font-size: 14px;
            }
            
            weight_group {
                background-color: #44475a
            }
        """)

    def setup_ui(self):
        """初始化UI组件"""

        # 标题
        self.title_label = QLabel("BMI 健康分析仪")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("""
            font: bold 24px '微软雅黑';
            color: #bd93f9;
            padding-bottom: 20px;
        """)
        self.main_layout.addWidget(self.title_label)

        # 输入区域
        self.setup_inputs()

        # 结果展示
        self.setup_outputs()

        # 按钮
        self.start_btn = QPushButton("开始计算")
        self.start_btn.setObjectName("start")
        self.main_layout.addWidget(self.start_btn)

        # 建议框
        self.advice_text = QTextEdit()
        self.advice_text.setObjectName("output")
        self.advice_text.setPlaceholderText("健康建议将在此显示...")
        self.advice_text.setReadOnly(True)
        self.main_layout.addWidget(self.advice_text)

    def setup_inputs(self):
        """设置输入区域"""
        input_layout = QHBoxLayout()
        input_layout.setSpacing(20)

        # 体重输入
        weight_group = QVBoxLayout()
        self.weight_input = QDoubleSpinBox()
        self.weight_input.setObjectName("input1")
        self.weight_input.setRange(20, 300)
        self.weight_input.setDecimals(1)
        self.weight_input.setValue(65.0)
        weight_group.addWidget(QLabel("体重 (kg)"))
        weight_group.addWidget(self.weight_input)

        # 身高输入
        height_group = QVBoxLayout()
        self.height_input = QDoubleSpinBox()
        self.height_input.setObjectName("input2")
        self.height_input.setRange(0.5, 2.5)
        self.height_input.setDecimals(2)
        self.height_input.setValue(1.75)
        height_group.addWidget(QLabel("身高 (m)"))
        height_group.addWidget(self.height_input)

        input_layout.addLayout(weight_group)
        input_layout.addLayout(height_group)
        self.main_layout.addLayout(input_layout)

    def setup_outputs(self):
        """设置结果展示区域"""
        output_layout = QHBoxLayout()

        # BMI值显示
        output_group = QVBoxLayout()
        self.bmi_label = QLabel("-")
        self.bmi_label.setObjectName("output1")
        self.bmi_label.setAlignment(Qt.AlignCenter)
        output_group.addWidget(QLabel("BMI 指数"))
        output_group.addWidget(self.bmi_label)

        output_layout.addLayout(output_group)
        self.main_layout.addLayout(output_layout)


if __name__ == "__main__":
    app = QApplication([])
    app.setFont(QFont("微软雅黑", 12))
    window = PyDraculaBMI()
    window.show()
    app.exec()