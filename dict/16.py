"""Write a Python program to get a dictionary from an object's fields. """


class dicobj():
    def __init__(self):
        self.x = "abc"
        self.y = "def"
        self.z = "gaa"


test = dicobj()
print(test.__dict__)
