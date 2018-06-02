# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simple_launcher.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(769, 176)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.particle_select_cbox = QtGui.QComboBox(self.centralwidget)
        self.particle_select_cbox.setObjectName(_fromUtf8("particle_select_cbox"))
        self.particle_select_cbox.addItem(_fromUtf8(""))
        self.particle_select_cbox.addItem(_fromUtf8(""))
        self.particle_select_cbox.addItem(_fromUtf8(""))
        self.particle_select_cbox.addItem(_fromUtf8(""))
        self.particle_select_cbox.addItem(_fromUtf8(""))
        self.particle_select_cbox.addItem(_fromUtf8(""))
        self.particle_select_cbox.addItem(_fromUtf8(""))
        self.particle_select_cbox.addItem(_fromUtf8(""))
        self.particle_select_cbox.addItem(_fromUtf8(""))
        self.particle_select_cbox.addItem(_fromUtf8(""))
        self.particle_select_cbox.addItem(_fromUtf8(""))
        self.particle_select_cbox.addItem(_fromUtf8(""))
        self.particle_select_cbox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.particle_select_cbox, 0, 0, 1, 1)
        self.particles_number_spinbox = QtGui.QSpinBox(self.centralwidget)
        self.particles_number_spinbox.setMinimum(1)
        self.particles_number_spinbox.setMaximum(10)
        self.particles_number_spinbox.setObjectName(_fromUtf8("particles_number_spinbox"))
        self.gridLayout.addWidget(self.particles_number_spinbox, 0, 1, 1, 1)
        self.show_particle_btn = QtGui.QPushButton(self.centralwidget)
        self.show_particle_btn.setObjectName(_fromUtf8("show_particle_btn"))
        self.gridLayout.addWidget(self.show_particle_btn, 0, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 769, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.particle_select_cbox.setItemText(0, _translate("MainWindow", "e+", None))
        self.particle_select_cbox.setItemText(1, _translate("MainWindow", "mu+", None))
        self.particle_select_cbox.setItemText(2, _translate("MainWindow", "e-", None))
        self.particle_select_cbox.setItemText(3, _translate("MainWindow", "mu-", None))
        self.particle_select_cbox.setItemText(4, _translate("MainWindow", "tau-e+", None))
        self.particle_select_cbox.setItemText(5, _translate("MainWindow", "mu+", None))
        self.particle_select_cbox.setItemText(6, _translate("MainWindow", "tau+", None))
        self.particle_select_cbox.setItemText(7, _translate("MainWindow", "nu_e", None))
        self.particle_select_cbox.setItemText(8, _translate("MainWindow", "nu_mu", None))
        self.particle_select_cbox.setItemText(9, _translate("MainWindow", "nu_tau", None))
        self.particle_select_cbox.setItemText(10, _translate("MainWindow", "nubar_e", None))
        self.particle_select_cbox.setItemText(11, _translate("MainWindow", "nubar_mu", None))
        self.particle_select_cbox.setItemText(12, _translate("MainWindow", "nubar_tau", None))
        self.show_particle_btn.setText(_translate("MainWindow", "Show Particle", None))

