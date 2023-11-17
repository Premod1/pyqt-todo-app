

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(352, 357)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.additem_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.add_it())
        self.additem_pushButton.setGeometry(QtCore.QRect(10, 60, 91, 41))
        self.additem_pushButton.setObjectName("additem_pushButton")
        self.deleteitem_pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.delete_it())
        self.deleteitem_pushButton_2.setGeometry(QtCore.QRect(120, 60, 101, 41))
        self.deleteitem_pushButton_2.setObjectName("deleteitem_pushButton_2")
        self.clearitem_pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.clear_it())
        self.clearitem_pushButton_3.setGeometry(QtCore.QRect(230, 60, 111, 41))
        self.clearitem_pushButton_3.setObjectName("clearitem_pushButton_3")
        self.additem_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.additem_lineEdit.setGeometry(QtCore.QRect(10, 10, 331, 41))
        self.additem_lineEdit.setObjectName("additem_lineEdit")
        self.mylist_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.mylist_listWidget.setGeometry(QtCore.QRect(10, 120, 331, 192))
        self.mylist_listWidget.setObjectName("mylist_listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 352, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #add item
    def add_it(self):
        item = self.additem_lineEdit.text()
        self.mylist_listWidget.addItem(item)
        self.additem_lineEdit.setText("")
  

    def delete_it(self):
        clicked = self.mylist_listWidget.currentRow()
        self.mylist_listWidget.takeItem(clicked)

    def clear_it(self):
        self.mylist_listWidget.clear()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ToDo List"))
        self.additem_pushButton.setText(_translate("MainWindow", "Add Item"))
        self.deleteitem_pushButton_2.setText(_translate("MainWindow", "Delete Item"))
        self.clearitem_pushButton_3.setText(_translate("MainWindow", "Clear All List"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
