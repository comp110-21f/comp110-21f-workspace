from __future__ import annotations
import math

class Vector:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    

    def __add__(self, rhs: Vector) -> Vector:
        """Overload the addition operator for Vectors."""
        return Vector(self.x + rhs.x, self.y + rhs.y)
    
    def __mul__(self, z: float) -> Vector:
        """Overload the multiplication operator for Vectors."""
        return Vector(self.x * z, self.y * z)

    def __div__(self, z: float) -> Vector:
        """Overload the multiplication operator for Vectors."""
        return Vector(self.x / z, self.y / z)

    def points_to_vector(p_1: tuple, p_2: tuple) -> Vector:
        return Vector(p_2[0] - p_1[0], p_2[1] - p_1[1])

    def magnitude(self) -> float:
        return math.sqrt((self.x)**2 + (self.y)**2)

    def normalize(self) -> Vector:
        return self.__div__(self.magnitude())
    
    
    def __sub__(self, rhs: Vector) -> Vector:
        """Overload the multiplication operator for Vectors."""
        return Vector(self.x - rhs.x , self.y - rhs.y)

    def to_tuple(self) -> tuple:
        return (self.x, self.y)

    def __repr__(self):
        return ("Vector: " + str(self.x) + ", " + str(self.y))