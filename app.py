from mandelbrot import Mandelbrot

# Set the default values
max_iter = 250
height = 1920
width = 1080

# Create a new Mandelbrot object
mandelbrot = Mandelbrot(max_iter, height, width)

# Generate the image
mandelbrot.generateImage()