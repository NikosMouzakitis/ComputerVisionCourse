import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import skimage as image_tool
from skimage import measure
from skimage.filters import threshold_otsu

A = mpimg.imread('Mermaid.jpg')
cols = A.shape[1]
rows = A.shape[0]
gray = np.ones([rows,cols])
b, g, r    = A[:, :, 0], A[:, :, 1], A[:, :, 2]

gray  = b  
gray=gray.astype(int)
plt.figure(1)
plt.imshow(gray, cmap = "gray")
plt.title("Selected channel")

thresh = threshold_otsu(gray)
bin_img = gray > thresh
bin_img=bin_img.astype(int)

plt.figure(2)
plt.imshow(bin_img,cmap=plt.cm.gray)
plt.title('Binary image')

[Labeled_image,num_of_neighbors] = measure.label(bin_img,  neighbors=4,background=False,return_num=True)

Group_connected_list=image_tool.measure.regionprops(Labeled_image)

List_of_Areas=[]
List_of_Areas.append([d['area'] for d in Group_connected_list ] )
List_of_Areas = np.transpose(List_of_Areas)

Position_of_Areas=[i for i, e in enumerate(Group_connected_list)]
Position_of_Areas=np.asarray(Position_of_Areas, dtype=np.int32) + 1

plt.figure(3)
hist1= plt.hist(gray, bins='auto')
plt.title("Histogram with 'auto' bins")
plt.show()

Position_from_0_to_100=[i for i, e in enumerate(List_of_Areas) if e <=100]
Position_from_0_to_100=np.transpose(Position_from_0_to_100)+1

Position_from_0_to_200=[i for i, e in enumerate(List_of_Areas) if e <= 200]
Position_from_0_to_200=np.transpose(Position_from_0_to_200)+1

Position_from_0_MAX=[i for i,e in enumerate(List_of_Areas) if e >= 0]
Position_from_0_MAX=np.transpose(Position_from_0_MAX)+1
#----------------------------------------------------------------------------------------------------------------------

Image_from_0_to_100=[]
Image_from_0_to_200=[]
Image_from_0_MAX=[]

for i in range(len(Position_from_0_to_100)):    
    Image_from_0_to_100.append(Labeled_image==Position_from_0_to_100[i])

for i in range(len(Position_from_0_to_200)):    
    Image_from_0_to_200.append(Labeled_image==Position_from_0_to_200[i])
    
for i in range(len(Position_from_0_MAX)):    
    Image_from_0_MAX.append(Labeled_image==Position_from_0_MAX[i])


 
for i in range(len(Position_from_0_to_100)):
    
    Image_from_0_to_100[i]=np.asarray(Image_from_0_to_100[i], dtype=np.int32)
    
for i in range(len(Position_from_0_to_200)):    
    
    Image_from_0_to_200[i]=np.asarray(Image_from_0_to_200[i], dtype=np.int32)

for i in range(len(Position_from_0_MAX)):      
    
    Image_from_0_MAX[i]=np.asarray(Image_from_0_MAX[i], dtype=np.int32)
    
 
Image_from_0_to_100=sum(Image_from_0_to_100)
Image_from_0_to_200=sum(Image_from_0_to_200)
Image_from_0_MAX=sum(Image_from_0_MAX)

plt.figure(4)

fig3=plt.figure(4)

subplot3 = fig3.add_subplot(2,3,1)
plt.imshow(A)
plt.title("RGB image")

subplot3 = fig3.add_subplot(2,3,2)
plt.imshow(gray, cmap = "gray")
plt.title("Selected channel")

subplot3=fig3.add_subplot(2, 3, 3)
plt.imshow(Labeled_image )
subplot3.set_title('Original_labeled_Image')

subplot3=fig3.add_subplot(2, 3, 4)
plt.imshow(Image_from_0_to_100,cmap = "gray")
subplot3.set_title('0_to_100')

subplot3=fig3.add_subplot(2, 3, 5)
plt.imshow(Image_from_0_to_200,cmap = "gray")
subplot3.set_title('0_to_200')

subplot3=fig3.add_subplot(2, 3, 6)
plt.imshow(Image_from_0_MAX,cmap = "gray")
subplot3.set_title('0_to_MAX')



