def get_radius(prompt) :
    r = int(input(prompt))
    return r
def get_circle_area(radius) :
    area = 3.14*(radius**2)
    return area
def show_circle_area() :
    radius = get_radius('반지름의 길이는?')
    area = get_circle_area(radius)
    print('원의 넓이는:', '3.14*' ,radius, '*',radius, '=', area)
show_circle_area()