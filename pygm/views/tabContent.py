# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tabContent.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import common.commonString


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(460, 541)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 461, 541))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.tabContainer_v = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.tabContainer_v.setContentsMargins(4, 4, 4, 4)
        self.tabContainer_v.setObjectName("tabContainer_v")
        self.deviceContainer = QtWidgets.QHBoxLayout()
        self.deviceContainer.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.deviceContainer.setObjectName("deviceContainer")
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.deviceContainer.addWidget(self.comboBox)
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
        self.shimen_cb = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.shimen_cb.setObjectName("shimen_cb")
        self.horizontalLayout_3.addWidget(self.shimen_cb)
        self.baotu_cb = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.baotu_cb.setObjectName("baotu_cb")
        self.horizontalLayout_3.addWidget(self.baotu_cb)
        self.mijing_cb = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.mijing_cb.setObjectName("mijing_cb")
        self.horizontalLayout_3.addWidget(self.mijing_cb)
        self.yunbiao_cb = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.yunbiao_cb.setObjectName("yunbiao_cb")
        self.horizontalLayout_3.addWidget(self.yunbiao_cb)
        self.fuben_cb = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.fuben_cb.setObjectName("fuben_cb")
        self.horizontalLayout_3.addWidget(self.fuben_cb)
        self.zhuogui_cb = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.zhuogui_cb.setObjectName("zhuogui_cb")
        self.horizontalLayout_3.addWidget(self.zhuogui_cb)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
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
        self.duizhang_cb = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.duizhang_cb.setObjectName("duizhang_cb")
        self.horizontalLayout_4.addWidget(self.duizhang_cb)
        self.accept_cb = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.accept_cb.setObjectName("accept_cb")
        self.horizontalLayout_4.addWidget(self.accept_cb)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.start_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.start_btn.setObjectName("start_btn")
        self.horizontalLayout_4.addWidget(self.start_btn)
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "日常"))
        self.shimen_cb.setText(_translate("Form", "师门"))
        self.baotu_cb.setText(_translate("Form", "宝图"))
        self.mijing_cb.setText(_translate("Form", "秘境"))
        self.yunbiao_cb.setText(_translate("Form", "运镖"))
        self.fuben_cb.setText(_translate("Form", "副本"))
        self.zhuogui_cb.setText(_translate("Form", "捉鬼"))
        self.label_5.setText(_translate("Form", "操作"))
        self.duizhang_cb.setText(_translate("Form", "任命队长"))
        self.accept_cb.setText(_translate("Form", "接受任何人组队"))
        self.start_btn.setText(_translate("Form", "start"))
        self.label_4.setText(_translate("Form", "log"))
        self.plainTextEdit.setPlainText(_translate("Form", common.commonString.log_example))
