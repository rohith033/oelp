# this system uses edge detection followed with hough line transfrom 
# we would be drawing rectangular boxs around the segmented books
import cv2 
import numpy as np
import os
from utli import rename,Extract_Text_From_Img
for i in range(64):
    input_image = 'image'+str(i)
    if(os.path.exists('./bookspines/'+input_image) == False):
        os.makedirs('./bookspines/'+input_image)
    if(os.path.exists('./internal/'+input_image) == False):
        os.makedirs('./internal/'+input_image)
    random_image = cv2.imread('Datasetbooks/'+input_image+'.jpeg')
    shaped_image = cv2.resize(random_image,(600,450))
    shaped_imageX=shaped_image
    cv2.imwrite(f'internal/{input_image}/shaped_image.jpeg',shaped_image)
    shaped_image = cv2.bilateralFilter(shaped_image,9,150,150)
    edges = cv2.Canny(shaped_image,50,200,None, 3)
    coloured_edges = cv2.cvtColor(edges,cv2.COLOR_GRAY2BGR)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,1))
    edges = cv2.dilate(edges, kernel,iterations=1) 
    cv2.imwrite(f'internal/{input_image}/edges.jpeg', edges)
    cv2.imwrite(f'internal/{input_image}/coloured_edges.jpeg',coloured_edges)
    lines= cv2.HoughLinesP(edges,1,np.pi/180, 50,None,50,1)
    lines=lines.tolist()
    lines.sort()
    X=0
    if lines is not None:
            for i in range(0, len(lines)):
                l = lines[i][0]
                cv2.line(shaped_image, (l[0],0),(l[0],450), (0,0,255),2, cv2.LINE_AA)
                if(X!=l[0]):
                    crop = shaped_imageX[0:450,X:l[0]]
                    img = cv2.rotate(crop,cv2.ROTATE_90_COUNTERCLOCKWISE)
                    cv2.imwrite(f"bookspines/{input_image}/book{i}.jpeg", img)
                    X=l[0] 
                    cv2.line(shaped_image, (600,0),(600,450), (0,0,255),2, cv2.LINE_AA)
    crop = shaped_imageX[0:450,X:600]
    img = cv2.rotate(crop,cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imwrite(f"bookspines/{input_image}/booklast.jpeg", img)
    print(lines)
    cv2.imwrite(f"internal/{input_image}/spines.jpeg",shaped_image)

    # the method of houge transform is getting influnced by books of same type next to each other 
    # as it is showing no edge btw the books of the same type next to each other
    # the quality of image is also influcing same photo with two different types of lighting showing 
    # different results making it prone to sensitivity
    # methode 2 using cnn based system

