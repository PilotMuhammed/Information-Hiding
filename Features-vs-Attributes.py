'''

Requirements:
- Pillow pckg.
- Opencv pckg.
- Matplotlib pckg.
- Img. ( one image for testing )

'''
## Extracting Basic Image Attributes
from PIL import Image
# Load the image
image_path = '1.jpeg'
image = Image.open(image_path)

# Extract basic attributes
image_format = image.format
image_size = image.size
image_mode = image.mode
print(f"Format: {image_format}, Size: {image_size}, Mode: {image_mode}")


## Extracting Image Edges ( as an example for img. Features )

import cv2
import matplotlib.pyplot as plt
# Load the image
image_path = '1.png'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#convert image to grayscale
# Save the grayscale image
cv2.imwrite('grayscale_image.jpeg', image)
# Apply Canny edge detector
edges = cv2.Canny(image, threshold1=220, threshold2=255)
# Display the result
plt.imshow(edges, cmap='gray')
plt.title('Edge Image')
plt.show()
