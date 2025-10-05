import math

class GeometryCalculator:

    def calculate_circle_area(self, radius):
        return math.pi * radius ** 2

    def calculate_rectangle_area(self, length, width):
        return length * width

if __name__ == "__main__":
    calculator = GeometryCalculator()

    # TODO: Implement circle area
    # In geometry_calculator.py on feature/circle-area branch
    
    radius = 4
    print(f"The area of the circle with radius {radius} = {calculator.calculate_circle_area(radius)}")
    print(f"The perimeter of the circle with radius {radius} = {2 * math.pi * radius}")
    