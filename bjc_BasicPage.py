from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BasicPage(object):
    def setupUi(self, BasicPage):
        BasicPage.setObjectName("BasicPage")
        BasicPage.resize(320, 487)
        BasicPage.setFixedSize(320, 487)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./image/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BasicPage.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(BasicPage)
        self.centralwidget.setObjectName("centralwidget")
        self.lblbasic_Strategy = QtWidgets.QLabel(self.centralwidget)
        self.lblbasic_Strategy.setGeometry(QtCore.QRect(0, -10, 321, 511))
        self.lblbasic_Strategy.setStyleSheet("image: url(./image/basic_strategy.jpg);")
        self.lblbasic_Strategy.setText("")
        self.lblbasic_Strategy.setObjectName("lblbasic_Strategy")
        BasicPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BasicPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 21))
        self.menubar.setObjectName("menubar")
        BasicPage.setMenuBar(self.menubar)

        self.retranslateUi(BasicPage)
        QtCore.QMetaObject.connectSlotsByName(BasicPage)

    def retranslateUi(self, BasicPage):
        _translate = QtCore.QCoreApplication.translate
        BasicPage.setWindowTitle(_translate("BasicPage", "Basic Strategy"))


if __name__ == "__main__":
    import sys
    import image_rc
    app = QtWidgets.QApplication(sys.argv)
    BasicPage = QtWidgets.QBasicPage()
    ui = Ui_BasicPage()
    ui.setupUi(BasicPage)
    BasicPage.show()
    sys.exit(app.exec_())
