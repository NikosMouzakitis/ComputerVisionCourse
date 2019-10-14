
## Implementation of a labeling algorithm
## on a binary image. (4 and 8 neighbors).
## ComputerVision course, Exercise.

import numpy as np 
import matplotlib.pyplot as plt

def exists(tag, eq):
    for i in range(len(eq)):
        if(tag == eq[i][2]):
            return 1
    return 0
        
print("Creation of the initial picture to label")
eq = []

A = [
      [0, 0, 0, 1, 0, 0, 0, 0],
      [0, 1, 1, 0, 1, 0, 1, 1],
      [0, 1, 1, 0, 0, 1, 1, 1],
      [1, 0, 1, 0, 1, 1, 1, 1],
      [0, 1, 1, 0, 0, 0, 1, 1],
      [0, 1, 1, 0, 0, 0, 1, 1],
      [0, 1, 1, 0, 0, 0, 0, 0],
      [0, 0, 0, 1, 1, 0, 0, 0],
      [1, 1, 0, 1, 1, 1, 0, 1],
      [0, 1, 0, 1, 1, 0, 0, 0],
      [1, 0, 0, 0, 1, 1, 1, 1],
#      [0, 0, 0, 1, 1, 0, 0, 0],
#      [1, 0, 1, 0, 1, 1, 1, 1],
#      [0, 0, 0, 1, 1, 0, 0, 0],
#      [1, 0, 1, 0, 1, 0, 1, 1],
      [0, 0, 0, 1, 1, 0, 0, 0],
      [0, 1, 1, 0, 0, 0, 1, 1],
      [0, 1, 1, 0, 0, 0, 0, 1],
      [0, 0, 0, 1, 1, 0, 1, 1],
      [1, 0, 0, 1, 1, 1, 0, 1],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [1, 0, 1, 0, 1, 1, 1, 1],
      [1, 0, 0, 0, 0, 1, 1, 1],
      [1, 0, 0, 1, 1, 1, 0, 1],
      [1, 0, 0, 1, 1, 1, 0, 1],
      [0, 0, 0, 0, 0, 0, 0, 0]
      ]

A = np.asarray(A, dtype = bool)
A = A.astype(int)
plt.figure(1)
plt.imshow(A, cmap="gray")
plt.show()

n = (int)(input("Select neigbor(4 or 8) to be used: "))
#n = 8 #given n = 4 , still on dev.
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
            crk = 1
            #print('Run %d %d ' %(i,j))        
            #    Special checks for pixels in first row,
            #    and first column.
            if( i == 0):
                rk = 0        
            if( j == 0):
                ck = 0
            if(j == cols - 1):
                crk = 0
                
            # check if pixel is on the foreground.
            if(A[i][j] == 1):
                    
                #trivial for first pixel (0,0)
                if( rk == 0 and ck == 0):
                    L[i][j] = 1
                  
                if(rk == 1):
                    # checking the upper row.
                    if(L[i-1][j] != 0):
                        L[i][j] = L[i-1][j]
                        #editing equivelant label.
                        if( (ck == 1) and (L[i][j-1] != 0) ):
                            if(L[i][j-1] != L[i][j]):
                                w = L[i][j] - L[i][j-1]
                                if(w < 0):
                                    tag = str(L[i][j])+str(L[i][j-1])
                                if(w > 0):
                                    tag = str(L[i][j-1])+str(L[i][j])
                                ret = exists(tag, eq)
                                    
                                if( (ret == 0) and (w != 0)) :
                                    print('')
                                    print(w)
                                    eq.append([L[i][j], L[i][j-1], tag])   
                                    #L[i][j-1] = L[i][j]
                            
                        continue;           
                if(ck == 1):
                   #checking the left column.                    
                   if(L[i][j-1] != 0):
                       L[i][j] = L[i][j-1]
                       continue;         
               
                        
                L[i][j] = number_of_labels + 1
                #increase the number of labels by one
                number_of_labels = number_of_labels+1

######## code for 8-neighbors
if( n == 8) :
    for i in range(rows):    
        for j in range(cols):        
            tag = ''
            rk = 1 # row exists on top of current pixel.
            ck = 1 # column exists on left of current pixel.
            rur = 1 # right upper row pixel exists.
            print('%d %d' %(i,j))
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
                    continue
                if(rk == 1):
                    # checking the upper row.
                    if(L[i-1][j] != 0):
                        L[i][j] = L[i-1][j]
                        
                        if( (L[i][j-1] != 0) and (L[i][j-1]!=L[i][j]) and (j != 0) ):
                            
                            w = L[i][j] - L[i][j-1]
                            if(w < 0):
                                tag = str(L[i][j])+str(L[i][j-1])
                            else:
                                tag = str(L[i][j-1])+str(L[i][j])
                            ret = exists(tag, eq)
                            
                            if( (ret == 0) and (w != 0)):
                                print('1')
                                print(L)
                                eq.append([L[i][j], L[i][j-1], tag])
                                print("Appending to eq: %d %d and i: %d j:%d"%(L[i][j],L[i][j-1],i,j))
                            L[i][j-1] = L[i][j]
                            print('w: %d tag: %s'%(w, tag))
                        print('Up')
                        continue;
                       
                    if( (ck == 1) and (L[i-1][j-1] != 0) ):
                        L[i][j] = L[i-1][j-1]
                        
                        if( (L[i][j-1] != 0) and (L[i][j-1] != L[i][j]) ):
                            
                            w = L[i][j] - L[i][j-1]
                            if(w < 0):
                                tag = str(L[i][j])+str(L[i][j-1])
                            if(w > 0):
                                tag = str(L[i][j])+str(L[i][j-1])
                            ret = exists(tag, eq)
                                
                            if( (ret == 0) and (w != 0)) :
                                print('2')
                                print(w)
                                print("Appending to eq: %d %d and i: %d j:%d"%(L[i][j],L[i-1][j-1],i,j))
                                eq.append([L[i][j], L[i-1][j-1], tag])
                            
                        print('UpLEFT')
                        continue;    
                        
#                    if( (ck == 1) and (L[i+1][j-1] != 0) ):
#                        print(" sigkrinw: (%d, %d)=%d me (%d,%d)=%d"%(i,j,L[i][j],i+1,j-1,L[i+1][j-1]))
#                        L[i][j] = L[i+1][j-1]
#                        continue                        
                    if( (rur != 0) and L[i-1][j+1] != 0):
                        L[i][j] = L[i-1][j+1]
                        print('UpRight')
                        if(L[i][j-1] != 0):
                            L[i][j-1] = L[i][j]
                            
                            w = L[i][j] - L[i][j-1]
                            if(w < 0):
                                tag = str(L[i][j])+str(L[i][j-1])
                            if(w > 0):
                                tag = str(L[i][j-1])+str(L[i][j])
                            ret = exists(tag, eq)
                                
                            if( (ret == 0) and (w != 0)) :
                                print('3')
                                print(w)
                                print("Appending to eq: %d %d and i: %d j:%d"%(L[i][j],L[i][j-1],i,j))
                                eq.append([L[i][j], L[i][j-1], tag])    
                        continue;              
                if(ck == 1):
                    #checking the left column.                    
                    if(L[i][j-1] != 0):
                        L[i][j] = L[i][j-1]
                        print('LEFT')
                        continue;
                    
                L[i][j] = number_of_labels + 1
                #increase the number of labels by one
                number_of_labels = number_of_labels+1

print("List before doing changes in the labels found")                
print(L)
     
###############################################                        
if(n == 8): # another time traversing the array cause in 8-neigbors we missed some of
            # of the neighbors.
    for i in range(rows):
        
        for j in range(cols):
            
            rk = 1 # row exists on top of current pixel.
            ck = 1 # column exists on left of current pixel.
            rur = 1 # right upper row pixel exists.
                
            if( i == 0):
                rk = 0        
            if( j == 0):
                ck = 0            
            if( j == A[0].size - 1):
                rur = 0 
            
            if(L[i][j] != 0):
                
                #up-left
                if( (j!=0) and (i!= 0)) :
                    if( (L[i-1][j-1]!= 0) and (L[i-1][j-1]!= L[i][j] ) ):
                        w = L[i][j] - L[i-1][j-1]
                        if(w < 0):
                            tag = str(L[i][j])+str(L[i-1][j-1])
                        if(w > 0):
                            tag = str(L[i-1][j-1])+str(L[i][j])
                        ret = exists(tag, eq)
                                    
                        if( (ret == 0) and (w != 0)) :
                            print("Appending to eq: %d %d and i: %d j:%d"%(L[i][j],L[i-1][j-1],i,j))
                            eq.append([L[i][j], L[i-1][j-1], tag])    
                            
                if(j!=0):
                    if( (L[i][j-1]!= 0) and (L[i][j-1]!= L[i][j] ) ):
                        w = L[i][j] - L[i][j-1]
                        if(w < 0):
                            tag = str(L[i][j])+str(L[i][j-1])
                        if(w > 0):
                            tag = str(L[i][j-1])+str(L[i][j])
                        ret = exists(tag, eq)
                                    
                        if( (ret == 0) and (w != 0)) :
                            print("Appending to eq: %d %d and i: %d j:%d"%(L[i][j],L[i][j-1],i,j))
                            eq.append([L[i][j], L[i][j-1], tag])    
                    
                    if( (i!= rows-1) and (L[i+1][j-1]!= 0) and (L[i+1][j-1]!= L[i][j] )  ):
                        w = L[i][j] - L[i+1][j-1]
                        if(w < 0):
                            tag = str(L[i][j])+str(L[i+1][j-1])
                        if(w > 0):
                            tag = str(L[i+1][j-1])+str(L[i][j])
                        ret = exists(tag, eq)
                                    
                        if( (ret == 0) and (w != 0)) :
                            print("Appending to eq: %d %d and i: %d j:%d"%(L[i][j],L[i+1][j-1],i,j))
                            eq.append([L[i][j], L[i+1][j-1], tag])        
                        
                        
                if(i!= 0):
                    if( (L[i-1][j]!= 0) and (L[i-1][j]!= L[i][j] ) ):
                        w = L[i][j] - L[i-1][j]
                        if(w < 0):
                            tag = str(L[i][j])+str(L[i-1][j])
                        if(w > 0):
                            tag = str(L[i-1][j])+str(L[i][j])
                        ret = exists(tag, eq)
                                    
                        if( (ret == 0) and (w != 0)) :
                            print("Appending to eq: %d %d and i: %d j:%d"%(L[i][j],L[i-1][j],i,j))
                            eq.append([L[i][j], L[i-1][j], tag])    
                        
print("EQ NOW AFTER NEW CODE IS")
print(eq)
to_remember = []

for indx in range(len(eq)):

    print('Equivelant labels adjustment')
    print(eq)
    print('L is now: ')
    print(L)
     
    a = eq[indx][0]
    b = eq[indx][1]
    
    tmpval = 0
    found_in_remember = 0
    
    for i in range(len(to_remember)):
        
        if(a == to_remember[i][0]):
            found_in_remember = 1
            tmpval = to_remember[i][1]
    
    for i in range(rows):
        for j in range(cols):
            if(L[i][j] == b):
                if(found_in_remember):
                    print('Found in remember')
                    print('%d to %d'%(L[i][j], tmpval))
                    L[i][j] = tmpval
                    print(L[i][j])
                else:                
                    print('%d to %d'%(L[i][j], a))
                    L[i][j] = a
                    print(L[i][j])
    if(found_in_remember):
        to_remember.append([b, tmpval])    
    else:
        to_remember.append([b,a])
     
print('After processing')
print(L)
# editing L to get incrementing labels 1 to max
# without skipping integers, as implemented above.
tmp = []
total_labels = 0
# place in tmp each different label of L array
for i in range(rows):
    for j in range(cols):
        found = 0
        val = L[i][j]
        if(val == 0):
            continue
        if(len(tmp) == 0):
            tmp.append(val)
            total_labels = total_labels+1
            continue
        else:
            for k in range(len(tmp)):
                if(tmp[k] == val):
                    found = found + 1
                    break
            if(found == 1):
                continue
            tmp.append(val)
            total_labels = total_labels+1
toadd = 0

for k in range(len(tmp)):
    #print('Checking for %d label'%(tmp[k]))
    toadd = toadd + 1

    for i in range(rows):
        for j in range(cols):
            
            if(L[i][j] == tmp[k]):
                L[i][j] = toadd
                #print('Place : %d %d'%(toadd, L[i][j]))
    
    
if(n == 4 or n == 8):
    print('Labeled image')
    print('Total labels found: %d'%(total_labels))
    plt.figure(2)
    plt.imshow(L)
    plt.title('Labeled binary image')
    plt.show()
    
