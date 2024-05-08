#Python

# This will calculate shape areas

def main():
    print("this is our shapes program")
    tri_area = calc_tri_area(5, 12)
    print(f"The area of triangle is {tri_area}.")

def calc_tri_area(b, h):
    area = 1/2 * h * b
    return area

main()