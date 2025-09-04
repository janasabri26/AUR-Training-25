import numpy as np
import matplotlib.pyplot as plt
import cv2


def convolve(image,kernel):
    k_rows, k_columns = kernel.shape 
    kernel =np.flipud(np.fliplr(kernel))
    
    i_rows,i_columns=image.shape
    pad_h=k_rows//2
    pad_v=k_columns//2
    padded=np.pad(image,((pad_h,pad_h),(pad_v,pad_v)),mode="constant",constant_values=0)

    output_image=np.zeros_like(image,dtype=float)
    for i in range(i_rows):
        for j in range(i_columns):
            region=padded[i:i+k_rows,j:j+k_columns]
            output_image[i,j]=np.sum(region*kernel)
    output_image= np.clip(output_image, 0, 255).astype(np.uint8)
    return output_image

image_path=input("enter the image path:")
image=cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)

image=cv2.resize(image, (800, 600))


if image is None:
    print("Error couldn't load an image")





#test
img = image
gaussian_filtered = cv2.GaussianBlur(img, (5, 5), 1)
median_filtered = cv2.medianBlur(img, 5)

fig, axes = plt.subplots(2, 3, figsize=(8, 8))
axes[0, 0].imshow(img,cmap='gray')
axes[0, 0].set_title('Original Image')
axes[0, 0].axis('off')
axes[0, 1].imshow(convolve(img, np.ones((5, 5)) / 25),cmap='gray')
axes[0, 1].set_title('Box Filter')
axes[0, 1].axis('off')

axes[1, 0].imshow(convolve(img, np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])),cmap='gray'
)
axes[1, 0].set_title('Horizontal Sobel Filter')
axes[1, 0].axis('off')

axes[1, 1].imshow(convolve(img, np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])),cmap='gray'
)
axes[1, 1].set_title('Vertical Sobel Filter')
axes[1, 1].axis('off')

axes[1, 2].imshow(gaussian_filtered,cmap='gray')
axes[1, 2].set_title("Gaussian Filter")
axes[1, 2].axis('off')

axes[0, 2].imshow(median_filtered,cmap='gray')
axes[0, 2].set_title("Median Filter")
axes[0, 2].axis('off')

plt.show()


