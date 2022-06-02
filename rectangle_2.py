from rectangle import Rectangle, Square, Circle

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

print(rect_1.get_area())
print(rect_2.get_area())


square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_area_square())
print(square_2.get_area_square())

circle_1 = Circle(6)
circle_2 = Circle(12)

print(round(circle_1.get_area_circle()))
print(round(circle_2.get_area_circle()))

figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]
for figure in figures:
    if isinstance(figure, Square):
        print("площадь квадрата = ", figure.get_area_square())
    elif isinstance(figure, Circle):
        print("площадь круга = ", figure.get_area_circle())
    else:
        print("площадь прямоугольника = ",figure.get_area())


# C:\Users\1\PycharmProjects\pythonProject_16\venv\Scripts\python.exe C:/Users/1/PycharmProjects/pythonProject_16/rectangle_2.py
# 12
# 60
# 25
# 100
# 108
# 432
# площадь прямоугольника =  12
# площадь прямоугольника =  60
# площадь квадрата =  25
# площадь квадрата =  100
# площадь круга =  108
# площадь круга =  432




