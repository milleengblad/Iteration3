
from PyQt6 import QtCore, QtGui, QtWidgets
from GUIvindue5 import Ui_Window5

class Ui_Window4(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Window5()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, Window4):
        Window4.setObjectName("Window4")
        Window4.resize(799, 600)
        self.centralwidget = QtWidgets.QWidget(Window4)
        self.centralwidget.setObjectName("centralwidget")
        self.vindue4 = QtWidgets.QTextEdit(self.centralwidget)
        self.vindue4.setGeometry(QtCore.QRect(0, 0, 801, 111))
        self.vindue4.setStyleSheet("background-color: rgb(148, 17, 0);")
        self.vindue4.setObjectName("vindue4")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 473, 811, 91))
        self.textEdit_2.setStyleSheet("background-color: rgb(148, 17, 0);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.vindue4_2 = QtWidgets.QWidget(self.centralwidget)
        self.vindue4_2.setGeometry(QtCore.QRect(0, 110, 801, 371))
        self.vindue4_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.vindue4_2.setObjectName("vindue4_2")
        self.textEdit_6 = QtWidgets.QTextEdit(self.vindue4_2)
        self.textEdit_6.setGeometry(QtCore.QRect(10, 20, 121, 31))
        self.textEdit_6.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_10 = QtWidgets.QTextEdit(self.vindue4_2)
        self.textEdit_10.setGeometry(QtCore.QRect(160, 20, 401, 31))
        self.textEdit_10.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.textEdit_10.setObjectName("textEdit_10")
        self.textEdit_4 = QtWidgets.QTextEdit(self.vindue4_2)
        self.textEdit_4.setGeometry(QtCore.QRect(680, 20, 111, 31))
        self.textEdit_4.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.textEdit_4.setObjectName("textEdit_4")
        self.tableWidget = QtWidgets.QTableWidget(self.vindue4_2)
        self.tableWidget.setGeometry(QtCore.QRect(160, 60, 521, 271))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setBackground(brush)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(214, 214, 214))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(214, 214, 214))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(214, 214, 214))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        self.tableWidget.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(214, 214, 214))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        self.tableWidget.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(214, 214, 214))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        self.tableWidget.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 4, item)
        self.pushButton_1 = QtWidgets.QPushButton(self.vindue4_2)
        self.pushButton_1.setGeometry(QtCore.QRect(10, 50, 121, 31))
        self.pushButton_1.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.vindue4_2)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 80, 121, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.vindue4_2)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 110, 121, 31))
        self.pushButton_3.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.vindue4_2)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 140, 121, 31))
        self.pushButton_4.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.vindue4_2)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 170, 121, 31))
        self.pushButton_5.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.vindue4_2)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 200, 121, 31))
        self.pushButton_6.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.vindue4_2)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 230, 121, 31))
        self.pushButton_7.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.vindue4_2)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 260, 121, 31))
        self.pushButton_8.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.vindue4_2)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 290, 121, 31))
        self.pushButton_9.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.pushButton_9.setObjectName("pushButton_9")


        self.pushButton = QtWidgets.QPushButton(self.vindue4_2, clicked = lambda: self.openWindow())


        self.pushButton.setGeometry(QtCore.QRect(679, 330, 111, 31))
        self.pushButton.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.pushButton.setObjectName("pushButton")
        Window4.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Window4)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 21))
        self.menubar.setObjectName("menubar")
        Window4.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Window4)
        self.statusbar.setObjectName("statusbar")
        Window4.setStatusBar(self.statusbar)

        self.retranslateUi(Window4)
        QtCore.QMetaObject.connectSlotsByName(Window4)

    def retranslateUi(self, Window4):
        _translate = QtCore.QCoreApplication.translate
        Window4.setWindowTitle(_translate("Window4", "MainWindow"))
        self.vindue4.setHtml(_translate("Window4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:700; color:#ffffff;\">BestBooking</span></p></body></html>"))
        self.textEdit_6.setHtml(_translate("Window4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Søg...</p></body></html>"))
        self.textEdit_10.setHtml(_translate("Window4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Du er her:   Skema   &gt;   BestBooking</p></body></html>"))
        self.textEdit_4.setHtml(_translate("Window4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Log af</span></p></body></html>"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Window4", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Window4", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Window4", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Window4", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Window4", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Window4", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Window4", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Window4", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Window4", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("Window4", "10"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Window4", "Lektion "))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Window4", "Dato"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Window4", "Tid"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Window4", "Sted"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Window4", "Lokale"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Window4", "Forelæsning"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Window4", "29-03-2022"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Window4", "10:15-11:00"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("Window4", "KU"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("Window4", "105"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("Window4", "Forelæsning"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("Window4", "29-03-2022"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("Window4", "11:15-12:00"))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("Window4", "KU"))
        item = self.tableWidget.item(1, 4)
        item.setText(_translate("Window4", "105"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("Window4", "SAU"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("Window4", "01-04-2022"))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("Window4", "08:15-09:00"))
        item = self.tableWidget.item(2, 3)
        item.setText(_translate("Window4", "KU"))
        item = self.tableWidget.item(2, 4)
        item.setText(_translate("Window4", "210"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("Window4", "SAU"))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("Window4", "01-04-2022"))
        item = self.tableWidget.item(3, 2)
        item.setText(_translate("Window4", "09:15-10:00"))
        item = self.tableWidget.item(3, 3)
        item.setText(_translate("Window4", "KU"))
        item = self.tableWidget.item(3, 4)
        item.setText(_translate("Window4", "210"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("Window4", "Forelæsning"))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("Window4", "06-04-2022"))
        item = self.tableWidget.item(4, 2)
        item.setText(_translate("Window4", "08:00-09:00"))
        item = self.tableWidget.item(4, 3)
        item.setText(_translate("Window4", "DTU"))
        item = self.tableWidget.item(4, 4)
        item.setText(_translate("Window4", "99"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("Window4", "SAU"))
        item = self.tableWidget.item(5, 1)
        item.setText(_translate("Window4", "06-04-2022"))
        item = self.tableWidget.item(5, 2)
        item.setText(_translate("Window4", "09:00-10:00"))
        item = self.tableWidget.item(5, 3)
        item.setText(_translate("Window4", "DTU"))
        item = self.tableWidget.item(5, 4)
        item.setText(_translate("Window4", "99"))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("Window4", "Forelæsning"))
        item = self.tableWidget.item(6, 1)
        item.setText(_translate("Window4", "12-04-2022"))
        item = self.tableWidget.item(6, 2)
        item.setText(_translate("Window4", "15:15-16:00"))
        item = self.tableWidget.item(6, 3)
        item.setText(_translate("Window4", "KU"))
        item = self.tableWidget.item(6, 4)
        item.setText(_translate("Window4", "107"))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("Window4", "Forelæsning"))
        item = self.tableWidget.item(7, 1)
        item.setText(_translate("Window4", "12-04-2022"))
        item = self.tableWidget.item(7, 2)
        item.setText(_translate("Window4", "16:15-17:00"))
        item = self.tableWidget.item(7, 3)
        item.setText(_translate("Window4", "KU"))
        item = self.tableWidget.item(7, 4)
        item.setText(_translate("Window4", "107"))
        item = self.tableWidget.item(8, 0)
        item.setText(_translate("Window4", "Forelæsning"))
        item = self.tableWidget.item(8, 1)
        item.setText(_translate("Window4", "25-04-2022"))
        item = self.tableWidget.item(8, 2)
        item.setText(_translate("Window4", "10:00-11:00"))
        item = self.tableWidget.item(8, 3)
        item.setText(_translate("Window4", "DTU"))
        item = self.tableWidget.item(8, 4)
        item.setText(_translate("Window4", "97"))
        item = self.tableWidget.item(9, 0)
        item.setText(_translate("Window4", "SAU"))
        item = self.tableWidget.item(9, 1)
        item.setText(_translate("Window4", "25-04-2022"))
        item = self.tableWidget.item(9, 2)
        item.setText(_translate("Window4", "12:00-13:00"))
        item = self.tableWidget.item(9, 3)
        item.setText(_translate("Window4", "DTU"))
        item = self.tableWidget.item(9, 4)
        item.setText(_translate("Window4", "97"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_1.setText(_translate("Window4", "Skema"))
        self.pushButton_2.setText(_translate("Window4", "Kurser"))
        self.pushButton_3.setText(_translate("Window4", "Kurser"))
        self.pushButton_4.setText(_translate("Window4", "Eksamen"))
        self.pushButton_5.setText(_translate("Window4", "KU/DTU mail"))
        self.pushButton_6.setText(_translate("Window4", "Selvbetjening"))
        self.pushButton_7.setText(_translate("Window4", "Hjælp"))
        self.pushButton_8.setText(_translate("Window4", "Om KU"))
        self.pushButton_9.setText(_translate("Window4", "Om DTU"))
        self.pushButton.setText(_translate("Window4", "Vælg lektion"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window4 = QtWidgets.QMainWindow()
    ui = Ui_Window4()
    ui.setupUi(Window4)
    Window4.show()
    sys.exit(app.exec())
