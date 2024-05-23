class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1  # 좌측 상단 x 좌표
        self.y1 = y1  # 좌측 상단 y 좌표
        self.x2 = x2  # 우측 하단 x 좌표
        self.y2 = y2  # 우측 하단 y 좌표

    def getArea(self):
        return (self.x2 - self.x1) * (self.y2 - self.y1)

    def getPerimeter(self):
        return 2 * ((self.x2 - self.x1) + (self.y2 - self.y1))

    def show(self):
        print(f'좌측 상단 꼭지점이 ({self.x1}, {self.y1})이고 우측 하단 꼭지점이 ({self.x2}, {self.y2})인 사각형입니다.')

# 주 프로그램부
r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()
r1.show()
print(f'넓이는 {a}, 둘레는 {p}')