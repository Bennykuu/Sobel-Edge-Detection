# Sobel-Edge-Detection

This project shows how to implement Sobel edge detection with Python using the Pillow library. The script locates edges of images through change in brightness gradients. It utilizes the Sobel filter to find gradients in the horizontal x and vertical y direction, then combines them and generates an image representing the intensity of edges that were found.

### 1. How It Works
1.  Sobel Filter:
        The Sobel filter is a mathematical operator used to calculate gradients in an image. It uses two 3×3 matrices, defined as:   
        **Sobel filter for the x-direction (\(G_x\)):**

\[
G_x =
\begin{bmatrix}
1 & 0 & -1 \\
2 & 0 & -2 \\
1 & 0 & -1
\end{bmatrix}
\]

