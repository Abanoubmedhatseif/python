import shapes

def main():
    r1 = shapes.Rectangle("red", 5, 5)
    print(r1.calculate_area())
    print(r1._color)
    print(r1.name)

main()