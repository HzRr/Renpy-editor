# Form implementation generated from reading ui file 'DialogEdit.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 400)
        self.btnDialogEditDefine = QtWidgets.QPushButton(Form)
        self.btnDialogEditDefine.setGeometry(QtCore.QRect(490, 340, 75, 24))
        self.btnDialogEditDefine.setObjectName("btnDialogEditDefine")
        self.btnDialogEditExit = QtWidgets.QPushButton(Form)
        self.btnDialogEditExit.setGeometry(QtCore.QRect(590, 340, 75, 24))
        self.btnDialogEditExit.setObjectName("btnDialogEditExit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "添加台词"))
        self.btnDialogEditDefine.setText(_translate("Form", "确定"))
        self.btnDialogEditExit.setText(_translate("Form", "取消"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
