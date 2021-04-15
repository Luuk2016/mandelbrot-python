from PIL import Image, ImageDraw

class Mandelbrot:

    def __init__(self, max_iter, width, height):
        self.max_iter = max_iter
        self.width = width
        self.height = height

    def calculate(self, c):
        z = 0
        n = 0
        while abs(z) <= 2 and n < self.max_iter:
            z = z*z + c
            n += 1
        return n

    def generateImage(self):
        RE_START = -2
        RE_END = 1
        IM_START = -1
        IM_END = 1

        im = Image.new('RGB', (self.width, self.height), (0, 0, 0))
        draw = ImageDraw.Draw(im)

        for x in range(0, self.width):
            for y in range(0, self.height):

                # Convert the pixel coordinate to a complex number
                c = complex(RE_START + (x / self.width) * (RE_END - RE_START),
                            IM_START + (y / self.height) * (IM_END - IM_START))

                # Calculate the total number of iterations
                m = self.calculate(c)

                # Calculate the color based on the number of iterations
                color = 255 - int(m * 255 / self.max_iter)

                # Plot the point
                draw.point([x, y], (color, color, color))

        im.save('mandelbrot.png', 'PNG')