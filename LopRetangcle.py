class Rectangle:
    def __init__(self,x,y,Color) :
        self.x = x
        self.y = y
        self.Color = Color
    def perimeter(self):
        return (self.x+self.y)*2
    def area(self):
        return self.x*self.y
    def color(self):
        return self.Color.lower().capitalize()
    

if __name__ == '__main__':
    arr = input().split()
    if int(arr[0]) > 0 and int(arr[1]) > 0:
        r = Rectangle(int(arr[0]), int(arr[1]), arr[2]) 
        print('{} {} {}'.format(r.perimeter(), r.area(), r.color())) 
    else: print('INVALID')