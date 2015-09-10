from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, EllipseAsset, PolygonAsset

red= Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

thinline = LineStyle(1, black)

rectangle1 = RectangleAsset(50, 20, thinline, blue)
rectangle2 = RectangleAsset(100,40, thinline,red)

Sprite(rectangle1, (225,210))
Sprite(rectangle2, (200, 200))

myapp = App()
myapp.run()