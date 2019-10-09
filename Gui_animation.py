import os
import numpy as np
from numpy import cos,sin
from mayavi.mlab import contour3d
import mayavi

os.environ['ETS_TOOLKIT'] = 'qt4'
from pyface.qt import QtGui
from traits.api import HasTraits, Instance, on_trait_change
from traitsui.api import View, Item
from mayavi.core.ui.api import MayaviScene, MlabSceneModel,SceneEditor
from mayavi import mlab
import image_to_video

global selected_H
global temp
global previous_H
global user_data_change
global time1,time2,time3
global make_video
global L,P,D,A,B,TL,TP,TD,TA,TB,eps,mu,x1,x2,x3,x4,mass,ni,K,kappa,delta,a


def trig_video(temp):
    global make_video
    make_video=temp

def change_animations():
    global user_data_change
    print("well well, this should work today")
    user_data_change=1
    Visualization()


def pause_animation():
    global temp,selected_H
    temp= selected_H
    print(temp,selected_H)
    selected_H=0
    print(temp,selected_H)
    
def play_animation():
    global temp,selected_H
    print(temp,selected_H)
    selected_H=temp
    print("This function will resume the animation")
    print(temp,selected_H)


def change_selected_H(user_selection):
    global selected_H
    selected_H= user_selection
    print("change_selected_H working ",user_selection )

def update_time(t1,t2,t3):
    global time1,time2,time3
    time1,time2,time3=t1,t2,t3
     
    
def get_time():
    global time1,time2,time3
    return(time1,time2,time3)

def update_H(t_temp1,t_temp2,t_temp3,x,y,z):
    global selected_H,previous_H
    global L,P,D,A,B,TL,TP,TD,TA,TB,eps,mu,x1,x2,x3,x4,mass,ni,K,kappa,delta,a
#    print("update H function working")
#    print(t_temp1,t_temp2,t_temp3)
#    x, y, z = np.ogrid[-3:3:60j, -3:3:60j, -3:3:60j]
#    print("selected H = ", selected_H)
#    print(selected_H,previous_H)
    
    
    eps,mu = 0,10**(-7)
    x1,x2,x3,x4 = 0.23,0.54,0.81,0.37
    mass,ni,K,kappa = 10**(-12) , 2 , 2*10^12 , 1000
    delta,a = 0.001,1
    Ei,omegaL,phi=0.5,10**12,0.01
    alpha,beta,gamma = 0.1,0.5,0.3
    mass_by_h_bar = mass/(10**-12)
    
    ## mode 1
    if selected_H==1:    
       H=  ((0.5  +  (x*cos(t_temp1))*(x*cos(t_temp1)) + 
             (y*cos(t_temp2))*(y*cos(t_temp2)) - (z*cos(t_temp3))*(z*cos(t_temp3))  )
                * (x**2 + y**2+ z**2-0.00000000000001)   )
    if selected_H==2:
        H= ( (1.5 + (x*z*y*cos(t_temp1)*cos(t_temp2)*cos(t_temp3))*(((cos(x*cos(t_temp1)))**2) + 0.5*(sin(x*cos(t_temp1)))**2)**0.5)
                *(x**2 + y**2+ z**2-0.0000000000005) )
    if selected_H==3:
        H= (    (3*cos(x*cos(t_temp1))+3*cos(y*cos(t_temp2))+3*cos(z*cos(t_temp3))
                +4*cos(x*cos(t_temp1))*cos(y*cos(t_temp2))*cos(z*cos(t_temp3)))
                * (x**2 + y**2+ z**2-0.00000000000001)  )
    if selected_H==4:
        H= (    ((x*cos(t_temp1))+(x*cos(t_temp1))**2+(y*cos(t_temp2)+z*cos(t_temp3))**2)
                *(x**2 + y**2+ z**2-0.0000000000005)    )
    if selected_H==5:
        H=(     ((x*z*y*cos(t_temp1)*cos(t_temp2)*cos(t_temp3)) 
                *(((cos(x*cos(t_temp1)))**2+(sin(x*cos(t_temp1)))**2)**0.5)+1.95
                +((x*cos(t_temp1))**2+(y*cos(t_temp2))**2-(z*cos(t_temp3))**2)
                +((x*cos(t_temp1)*y*cos(t_temp2)/z*cos(t_temp3))**3)
                *(3*cos(x*cos(t_temp1))+3*cos(y*cos(t_temp2))+3*cos(z*cos(t_temp3))
                +4*cos(x*cos(t_temp1))*cos(y*cos(t_temp2))*cos(z*cos(t_temp3)))
                +((x*cos(t_temp1)*y*cos(t_temp2)/z*cos(t_temp3))**6)
                *((x*cos(t_temp1))+(x*cos(t_temp2))**2+(y*cos(t_temp2)+z*cos(t_temp3))**2)  )
                *(x**2 + y**2+ z**2-0.0000000000005)    )
    ## mode 2
    
    
#    if selected_H==1:    
#       H=  ((Ei*(ni**2)  +  mass*omegaL*(((1+eps)*x*cos(t_temp1))**2) + 
#             ((1-mu)*y*cos(t_temp2))**2 - (z*cos(t_temp3) - cos(phi))**2  )
#                * (x**2 + y**2+ z**2-0.00000000000001)   )
#    
#    if selected_H==2:
#        H= ( (1.5 + (x*z*y*cos(t_temp1)*cos(t_temp2)*cos(t_temp3))*(((cos(x*cos(t_temp1)))**2) 
#                + 0.5*(sin(x*cos(t_temp1)))**2)**0.5) * ( alpha*(x1*x2+x3*x4)+beta*(x1*x3+x2*x4)+gamma*(x1*x4+x4*x3)+0.65 )
#                *(x**2 + y**2+ z**2-0.0000000000005) )
#    
#    if selected_H==3:
#        H= (  2*mass_by_h_bar * (3*cos(x*cos(t_temp1))+3*cos(y*cos(t_temp2))+3*cos(z*cos(t_temp3))
#                +4*cos(x*cos(t_temp1))*cos(y*cos(t_temp2))*cos(z*cos(t_temp3)))
#                * (x**2 + y**2+ z**2-0.00000000000001)  )
#    
#    if selected_H==4:
#        H= (    (K/2*mass)*((a*x*cos(t_temp1))+kappa*sin(delta)*(x*cos(t_temp1))**2+(cos(delta)*y*cos(t_temp2)+z*cos(t_temp3))**2)
#                *(x**2 + y**2+ z**2-0.0000000000005)    )
#        
#    if selected_H==5:
#        
#        
#        H = ((  ((Ei*(ni**2)  +  mass*omegaL*(((1+eps)*x*cos(t_temp1))**2) + 
#                  ((1-mu)*y*cos(t_temp2))**2 - (z*cos(t_temp3) - cos(phi))**2  ))
#            
#                +
#            
#               ( ( (x*z*y*cos(t_temp1)*cos(t_temp2)*cos(t_temp3))*(((cos(x*cos(t_temp1)))**2) 
#                + 0.5*(sin(x*cos(t_temp1)))**2)**0.5) * ( alpha*(x1*x2+x3*x4)+beta*(x1*x3+x2*x4)+gamma*(x1*x4+x4*x3) )
#                 )
#                
#                +
#                
#                (  2*mass_by_h_bar * (3*cos(x*cos(t_temp1))+3*cos(y*cos(t_temp2))+3*cos(z*cos(t_temp3))
#                +4*cos(x*cos(t_temp1))*cos(y*cos(t_temp2))*cos(z*cos(t_temp3)))
#                  )
#                
#                +
#                
#                (    (K/2*mass)*((a*x*cos(t_temp1))+kappa*sin(delta)*(x*cos(t_temp1))**2+(cos(delta)*y*cos(t_temp2)+z*cos(t_temp3))**2)
#                  )  )
#                *(x**2 + y**2+ z**2-0.0000000000005)    )
        
        
#        
#        H = (     ((x*z*y*cos(t_temp1)*cos(t_temp2)*cos(t_temp3)) 
#                *(((cos(x*cos(t_temp1)))**2+(sin(x*cos(t_temp1)))**2)**0.5)
#                
#                +1.95+((x*cos(t_temp1))**2+(y*cos(t_temp2))**2-(z*cos(t_temp3))**2)
#                
#                +((x*cos(t_temp1)*y*cos(t_temp2)/z*cos(t_temp3))**3)
#                *(3*cos(x*cos(t_temp1))+3*cos(y*cos(t_temp2))+3*cos(z*cos(t_temp3))
#                +4*cos(x*cos(t_temp1))*cos(y*cos(t_temp2))*cos(z*cos(t_temp3)))
#                
#                +((x*cos(t_temp1)*y*cos(t_temp2)/z*cos(t_temp3))**6)
#                *((x*cos(t_temp1))+(x*cos(t_temp2))**2+(y*cos(t_temp2)+z*cos(t_temp3))**2)  )
#                *(x**2 + y**2+ z**2-0.0000000000005)    )
#                
    if selected_H==0:
        t_temp1,t_temp2,t_temp3=0,0,0
        H =(  x**2+y**2+z**2  )
    return(H)

class Visualization(HasTraits):
    scene = Instance(MlabSceneModel, ())
   
    @on_trait_change('scene.activated')
    def update_plot(self):

        @mlab.animate(delay=10)
        def anim():
            global  L,P,D,A,B,TL,TP,TD,TA,TB,eps,mu,x1,x2,x3,x4,mass,ni,K,kappa,delta,a
            if os.path.isfile("user_data.txt"):
                with open("user_data.txt","r") as f:
                    L,P,D,A,B,TL,TP,TD,TA,TB,eps,mu,x1,x2,x3,x4,mass,ni,K,kappa,delta,a =f.read().split(",") 
            else:
               print("File doesn't exist loading default data")
               L,P,D,A,B= '3.00','3.00','3.00','2.3','2.7'
               TL,TP,TD,TA,TB='0.05','0.05','0.05','0.05','0.05'
               eps,mu,x1,x2,x3,x4,mass,ni,K,kappa,delta,a = '0.23','0.354','0.5265','0.56','0.56','0.61','0.12','0.32','0.52','0.78','0.921','0.01'
            L,P,D,A,B,TL,TP,TD,TA,TB,eps,mu,x1,x2,x3,x4,mass,ni,K,kappa,delta,a= [float(i) for i in [L,P,D,A,B,TL,TP,TD,TA,TB,eps,mu,x1,x2,x3,x4,mass,ni,K,kappa,delta,a]]

            global H,temp,previous_H,user_data_change,make_video
            t1, t2, t3 = TL,TP,TD
            make_video=0
            x, y, z = np.ogrid[-L:L:60j, -P:P:60j, -D:D:60j]
            t_temp1, t_temp2, t_temp3 = 0, 0, 0
            H = update_H(t_temp1,t_temp2,t_temp3,x,y,z)
            obj = contour3d(H, contours=[0], transparent=False,color=(0.66,0.66,0.9))
            mlab.figure(mlab.gcf(), bgcolor=(1,1,1))
            print(selected_H,previous_H)
            i=0
            while(1):
                if selected_H == previous_H:
                    t_temp1=t_temp1+t1
                    t_temp2=t_temp2+t2
                    t_temp3=t_temp3+t3
                    obj.mlab_source.scalars = update_H(t_temp1,t_temp2,t_temp3,x,y,z)
                    update_time(t_temp1,t_temp2,t_temp3)
                    if make_video!=0 and i<make_video*10:    
                        mlab.savefig(filename=os.getcwd()+'\\Images\\H_{}.png'.format(i))
                        i=i+1
                    if make_video>0 and i==make_video*10:
                        print("now make a video!!")
                        image_to_video.convert_to_video(int(make_video))
                        i=i+1
                    yield
                    
                else:
                    self.scene.mlab.clf()
                    print("yes")
                    
                    previous_H=selected_H
                    print(selected_H,previous_H)
                    print("Hope this will work")
                    anim()
                    
                
        anim()
        


    view = View(Item('scene', editor=SceneEditor(scene_class=MayaviScene),
                     height=300, width=300, show_label=False),
                resizable=True )   

class MayaviQWidget_main(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
#        print("H3")
        global selected_H,previous_H,user_data_change
        selected_H,previous_H=5,5
        user_data_change=0
        layout = QtGui.QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.visualization = Visualization()
        
        self.ui = self.visualization.edit_traits(parent=self,
                                                 kind='subpanel').control
        layout.addWidget(self.ui)
        self.ui.setParent(self)
        