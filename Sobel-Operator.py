from PIL import Image
import numpy as np

class SobelEdgeDetection:
    def __init__(self, image_path, min_threshold=30, max_threshold=200):
        self.image_path = image_path.strip().strip('"').strip("'")
        self.min_threshold = min_threshold
        self.max_threshold = max_threshold

        # Converts the image to grayscale (brightness values from 0 to 255)
        self.image = Image.open(self.image_path).convert("L")

        # Define Sobel filters for x- and y-directions
        self.sobel_x = np.array([[1, 0, -1],
                                 [2, 0, -2],
                                 [1, 0, -1]])

        self.sobel_y = np.array([[1, 2, 1],
                                 [0, 0, 0],
                                 [-1, -2, -1]])

    def apply_sobel_filter(self):
        # Convert the image into a numpy array
        image_array = np.array(self.image)

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
                gx = np.sum(region * self.sobel_x)
                gy = np.sum(region * self.sobel_y)

                # Store the values
                gradient_x[y, x] = gx
                gradient_y[y, x] = gy

                # Calculate edge strength
                gradient[y, x] = np.sqrt(gx ** 2 + gy ** 2)

        # Apply threshold
        gradient[gradient < self.min_threshold] = 30
        gradient[gradient > self.max_threshold] = 255

        edge_image = Image.fromarray(gradient)
        return edge_image

    def show_edge_image(self):
        edge_image = self.apply_sobel_filter()
        edge_image.show()

    def save_edge_image(self, output_path="sobel_edge_output.jpg"):
        edge_image = self.apply_sobel_filter()
        edge_image.save(output_path)

picture = input("Which image do you want to use: ")
edge_detector = SobelEdgeDetection(picture, min_threshold=30, max_threshold=200)
edge_detector.show_edge_image()  
edge_detector.save_edge_image("sobel_edge_output.jpg")
