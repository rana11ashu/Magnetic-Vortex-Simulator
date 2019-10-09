from PIL import Image, ImageDraw
from math import floor
from pylab import array
import cv2, numpy
from skimage import img_as_bool, io, color
from skimage.morphology import skeletonize
import numpy as np
import matplotlib.pyplot as plt
from pylab import margins,gca,NullLocator
from scipy.interpolate import UnivariateSpline
from scipy import optimize
import os


global image_path

def get_image_path(fileName):
    global image_path
    image_path=fileName
    
    
def process_image():
    global image_path
    
## functions to be used inside
    def findMinDiff(arr, n): 
            # Initialize difference as infinite 
            diff = 10**20
            min1=None
            min2=None
            # Find the min diff by comparing difference 
            # of all possible pairs in given array 
            for i in range(n-1): 
                for j in range(i+1,n): 
                    if abs(arr[i]-arr[j]) < diff: 
                        diff = abs(arr[i] - arr[j])
                        min1=i
                        min2=j
          
            # Return min diff 
            return diff,min1,min2 
    
    
#########################################################################
###                 Scaling of Original Image
#########################################################################    
    input_image=Image.open(image_path)
    input_pixels = input_image.load()
   
    new_size = (240,210)
    # Create output image
    output_image = Image.new("RGB", new_size)
    draw = ImageDraw.Draw(output_image)
            
    x_scale = input_image.width / output_image.width
    y_scale = input_image.height / output_image.height
            
    # Copy pixels
    for x in range(output_image.width):
        for y in range(output_image.height):
            xp, yp = floor(x * x_scale), floor(y * y_scale)
            draw.point((x, y), input_pixels[xp, yp])
    output_image.save("original_scaled_image.png")    
#########################################################################
###              Filters
#########################################################################
    
### Filter: Contrast ###  
    input_image=Image.open("original_scaled_image.png")
    input_pixels=input_image.load()
    contrast_image = Image.new("RGB", input_image.size)
    draw = ImageDraw.Draw(contrast_image)
    
    # Find minimum and maximum luminosity
    imin = 255
    imax = 0
    for x in range(input_image.width):
        for y in range(input_image.height):
            r, g, b = input_pixels[x, y]
            i = (r + g + b) / 3
            if imin>i:
                imin=i
            if imax<i:
                imax=i
                
    # Generate image
    for x in range(contrast_image.width):
        for y in range(contrast_image.height):
            r, g, b = input_pixels[x, y]
            # Current luminosity
            i = (r + g + b) / 3
            if i==0:
                i=0.001
            # New luminosity
            ip = 255 * (i - imin) / (imax - imin)
            r = int(r * ip / i)
            g = int(g * ip / i)
            b = int(b * ip / i)
            draw.point((x, y), (r, g, b))
    contrast_image.save("filter_contrast.png")

### Filter : B&W  ###  
    image_file = Image.open("filter_contrast.png") # open colour image
    gray = image_file.convert('L')
    bw = gray.point(lambda x: 0 if x<128 else 255, '1')
    #image_file = image_file.convert('1') # convert image to black and white
    bw.save("B&W.png")
    
## Separate contour & Skeleton
    count_contour_image=0
    count_skeleton_image=0
   
    image=Image.open("B&W.png")
    im = array(image.convert('L'))
    contours, hier = cv2.findContours(im.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)    
    
    for i in range(len(contours)):
        
        output_canvas = numpy.zeros(im.shape, dtype=numpy.uint8)
        cv2.drawContours(output_canvas, contours, i,(255, 255, 255), -1)
        cv2.imwrite("filter_contour_separate_{}.png".format(i+1), output_canvas)
        count_contour_image+=1
        
        image = ( img_as_bool(color.rgb2gray(io.imread("filter_contour_separate_{}.png".format(i+1)))) )        
        skeleton = skeletonize(image) 
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(8,4))
        axes.imshow(skeleton, cmap=plt.cm.gray)
        margins(0,0)
        gca().xaxis.set_major_locator(NullLocator())
        gca().yaxis.set_major_locator(NullLocator())
        plt.savefig("filter_skeleton_separate_{}.png".format(i+1), bbox_inches='tight',pad_inches = 0)
        new_size=(240,210)
        input_image = Image.open("filter_skeleton_separate_{}.png".format(i+1))
        input_pixels = input_image.load()
        origin = (5, 5)
        end = (input_image.width-3,input_image.height-3)
        output_image = Image.new("RGB", (end[0] - origin[0], end[1] - origin[1]))
        draw = ImageDraw.Draw(output_image)
        for x in range(output_image.width):
            for y in range(output_image.height):
                xp, yp = x + origin[0], y + origin[1]
                draw.point((x, y), input_pixels[xp, yp])    
        input_image=output_image
        input_pixels = input_image.load()
        output_image = Image.new("RGB", new_size)
        draw = ImageDraw.Draw(output_image)
        x_scale = input_image.width / output_image.width
        y_scale = input_image.height / output_image.height
        for x in range(output_image.width):
            for y in range(output_image.height):
                xp, yp = floor(x * x_scale), floor(y * y_scale)
                draw.point((x, y), input_pixels[xp, yp])
        output_image.save("filter_skeleton_separate_{}.png".format(i+1))
        count_skeleton_image+=1
        
        # IMAGE SEPARATION            
        image_sep=Image.open("filter_skeleton_separate_{}.png".format(i+1))            
        input_pixels=image_sep.load()
        image_sep = image_sep.copy();
        image_pixels=image_sep.load()
        validIntersection = [[0,255,0,255,0,0,255,0],[0,0,255,0,255,0,0,255],[255,0,0,255,0,255,0,0],
                             [0,255,0,0,255,0,255,0],[0,0,255,0,0,255,0,255],[255,0,0,255,0,0,255,0],
                             [0,255,0,0,255,0,0,255],[255,0,255,0,0,255,0,0],[0,255,0,0,0,255,0,255],
                             [0,255,0,255,0,0,0,255],[0,255,0,255,0,255,0,0],[0,0,0,255,0,255,0,255],
                             [255,0,255,0,0,0,255,0],[255,0,255,0,255,0,0,0],[0,0,255,0,255,0,255,0],
                             [255,0,0,0,255,0,255,0],[255,0,0,255,255,255,0,0],[0,0,255,0,0,255,255,255],
                             [255,255,0,0,255,0,0,255],[0,255,255,255,0,0,255,0],[255,0,255,255,0,0,255,0],
                             [255,0,255,0,0,255,255,0],[255,0,255,255,0,255,255,0],[0,255,255,0,255,0,255,255],
                             [255,255,0,255,255,0,255,0],[255,255,0,0,255,0,255,0],[0,255,255,0,255,0,255,0],
                             [0,0,255,0,255,0,255,255],[255,0,0,255,255,0,255,0],[255,0,255,0,255,255,0,255],
                             [255,0,255,0,255,255,0,0],[255,0,255,0,255,0,0,255],[0,255,0,0,255,0,255,255],
                             [0,255,255,0,255,0,0,255],[255,255,0,255,0,0,255,0],[0,255,0,255,255,0,255,0],
                             [0,0,255,0,255,255,0,255],[255,0,255,0,0,255,0,255],[255,0,0,255,0,255,255,0],
                             [255,0,255,255,0,255,0,0]];
        #image = image/255;
        intersections = list();
        for x in range(1,image_sep.width-1):
            for y in range(1,image_sep.height-1):
                if image_pixels[x,y][1] == 255:
                    x_1, y_1, x1, y1 = x-1, y-1, x+1, y+1;
                    neighbours =[ image_pixels[x_1,y][1], 
                                 image_pixels[x_1,y1][1], image_pixels[x,y1][1], image_pixels[x1,y1][1],
                                 image_pixels[x1,y][1], image_pixels[x1,y_1][1], image_pixels[x,y_1][1], image_pixels[x_1,y_1][1] ]
        
                    #valid = True;
                    if neighbours in validIntersection:
                        intersections.append((y,x));
        # Filter intersections to make sure we don't count them twice or ones that are very close together
        for point1 in intersections:
            for point2 in intersections:
                if (((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2) < 10**2) and (point1 != point2):
                    intersections.remove(point2);
        intersections = list(set(intersections));
        print(intersections)
        
        
        output_image = Image.new("RGB", image_sep.size)
        draw = ImageDraw.Draw(output_image)
        for x in range(output_image.width):
            for y in range(output_image.height):
                draw.point([x, y], input_pixels[x, y])
        
        
        for junc in range(len(intersections)):
            count_skeleton_image-=1
        
            [(y,x)]=[intersections[junc]]
            draw.point([x,y],(0,0,0))            
            draw.point([x-1,y],(0,0,0))
            draw.point([x+1,y],(0,0,0))
            draw.point([x,y-1],(0,0,0))
            draw.point([x,y+1],(0,0,0))
            draw.point([x-1,y-1],(0,0,0))
            draw.point([x+1,y+1],(0,0,0))
            draw.point([x-1,y+1],(0,0,0))
            draw.point([x+1,y-1],(0,0,0))
            
            x_temp=[]
            y_temp=[]
            for x_var in range(x-5+1,x+5):
                for y_var in range(y-5+1,y+5):
                    if x_var==x-5+1 or x_var==x+5-1 or y_var==y-5+1 or y_var==y+5-1:
                        if input_pixels[x_var,y_var][1]==255:
                            x_temp.append(x_var)
                            y_temp.append(y_var)
            print("yes",x_temp,y_temp)
            print("x,y " ,x,y)
            dydx=[]
            for diff_loop in range(len(x_temp)):
                if  x_temp[diff_loop]-x==0:
                    diff_temp= (y_temp[diff_loop]-y) / 0.1
                else:
                    print(x_temp[diff_loop],x)
                    diff_temp= (y_temp[diff_loop]-y) / (x_temp[diff_loop]-x)
                dydx.append(diff_temp)
            print(x_temp,y_temp)
            print(dydx)
            
            
            
            for min_loop in range(   floor( len(dydx)/2 )   ):
                dst,idx1,idx2=findMinDiff(dydx,len(dydx))
                print(idx1,idx2)
                
                ### Line Separation
                image_ls=output_image
                im_ls = array(image_ls.convert('L'))
                
                contours_ls, hier_ls = cv2.findContours(im_ls, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)    
                output_canvas_ls = numpy.zeros(im_ls.shape, dtype=numpy.uint8)
                for i_ls in range(len(contours_ls)):
                    if cv2.pointPolygonTest(contours_ls[i_ls],(x_temp[idx1],y_temp[idx1]),False)!=-1:
                        print("done0")
                        #output_canvas = numpy.zeros(image.shape, dtype=numpy.uint8)
                        cv2.drawContours(output_canvas_ls, contours_ls, i_ls,(255, 255, 255), -1)
        
                    if cv2.pointPolygonTest(contours_ls[i_ls],(x_temp[idx2],y_temp[idx2]),False)!=-1:
                        print("done")
                        cv2.drawContours(output_canvas_ls, contours_ls, i_ls,(255, 255, 255), -1)     
                cv2.imwrite("filter_skeleton_separate_{}.png".format(i+1+min_loop+junc), output_canvas_ls)
                count_skeleton_image+=1
        
                dydx = [e for e in dydx if e not in (dydx[idx1],dydx[idx2])]
                x_temp = [e for e in x_temp if e not in (x_temp[idx1],x_temp[idx2])]
                y_temp = [e for e in y_temp if e not in (y_temp[idx1],y_temp[idx2])]
            if len(x_temp)!=0:
                for i_ls in range(len(contours_ls)):
                    if cv2.pointPolygonTest(contours_ls[i_ls],(x_temp[0],y_temp[0]),False)!=-1:
                        output_canvas_ls = numpy.zeros(im_ls.shape, dtype=numpy.uint8)
                        cv2.drawContours(output_canvas_ls, contours_ls, i_ls,(255, 255, 255), -1)
                cv2.imwrite("filter_skeleton_separate_{}.png".format(i+1+min_loop+1+junc), output_canvas_ls)
                count_skeleton_image+=1
        
                del dydx
                del x_temp
                del y_temp
                
    print("No of contour images are ",count_contour_image)
    print("No of skeleton images are ",count_skeleton_image)
        
#################################################################################################
#            Smoothing(K=5), Save, Smoothing(K=1), Bigger Circle, Derivative Test,            #    
#################################################################################################
        
    def distance(P1, P2):
        return ((P1[0] - P2[0])**2 + (P1[1] - P2[1])**2) ** 0.5
    
    def optimized_path(coords, start=None):
        if start is None:
            start = coords[0]
        pass_by = coords
        path_connected = [start]
        pass_by.remove(start)
        while pass_by:
            nearest = min(pass_by, key=lambda x: distance(path_connected[-1], x))
            path_connected.append(nearest)
            pass_by.remove(nearest)
        return path_connected
    def calc_R(xc, yc):
        """ calculate the distance of each 2D points from the center (xc, yc) """
        return np.sqrt((x-xc)**2 + (y-yc)**2)
    
    def f_2(c):
        """ calculate the algebraic distance between the data points and the mean circle centered at c=(xc, yc) """
        Ri = calc_R(*c)
        return Ri - Ri.mean()
    
    original_image=Image.open("original_scaled_image.png")
    circle_image=Image.new("RGB", input_image.size)
    circle_image.paste(original_image)
    draw_circles=ImageDraw.Draw(circle_image)        
    
    for image_number in range(count_skeleton_image):
        print(image_number+1)
        input_image=Image.open("filter_skeleton_separate_{}.png".format(image_number+1))
        input_pixels = input_image.load()
        x_data=[]
        y_data=[]        
        circle_x=[]
        circle_y=[]
        circle_radius=[]
        count=0
        #print(input_pixels[0,0])
        #print(len(str(input_pixels[0,0])))
        if len(str(input_pixels[0,0]))==9:
            for x in range(input_image.width):
                for y in range(input_image.height):
                    if input_pixels[x,y][1]==255:
                            count=count+1
                            x_data.append(x)
                            y_data.append(input_image.height-y)
            #print("1",count,x_data,y_data)
        else:
            for x in range(input_image.width):
                for y in range(input_image.height):
                    if input_pixels[x,y]==255:
                            count=count+1
                            x_data.append(x)
                            y_data.append(input_image.height-y)
            #print("0",count,x_data,y_data)
        #plt.plot(x_data,y_data) 
        if len(x_data)<=5:
            continue
        
        #####  Nearest Neighbour #####
        start = None
        points=[[i,j] for i,j in zip(x_data,y_data)]
        points = optimized_path(points,start)
        
        # Smoothing
        points=np.array(points)
        distance_smooth = np.cumsum( np.sqrt(np.sum( np.diff(points, axis=0)**2, axis=1 )) )
        distance_smooth = np.insert(distance_smooth, 0, 0)/distance_smooth[-1]
        splines = [UnivariateSpline(distance_smooth, coords, k=5, s=None) for coords in points.T]
        alpha = np.linspace(0, 1, 75)
        points_fitted = np.vstack( spl(alpha) for spl in splines ).T
        plt.clf()
        axes = plt.gca()
        axes.set_xlim(1,input_image.width)
        axes.set_ylim(1,input_image.height)
        margins(0,0)
        gca().xaxis.set_major_locator(NullLocator())
        gca().yaxis.set_major_locator(NullLocator())
        #fig.set_size_inches()
        plt.plot(points_fitted.T[0],points_fitted.T[1],color=(0,0,0))
        plt.savefig("smooth_image_{}.png".format(image_number+1), bbox_inches='tight', pad_inches = 0)
        plt.clf()

        ########################################
        #               Save Image             #
        ########################################
        input_image = Image.open("smooth_image_{}.png".format(image_number+1))  
        input_pixels = input_image.load()
        print("input_image_size=",input_image.size)
        origin = (4, 0)
        end = (input_image.width,input_image.height-3)
        # Create output image
        output_image = Image.new("RGB", (end[0] - origin[0], end[1] - origin[1]))
        draw = ImageDraw.Draw(output_image)
        # Copy pixels
        for x in range(output_image.width):
            for y in range(output_image.height):
                xp, yp = x + origin[0], y + origin[1]
                draw.point((x, y), input_pixels[xp, yp])
        output_image.save("smooth_image_{}.png".format(image_number+1))
        
        
        
        ########################################
        ####    Bigger Circle Detection    #####
        ########################################            
        x_np=points_fitted.T[0]
        y_np=points_fitted.T[1]
        x_m=x_np.mean()
        y_m=y_np.mean()
        x=x_np
        y=y_np
        center_estimate = x_m, y_m
        center_2, ier = optimize.leastsq(f_2, center_estimate)

        xc_2, yc_2 = center_2
        Ri_2       = calc_R(*center_2)
        R_2        = Ri_2.mean()
        #residu_2   = sum((Ri_2 - R_2)**2)
        circle_x.append(xc_2)
        circle_y.append(yc_2)
        circle_radius.append(R_2)
        
        print("big circle",xc_2,yc_2,R_2)
        
        x,y,r=xc_2,yc_2,R_2
        input_image=Image.open("filter_skeleton_separate_{}.png".format(image_number+1))
        output_image = Image.new("RGB", input_image.size)
        output_image.paste(input_image)
        draw = ImageDraw.Draw(output_image)
        
        
        
        draw.ellipse((x-r, input_image.height-y-r, x+r, input_image.height-y+r), outline=(255,0,0))
        output_image.save("circles_{}.png".format(image_number+1))
        
        draw_circles.ellipse((x-r, input_image.height-y-r, x+r, input_image.height-y+r), outline=(255,0,0))
        
        
        
        
        ########################################
        #             Smoothing(k=1)           #
        ########################################
        distance_smooth = np.cumsum( np.sqrt(np.sum( np.diff(points, axis=0)**2, axis=1 )) )
        distance_smooth = np.insert(distance_smooth, 0, 0)/distance_smooth[-1]
        splines = [UnivariateSpline(distance_smooth, coords, k=1, s=None) for coords in points.T]
        alpha = np.linspace(0, 1, 75)
        points_fitted_1 = np.vstack( spl(alpha) for spl in splines ).T
        
        
                    
        ###########################################
        #              Derivative Test           #
        ###########################################  
        x_np=points_fitted_1.T[0]
        y_np=points_fitted_1.T[1]
        dydx=[]
        x=[]
        y=[]
        for i in range(len(x_np)-1):
            x.append(x_np[i])
            y.append(y_np[i]) 
            
        #First Derivative
        for i in range(0,len(x)-1):
            dydx.append( (y[i+1]-y[i]) / (x[i+1]-x[i]) )    
        #plt.plot(x[0:len(x)-1],dydx)
        
        #Second Derivative
        d2y_dx2=[]
        for i in range(0,len(x)-2):
            d2y_dx2.append( (dydx[i+1]-dydx[i]) / (x[i+1]-x[i]) )    
        #plt.plot(x[0:len(x)-2],d2y_dx2)
        
        ###########################################
        #  Find Line Segment for smaller circles  #
        ###########################################
        
        index=[]
        i=0
        while(i< (len(d2y_dx2)-1)):
            #print(i,d2y_dx2[i])
            for j in range(i+1,len(d2y_dx2)):
                if( round(d2y_dx2[i]) != round(d2y_dx2[j],4) ):
                    index.append(j)
                    i=j
                    print(i)
                    break
            i=i+1   
        print(index)    
        
        ###########################################
        #  Find Line Segment for smaller circles  #
        ###########################################
        index.insert(0,0)
        index.append(len(points_fitted)-1)
        
        for i in range(len(index)-1):
            #print(index[i],index[i+1])
            if index[i+1]-index[i]<=5:
                print(image_number+1,"circle removed due to less number of points")
                continue
            x_np=points_fitted.T[0][ index[i]:index[i+1] ]
            y_np=points_fitted.T[1][ index[i]:index[i+1] ]
            reference_point=( points_fitted.T[0][ round( (index[i]+index[i+1]) /2 ) ],
                             points_fitted.T[1][ round( (index[i]+index[i+1]) /2 ) ]  )
            x_m=x_np.mean()
            y_m=y_np.mean()
            x=x_np
            y=y_np
            center_estimate = x_m, y_m
            center_2, ier = optimize.leastsq(f_2, center_estimate)

            xc_2, yc_2 = center_2
            Ri_2       = calc_R(*center_2)
            R_2        = Ri_2.mean()
            x,y,r=xc_2,yc_2,R_2
            print("small Circles",x,y,r)
            #residu_2   = sum((Ri_2 - R_2)**2)
            if r>=2*max(input_image.width,input_image.height):
                print("circle removed as it was a straight line")
                continue
            
            flag=0
            if r>min(input_image.height,input_image.width):
                for k in range(len(circle_x)):
                    if circle_radius[k]>min(input_image.height,input_image.width):
                        centre_diff=np.sqrt( (x-circle_x[k])**2 + (y-circle_y[k])**2 )
                        #radius_diff=abs(circle_radius-r)
                        if centre_diff<=min(r,circle_radius[k]):
                            flag=1
            if flag==1:
                print(image_number+1,"circle removed due to extra larger circle overlapping")
                continue
            
            flag=0        
            for k in range(len(circle_x)):
                if abs(circle_radius[k]-r)<50:
                    centre_diff =  np.sqrt( (x-circle_x[k])**2 + (y-circle_y[k])**2 )
                    ref_dist_1  =  np.sqrt( (reference_point[0]-circle_x[k])**2 + 
                                           (reference_point[1]-circle_y[k])**2 )
                    ref_dist_2  =  np.sqrt( (reference_point[0]-x)**2 + 
                                           (reference_point[1]-y)**2 )
                    if centre_diff-abs(ref_dist_1-ref_dist_2)<1:
                       print('centre_diff',centre_diff,'ref_dist_1',ref_dist_1,'ref_dist_2',ref_dist_2) 
                       flag=1
                        
                        
            if flag==1:
                print(image_number+1,"circle removed due to extreme closeness")
                continue
            
            
                    
            circle_x.append(xc_2)
            circle_y.append(yc_2)
            circle_radius.append(R_2)
            x,y,r=xc_2,yc_2,R_2
        
            draw.ellipse((x-r, input_image.height-y-r, x+r, input_image.height-y+r), outline=(0,255,255))
            output_image.save("circles_{}.png".format(image_number+1))
            
            draw_circles.ellipse((x-r, input_image.height-y-r, x+r, input_image.height-y+r), outline=(0,255,255))
            
        print(circle_x,circle_y,circle_radius)
        print('\n\n')
        
        circle_image.save("circles.png")
    return(os.getcwd()+'\\circles.png')
    
    
    
 
    
#process_image()
   