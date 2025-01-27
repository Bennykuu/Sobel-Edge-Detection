from PIL import Image
import numpy as np

picture = input("which image do you wanna us:").strip().strip('"').strip("'")

# Converts the image to grayscale (brightness values from 0 to 255)
image = Image.open(picture).convert("L")

# Define Sobel filters for x- and y-directions
sobel_x = np.array([[1, 0, -1],
                    [2, 0, -2],
                    [1, 0, -1]])

sobel_y = np.array([[ 1,  2,  1],
                    [ 0,  0,  0],
                    [-1, -2, -1]])

# Convert the image into a numpy array
image_array = np.array(image)

# Empty arrays for gradients in the x-direction, y-direction, and edge strength
gradient_x = np.zeros_like(image_array)
gradient_y = np.zeros_like(image_array)
gradient = np.zeros_like(image_array)

# Padding extends the image by 1 pixel on all sides to solve edge issues.
# The border will be filled with the nearest values (mode='edge').
# ((1, 1), (1, 1)): Indicates that 1 pixel is added
padded_image = np.pad(image_array, ((1, 1), (1, 1)), mode='edge')

# Apply the filter
for y in range(image_array.shape[0]):
    for x in range(image_array.shape[1]):
        # Sobel filter is a 3x3 matrix (3x3 region)
        region = padded_image[y:y + 3, x:x + 3]

        # Calculate gradients
        gx = np.sum(region * sobel_x)
        gy = np.sum(region * sobel_y)

        # Store the values
        gradient_x[y, x] = gx
        gradient_y[y, x] = gy

        # Calculate edge strength
        gradient[y,x] = np.sqrt(gx ** 2 + gy ** 2)

# threshold
min_threshold = 30
max_threshold = 200

# Apply threshold
gradient[gradient < min_threshold] = 30
gradient[gradient > max_threshold] = 255

edge_image = Image.fromarray(gradient)
edge_image.show()