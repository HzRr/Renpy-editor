# Form implementation generated from reading ui file 'dialogEdit.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DialogEdit(object):
    def setupUi(self, DialogEdit):
        DialogEdit.setObjectName("DialogEdit")
        DialogEdit.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        DialogEdit.resize(285, 344)
        self.layoutWidget = QtWidgets.QWidget(DialogEdit)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 10, 260, 303))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelDialogInput = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelDialogInput.setFont(font)
        self.labelDialogInput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelDialogInput.setObjectName("labelDialogInput")
        self.verticalLayout.addWidget(self.labelDialogInput)
        self.DialogInput = QtWidgets.QPlainTextEdit(self.layoutWidget)
        self.DialogInput.setObjectName("DialogInput")
        self.verticalLayout.addWidget(self.DialogInput)
        self.labelChar01 = QtWidgets.QLabel(self.layoutWidget)
        self.labelChar01.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelChar01.setObjectName("labelChar01")
        self.verticalLayout.addWidget(self.labelChar01)
        self.comboBoxCharacter = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBoxCharacter.setTabletTracking(False)
        self.comboBoxCharacter.setObjectName("comboBoxCharacter")
        self.comboBoxCharacter.addItem("")
        self.verticalLayout.addWidget(self.comboBoxCharacter)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnDialogEditDefine = QtWidgets.QPushButton(self.layoutWidget)
        self.btnDialogEditDefine.setObjectName("btnDialogEditDefine")
        self.horizontalLayout.addWidget(self.btnDialogEditDefine)
        self.btnDialogEditExit = QtWidgets.QPushButton(self.layoutWidget)
        self.btnDialogEditExit.setObjectName("btnDialogEditExit")
        self.horizontalLayout.addWidget(self.btnDialogEditExit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(DialogEdit)
        QtCore.QMetaObject.connectSlotsByName(DialogEdit)

    def retranslateUi(self, DialogEdit):
        _translate = QtCore.QCoreApplication.translate
        DialogEdit.setWindowTitle(_translate("DialogEdit", "台词编辑"))
        self.labelDialogInput.setText(_translate("DialogEdit", "请输入台词"))
        self.labelChar01.setText(_translate("DialogEdit", "人物"))
        self.comboBoxCharacter.setItemText(0, _translate("DialogEdit", "测试"))
        self.btnDialogEditDefine.setText(_translate("DialogEdit", "确定"))
        self.btnDialogEditExit.setText(_translate("DialogEdit", "取消"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogEdit = QtWidgets.QWidget()
    ui = Ui_DialogEdit()
    ui.setupUi(DialogEdit)
    DialogEdit.show()
    sys.exit(app.exec())
