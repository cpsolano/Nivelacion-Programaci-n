import numpy as np
from skimage import io
import matplotlib.pyplot as plt
photo = io.imread("Captura.PNG")
print type(photo)

print photo.shape
plt.imshow(photo)

plt.imshow(photo[::-1])
plt.show()
plt.imshow(photo[:,::-1])
plt.show()
plt.imshow(photo[50:150, 150:280])
plt.show()
plt.imshow(photo[::2,::2])

photo_sin = np.sin(photo)
print photo_sin

print np.sum(photo)
print np.prod(photo)
print np.mean(photo)
print np.std(photo)
print np.var(photo)
print np.min(photo)
print np.max(photo)
print np.argmin(photo)
print np.argmax(photo)

z = np.array([1,2,3,4,5])
print z < 3
print z > 3
print z[z > 3]

photo_masked = np.where(photo > 100, 255, 0)
plt.imshow(photo_masked)

a_array = np.array([1,2,3,4,5])
b_array = np.array([6,7,8,9,10])
print a_array + b_array
print a_array + 30
print a_array * b_array
print a_array * 10

plt.imshow(photo[:,:,0].T) #gira la imagen
x = np.array([2,1,4,3,5])
print np.sort(x) #ordena los valores dentro del arreglo
