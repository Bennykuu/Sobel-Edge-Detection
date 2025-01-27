# Sobel-Edge-Detection

This project shows how to implement Sobel edge detection with Python using the Pillow library. The script locates edges of images through change in brightness gradients. It utilizes the Sobel filter to find gradients in the horizontal x and vertical y direction, then combines them and generates an image representing the intensity of edges that were found.

### 1. How It Works

2. **Image Preprocessingr**:
   The input image is Converted to grayscale. To avoid boundary issues when applying filters, the border is padded by 1 pixel (using edge replication).

2. **Sobel Filter**:  
   The Sobel filter is a mathematical operator used to calculate gradients in an image. It uses two 3×3 matrices, defined as:

   **Sobel filter for the x-direction ($G_x$)**:
   
   <div align="center">  
   $$G_x = \left[ \matrix{ 1 & 0 & -1 \cr 2 & 0 & -2 \cr 1 & 0 & -1 } \right]$$  
   <div align="left"> 

   **Sobel filter for the y-direction ($G_y$)**:

   <div align="center">  
   $$G_y = \left[ \matrix{ 1 & 2 & 1 \cr 0 & 0 & 0 \cr -1 & -2 & -1 } \right]$$ 
   <div align="left"> 

   These matrices detect changes in brightness:  
   - $G_x$: Detects vertical edges.  
   - $G_y$: Detects horizontal edges.

3. **Gradient Calculation**:   
   For each pixel in the image, a 3x3 region around the pixel is multiplied elementwise by ($G_x$)​ and ($G_y$).
   The horizontal ($g_x$) and vertical ($g_y$) gradients are computed with:
   
   <div align="center">  
   $$g_x = \sum_{k=1}^n(A \cdot G_x)$$,   $$g_y = \sum_{k=1}^n(A \cdot G_y)$$    
   <div align="left">  
   <br>
      
   A is define as the source image. The resulting gradient approximations can be combined to give the gradient magnitude, using   

   <div align="center">  
   $$g = \sqrt{g_x^2 + g_y^2}$$   
   <div align="left">   

4. **Thresholding**:   
   The gradient magnitude is thresholded to keep only strong edges. Pixels with gradient values less than a minimum threshold are set to 0, and those greater than a maximum threshold are set to 255.

   <div align="center">
   $$n = \{ 0 \text{ if } g < \text{min threshold}, \, 255 \text{ if } g > \text{max threshold} \} $$
   <div align="left"> 
   
### 2. example
##### input image (cat1.jpg, Test2.png):
<p align="left">
  <img src="example_Images/cat1.jpg" width="500" />
  <img src="example_Images/Test2.png" width="450" />
</p>

##### Output: The generated ASCII art (Cat ASCII Faktor 4, Test ASCII Faktor 8):
<p align="left">
  <img src="example_Images/cat1_ascii_factor4.PNG" width="500" />
  <img src="example_Images/Test2_ascii_factor8.PNG" width="450" />
</p>
