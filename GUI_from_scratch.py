# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_from_scratch.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QFileDialog,QMessageBox
import os
import GuiFromScratch_mayavi
import Gui_animation
import Gui_mayavi_leftPanel
import Gui_image_leftPanel
import Gui_img_processing_PyQt5
#import image_to_video

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1140, 825)
        
        self.default_value_function()
        
    ## CENTRAL WIDGET
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        
    ## GRID LAYOUTS
        self.gridLayout_main = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_main.setObjectName("gridLayout_main")
        
        self.gridLayout_left = QtWidgets.QGridLayout()
        self.gridLayout_left.setObjectName("gridLayout_left")
        self.gridLayout_main.addLayout(self.gridLayout_left, 0, 0, 2, 1)
        
        self.gridLayout_centre = QtWidgets.QGridLayout()
        self.gridLayout_centre.setObjectName("gridLayout_centre")
        self.gridLayout_main.addLayout(self.gridLayout_centre, 0, 1, 2, 1)
        
        self.gridLayout_right_1 = QtWidgets.QGridLayout()
        self.gridLayout_right_1.setObjectName("gridLayout_right_1")
        self.gridLayout_main.addLayout(self.gridLayout_right_1, 0, 2, 1, 1)        
        
        self.gridLayout_right_2 = QtWidgets.QGridLayout()
        self.gridLayout_right_2.setObjectName("gridLayout_right_2")
        self.gridLayout_main.addLayout(self.gridLayout_right_2, 0, 3, 1, 1)
               
        self.gridLayout_main.setColumnStretch(0, 1)
        self.gridLayout_main.setColumnStretch(1, 8)
        self.gridLayout_main.setColumnStretch(2, 2)
        self.gridLayout_main.setColumnStretch(3, 2)
        

        self.gridLayout_H1 = QtWidgets.QGridLayout()
        self.gridLayout_H1.setObjectName("gridLayout_H1")
        self.gridLayout_right_1.addLayout(self.gridLayout_H1, 1, 0, 1, 1)
       
        self.gridLayout_H2 = QtWidgets.QGridLayout()
        self.gridLayout_H2.setObjectName("gridLayout_H2")
        self.gridLayout_right_2.addLayout(self.gridLayout_H2, 1, 0, 1, 1)

        self.gridLayout_H3 = QtWidgets.QGridLayout()
        self.gridLayout_H3.setObjectName("gridLayout_H3")
        self.gridLayout_right_1.addLayout(self.gridLayout_H3, 2, 0, 1, 1)

        self.gridLayout_H4 = QtWidgets.QGridLayout()
        self.gridLayout_H4.setObjectName("gridLayout_H4")
        self.gridLayout_right_2.addLayout(self.gridLayout_H4, 2, 0, 1, 1)

        self.gridLayout_H5 = QtWidgets.QGridLayout()
        self.gridLayout_H5.setObjectName("gridLayout_H5")
        self.gridLayout_right_1.addLayout(self.gridLayout_H5, 3, 0, 1, 1)
        
        self.gridLayout_H6 = QtWidgets.QGridLayout()
        self.gridLayout_H6.setObjectName("gridLayout_H6")
        self.gridLayout_right_2.addLayout(self.gridLayout_H6, 3, 0, 1, 1)



    ## LABELS
#        self.label_empty_row0 = QtWidgets.QLabel(self.centralwidget)
#        self.label_empty_row0.setObjectName("label_empty_row1")
#        self.gridLayout_left.addWidget(self.label_empty_row0, 0, 0 , 1, 1)
    
        self.label_GP = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_GP.setFont(font)
        self.label_GP.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_GP.setIndent(-1)
        self.label_GP.setObjectName("label_GP")
        self.gridLayout_left.addWidget(self.label_GP, 1, 0, 1, 4)
    
    
    
        self.label_length = QtWidgets.QLabel(self.centralwidget)
        self.label_length.setAlignment(QtCore.Qt.AlignCenter)
        self.label_length.setObjectName("label_length")
        self.gridLayout_left.addWidget(self.label_length, 2, 0, 1, 1)

        self.label_timeL = QtWidgets.QLabel(self.centralwidget)
        self.label_timeL.setAlignment(QtCore.Qt.AlignCenter)
        self.label_timeL.setObjectName("label_timeL")
        self.gridLayout_left.addWidget(self.label_timeL, 2, 2, 1, 1)

        self.label_pitch = QtWidgets.QLabel(self.centralwidget)
        self.label_pitch.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pitch.setObjectName("label_pitch")
        self.gridLayout_left.addWidget(self.label_pitch, 3, 0, 1, 1)

        self.label_timeP = QtWidgets.QLabel(self.centralwidget)
        self.label_timeP.setAlignment(QtCore.Qt.AlignCenter)
        self.label_timeP.setObjectName("label_timeP")
        self.gridLayout_left.addWidget(self.label_timeP, 3, 2, 1, 1)
        
        self.label_diameter = QtWidgets.QLabel(self.centralwidget)
        self.label_diameter.setAlignment(QtCore.Qt.AlignCenter)
        self.label_diameter.setObjectName("label_diameter")
        self.gridLayout_left.addWidget(self.label_diameter, 4, 0, 1, 1)
        
        self.label_timeD = QtWidgets.QLabel(self.centralwidget)
        self.label_timeD.setAlignment(QtCore.Qt.AlignCenter)
        self.label_timeD.setObjectName("label_timeD")
        self.gridLayout_left.addWidget(self.label_timeD, 4, 2, 1, 1)
      
        self.label_lattice_para_a = QtWidgets.QLabel(self.centralwidget)
        self.label_lattice_para_a.setAlignment(QtCore.Qt.AlignCenter)
        self.label_lattice_para_a.setObjectName("label_lattice_para_a")
        self.gridLayout_left.addWidget(self.label_lattice_para_a, 5, 0, 1, 1)
        
        self.label_timeA = QtWidgets.QLabel(self.centralwidget)
        self.label_timeA.setAlignment(QtCore.Qt.AlignCenter)
        self.label_timeA.setObjectName("label_timeA")
        self.gridLayout_left.addWidget(self.label_timeA, 5, 2, 1, 1)
        
        self.label_lattice_para_b = QtWidgets.QLabel(self.centralwidget)
        self.label_lattice_para_b.setAlignment(QtCore.Qt.AlignCenter)
        self.label_lattice_para_b.setObjectName("label_lattice_para_b")
        self.gridLayout_left.addWidget(self.label_lattice_para_b, 6, 0, 1, 1)
        
        self.label_timeB = QtWidgets.QLabel(self.centralwidget)
        self.label_timeB.setAlignment(QtCore.Qt.AlignCenter)
        self.label_timeB.setObjectName("label_timeB")
        self.gridLayout_left.addWidget(self.label_timeB, 6, 2, 1, 1)
    
    
#    
#        self.label_empty_row7 = QtWidgets.QLabel(self.centralwidget)
#        self.label_empty_row7.setObjectName("label_empty_row1")
#        self.gridLayout_left.addWidget(self.label_empty_row7, 7, 0 , 1, 1)
#      
        self.label_Hamiltonian = QtWidgets.QLabel(self.centralwidget)
        self.label_Hamiltonian.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Hamiltonian.setObjectName("label_Hamiltonian")
        self.gridLayout_left.addWidget(self.label_Hamiltonian, 8, 0, 1, 1)
        
#        self.label_empty_row9 = QtWidgets.QLabel(self.centralwidget)
#        self.label_empty_row9.setObjectName("label_empty_row1")
#        self.gridLayout_left.addWidget(self.label_empty_row9, 9, 0 , 1, 1)
#        
        
        
        self.label_MP = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_MP.setFont(font)
        self.label_MP.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_MP.setObjectName("label_MP")
        self.gridLayout_left.addWidget(self.label_MP, 10, 0, 1, 4)
        
        
        
        self.label_eps = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_eps.setFont(font)
        self.label_eps.setAlignment(QtCore.Qt.AlignCenter)
        self.label_eps.setObjectName("label_eps")
        self.gridLayout_left.addWidget(self.label_eps, 11, 0, 1, 1)
        
        self.label_mu = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_mu.setFont(font)
        self.label_mu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mu.setObjectName("label_mu")
        self.gridLayout_left.addWidget(self.label_mu, 11, 2, 1, 1)
        
        self.label_x1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_x1.setFont(font)
        self.label_x1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_x1.setObjectName("label_x1")
        self.gridLayout_left.addWidget(self.label_x1, 12, 0, 1, 1)
        
        self.label_x2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_x2.setFont(font)
        self.label_x2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_x2.setObjectName("label_x2")
        self.gridLayout_left.addWidget(self.label_x2, 12, 2, 1, 1)
        
        self.label_x3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_x3.setFont(font)
        self.label_x3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_x3.setObjectName("label_x3")
        self.gridLayout_left.addWidget(self.label_x3, 13, 0, 1, 1)
        
        self.label_x4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_x4.setFont(font)
        self.label_x4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_x4.setObjectName("label_x4")
        self.gridLayout_left.addWidget(self.label_x4, 13, 2, 1, 1)
        
        self.label_mass = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_mass.setFont(font)
        self.label_mass.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mass.setObjectName("label_mass")
        self.gridLayout_left.addWidget(self.label_mass, 14, 0, 1, 1)
        
        self.label_ni = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_ni.setFont(font)
        self.label_ni.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ni.setObjectName("label_ni")
        self.gridLayout_left.addWidget(self.label_ni, 14, 2, 1, 1)
        
        self.label_K = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_K.setFont(font)
        self.label_K.setAlignment(QtCore.Qt.AlignCenter)
        self.label_K.setObjectName("label_K")
        self.gridLayout_left.addWidget(self.label_K, 15, 0, 1, 1)
        
        self.label_kappa = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_kappa.setFont(font)
        self.label_kappa.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kappa.setObjectName("label_kappa")
        self.gridLayout_left.addWidget(self.label_kappa, 15, 2, 1, 1)
        
        self.label_delta = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_delta.setFont(font)
        self.label_delta.setAlignment(QtCore.Qt.AlignCenter)
        self.label_delta.setObjectName("label_delta")
        self.gridLayout_left.addWidget(self.label_delta, 16, 0, 1, 1)

        self.label_a = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_a.setFont(font)
        self.label_a.setAlignment(QtCore.Qt.AlignCenter)
        self.label_a.setObjectName("label_a")
        self.gridLayout_left.addWidget(self.label_a, 16, 2, 1, 1)
        
#        self.label_empty_row17 = QtWidgets.QLabel(self.centralwidget)
#        self.label_empty_row17.setObjectName("label_empty_row1")
#        self.gridLayout_left.addWidget(self.label_empty_row17, 17, 0 , 1, 1)
#        
#        self.label_empty_row19 = QtWidgets.QLabel(self.centralwidget)
#        self.label_empty_row19.setObjectName("label_empty_row1")
#        self.gridLayout_left.addWidget(self.label_empty_row19, 19, 0 , 1, 1)
#        
        self.label_example = QtWidgets.QLabel(self.centralwidget)
        self.label_example.setAlignment(QtCore.Qt.AlignCenter)
        self.label_example.setObjectName("label_example")
        self.gridLayout_left.addWidget(self.label_example, 24, 0, 1, 1)
       
#        self.label_empty_browse = QtWidgets.QLabel(self.centralwidget)
#        self.label_empty_browse.setObjectName("label_empty_browse")
#        self.gridLayout_H6.addWidget(self.label_empty_browse, 0, 1 , 1, 2)
        
        # Create widget
        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.pixmap = QtGui.QPixmap('super_imposed.png')
        self.pixmap = self.pixmap.scaled(340,270)
        self.label_image.setPixmap(self.pixmap)
#        self.gridLayout_left.addWidget(self.label_image,25,0,1,4)
        self.gridLayout_H5.addWidget(self.label_image, 0, 0,1,1)
#        self.label_image.resize(self.label_image.sizeHint())
        
        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.pixmap = QtGui.QPixmap('super_imposed.png')
        self.pixmap = self.pixmap.scaled(340,240)
        self.label_image.setPixmap(self.pixmap)
        self.gridLayout_H6.addWidget(self.label_image,1,0,1,2)
        
##        self.show()

    
    ## LINEEDITS
    
        self.lineEdit_length = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_length.setObjectName("lineEdit_length")
        self.gridLayout_left.addWidget(self.lineEdit_length, 2, 1, 1, 1)
        
        self.lineEdit_pitch = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pitch.setObjectName("lineEdit_pitch")
        self.gridLayout_left.addWidget(self.lineEdit_pitch, 3, 1, 1, 1)
        
        self.lineEdit_diameter = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_diameter.setObjectName("lineEdit_diameter")
        self.gridLayout_left.addWidget(self.lineEdit_diameter, 4, 1, 1, 1)
    
        self.lineEdit_lattice_para_a = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_lattice_para_a.setObjectName("lineEdit_lattice_para_a")
        self.gridLayout_left.addWidget(self.lineEdit_lattice_para_a, 5, 1, 1, 1)
      
        self.lineEdit_lattice_para_b = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_lattice_para_b.setObjectName("lineEdit_lattice_para_b")
        self.gridLayout_left.addWidget(self.lineEdit_lattice_para_b, 6, 1, 1, 1)
    
    
    
        self.lineEdit_timeL = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_timeL.setObjectName("lineEdit_timeL")
        self.gridLayout_left.addWidget(self.lineEdit_timeL, 2, 3, 1, 1)

        self.lineEdit_timeP = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_timeP.setObjectName("lineEdit_timeP")
        self.gridLayout_left.addWidget(self.lineEdit_timeP, 3, 3, 1, 1)

        self.lineEdit_timeD = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_timeD.setObjectName("lineEdit_timeD")
        self.gridLayout_left.addWidget(self.lineEdit_timeD, 4, 3, 1, 1)

        self.lineEdit_timeA = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_timeA.setObjectName("lineEdit_timeA")
        self.gridLayout_left.addWidget(self.lineEdit_timeA, 5, 3, 1, 1)

        self.lineEdit_timeB = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_timeB.setObjectName("lineEdit_timeB")
        self.gridLayout_left.addWidget(self.lineEdit_timeB, 6, 3, 1, 1)


    
        self.lineEdit_eps = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_eps.setObjectName("lineEdit_eps")
        self.gridLayout_left.addWidget(self.lineEdit_eps, 11, 1, 1, 1)
        
        self.lineEdit_mu = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_mu.setObjectName("lineEdit_mu")
        self.gridLayout_left.addWidget(self.lineEdit_mu, 11, 3, 1, 1)
               
        self.lineEdit_x1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_x1.setObjectName("lineEdit_x1")
        self.gridLayout_left.addWidget(self.lineEdit_x1, 12, 1, 1, 1)
        
        self.lineEdit_x2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_x2.setObjectName("lineEdit_x2")
        self.gridLayout_left.addWidget(self.lineEdit_x2, 12, 3, 1, 1)

        self.lineEdit_x3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_x3.setObjectName("lineEdit_x3")
        self.gridLayout_left.addWidget(self.lineEdit_x3, 13, 1, 1, 1)
    
        self.lineEdit_x4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_x4.setObjectName("lineEdit_x4")
        self.gridLayout_left.addWidget(self.lineEdit_x4, 13, 3, 1, 1)
    
        self.lineEdit_mass = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_mass.setObjectName("lineEdit_mass")
        self.gridLayout_left.addWidget(self.lineEdit_mass, 14, 1, 1, 1)
    
        self.lineEdit_ni = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ni.setObjectName("lineEdit_ni")
        self.gridLayout_left.addWidget(self.lineEdit_ni, 14, 3, 1, 1)      
        
        self.lineEdit_K = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_K.setObjectName("lineEdit_K")
        self.gridLayout_left.addWidget(self.lineEdit_K, 15, 1, 1, 1)
        
        self.lineEdit_kappa = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_kappa.setObjectName("lineEdit_kappa")
        self.gridLayout_left.addWidget(self.lineEdit_kappa, 15, 3, 1, 1)        
        
        self.lineEdit_delta = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_delta.setObjectName("lineEdit_delta")
        self.gridLayout_left.addWidget(self.lineEdit_delta, 16, 1, 1, 1)

        self.lineEdit_a = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_a.setObjectName("lineEdit_a")
        self.gridLayout_left.addWidget(self.lineEdit_a, 16, 3, 1, 1)

       
    ## PUSHBUTTONS
            
        self.pushButton_view_edit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_view_edit.setObjectName("pushButton_view_edit")
        self.gridLayout_left.addWidget(self.pushButton_view_edit, 8, 3, 1, 1)
        self.pushButton_view_edit.clicked.connect(self.func_view_edit)
    
        self.pushButton_load = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_load.setObjectName("pushButton_load")
        self.gridLayout_left.addWidget(self.pushButton_load, 18, 0, 1, 1)
        self.pushButton_load.clicked.connect(self.func_load)
        
        self.pushButton_default = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_default.setObjectName("pushButton_default")
        self.gridLayout_left.addWidget(self.pushButton_default, 18, 1, 1, 1)
        self.pushButton_default.clicked.connect(self.func_default)
        
        self.pushButton_saveasfile = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_saveasfile.setObjectName("pushButton_saveasfile")
        self.gridLayout_left.addWidget(self.pushButton_saveasfile, 18, 2, 1, 1)
        self.pushButton_saveasfile.clicked.connect(self.func_saveasfile)
                                                   
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.gridLayout_left.addWidget(self.pushButton_clear, 18, 3, 1, 1)
        self.pushButton_clear.clicked.connect(self.func_clear)       

        self.pushButton_show_change = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_show_change.setFont(font)
        self.pushButton_show_change.setObjectName("pushButton_show_change")
        self.gridLayout_left.addWidget(self.pushButton_show_change, 20, 1, 1, 2)
        self.pushButton_show_change.clicked.connect(self.func_show_change)
       
        self.pushButton_run = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_run.setCheckable(True)
        self.pushButton_run.setObjectName("pushButton_run")
        self.gridLayout_left.addWidget(self.pushButton_run, 24, 3, 1, 1)
        self.pushButton_run.clicked.connect(self.func_run)
        
        self.pushButton_screenshot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_screenshot.setObjectName("pushButton_screenshot")
        self.gridLayout_left.addWidget(self.pushButton_screenshot, 23, 0, 1, 2)
        self.pushButton_screenshot.clicked.connect(self.func_screenshot)
        
        
        self.pushButton_super_impose = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_super_impose.setObjectName("pushButton_super_impose")
        self.gridLayout_left.addWidget(self.pushButton_super_impose, 23, 2, 1, 2)
        self.pushButton_super_impose.clicked.connect(self.func_super_impose)
        
        
#        self.pushButton_timer = QtWidgets.QPushButton(self.centralwidget)
#        self.pushButton_timer.setCheckable(True)
#        self.pushButton_timer.setObjectName("pushButton_timer")
#        self.gridLayout_centre.addWidget(self.pushButton_timer, 4, 3, 1, 1)
        
        self.pushButton_export_video = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_export_video.setObjectName("pushButton_export_video")
        self.pushButton_export_video.setCheckable(True)
        self.gridLayout_centre.addWidget(self.pushButton_export_video, 4, 4, 1, 1)
        self.pushButton_export_video.clicked.connect(self.func_export_video)

        self.pushButton_pauseNplay_main = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pauseNplay_main.setCheckable(True)
        self.pushButton_pauseNplay_main.setObjectName("pushButton_pauseNplay_main")
        self.gridLayout_centre.addWidget(self.pushButton_pauseNplay_main, 3, 3, 1, 2)
        self.pushButton_pauseNplay_main.clicked.connect(self.pauseNplay)

        
        self.pushButton_freeze_for_image = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_freeze_for_image.setObjectName("pushButton_freeze_for_image")
        self.gridLayout_centre.addWidget(self.pushButton_freeze_for_image, 3, 0, 1, 1)
        self.pushButton_freeze_for_image.clicked.connect(self.freeze_for_image)
        
        self.pushButton_browse = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_browse.setObjectName("pushButton_browse")
        self.gridLayout_H6.addWidget(self.pushButton_browse, 0, 0, 1, 1)
        self.pushButton_browse.clicked.connect(self.func_browse)
        
        self.pushButton_process = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_process.setObjectName("pushButton_process")
        self.gridLayout_H6.addWidget(self.pushButton_process, 0, 1, 1, 1)
        self.pushButton_process.clicked.connect(self.func_process)
        
#        self.pushButton_pauseNplay_H3 = QtWidgets.QPushButton(self.centralwidget)
#        self.pushButton_pauseNplay_H3.setCheckable(True)
#        self.pushButton_pauseNplay_H3.setObjectName("pushButton_pauseNplay_H3")
#        self.gridLayout_H3.addWidget(self.pushButton_pauseNplay_H3, 1, 0, 1, 1)
#        
#        self.pushButton_pauseNplay_H2 = QtWidgets.QPushButton(self.centralwidget)
#        self.pushButton_pauseNplay_H2.setCheckable(True)
#        self.pushButton_pauseNplay_H2.setObjectName("pushButton_pauseNplay_H2")
#        self.gridLayout_H2.addWidget(self.pushButton_pauseNplay_H2, 1, 0, 1, 1)
#      
#        self.pushButton_pauseNplay_H4 = QtWidgets.QPushButton(self.centralwidget)
#        self.pushButton_pauseNplay_H4.setCheckable(True)
#        self.pushButton_pauseNplay_H4.setObjectName("pushButton_pauseNplay_H4")
#        self.gridLayout_H4.addWidget(self.pushButton_pauseNplay_H4, 1, 0, 1, 1)
#       
#        self.pushButton_pauseNplay_H = QtWidgets.QPushButton(self.centralwidget)
#        self.pushButton_pauseNplay_H.setCheckable(True)
#        self.pushButton_pauseNplay_H.setObjectName("pushButton_pauseNplay_H")
#        self.gridLayout_H5.addWidget(self.pushButton_pauseNplay_H, 1, 0, 1, 1)
#        
#        self.pushButton_pauseNplay_H1 = QtWidgets.QPushButton(self.centralwidget)
#        self.pushButton_pauseNplay_H1.setCheckable(True)
#        self.pushButton_pauseNplay_H1.setObjectName("pushButton_pauseNplay_H1")
#        self.gridLayout_H1.addWidget(self.pushButton_pauseNplay_H1, 1, 0, 1, 1)
#        
#        self.pushButton_pauseNplay_H6 = QtWidgets.QPushButton(self.centralwidget)
#        self.pushButton_pauseNplay_H6.setCheckable(True)
#        self.pushButton_pauseNplay_H6.setObjectName("pushButton_pauseNplay_H6")
#        self.gridLayout_H6.addWidget(self.pushButton_pauseNplay_H6, 1, 0, 1, 1)
        
       
    ## RADIO BUTTONS
        self.radioButton_H4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_H4.setObjectName("radioButton_H4")
        self.gridLayout_centre.addWidget(self.radioButton_H4, 1, 3, 1, 1)
        self.radioButton_H4.clicked.connect(lambda:self.main_animation(4))
        
        self.radioButton_H1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_H1.setObjectName("radioButton_H1")
        self.gridLayout_centre.addWidget(self.radioButton_H1, 1, 0, 1, 1)
        self.radioButton_H1.clicked.connect(lambda:self.main_animation(1))
        
        self.radioButton_H = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_H.setChecked(True)
        self.radioButton_H.setObjectName("radioButton_H")
        self.gridLayout_centre.addWidget(self.radioButton_H, 1, 4, 1, 1)
        self.radioButton_H.clicked.connect(lambda:self.main_animation(5))
        
        self.radioButton_H3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_H3.setObjectName("radioButton_H3")
        self.gridLayout_centre.addWidget(self.radioButton_H3, 1, 2, 1, 1)
        self.radioButton_H3.clicked.connect(lambda:self.main_animation(3))
        
        self.radioButton_H2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_H2.setObjectName("radioButton_H2")
        self.gridLayout_centre.addWidget(self.radioButton_H2, 1, 1, 1, 1)
        self.radioButton_H2.clicked.connect(lambda:self.main_animation(2))
   
    
    ## DROPDOWN COMBOBOX
    
        self.comboBox_examples = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_examples.setObjectName("comboBox_examples")
        self.comboBox_examples.addItem("")
        self.comboBox_examples.addItem("")
        self.comboBox_examples.addItem("")
        self.comboBox_examples.addItem("")
        self.comboBox_examples.addItem("")
        self.comboBox_examples.addItem("")
        self.comboBox_examples.addItem("")
#        self.comboBox_examples.addItem("")
#        self.comboBox_examples.addItem("")
#        self.comboBox_examples.addItem("")
        self.gridLayout_left.addWidget(self.comboBox_examples, 24, 1, 1, 2)
        
        
        self.comboBox_Hamiltonian = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Hamiltonian.setEditable(False)
        self.comboBox_Hamiltonian.setObjectName("comboBox_Hamiltonian")
        self.comboBox_Hamiltonian.addItem("")
        self.comboBox_Hamiltonian.addItem("")
        self.comboBox_Hamiltonian.addItem("")
        self.comboBox_Hamiltonian.addItem("")
        self.comboBox_Hamiltonian.addItem("")
        self.comboBox_Hamiltonian.addItem("")
        self.comboBox_Hamiltonian.addItem("")
        self.gridLayout_left.addWidget(self.comboBox_Hamiltonian, 8, 1, 1, 2)
        


    ## Graphics View
        
        
    
#        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
#        self.graphicsView.setObjectName("graphicsView")
#        self.gridLayout_left.addWidget(self.graphicsView, 22, 0, 1, 4)
        
#        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
#        self.graphicsView_2.setObjectName("graphicsView_2")
#        self.gridLayout_left.addWidget(self.graphicsView_2, 24, 0, 1, 4)
       
        self.container_main=QtWidgets.QWidget()
        self.mayavi_widget_main = Gui_animation.MayaviQWidget_main(self.container_main)
        self.gridLayout_centre.addWidget(self.mayavi_widget_main,2,0,1,5)
        
        container_H1 = QtWidgets.QWidget()
        mayavi_widget_H1 = GuiFromScratch_mayavi.MayaviQWidget_H1(container_H1)
        self.gridLayout_H1.addWidget(mayavi_widget_H1, 0, 0,1,1)
        
        container_H2 = QtWidgets.QWidget()
        mayavi_widget_H2 = GuiFromScratch_mayavi.MayaviQWidget_H2(container_H2)
        self.gridLayout_H2.addWidget(mayavi_widget_H2, 0, 0,1,1)
        
        container_H3 = QtWidgets.QWidget()
        mayavi_widget_H3 = GuiFromScratch_mayavi.MayaviQWidget_H3(container_H3)
        self.gridLayout_H3.addWidget(mayavi_widget_H3, 0, 0,1,1)
        
        container_H4 = QtWidgets.QWidget()
        mayavi_widget_H4 = GuiFromScratch_mayavi.MayaviQWidget_H4(container_H4)
        self.gridLayout_H4.addWidget(mayavi_widget_H4, 0, 0,1,1)
        
        container_H5 = QtWidgets.QWidget()
        mayavi_widget_H5 = GuiFromScratch_mayavi.MayaviQWidget_H5(container_H5)
        self.gridLayout_left.addWidget(mayavi_widget_H5,25,0,1,4)
        
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_H5.addWidget(self.graphicsView, 0, 0, 1, 1)
        
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.gridLayout_H6.addWidget(self.graphicsView_2, 1, 0, 1, 2)

        
        

#        container_H6 = QtWidgets.QWidget()
#        mayavi_widget_H6 = GuiFromScratch_mayavi.MayaviQWidget_H6(container_H6)
#        self.gridLayout_H6.addWidget(mayavi_widget_H6, 1, 0,1,1)          
        
        
        self.container_left=QtWidgets.QWidget()
        self.mayavi_widget_left = Gui_mayavi_leftPanel.MayaviQWidget(self.container_left)
        self.gridLayout_left.addWidget(self.mayavi_widget_left,22, 0, 1, 4)
        
    ## SPACER
#        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
#        self.gridLayout_left.addItem(spacerItem, 22, 1, 1, 1)
#        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
#        self.gridLayout_left.addItem(spacerItem, 24, 1, 1, 1)
    
    
    ## DOUBLE SPIN BOX
        self.doubleSpinBox_timer = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_timer.setMaximum(100.0)
        self.doubleSpinBox_timer.setProperty("value", 20.0)
        self.doubleSpinBox_timer.setObjectName("doubleSpinBox_timer")
        self.gridLayout_centre.addWidget(self.doubleSpinBox_timer, 4, 3, 1, 1)
        
        
        
        

    
      
      
        
       
         
        
           
         
        
    ## MENU BAR
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1140, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionLoad.triggered.connect(self.func_load)
        
        
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.triggered.connect(self.func_saveasfile)
        
        
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionSource_Code = QtWidgets.QAction(MainWindow)
        self.actionSource_Code.setObjectName("actionSource_Code")
        self.actionFormulation = QtWidgets.QAction(MainWindow)
        self.actionFormulation.setObjectName("actionFormulation")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionSave_as.triggered.connect(self.func_saveasfile)
        
#        self.actionSave_All = QtWidgets.QAction(MainWindow)
#        self.actionSave_All.setObjectName("actionSave_All")
        self.actionTheme = QtWidgets.QAction(MainWindow)
        self.actionTheme.setObjectName("actionTheme")
        self.actionLanguage = QtWidgets.QAction(MainWindow)
        self.actionLanguage.setObjectName("actionLanguage")
#        self.actionLoad_Recent_Data = QtWidgets.QAction(MainWindow)
#        self.actionLoad_Recent_Data.setObjectName("actionLoad_Recent_Data")
        self.actionPrint = QtWidgets.QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit.triggered.connect(self.close)
        
        self.menuFile.addAction(self.actionLoad)
#        self.menuFile.addAction(self.actionLoad_Recent_Data)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
#        self.menuFile.addAction(self.actionSave_All)
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addAction(self.actionSource_Code)
        self.menuHelp.addAction(self.actionFormulation)
        self.menuHelp.addAction(self.actionAbout)
        self.menuSettings.addAction(self.actionTheme)
        self.menuSettings.addAction(self.actionLanguage)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
    
    ##  Mayavi Animation widget
        self.mayavi_widget_main = Gui_animation.MayaviQWidget_main(self.container_main)
        self.gridLayout_centre.addWidget(self.mayavi_widget_main,2,0,1,5)
        


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
   
    
    def close(self):
        sys.exit()
        
    def default_value_function(self):
        L,P,D,A,B= '3.00','3.00','3.00','2.3','2.7'
        TL,TP,TD,TA,TB='0.05','0.05','0.05','0.05','0.05'
        
        eps,mu,x1,x2,x3,x4,mass,ni,K,kappa,delta,a = '0.23','0.354','0.5265','0.56','0.56','0.61','0.12','0.32','0.52','0.78','0.921','0.01'
       
        with open("user_data.txt", "w") as f:
                f.write(f"{L},{P},{D},{A},{B},{TL},{TP},{TD},{TA},{TB},{eps},{mu},{x1},{x2},{x3},{x4},{mass},{ni},{K},{kappa},{delta},{a}")
        f.close()


    def func_load(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None,"Open File","","Text File (*.txt);;All Files (*)",os.path.dirname(os.path.realpath(__file__)), options=options)
        if fileName:
            print(fileName)
        if fileName:
            with open(fileName,"r") as f:
                L,P,D,A,B,TL,TP,TD,TA,TB,eps,mu,x1,x2,x3,x4,mass,ni,K,kappa,delta,a=f.read().split(",") 
        else:
            print("Invalid / Corrupted File")
        
        self.lineEdit_length.setText(L)
        self.lineEdit_pitch.setText(P)
        self.lineEdit_diameter.setText(D)        
        self.lineEdit_lattice_para_b.setText(A)
        self.lineEdit_lattice_para_a.setText(B)    
        self.lineEdit_timeL.setText(TL)
        self.lineEdit_timeP.setText(TP)
        self.lineEdit_timeD.setText(TD)
        self.lineEdit_timeA.setText(TA)
        self.lineEdit_timeB.setText(TB)
        
        self.lineEdit_eps.setText(eps)
        self.lineEdit_mu.setText(mu)
        self.lineEdit_x1.setText(x1)
        self.lineEdit_x2.setText(x2)
        self.lineEdit_x3.setText(x3)
        self.lineEdit_x4.setText(x4)
        self.lineEdit_mass.setText(mass)
        self.lineEdit_ni.setText(ni)
        self.lineEdit_K.setText(K)
        self.lineEdit_kappa.setText(kappa)
        self.lineEdit_delta.setText(delta)
        self.lineEdit_a.setText(a)
        
        
        
        
        
        
            
    def func_default(self):
        print("functioning_default")
        L,P,D,A,B= '3.00','3.00','3.00','2.3','2.7'
        TL,TP,TD,TA,TB='0.05','0.05','0.05','0.05','0.05'
        
        eps,mu,x1,x2,x3,x4,mass,ni,K,kappa,delta,a = '0.23','0.354','0.5265','0.56','0.56','0.61','0.12','0.32','0.52','0.78','0.921','0.01'
        
        self.lineEdit_length.setText(L)
        self.lineEdit_pitch.setText(P)
        self.lineEdit_diameter.setText(D)        
        self.lineEdit_lattice_para_b.setText(A)
        self.lineEdit_lattice_para_a.setText(B)    
        self.lineEdit_timeL.setText(TL)
        self.lineEdit_timeP.setText(TP)
        self.lineEdit_timeD.setText(TD)
        self.lineEdit_timeA.setText(TA)
        self.lineEdit_timeB.setText(TB)
        
        self.lineEdit_eps.setText(eps)
        self.lineEdit_mu.setText(mu)
        self.lineEdit_x1.setText(x1)
        self.lineEdit_x2.setText(x2)
        self.lineEdit_x3.setText(x3)
        self.lineEdit_x4.setText(x4)
        self.lineEdit_mass.setText(mass)
        self.lineEdit_ni.setText(ni)
        self.lineEdit_K.setText(K)
        self.lineEdit_kappa.setText(kappa)
        self.lineEdit_delta.setText(delta)
        self.lineEdit_a.setText(a)
        
        
         
    def func_saveasfile(self):
        print("save as file")                       
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(None,"Save File","data.txt","Text Files (*.txt);;All Files (*)", options=options)
        if fileName:
            print(fileName)
            L=float(self.lineEdit_length.text())
            P=float(self.lineEdit_pitch.text())
            D=float(self.lineEdit_diameter.text()) 
            A=float(self.lineEdit_pitch.text())
            B=float(self.lineEdit_diameter.text()) 
            TL=float(self.lineEdit_timeL.text())
            TP=float(self.lineEdit_timeP.text())
            TD=float(self.lineEdit_timeD.text())
            TA=float(self.lineEdit_timeA.text())
            TB=float(self.lineEdit_timeB.text())
            
            eps=float(self.lineEdit_eps.text())
            mu=float(self.lineEdit_mu.text())
            x1=float(self.lineEdit_x1.text())
            x2=float(self.lineEdit_x2.text())
            x3=float(self.lineEdit_x3.text())
            x4=float(self.lineEdit_x4.text())
            mass=float(self.lineEdit_mass.text())
            ni=float(self.lineEdit_ni.text())
            K=float(self.lineEdit_K.text())
            kappa=float(self.lineEdit_kappa.text())
            delta=float(self.lineEdit_delta.text())
            a=float(self.lineEdit_a.text())
        
            with open(fileName, "w") as f:
                f.write(f"{L},{P},{D},{A},{B},{TL},{TP},{TD},{TA},{TB},{eps},{mu},{x1},{x2},{x3},{x4},{mass},{ni},{K},{kappa},{delta},{a}")
            
            
    def func_clear(self):
        print("functioning_clear")
        length,pitch,diameter,lattice_para_a, lattice_para_b= '','','','',''
        timeL,timeP,timeD,timeA,timeB='','','','',''
        eps,mu,x1,x2,x3,x4,mass,ni,K,kappa,delta,a='','','','','','','','','','','',''
        self.lineEdit_length.setText(length)
        self.lineEdit_pitch.setText(pitch)
        self.lineEdit_diameter.setText(diameter)        
        self.lineEdit_lattice_para_b.setText(lattice_para_b)
        self.lineEdit_lattice_para_a.setText(lattice_para_a)
        self.lineEdit_timeL.setText(timeL)
        self.lineEdit_timeP.setText(timeP)
        self.lineEdit_timeD.setText(timeD)
        self.lineEdit_timeA.setText(timeA)
        self.lineEdit_timeB.setText(timeB)
        
        self.lineEdit_eps.setText(eps)
        self.lineEdit_mu.setText(mu)
        self.lineEdit_x1.setText(x1)
        self.lineEdit_x2.setText(x2)
        self.lineEdit_x3.setText(x3)
        self.lineEdit_x4.setText(x4)
        self.lineEdit_mass.setText(mass)
        self.lineEdit_ni.setText(ni)
        self.lineEdit_K.setText(K)
        self.lineEdit_kappa.setText(kappa)
        self.lineEdit_delta.setText(delta)
        self.lineEdit_a.setText(a)
        
    def func_show(self):
        print("coming soon!!")
        

    def func_view_edit(self):
        index_hamiltonian = self.comboBox_Hamiltonian.currentIndex()-1
        if index_hamiltonian>=0:
            print("yes")
            '''H="H1","H2","H3","H4","H","All"
            
            
            
            text, okPressed = QInputDialog.getText(None, "Hamiltonian Equation",H[index_hamiltonian], QLineEdit.Normal, H[index_hamiltonian])
            if okPressed and text != '':
                print(text) '''

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Hamiltonian Equation")
        
        
        H=[]
        H.append('This is H1')
        H.append('This is H2')
        H.append('This is H3')
        H.append('This is H4')
        H.append('This is H')
        
        msg.setText(H[index_hamiltonian])
        msg.setInformativeText("This is additional information")
        
#        msg.addButton(QtWidgets.QPushButton('Edit'),QMessageBox.YesRole )
        #msg.additem
        
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
#        retval = msg.exec_()
        '''if retval==0:
            dialog = QtWidgets.QInputDialog(None)
            dialog.resize(QtCore.QSize(1000, 1000))
            dialog.setWindowTitle("Import website")
            dialog.setLabelText(H[index_hamiltonian])
            dialog.setTextValue(H[index_hamiltonian])
            dialog.setTextEchoMode(QtWidgets.QLineEdit.Normal)
            
            
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                i = dialog.textValue()
                print(i)'''
#        text, okPressed = QInputDialog.getText(None, "Hamiltonian Equation",H[index_hamiltonian], QLineEdit.Normal, H[index_hamiltonian])
#        if okPressed and text != '':
#            print(text)
#            print(retval)
            
            
    def func_show_change(self):
        print("show/change working")
        L=float(self.lineEdit_length.text())
        P=float(self.lineEdit_pitch.text())
        D=float(self.lineEdit_diameter.text()) 
        A=float(self.lineEdit_pitch.text())
        B=float(self.lineEdit_diameter.text()) 
        TL=float(self.lineEdit_timeL.text())
        TP=float(self.lineEdit_timeP.text())
        TD=float(self.lineEdit_timeD.text())
        TA=float(self.lineEdit_timeA.text())
        TB=float(self.lineEdit_timeB.text())
        
        eps=float(self.lineEdit_eps.text())
        mu=float(self.lineEdit_mu.text())
        x1=float(self.lineEdit_x1.text())
        x2=float(self.lineEdit_x2.text())
        x3=float(self.lineEdit_x3.text())
        x4=float(self.lineEdit_x4.text())
        mass=float(self.lineEdit_mass.text())
        ni=float(self.lineEdit_ni.text())
        K=float(self.lineEdit_K.text())
        kappa=float(self.lineEdit_kappa.text())
        delta=float(self.lineEdit_delta.text())
        a=float(self.lineEdit_a.text())
        
        with open("user_data.txt","w") as f:
            f.write(f"{L},{P},{D},{A},{B},{TL},{TP},{TD},{TA},{TB},{eps},{mu},{x1},{x2},{x3},{x4},{mass},{ni},{K},{kappa},{delta},{a}")
        f.close() 
        
        GuiFromScratch_mayavi.change_plots()
#        Gui_animation.change_animations()
        self.radioButton_H.setChecked(True)
        self.mayavi_widget_main = Gui_animation.MayaviQWidget_main(self.container_main)
        self.gridLayout_centre.addWidget(self.mayavi_widget_main,2,0,1,5)
        
        
        
#    def main_animation(self,user_selection):
#        
##        self.gridLayout_centre.removeWidget(self.mayavi_widget_main)
##        sip.delete(self.mayavi_widget_main)
##        self.mayavi_widget_main = None
#        print(user_selection)
##        self.container_main=QtWidgets.QWidget()
#        self.mayavi_widget_main = Gui_animation.MayaviQWidget_main(self.container_main)
#        self.gridLayout_centre.addWidget(self.mayavi_widget_main,2,0,1,5)
#        self.main_animation(user_selection)
##        Gui_animation.MayaviQWidget_main.stop_previous_animation(self)
##        #temp='MayaviQWidget_main'+ str(user_selection)
#        #print(temp)
#        #temp=Gui_animation.change_selected_H(user_selection)
#                #getattr(Gui_animation,temp)(self.container_main)
#        #self.gridLayout_centre.addWidget(self.mayavi_widget_main,2,0,1,5)
    
    def main_animation(self,user_selection):
        print("main_animation")
        Gui_animation.change_selected_H(user_selection)
        
        
    def pauseNplay(self):
        if self.pushButton_pauseNplay_main.text()=="Pause": 
            Gui_animation.pause_animation()
            self.pushButton_pauseNplay_main.setText("Play")
            
        else:
            Gui_animation.play_animation()
            self.pushButton_pauseNplay_main.setText("Pause")
            
        print("coming soon!!")
        
    def freeze_for_image(self):
        time1,time2,time3=Gui_animation.get_time()
        print(time1,time2,time3)
        Gui_mayavi_leftPanel.get_time(time1,time2,time3,1)
        self.radioButton_H.setChecked(True)
        self.mayavi_widget_main = Gui_animation.MayaviQWidget_main(self.container_main)
        self.gridLayout_centre.addWidget(self.mayavi_widget_main,2,0,1,5)
        
    def func_screenshot(self):
        print("lets capture the flag !!")
        Gui_mayavi_leftPanel.take_screenshot()
        
    def func_super_impose(self):
        Gui_mayavi_leftPanel.make_count_zero()
        Gui_image_leftPanel.overlay_images()
        
        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.pixmap = QtGui.QPixmap('super_imposed.png')
        self.pixmap = self.pixmap.scaled(340,270)
        self.label_image.setPixmap(self.pixmap)
        self.gridLayout_H5.addWidget(self.label_image,0,0,1,4)
        
    def func_browse(self):
        print("lets browse something new!!")
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None,"Open File","","Text File (*.jpg);;All Files (*)",os.path.dirname(os.path.realpath(__file__)), options=options)
        if fileName:
            print(fileName)
                  # Create widget
            self.label_image_exp = QtWidgets.QLabel(self.centralwidget)
            self.pixmap = QtGui.QPixmap(fileName)
            self.pixmap = self.pixmap.scaled(340,240)
            self.label_image_exp.setPixmap(self.pixmap)
    #        self.gridLayout_left.addWidget(self.label_image_exp,25,0,1,4)
            self.gridLayout_H6.addWidget(self.label_image_exp, 1, 0,1,2)
    #        self.label_image_exp.resize(self.label_image_exp.sizeHint())
            Gui_img_processing_PyQt5.get_image_path(fileName)
    def func_process(self):
#        print("function process")
        circles_image_path=Gui_img_processing_PyQt5.process_image()
        print(circles_image_path)
        self.label_image_exp = QtWidgets.QLabel(self.centralwidget)
        self.pixmap = QtGui.QPixmap(circles_image_path)
        self.pixmap = self.pixmap.scaled(340,240)
        self.label_image_exp.setPixmap(self.pixmap)
        self.gridLayout_H6.addWidget(self.label_image_exp, 1, 0,1,2)
    def func_export_video(self):
        
        time = self.doubleSpinBox_timer.value()
        print(time)
        Gui_animation.trig_video(int(time))

    def func_run(self):
        print("Run")
        
#        if fileName:
#            print(fileName)
#                  # Create widget
#            self.label_image_exp = QtWidgets.QLabel(self.centralwidget)
#            self.pixmap = QtGui.QPixmap(fileName)
#            self.pixmap = self.pixmap.scaled(340,240)
#            self.label_image_exp.setPixmap(self.pixmap)
#    #        self.gridLayout_left.addWidget(self.label_image_exp,25,0,1,4)
#            self.gridLayout_H6.addWidget(self.label_image_exp, 1, 0,1,2)
#    #        self.label_image_exp.resize(self.label_image_exp.sizeHint())
#            Gui_img_processing_PyQt5.get_image_path(fileName)
        
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Magnetic Vortex Simulator"))
        
        self.label_GP.setText(_translate("MainWindow", "Geometric Parameters"))
        
        self.label_length.setText(_translate("MainWindow", "Length"))
        self.label_pitch.setText(_translate("MainWindow", "Pitch"))
        self.label_diameter.setText(_translate("MainWindow", "Diameter"))
        self.label_lattice_para_a.setText(_translate("MainWindow", "Lattice Param (a)"))
        self.label_lattice_para_b.setText(_translate("MainWindow", "Lattice Param (b)"))
        self.label_timeL.setText(_translate("MainWindow", "Time (L)"))
        self.label_timeP.setText(_translate("MainWindow", "Time (P)"))
        self.label_timeD.setText(_translate("MainWindow", "Time (D)"))
        self.label_timeA.setText(_translate("MainWindow", "Time (a)"))
        self.label_timeB.setText(_translate("MainWindow", "Time (b)"))
        self.label_Hamiltonian.setText(_translate("MainWindow", "Hamiltonian"))
        
        self.label_MP.setText(_translate("MainWindow", "Material Properties"))

        self.label_eps.setText(_translate("MainWindow", "ε"))
        self.label_mu.setText(_translate("MainWindow", "μ"))
        self.label_x1.setText(_translate("MainWindow", "x₁"))
        self.label_x2.setText(_translate("MainWindow", "x₂"))
        self.label_x3.setText(_translate("MainWindow", "x₃"))
        self.label_x4.setText(_translate("MainWindow", "x₄"))
        self.label_mass.setText(_translate("MainWindow", "m*"))
        self.label_ni.setText(_translate("MainWindow", "nᵢ"))
        self.label_K.setText(_translate("MainWindow", "K"))
        self.label_kappa.setText(_translate("MainWindow", "k"))
        self.label_delta.setText(_translate("MainWindow", "δ"))
        self.label_a.setText(_translate("MainWindow", "a"))
#        self.label_empty_browse.setText(_translate("MainWindow", "                                  "))
        
        self.label_example.setText(_translate("MainWindow", "Examples"))
           
          
        
        self.lineEdit_lattice_para_a.setText(_translate("MainWindow", "2.3"))
        self.lineEdit_timeA.setText(_translate("MainWindow", "0.05"))
        self.lineEdit_timeD.setText(_translate("MainWindow", "0.05"))
        self.lineEdit_length.setText(_translate("MainWindow", "3.00"))
        self.lineEdit_timeB.setText(_translate("MainWindow", "0.05"))
        self.lineEdit_lattice_para_b.setText(_translate("MainWindow","2.7"))
        self.lineEdit_timeL.setText(_translate("MainWindow", "0.05"))
        self.lineEdit_pitch.setText(_translate("MainWindow", "3.00"))
        self.lineEdit_timeP.setText(_translate("MainWindow", "0.05"))
        self.lineEdit_diameter.setText(_translate("MainWindow", "3.00"))
        
        self.lineEdit_eps.setText(_translate("MainWindow", "0.2"))
        self.lineEdit_mu.setText(_translate("MainWindow", "0.25"))
        self.lineEdit_x1.setText(_translate("MainWindow", "0.4"))
        self.lineEdit_x2.setText(_translate("MainWindow", "0.56"))
        self.lineEdit_x3.setText(_translate("MainWindow", "0.64  "))
        self.lineEdit_x4.setText(_translate("MainWindow", "0.54"))
        self.lineEdit_mass.setText(_translate("MainWindow", "0.62"))
        self.lineEdit_ni.setText(_translate("MainWindow", "0.12"))
        self.lineEdit_K.setText(_translate("MainWindow", "0.60"))
        self.lineEdit_kappa.setText(_translate("MainWindow", "0.21"))
        self.lineEdit_delta.setText(_translate("MainWindow", "0.32"))
        self.lineEdit_a.setText(_translate("MainWindow", "0.51"))
        
        
        self.pushButton_run.setText(_translate("MainWindow", "Run"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear"))
        self.pushButton_default.setText(_translate("MainWindow", "Default"))
        self.pushButton_saveasfile.setText(_translate("MainWindow", "Save as File"))
        self.pushButton_load.setText(_translate("MainWindow", "Load"))
        self.pushButton_show_change.setText(_translate("MainWindow", "Show / Change"))
        self.pushButton_screenshot.setText(_translate("MainWindow", "Screenshot"))
        self.pushButton_super_impose.setText(_translate("MainWindow", "Superimpose"))
        self.pushButton_view_edit.setText(_translate("MainWindow", "View / Edit"))
        self.pushButton_pauseNplay_main.setText(_translate("MainWindow", "Pause"))
#        self.pushButton_pauseNplay_H3.setText(_translate("MainWindow", "Pause"))
#        self.pushButton_pauseNplay_H2.setText(_translate("MainWindow", "Pause"))
#        self.pushButton_pauseNplay_H4.setText(_translate("MainWindow", "Pause"))
#        self.pushButton_pauseNplay_H.setText(_translate("MainWindow", "Pause"))
#        self.pushButton_pauseNplay_H1.setText(_translate("MainWindow", "Pause"))
#        self.pushButton_pauseNplay_H6.setText(_translate("MainWindow", "Pause"))
#        self.pushButton_timer.setText(_translate("MainWindow", "Set Timer"))
        self.pushButton_export_video.setText(_translate("MainWindow", "Export Video"))
        self.pushButton_freeze_for_image.setText(_translate("MainWindow", "Freeze Image / Start Animation"))
        self.pushButton_browse.setText(_translate("MainWindow", "Browse"))
        self.pushButton_process.setText(_translate("MainWindow", "Process"))
        
        self.comboBox_examples.setItemText(0, _translate("MainWindow", "Select"))
        self.comboBox_examples.setItemText(1, _translate("MainWindow", "PCMS"))
        self.comboBox_examples.setItemText(2, _translate("MainWindow", "Jayant"))
        self.comboBox_examples.setItemText(3, _translate("MainWindow", "PCMS+DNA"))
        self.comboBox_examples.setItemText(4, _translate("MainWindow", "Cinnamic"))
        self.comboBox_examples.setItemText(5, _translate("MainWindow", "CNT"))
        self.comboBox_examples.setItemText(6, _translate("MainWindow", "CNT(2)"))
#        self.comboBox_examples.setItemText(7, _translate("MainWindow", "Nanobrain (NB)"))
#        self.comboBox_examples.setItemText(8, _translate("MainWindow", "DNA"))
#        self.comboBox_examples.setItemText(9, _translate("MainWindow", "DNA+NB"))
        
        
        self.comboBox_Hamiltonian.setItemText(0, _translate("MainWindow", "Select"))
        self.comboBox_Hamiltonian.setItemText(1, _translate("MainWindow", "H1"))
        self.comboBox_Hamiltonian.setItemText(2, _translate("MainWindow", "H2"))
        self.comboBox_Hamiltonian.setItemText(3, _translate("MainWindow", "H3"))
        self.comboBox_Hamiltonian.setItemText(4, _translate("MainWindow", "H4"))
        self.comboBox_Hamiltonian.setItemText(5, _translate("MainWindow", " H=H1+H2+H3+H4"))
        self.comboBox_Hamiltonian.setItemText(6, _translate("MainWindow", "All"))
         
        self.radioButton_H4.setText(_translate("MainWindow", "H4"))
        self.radioButton_H1.setText(_translate("MainWindow", "H1"))
        self.radioButton_H.setText(_translate("MainWindow", "H=H1 + H2 + H3 + H4"))
        self.radioButton_H3.setText(_translate("MainWindow", "H3"))
        self.radioButton_H2.setText(_translate("MainWindow", "H2"))
        
        
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))
        self.actionSource_Code.setText(_translate("MainWindow", "Source Code"))
        self.actionFormulation.setText(_translate("MainWindow", "Formulation"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionSave_as.setText(_translate("MainWindow", "Save As"))
#        self.actionSave_All.setText(_translate("MainWindow", "Save All"))
        self.actionTheme.setText(_translate("MainWindow", "Themes"))
        self.actionLanguage.setText(_translate("MainWindow", "Language"))
#        self.actionLoad_Recent_Data.setText(_translate("MainWindow", "Load Recent Data"))
        self.actionPrint.setText(_translate("MainWindow", "Print"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        
        
        
if __name__ == "__main__":
    import sys
       
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

