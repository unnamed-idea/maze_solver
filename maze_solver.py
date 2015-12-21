#maze solver by talha korkmaz, @ talhakorkmaz.com
#pre and post image processing is made by me, 
#implemented A* algorithm from https://hg.python.org/cpython/file/2.7/Lib/Queue.py

import sys
import pickle
from Queue import Queue  
import cv2


img=cv2.imread('maze.jpg',0)

img = img[19:681, 20:681]
img=cv2.bilateralFilter(img,8,50,50)

ret,img=cv2.threshold(img,200,255,cv2.THRESH_BINARY)


for i in range(662):
    for j in range(661):
        try:
            if img[i][j]==0 and img[i+1][j]==255 and img[i-1][j]==255 and img[i][j+1]==255 and img[i][j-1]==255:
                img[i][j]=255
        except:
            pass



start = (3,332)
end = (660,327)


def getadjacent(n):  
    x,y = n
    return [(x-1,y),(x,y-1),(x+1,y),(x,y+1)]

def BFS(start, end, pixels):

    queue = Queue()
    queue.put([start]) 

    while not queue.empty():

        path = queue.get()
        
        pixel = path[-1]
       
        if pixel == end:
            return path

        for adjacent in getadjacent(pixel):
            x,y = adjacent

            if x > 0 and y > 0 and img[x][y]==255 and x<661 and y<661:

                pixels[x][y] = 230
                new_path = list(path)
                new_path.append(adjacent)
                queue.put(new_path)


path = BFS(start, end, img)

path_img = cv2.imread('p2.jpg')
path_pixels = path_img
new=img.copy()
for position in path:
    x,y = position
    img[x][y] = 0 # red
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
f = open('finali.pckl', 'wb')
pickle.dump(path, f)
f.close()
print('done')
