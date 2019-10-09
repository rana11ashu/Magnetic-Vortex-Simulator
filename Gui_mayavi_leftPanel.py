import os
import numpy as np
from numpy import cos,sin
from mayavi.mlab import contour3d

os.environ['ETS_TOOLKIT'] = 'qt4'
from pyface.qt import QtGui
from traits.api import HasTraits, Instance, on_trait_change
from traitsui.api import View, Item
from mayavi.core.ui.api import MayaviScene, MlabSceneModel,SceneEditor
from mayavi import mlab
global selected_H
global temp
global previous_H
global user_data_change
from tvtk.api import tvtk

global time1,time2,time3,flag
global fig
global vcp
global count
flag=0
count=0

def get_time(t1,t2,t3,flag1):
    global time1,time2,time3,flag
    time1,time2,time3,flag=t1,t2,t3,flag1
#    print(time1,time2,time3,flag)
    Visualization.trigger()
def make_count_zero():
    global count
    count=0
    
def take_screenshot():
    global fig,count,flag
    if flag==0 or flag==1:
        count=0
        for i in range(10000):
                 if os.path.isfile("figure_captured_{}.png".format(i)):
                     print("yes")
                     os.remove("figure_captured_{}.png".format(i))
                 else:
                    break
        flag=2
    print("It should be captured today!!")
#    vcp.view_controls=False
    vcp.implicit_plane.widget.enabled = False
    
    mlab.savefig("figure_captured_{}.png".format(count),figure=fig,size=(800,800))
    vcp.implicit_plane.widget.enabled = True
    count=count+1
    



class Visualization(HasTraits):
    scene = Instance(MlabSceneModel, ())

    @on_trait_change('scene.activated')
    def update_plot(self):
        global fig
        global vcp        
        global time1,time2,time3,flag
        if os.path.isfile("user_data.txt"):
            with open("user_data.txt","r") as f:
                L,P,D,A,B,TL,TP,TD,TA,TB,eps,mu,x1,x2,x3,x4,mass,ni,K,kappa,delta,a =f.read().split(",") 
        else:
           print("File doesn't exist loading default data")
           L,P,D,A,B= '3.00','3.00','3.00','2.3','2.7'
           TL,TP,TD,TA,TB='0.05','0.05','0.05','0.05','0.05'
           eps,mu,x1,x2,x3,x4,mass,ni,K,kappa,delta,a = '0.23','0.354','0.5265','0.56','0.56','0.61','0.12','0.32','0.52','0.78','0.921','0.01'
        L,P,D,A,B,TL,TP,TD,TA,TB,eps,mu,x1,x2,x3,x4,mass,ni,K,kappa,delta,a= [float(i) for i in [L,P,D,A,B,TL,TP,TD,TA,TB,eps,mu,x1,x2,x3,x4,mass,ni,K,kappa,delta,a]]
        
        t_temp1,t_temp2,t_temp3=0,0,0
        if flag==1:
            t_temp1,t_temp2,t_temp3=time1,time2,time3
        print(t_temp1,t_temp2,t_temp3)
        ap = tvtk.AppendPolyData()
        x, y, z = np.ogrid[-L:L:60j, -P:P:60j, -D:D:60j]   
        
        H=(     ((x*z*y*cos(t_temp1)*cos(t_temp2)*cos(t_temp3)) 
                *(((cos(x*cos(t_temp1)))**2+(sin(x*cos(t_temp1)))**2)**0.5)+1.95
                +((x*cos(t_temp1))**2+(y*cos(t_temp2))**2-(z*cos(t_temp3))**2)
                +((x*cos(t_temp1)*y*cos(t_temp2)/z*cos(t_temp3))**3)
                *(3*cos(x*cos(t_temp1))+3*cos(y*cos(t_temp2))+3*cos(z*cos(t_temp3))
                +4*cos(x*cos(t_temp1))*cos(y*cos(t_temp2))*cos(z*cos(t_temp3)))
                +((x*cos(t_temp1)*y*cos(t_temp2)/z*cos(t_temp3))**6)
                *((x*cos(t_temp1))+(x*cos(t_temp2))**2+(y*cos(t_temp2)+z*cos(t_temp3))**2)  )
                *(x**2 + y**2+ z**2-0.0000000000005)    )
        src = contour3d(H, contours=[0], transparent=False,opacity=1.0)
        mlab.figure(mlab.gcf(), bgcolor=(0.7,0.8,0.6))        
        fig=mlab.gcf()
        fig.remove_child(fig.children[0])        
        data_out = src.module_manager.source.get_output_dataset()
        
        actor = src.actor.actors[0]
        polydata = tvtk.to_vtk(actor.mapper.input)
        
        ap.add_input_data(polydata)
        ap.update()
        
        surf = mlab.pipeline.surface(ap.output, figure=fig)
        surf.visible = False
        vcp = mlab.pipeline.scalar_cut_plane(ap.output, plane_orientation='z_axes', figure=fig)
#        outline = mlab.outline(surf, figure=fig)
    def trigger():
       
        global fig        
        global time1,time2,time3,flag
        global vcp
        mlab.clf(fig)
        if os.path.isfile("user_data.txt"):
            with open("user_data.txt","r") as f:
                L,P,D,A,B,TL,TP,TD,TA,TB,eps,mu,x1,x2,x3,x4,mass,ni,K,kappa,delta,a =f.read().split(",") 
        else:
           print("File doesn't exist loading default data")
           L,P,D,A,B= '3.00','3.00','3.00','2.3','2.7'
           TL,TP,TD,TA,TB='0.05','0.05','0.05','0.05','0.05'
           eps,mu,x1,x2,x3,x4,mass,ni,K,kappa,delta,a = '0.23','0.354','0.5265','0.56','0.56','0.61','0.12','0.32','0.52','0.78','0.921','0.01'
        L,P,D,A,B,TL,TP,TD,TA,TB,eps,mu,x1,x2,x3,x4,mass,ni,K,kappa,delta,a= [float(i) for i in [L,P,D,A,B,TL,TP,TD,TA,TB,eps,mu,x1,x2,x3,x4,mass,ni,K,kappa,delta,a]]
        
        t_temp1,t_temp2,t_temp3=0,0,0
        if flag==1:
            t_temp1,t_temp2,t_temp3=time1,time2,time3
        print(t_temp1,t_temp2,t_temp3)
        ap = tvtk.AppendPolyData()
        x, y, z = np.ogrid[-L:L:60j, -P:P:60j, -D:D:60j]   
        
        H=(     ((x*z*y*cos(t_temp1)*cos(t_temp2)*cos(t_temp3)) 
                *(((cos(x*cos(t_temp1)))**2+(sin(x*cos(t_temp1)))**2)**0.5)+1.95
                +((x*cos(t_temp1))**2+(y*cos(t_temp2))**2-(z*cos(t_temp3))**2)
                +((x*cos(t_temp1)*y*cos(t_temp2)/z*cos(t_temp3))**3)
                *(3*cos(x*cos(t_temp1))+3*cos(y*cos(t_temp2))+3*cos(z*cos(t_temp3))
                +4*cos(x*cos(t_temp1))*cos(y*cos(t_temp2))*cos(z*cos(t_temp3)))
                +((x*cos(t_temp1)*y*cos(t_temp2)/z*cos(t_temp3))**6)
                *((x*cos(t_temp1))+(x*cos(t_temp2))**2+(y*cos(t_temp2)+z*cos(t_temp3))**2)  )
                *(x**2 + y**2+ z**2-0.0000000000005)    )
        src = contour3d(H, contours=[0], transparent=False,opacity=1.0,figure=fig)
#        mlab.figure(mlab.gcf(), bgcolor=(0.7,0.8,0.6))        
        fig.remove_child(fig.children[0])        
        data_out = src.module_manager.source.get_output_dataset()
        
        actor = src.actor.actors[0]
        polydata = tvtk.to_vtk(actor.mapper.input)
        
        ap.add_input_data(polydata)
        ap.update()
        
        surf = mlab.pipeline.surface(ap.output, figure=fig)
        surf.visible = False
        vcp = mlab.pipeline.scalar_cut_plane(ap.output, plane_orientation='z_axes', figure=fig)
#        outline = mlab.outline(surf, figure=fig)
        print("its working")
#        vcp.implicit_plane.widget.enabled = False
       
        #mayavi.mlab.figure(obj1,bgcolor='white')
    view = View(Item('scene', editor=SceneEditor(scene_class=MayaviScene),
                     height=250, width=300, show_label=False),
                resizable=True )

class MayaviQWidget(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        layout = QtGui.QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.visualization = Visualization()
        
        self.ui = self.visualization.edit_traits(parent=self,
                                                 kind='subpanel').control
        layout.addWidget(self.ui)
        self.ui.setParent(self)
        