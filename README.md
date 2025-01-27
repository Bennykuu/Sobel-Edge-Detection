# Sobel-Edge-Detection

This project shows how to implement Sobel edge detection with Python using the Pillow library. The script locates edges of images through change in brightness gradients. It utilizes the Sobel filter to find gradients in the horizontal x and vertical y direction, then combines them and generates an image representing the intensity of edges that were found.

### 1. How It Works

2. **Image Preprocessingr**:
   The input image is Converted to grayscale. To avoid boundary issues when applying filters, the border is padded by 1 pixel (using edge replication).

2. **Sobel Filter**:  
   The Sobel filter is a mathematical operator used to calculate gradients in an image. It uses two 3×3 matrices, defined as:

   **Sobel filter for the x-direction (\(G_x\))**:  
   ```math
   G_x =
   \begin{bmatrix}
   1 & 0 & -1 \\
   2 & 0 & -2 \\
   1 & 0 & -1
   \end{bmatrix}
   ```

   **Sobel filter for the y-direction \(G_y\)**:  (\(G_x\))
   ```math
   G_y =
   \begin{bmatrix}
   1 & 2 & 1 \\
   0 & 0 & 0 \\
   -1 & -2 & -1
   \end{bmatrix}
   ```

   These matrices detect changes in brightness:  
   - \G_x\: Detects vertical edges.  
   - \G_y\: Detects horizontal edges.

3. **Gradient Calculation**:
   For each pixel in the image a 3x3 region around the pixel is multiplied element-wise by (\G_x\)​ and (\G_y\).
   The horizontal (\g_x\) and vertical (\g_y\) gradients are computed
   

