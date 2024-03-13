# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class CustomWidget(QWidget):

    def __init__(self,vivi):
        super().__init__()
        self.initUi(vivi)
        self.retranslateUi()

    def initUi(self,vivi):
        vivi.setObjectName("Form")
        vivi.resize(406, 353)
        self.verticalLayoutWidget = QtWidgets.QWidget(self) #Form
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 391, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.tabContainer_v = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.tabContainer_v.setContentsMargins(4, 4, 4, 4)
        self.tabContainer_v.setObjectName("tabContainer_v")
        self.deviceContainer = QtWidgets.QHBoxLayout()
        self.deviceContainer.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.deviceContainer.setObjectName("deviceContainer")
        self.deviceLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.deviceLabel.setScaledContents(True)
        self.deviceLabel.setIndent(1)
        self.deviceLabel.setOpenExternalLinks(False)
        self.deviceLabel.setObjectName("deviceLabel")
        self.deviceContainer.addWidget(self.deviceLabel)
        self.stateLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.stateLabel.setText("")
        self.stateLabel.setPixmap(QtGui.QPixmap("C:/Users/raosong/Downloads/led_green.png"))
        self.stateLabel.setObjectName("stateLabel")
        self.deviceContainer.addWidget(self.stateLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.deviceContainer.addItem(spacerItem)
        self.tabContainer_v.addLayout(self.deviceContainer)
        self.dailyContainer = QtWidgets.QVBoxLayout()
        self.dailyContainer.setContentsMargins(4, 4, 4, 4)
        self.dailyContainer.setObjectName("dailyContainer")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_3.setObjectName("label_3")
        self.dailyContainer.addWidget(self.label_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(4, -1, 4, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.shimenCheckbox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.shimenCheckbox.setObjectName("shimenCheckbox")
        self.horizontalLayout_3.addWidget(self.shimenCheckbox)
        self.baotuCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.baotuCheckBox.setObjectName("baotuCheckBox")
        self.horizontalLayout_3.addWidget(self.baotuCheckBox)
        self.mijingCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.mijingCheckBox.setObjectName("mijingCheckBox")
        self.horizontalLayout_3.addWidget(self.mijingCheckBox)
        self.yunbiaoCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.yunbiaoCheckBox.setObjectName("yunbiaoCheckBox")
        self.horizontalLayout_3.addWidget(self.yunbiaoCheckBox)
        self.fubencheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.fubencheckBox.setObjectName("fubencheckBox")
        self.horizontalLayout_3.addWidget(self.fubencheckBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.startBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.startBtn.setObjectName("startBtn")
        self.horizontalLayout_3.addWidget(self.startBtn)
        self.dailyContainer.addLayout(self.horizontalLayout_3)
        self.tabContainer_v.addLayout(self.dailyContainer)
        self.dailyContainer_2 = QtWidgets.QVBoxLayout()
        self.dailyContainer_2.setContentsMargins(4, 4, 4, 4)
        self.dailyContainer_2.setObjectName("dailyContainer_2")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_5.setObjectName("label_5")
        self.dailyContainer_2.addWidget(self.label_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(4, -1, 4, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.duizhangcheckbox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.duizhangcheckbox.setObjectName("duizhangcheckbox")
        self.horizontalLayout_4.addWidget(self.duizhangcheckbox)
        self.jieshouzuduicheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.jieshouzuduicheckBox.setObjectName("jieshouzuduicheckBox")
        self.horizontalLayout_4.addWidget(self.jieshouzuduicheckBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.dailyContainer_2.addLayout(self.horizontalLayout_4)
        self.tabContainer_v.addLayout(self.dailyContainer_2)
        self.logcontainer = QtWidgets.QVBoxLayout()
        self.logcontainer.setContentsMargins(4, 4, 4, 4)
        self.logcontainer.setObjectName("logcontainer")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.logcontainer.addWidget(self.label_4)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.logcontainer.addWidget(self.plainTextEdit)
        self.tabContainer_v.addLayout(self.logcontainer)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.tabContainer_v.addItem(spacerItem3)

        # self.retranslateUi(Form)  #form
        QtCore.QMetaObject.connectSlotsByName(vivi)

        # self.setLayout(vivi)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.deviceLabel.setText(_translate("Form", "device name"))
        self.label_3.setText(_translate("Form", "daily"))
        self.shimenCheckbox.setText(_translate("Form", "1"))
        self.baotuCheckBox.setText(_translate("Form", "2"))
        self.mijingCheckBox.setText(_translate("Form", "3"))
        self.yunbiaoCheckBox.setText(_translate("Form", "4"))
        self.fubencheckBox.setText(_translate("Form", "5"))
        self.startBtn.setText(_translate("Form", "start"))
        self.label_5.setText(_translate("Form", "operate"))
        self.duizhangcheckbox.setText(_translate("Form", "captain"))
        self.jieshouzuduicheckBox.setText(_translate("Form", "acceptanyone"))
        self.label_4.setText(_translate("Form", "log"))
        self.plainTextEdit.setPlainText(_translate("Form", "1.我从没觉得孤独，说的浪漫些，我完全自由\n"
"2.夕阳总会落在你身上，你也会快乐一场。\n"
"3.路过全世界，只为走向你。\n"
"4.于千万人中获你惊鸿，从此连生命也愿笑奉。\n"
"5.深情若是一桩悲剧，必定以死来句读\n"
"6.直到遇见你那一刻 我的星河才亮了起来.\n"
"7.简单的喜欢最长远 懂你的人最温柔\n"
"8.希望你的心情能像星星一样， 常年闪闪发亮，偶尔躲躲乌云。\n"
"9.向着月亮出发，即使不能到达，也能站在群星之中。\n"
"10.这份喜欢，迫在眉睫，阁下，你接好。\n"
"11.原来躲起来的星星也在努力发光啊。\n"
"12.也许，大海给贝壳下的定义是珍珠，也许时间给煤炭下的定义是钻石。\n"
"13.我们各自努力，最高处见。\n"
"14.猫咪在落叶里打滚儿，晚霞铺满天空，风把思念吹向你，我贪恋的人间不过是你而已。\n"
"15.你眼中的春和秋，胜过我见过的，爱过的一切山川与河流。\n"
"16.私心是希望你能陪我久一点.\n"
"17.我摘的果子，已酿成酒，只等你来添香解愁。\n"
"18.想用每日的温柔和月亮 换取一束光 最后将它化作星河 万倾赠与你.\n"
"19.风止于秋水，我止于你。\n"
"20.我想要的很简单：兜里有糖，肚里有墨，手里有活，卡里有钱，未来有你。"))


# if __name__ == "__main__":
#     app = QApplication([])
#     window = QtWidgets.QMainWindow()
#     ui = CustomWidget()
#     window.setCentralWidget(ui)
#     window.show()
#     sys.exit(app.exec_())
