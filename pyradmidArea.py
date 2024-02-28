import math

def calcBaseArea(side):
    return side ** 2

def calcSlantHeight(side_length, height):
    return math.sqrt((side_length / 2) ** 2 + height ** 2)

def square_pyramid_surface_area(side_length, height):
    base_area = calcBaseArea(side_length)
    slant_height = calcSlantHeight(side_length, height)
    lateral_area = 2 * side_length * slant_height
    surface_area = base_area + lateral_area
    return surface_area

def prntSurfArea(total_base_area, total_side_area):
    print("The total surface area of the square pyramid is:", total_base_area + total_side_area, "square feet")

def main():
    side = float(input("Enter the side length of the base of the square pyramid in feet: "))
    height = float(input("Enter the height of the square pyramid in feet: "))

    total_base_area = calcBaseArea(side)
    total_side_area = square_pyramid_surface_area(side, height) - total_base_area

    print(f"Base surface area of the square pyramid is {total_base_area} square feet.")
    print(f"Total surface area of all four sides of the square pyramid is {total_side_area} square feet.")
    prntSurfArea(total_base_area, total_side_area)

main()
