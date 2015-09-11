from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, EllipseAsset, PolygonAsset

red= Color(0xff0000, 1.0)
green = Color(0x00ff00, 0.5)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)

thinline = LineStyle(1, black)
thickline = LineStyle(4, black)

rectangle1 = RectangleAsset(100, 100, thinline, blue)
rectangle2 = RectangleAsset(100, 100, thinline, white)
ellipse = EllipseAsset(10, 10, thickline, blue)
#not finished polygon
triangle = PolygonAsset([(450, 500), (550, 550), (550, 400), (450,500)], thinline, green)


Sprite(rectangle1, (200,200))
Sprite(rectangle2, (250, 250))
Sprite(ellipse,(500, 500))
Sprite(triangle)

myapp = App()
myapp.run()