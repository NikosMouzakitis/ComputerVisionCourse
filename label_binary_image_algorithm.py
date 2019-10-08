
## Implementation of a labeling algorithm
## on a binary image. (4 and 8 neighbors).
## ComputerVision course, Exercise.

import numpy as np 
import matplotlib.pyplot as plt

print("Creation of the initial picture to label")

A = [ [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 1, 1, 0, 0, 1, 1, 1],
      [0, 1, 1, 0, 0, 0, 1, 1],
      [0, 1, 1, 0, 0, 0, 0, 0],
      [0, 0, 0, 1, 1, 0, 0, 0],
      [0, 0, 0, 1, 1, 0, 0, 0],
      [0, 0, 0, 1, 1, 0, 0, 0],
      [0, 0, 0, 1, 1, 0, 1, 1],
      [0, 0, 0, 0, 0, 0, 0, 0]]

 

A = np.asarray(A, dtype = bool)
A = A.astype(int)

plt.imshow(A, cmap="gray")
plt.show()

n = (int)(input("Select neigbor(4 or 8) to be used: "))
#n = 4 #given n = 4 , still on dev.
print('Selected %d neigbors for the algorithm' %(n))

if( (n != 4) and (n != 8)):
    print('Abnormal exit, run again with valid inputs.')
    
cols = A[0].size
rows = int(A.size / cols)


number_of_labels = 0 # number of total different labels
equals = [] # will be used to keep equivelant classes while
            # assigning different labels to pixels.


L = A.copy()

####### code for 4-neighbors
if( n == 4) :
    
    for i in range(rows):    
        for j in range(cols):        
            rk = 1 # row exists on top of current pixel.
            ck = 1 # column exists on left of current pixel.
            
            #print('Run %d %d ' %(i,j))        
            #    Special checks for pixels in first row,
            #    and first column.
            if( i == 0):
                rk = 0        
            if( j == 0):
                ck = 0            
            # check if pixel is on the foreground.
            if(A[i][j] == 1):
                    
                #trivial for first pixel (0,0)
                if( rk == 0 and ck == 0):
                    L[i][j] = 1
                    
                if(rk == 1):
                    # checking the upper row.
                    if(L[i-1][j] != 0):
                        L[i][j] = L[i-1][j]
                        continue;           
                        
                if(ck == 1):
                    #checking the left column.                    
                    if(L[i][j-1] != 0):
                        L[i][j] = L[i][j-1]
                        continue;
                L[i][j] = number_of_labels + 1
                #increase the number of labels by one
                number_of_labels = number_of_labels+1

####### code for 8-neighbors
if( n == 8) :
    
    for i in range(rows):    
        for j in range(cols):        
            rk = 1 # row exists on top of current pixel.
            ck = 1 # column exists on left of current pixel.
            rur = 1 # right upper row pixel exists.
            
            #print('Run %d %d ' %(i,j))        
            #    Special checks for pixels in first row,
            #    and first column.
            
            if( i == 0):
                rk = 0        
            if( j == 0):
                ck = 0            
            if( j == A[0].size - 1):
                rur = 0
            # check if pixel is on the foreground.
            if(A[i][j] == 1):
                    
                #trivial for first pixel (0,0)
                if( rk == 0 and ck == 0):
                    L[i][j] = 1
                    
                if(rk == 1):
                    
                    # checking the upper row.
                    if(L[i-1][j] != 0):
                        L[i][j] = L[i-1][j]
                        continue;
                    if(L[i-1][j-1] != 0):
                        L[i][j] = L[i-1][j-1]
                        continue;           
                    if( (rur != 0) and L[i-1][j+1] != 0):
                        L[i][j] = L[i-1][j+1]
                        continue;              
                        
                if(ck == 1):
                    #checking the left column.                    
                    if(L[i][j-1] != 0):
                        L[i][j] = L[i][j-1]
                        continue;
                    if(L[i-1][j-1] != 0):
                        L[i][j] = L[i-1][j-1]
                        continue;
                        
                L[i][j] = number_of_labels + 1
                #increase the number of labels by one
                number_of_labels = number_of_labels+1


if(n == 4 or n == 8):
    print('Labeled image')
    plt.imshow(L)
    plt.title('Labeled binary image')
    plt.show()
