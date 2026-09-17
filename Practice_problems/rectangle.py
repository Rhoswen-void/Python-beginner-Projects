class Rectangle:

    def __init__(self, width, height):
        self._width = width #_width represents a protected attribute that can be only accessed in the class
        self._height = height

    @property
    def width(self):
        return f"{self._width:.2f} cm"

    @property
    def height(self):
        return f"{self._height:.2f} cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width cant be zero or negative")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height cant be zero or negative")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted.")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted.")


rec1 = Rectangle(3,4)
rec1.height = 5
rec1.width = 6

print(rec1.height)

del rec1.width
del rec1.height



    