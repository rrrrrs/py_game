import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QLabel, QBoxLayout
from PyQt5.Qsci import QsciScintilla
import sys
import threading


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.statusLight = None
        self.log_edit = None
        self.index = 0
        self.initUI()

    def initUI(self):
        self.statusLight = QLabel()

        self.log_edit = QsciScintilla(self)
        self.log_edit.setMaximumWidth(500)
        self.setCentralWidget(self.log_edit)
        self.log_edit.setReadOnly(True)  # 设置为只读模式，防止用户修改日志内容

        # self.container = QBoxLayout(QBoxLayout_Direction=QBoxLayout.LeftToRight)


    def setStatusLight(self, status):
        m_yellow_SheetStyle = "min-width: 40px; min-height: 40px;max-width:40px; max-height: 40px;border-radius: 20px;  border:1px solid black;background:yellow";
        self.statusLight.setstyleSheet(m_yellow_SheetStyle)


    def log(self, msg):
        print(msg)
        self.log_edit.append(msg)  # 在QScintilla控件中添加一行日志消息
        time.sleep(1)

    def run(self):
        self.index = 0
        while 1:
            self.log("This is a log message {} \n".format(str(self.index)))
            time.sleep(1)
            self.index += 1

    def start(self):
        thread = threading.Thread(target=self.run)
        thread.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.resize(600, 600)

    mainWindow.show()
    mainWindow.start()
    sys.exit(app.exec_())
