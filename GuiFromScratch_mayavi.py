# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 17:38:34 2019

@author: lab_pc
"""

import os
import numpy as np
from numpy import cos,sin
from mayavi.mlab import contour3d
from mayavi import mlab

os.environ['ETS_TOOLKIT'] = 'qt4'
from pyface.qt import QtGui
from traits.api import HasTraits, Instance, on_trait_change
from traitsui.api import View, Item
from mayavi.core.ui.api import MayaviScene, MlabSceneModel,SceneEditor

global L,P,D,A,B,TL,TP,TD,TA,TB,eps,mu,x1,x2,x3,x4,mass,ni,K,kappa,delta,a
global obj1
#####################################################################
            #         VISUALIZATION FUNCTIONS              #
#####################################################################
            
def change_plots():
    global L,P,D,A,B,TL,TP,TD,TA,TB,eps,mu,x1,x2,x3,x4,mass,ni,K,kappa,delta,a
    
    Visualization_H1.trigger()
    Visualization_H2.trigger()
    Visualization_H3.trigger()
    Visualization_H4.trigger()
    Visualization_H5.trigger()
#    Visualization_H6.trigger()
    #Visualization_H1.update_plot(self)
    
    
def get_H(selected_H):
    get_user_data()
    x, y, z = np.ogrid[-L:L:60j, -P:P:60j, -D:D:60j]
    t=0
    if selected_H==1:    
       H=  ((0.5  +  (x*cos(t))*(x*cos(t)) + 
             (y*cos(t))*(y*cos(t)) - (z*cos(t))*(z*cos(t))  )
                * (x**2 + y**2+ z**2-0.00000000000001)   )
    if selected_H==2:
        H= ( (1.5 + (x*z*y*cos(t)*cos(t)*cos(t))*(((cos(x*cos(t)))**2) + 0.5*(sin(x*cos(t)))**2)**0.5)
                *(x**2 + y**2+ z**2-0.0000000000005) )
    if selected_H==3:
        H= (    (3*cos(x*cos(t))+3*cos(y*cos(t))+3*cos(z*cos(t))
                +4*cos(x*cos(t))*cos(y*cos(t))*cos(z*cos(t)))
                * (x**2 + y**2+ z**2-0.00000000000001)  )
    if selected_H==4:
        H= (    ((x*cos(t))+(x*cos(t))**2+(y*cos(t)+z*cos(t))**2)
                *(x**2 + y**2+ z**2-0.0000000000005)    )
    if selected_H==5:
        H=(     ((x*z*y*cos(t)*cos(t)*cos(t)) 
                *(((cos(x*cos(t)))**2+(sin(x*cos(t)))**2)**0.5)+1.95
                +((x*cos(t))**2+(y*cos(t))**2-(z*cos(t))**2)
                +((x*cos(t)*y*cos(t)/z*cos(t))**3)
                *(3*cos(x*cos(t))+3*cos(y*cos(t))+3*cos(z*cos(t))
                +4*cos(x*cos(t))*cos(y*cos(t))*cos(z*cos(t)))
                +((x*cos(t)*y*cos(t)/z*cos(t))**6)
                *((x*cos(t))+(x*cos(t))**2+(y*cos(t)+z*cos(t))**2)  )
                *(x**2 + y**2+ z**2-0.0000000000005)    )
    return H

            
def get_user_data():
    global L,P,D,A,B,TL,TP,TD,TA,TB,eps,mu,x1,x2,x3,x4,mass,ni,K,kappa,delta,a
    if os.path.isfile("user_data.txt"):
        with open("user_data.txt","r") as f:
            L,P,D,A,B,TL,TP,TD,TA,TB,eps,mu,x1,x2,x3,x4,mass,ni,K,kappa,delta,a =f.read().split(",") 
    else:
       print("File doesn't exist loading default data")
       L,P,D,A,B= '3.00','3.00','3.00','2.3','2.7'
       TL,TP,TD,TA,TB='0.05','0.05','0.05','0.05','0.05'
       eps,mu,x1,x2,x3,x4,mass,ni,K,kappa,delta,a = '0.23','0.354','0.5265','0.56','0.56','0.61','0.12','0.32','0.52','0.78','0.921','0.01'
    L,P,D,A,B,TL,TP,TD,TA,TB,eps,mu,x1,x2,x3,x4,mass,ni,K,kappa,delta,a= [float(i) for i in [L,P,D,A,B,TL,TP,TD,TA,TB,eps,mu,x1,x2,x3,x4,mass,ni,K,kappa,delta,a]]



class Visualization_H1(HasTraits):
    scene = Instance(MlabSceneModel, ())
    @on_trait_change('scene.activated')
    def update_plot(self):
        global H1_handle
        H1=get_H(1)
#        self.scene.mlab.clf(mlab.gcf())
        obj1=contour3d(H1, contours=[0], transparent=False)
        mlab.figure(mlab.gcf(), bgcolor=(1,1,1))
        H1_handle=mlab.gcf()
    def trigger():
        mlab.clf(H1_handle)
        H1=get_H(1)
        obj1=contour3d(H1, contours=[0], transparent=False, figure=H1_handle)
#        mlab.figure(H1_handle, bgcolor=(1,1,1)) 
    view = View(Item('scene', editor=SceneEditor(scene_class=MayaviScene),
                     height=250, width=300, show_label=False),
                resizable=True )
    
class Visualization_H2(HasTraits):
    scene = Instance(MlabSceneModel, ())
     
    @on_trait_change('scene.activated')
    def update_plot(self):
        global H2_handle
        H2=get_H(2)
        obj2=contour3d(H2, contours=[0], transparent=False)
        mlab.figure(mlab.gcf(), bgcolor=(1,1,1))
        H2_handle=mlab.gcf()
    def trigger():
        mlab.clf(H2_handle)
        H2=get_H(2)
        obj2=contour3d(H2, contours=[0], transparent=False, figure=H2_handle)
        
    view = View(Item('scene', editor=SceneEditor(scene_class=MayaviScene),
                     height=250, width=300, show_label=False),
                resizable=True )

    
class Visualization_H3(HasTraits):
    scene = Instance(MlabSceneModel, ())
     
    @on_trait_change('scene.activated')
    def update_plot(self):
        global H3_handle
        H3=get_H(3)
        obj3 = contour3d(H3, contours=[0], transparent=False)
        mlab.figure(mlab.gcf(), bgcolor=(1,1,1))
        H3_handle=mlab.gcf()
    def trigger():
        mlab.clf(H3_handle)
        H3=get_H(3)
        obj3=contour3d(H3, contours=[0], transparent=False, figure=H3_handle)
        
    view = View(Item('scene', editor=SceneEditor(scene_class=MayaviScene),
                     height=250, width=300, show_label=False),
                resizable=True )   
    
class Visualization_H4(HasTraits):
    scene = Instance(MlabSceneModel, ())
     
    @on_trait_change('scene.activated')
    def update_plot(self):
        global H4_handle
        H4=get_H(4)
        obj4 = contour3d(H4, contours=[0], transparent=False,color=(0.66,0.66,0.9))
        mlab.figure(mlab.gcf(), bgcolor=(1,1,1))
        H4_handle=mlab.gcf()
    def trigger():
        mlab.clf(H4_handle)
        H4=get_H(4)
        obj4=contour3d(H4, contours=[0], transparent=False, figure=H4_handle)
        
    view = View(Item('scene', editor=SceneEditor(scene_class=MayaviScene),
                     height=250, width=300, show_label=False),
                resizable=True )
    
class Visualization_H5(HasTraits):
    scene = Instance(MlabSceneModel, ())
     
    @on_trait_change('scene.activated')
    def update_plot(self):
        global H5_handle
        H5=get_H(5)
        obj5=contour3d(H5,contours=[0],transparent=False,color=(0.66,0.66,0.9))
        mlab.figure(mlab.gcf(), bgcolor=(1,1,1))
        H5_handle=mlab.gcf()
    def trigger():
        mlab.clf(H5_handle)
        H5=get_H(5)
        obj5=contour3d(H5, contours=[0], transparent=False, figure=H5_handle)
    view = View(Item('scene', editor=SceneEditor(scene_class=MayaviScene),
                     height=250, width=300, show_label=False),
                resizable=True )
    
    
    
#class Visualization_H6(HasTraits):
#    scene = Instance(MlabSceneModel, ())
#     
#    @on_trait_change('scene.activated')
#    def update_plot(self):
#        global H6_handle
#        H1=get_H(1)
#        contour3d(H1, contours=[0], transparent=False)
#        mlab.figure(mlab.gcf(), bgcolor=(1,1,1))
#        H6_handle=mlab.gcf()
#    def trigger():
#        mlab.clf(H6_handle)
#        H6=get_H(1)
#        obj6=contour3d(H6, contours=[0], transparent=False, figure=H6_handle)
#        
#    view = View(Item('scene', editor=SceneEditor(scene_class=MayaviScene),
#                     height=250, width=300, show_label=False),
#                resizable=True )
    
    
    
#####################################################################
            #         MAYAVI WIDGETS              #
#####################################################################
    
    
class MayaviQWidget_H1(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        layout = QtGui.QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.visualization = Visualization_H1()

        self.ui = self.visualization.edit_traits(parent=self,
                                                 kind='subpanel').control
        layout.addWidget(self.ui)
        self.ui.setParent(self)
        
        

    
class MayaviQWidget_H2(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        layout = QtGui.QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.visualization = Visualization_H2()

        self.ui = self.visualization.edit_traits(parent=self,
                                                 kind='subpanel').control
        layout.addWidget(self.ui)
        self.ui.setParent(self)     
        

    
class MayaviQWidget_H3(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        layout = QtGui.QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.visualization = Visualization_H3()

        self.ui = self.visualization.edit_traits(parent=self,
                                                 kind='subpanel').control
        layout.addWidget(self.ui)
        self.ui.setParent(self) 
        
        


    
class MayaviQWidget_H4(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        layout = QtGui.QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.visualization = Visualization_H4()

        self.ui = self.visualization.edit_traits(parent=self,
                                                 kind='subpanel').control
        layout.addWidget(self.ui)
        self.ui.setParent(self) 
        

    
class MayaviQWidget_H5(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        layout = QtGui.QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.visualization = Visualization_H5()

        self.ui = self.visualization.edit_traits(parent=self,
                                                 kind='subpanel').control
        layout.addWidget(self.ui)
        self.ui.setParent(self) 
        

    
#class MayaviQWidget_H6(QtGui.QWidget):
#    def __init__(self, parent=None):
#        QtGui.QWidget.__init__(self, parent)
#        layout = QtGui.QVBoxLayout(self)
#        layout.setContentsMargins(0,0,0,0)
#        layout.setSpacing(0)
#        self.visualization = Visualization_H6()
#
#        self.ui = self.visualization.edit_traits(parent=self,
#                                                 kind='subpanel').control
#        layout.addWidget(self.ui)
#        self.ui.setParent(self) 
#        
        
        