import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

'''
    Mouzakitis Nikolaos TP4460 hmu
    
    Tested with a fingerprint image found on google.   
'''
desired_difference = 1

test = mpimg.imread('fingerprint.jpg')
a = np.asarray(test[:,:,0], dtype = np.uint8 )

figure1 = plt.figure(1)
plt.imshow( a , cmap='gray')
plt.title('Fingerprint to test the algorithm')
plt.show()


mesi_timi_image = np.mean(a)
print('initial threshold: %f' %(mesi_timi_image))
rows = a.shape[0]
cols = a.shape[1]

# separating into 2 different labels the image
label_a = 44
label_b = 88
b = np.copy(a)

for i in range(rows):
    
    for j in range(cols):
        
        if( a[i][j] >= (int)(mesi_timi_image)):
            b[i][j] = label_b;
        else:
            b[i][j] = label_a;
            
run = 0

while(1):
    m1 = 0
    m2 = 0
    cnt_m1 = 0
    cnt_m2 = 0
    
    print('----------------\nRun: %d'%(run))
    for i in range(rows):
        for j in range(cols):
            if (b[i][j] == label_b):
                m1 = m1 + a[i][j]
                cnt_m1 += 1
            if (b[i][j] == label_a):
                m2 = m2 + a[i][j]
                cnt_m2 += 1
    
    m1 =  m1/cnt_m1
     
    print('m1: is %f' %(m1))   
    m2 =  m2/cnt_m2
     
    print('m2: is %f' %(m2))  
    run += 1              
    
    tmp = (m1 + m2)/ 2   
    print('error:  %f'%(abs(mesi_timi_image - tmp)) )
    if(abs(mesi_timi_image - tmp) <= desired_difference):
        break
    
    
    mesi_timi_image = tmp
    print('new calculated median value %f'%(mesi_timi_image) )
    
    for i in range(rows):
        for j in range(cols):    
            if( a[i][j] >= (int)(mesi_timi_image)):
                b[i][j] = label_b;
            else:
                b[i][j] = label_a;    
            
c = np.zeros([rows, cols])

for i in range(rows):
    for j in range(cols):
        if(a[i][j] >= mesi_timi_image):
            c[i][j] = 1;
        else:
            c[i][j] = 0

print('Segmented with: %f' %(mesi_timi_image)) 
figure2 = plt.figure(2)
plt.imshow( c , cmap='gray')
plt.title('Final segmentation')
plt.show()           
            
