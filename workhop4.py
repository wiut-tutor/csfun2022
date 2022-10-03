from PIL import Image
import matplotlib.pyplot as plt
#Read image
img=Image.open('.jpg')
#show image
plt.imshow(img)
plt.show()