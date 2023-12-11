from spherov2.types import Color

class Animaition:
    def __init__(self):
        self.angle_frames = [[[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 8, 8, 1],
[1, 1, 1, 1, 2, 8, 8, 1],
[1, 1, 1, 2, 2, 1, 1, 1],
[1, 1, 2, 2, 1, 1, 1, 1],
[1, 2, 2, 1, 1, 1, 1, 1],
[2, 2, 1, 1, 1, 1, 1, 1],
[2, 1, 1, 1, 1, 1, 1, 1]],
[[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 2, 8, 8, 1],
[1, 1, 1, 2, 2, 8, 8, 1],
[1, 1, 2, 2, 1, 1, 1, 1],
[1, 2, 2, 1, 1, 1, 1, 1],
[2, 2, 1, 1, 1, 1, 1, 1],
[2, 1, 1, 1, 1, 1, 1, 1]],
[[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 2, 2, 2, 8, 8, 1],
[1, 2, 2, 2, 2, 8, 8, 1],
[2, 2, 1, 1, 1, 1, 1, 1],
[2, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1]],
[[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1],
[2, 2, 2, 2, 2, 8, 8, 1],
[2, 2, 2, 2, 2, 8, 8, 1],
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1]],
[[1, 1, 1, 1, 1, 1, 1, 1],
[2, 1, 1, 1, 1, 1, 1, 1],
[2, 2, 1, 1, 1, 1, 1, 1],
[1, 2, 2, 2, 2, 8, 8, 1],
[1, 1, 2, 2, 2, 8, 8, 1],
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1]],
[[2, 1, 1, 1, 1, 1, 1, 1],
[2, 2, 1, 1, 1, 1, 1, 1],
[1, 2, 2, 1, 1, 1, 1, 1],
[1, 1, 2, 2, 1, 1, 1, 1],
[1, 1, 1, 2, 2, 8, 8, 1],
[1, 1, 1, 1, 2, 8, 8, 1],
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1]],
[[2, 1, 1, 1, 1, 1, 1, 1],
[2, 2, 1, 1, 1, 1, 1, 1],
[1, 2, 2, 1, 1, 1, 1, 1],
[1, 1, 2, 2, 1, 1, 1, 1],
[1, 1, 1, 2, 2, 1, 1, 1],
[1, 1, 1, 1, 2, 8, 8, 1],
[1, 1, 1, 1, 1, 8, 8, 1],
[1, 1, 1, 1, 1, 1, 1, 1]]]


        self.angle_pallete = [
Color(255, 255, 255),
Color(0, 0, 0),
Color(255, 0, 0),
Color(255, 64, 0),
Color(255, 128, 0),
Color(255, 191, 0),
Color(255, 255, 0),
Color(185, 246, 30),
Color(0, 255, 0),
Color(185, 255, 255),
Color(0, 255, 255),
Color(0, 0, 255),
Color(145, 0, 211),
Color(157, 48, 118),
Color(255, 0, 255),
Color(204, 27, 126)
]
        self.angle_fps = 10
        self.arrow_frames = [[[1, 1, 1, 2, 1, 1, 1, 1],
[1, 1, 2, 2, 1, 1, 1, 1],
[1, 2, 11, 2, 1, 1, 1, 1],
[2, 11, 11, 2, 2, 2, 2, 2],
[2, 11, 11, 2, 2, 2, 2, 2],
[1, 2, 11, 2, 1, 1, 1, 1],
[1, 1, 2, 2, 1, 1, 1, 1],
[1, 1, 1, 2, 1, 1, 1, 1]]]


        self.arrow_palette = [Color(255, 255, 255),
Color(0, 0, 0),
Color(255, 0, 0),
Color(255, 64, 0),
Color(255, 128, 0),
Color(255, 191, 0),
Color(255, 255, 0),
Color(185, 246, 30),
Color(0, 255, 0),
Color(185, 255, 255),
Color(0, 255, 255),
Color(0, 0, 255),
Color(145, 0, 211),
Color(157, 48, 118),
Color(255, 0, 255),
Color(204, 27, 126)]
        self.arrow_fps = 10
        self.return_frames = [[[1, 2, 2, 2, 2, 2, 1, 1],
[1, 2, 1, 2, 2, 1, 1, 1],
[1, 1, 2, 2, 1, 2, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 2, 2, 2, 1, 1, 1],
[1, 2, 1, 2, 1, 2, 1, 1],
[1, 2, 1, 2, 1, 2, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1]]]


        self.return_palette = [
Color(255, 255, 255), 
Color(0, 0, 0), 
Color(255, 0, 0), 
Color(255, 64, 0), 
Color(255, 128, 0), 
Color(255, 191, 0), 
Color(255, 255, 0), 
Color(185, 246, 30), 
Color(0, 255, 0), 
Color(185, 255, 255), 
Color(0, 255, 255), 
Color(0, 0, 255), 
Color(145, 0, 211), 
Color(157, 48, 118), 
Color(255, 0, 255), 
Color(204, 27, 126) 
]
        self.return_fps = 10
        self.check_frames = [[[1, 1, 1, 8, 1, 1, 1, 1],
[1, 1, 1, 8, 8, 1, 1, 1],
[1, 1, 1, 1, 8, 8, 1, 1],
[1, 1, 1, 1, 1, 8, 8, 1],
[1, 1, 1, 1, 8, 8, 1, 1],
[1, 1, 1, 8, 8, 1, 1, 1],
[1, 1, 8, 8, 1, 1, 1, 1],
[1, 8, 8, 1, 1, 1, 1, 1]],
[[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1]]]


        self.check_palette = [
Color(255, 255, 255),
Color(0, 0, 0),
Color(255, 0, 0),
Color(255, 64, 0),
Color(255, 128, 0),
Color(255, 191, 0),
Color(255, 255, 0),
Color(185, 246, 30),
Color(0, 255, 0),
Color(185, 255, 255),
Color(0, 255, 255),
Color(0, 0, 255),
Color(145, 0, 211),
Color(157, 48, 118),
Color(255, 0, 255),
Color(204, 27, 126)
]
        self.check_fps = 10
        self.heart_frames = [[[1, 1, 2, 2, 1, 1, 1, 1],
[1, 2, 2, 2, 2, 1, 1, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 2, 2, 2, 2, 1, 1, 1],
[1, 1, 2, 2, 1, 1, 1, 1]],

[[1, 1, 2, 2, 1, 1, 1, 1],
[1, 2, 2, 2, 2, 1, 1, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 2, 2, 2, 2, 1, 1, 1],
[1, 1, 2, 2, 1, 1, 1, 1]],

[[1, 1, 2, 2, 1, 1, 1, 1],
[1, 2, 2, 2, 2, 1, 1, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 2, 2, 2, 2, 1, 1, 1],
[1, 1, 2, 2, 1, 1, 1, 1]],

[[1, 1, 2, 2, 1, 1, 1, 1],
[1, 2, 2, 2, 2, 1, 1, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 2, 2, 2, 2, 1, 1, 1],
[1, 1, 2, 2, 1, 1, 1, 1]],

[[1, 1, 2, 2, 1, 1, 1, 1],
[1, 2, 2, 2, 2, 1, 1, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 2, 2, 2, 2, 1, 1, 1],
[1, 1, 2, 2, 1, 1, 1, 1]],

[[1, 1, 2, 2, 1, 1, 1, 1],
[1, 2, 2, 2, 2, 1, 1, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 2, 2, 2, 2, 1, 1, 1],
[1, 1, 2, 2, 1, 1, 1, 1]],

[[1, 1, 2, 2, 1, 1, 1, 1],
[1, 2, 2, 2, 2, 1, 1, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 2, 2, 2, 2, 1, 1, 1],
[1, 1, 2, 2, 1, 1, 1, 1]],

[[1, 2, 2, 2, 2, 1, 1, 1],
[2, 2, 2, 2, 2, 2, 1, 1],
[2, 2, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 2, 2],
[1, 2, 2, 2, 2, 2, 2, 2],
[2, 2, 2, 2, 2, 2, 2, 1],
[2, 2, 2, 2, 2, 2, 1, 1],
[1, 2, 2, 2, 2, 1, 1, 1]],

[[2, 2, 2, 2, 2, 2, 1, 1],
[2, 2, 2, 2, 2, 2, 2, 1],
[2, 2, 2, 2, 2, 2, 2, 2],
[2, 2, 2, 2, 2, 2, 2, 2],
[2, 2, 2, 2, 2, 2, 2, 2],
[2, 2, 2, 2, 2, 2, 2, 2],
[2, 2, 2, 2, 2, 2, 2, 1],
[2, 2, 2, 2, 2, 2, 1, 1]],

[[1, 2, 2, 2, 2, 1, 1, 1],
[2, 2, 2, 2, 2, 2, 1, 1],
[2, 2, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 2, 2],
[1, 2, 2, 2, 2, 2, 2, 2],
[2, 2, 2, 2, 2, 2, 2, 1],
[2, 2, 2, 2, 2, 2, 1, 1],
[1, 2, 2, 2, 2, 1, 1, 1]],

[[1, 1, 2, 2, 1, 1, 1, 1],
[1, 2, 2, 2, 2, 1, 1, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 2, 2, 2, 2, 1, 1, 1],
[1, 1, 2, 2, 1, 1, 1, 1]],

[[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 2, 2, 1, 1, 1, 1],
[1, 3, 2, 2, 2, 1, 1, 1],
[1, 1, 3, 2, 2, 2, 1, 1],
[1, 1, 3, 2, 2, 2, 1, 1],
[1, 3, 2, 2, 2, 1, 1, 1],
[1, 1, 2, 2, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1]],

[[1, 1, 2, 2, 1, 1, 1, 1],
[1, 2, 2, 2, 2, 1, 1, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 2, 2, 2, 2, 1, 1, 1],
[1, 1, 2, 2, 1, 1, 1, 1]],

[[1, 2, 2, 2, 2, 1, 1, 1],
[2, 2, 2, 2, 2, 2, 1, 1],
[2, 2, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 2, 2],
[1, 2, 2, 2, 2, 2, 2, 2],
[2, 2, 2, 2, 2, 2, 2, 1],
[2, 2, 2, 2, 2, 2, 1, 1],
[1, 2, 2, 2, 2, 1, 1, 1]],

[[2, 2, 2, 2, 2, 2, 1, 1],
[2, 2, 2, 2, 2, 2, 2, 1],
[2, 2, 2, 2, 2, 2, 2, 2],
[2, 2, 2, 2, 2, 2, 2, 2],
[2, 2, 2, 2, 2, 2, 2, 2],
[2, 2, 2, 2, 2, 2, 2, 2],
[2, 2, 2, 2, 2, 2, 2, 1],
[2, 2, 2, 2, 2, 2, 1, 1]],

[[1, 2, 2, 2, 2, 1, 1, 1],
[2, 2, 2, 2, 2, 2, 1, 1],
[2, 2, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 2, 2],
[1, 2, 2, 2, 2, 2, 2, 2],
[2, 2, 2, 2, 2, 2, 2, 1],
[2, 2, 2, 2, 2, 2, 1, 1],
[1, 2, 2, 2, 2, 1, 1, 1]],

[[1, 1, 2, 2, 1, 1, 1, 1],
[1, 2, 2, 2, 2, 1, 1, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 1, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 1, 1],
[1, 2, 2, 2, 2, 1, 1, 1],
[1, 1, 2, 2, 1, 1, 1, 1]],

[[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 2, 2, 1, 1, 1, 1],
[1, 3, 2, 2, 2, 1, 1, 1],
[1, 1, 3, 2, 2, 2, 1, 1],
[1, 1, 3, 2, 2, 2, 1, 1],
[1, 3, 2, 2, 2, 1, 1, 1],
[1, 1, 2, 2, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1]]]


        self.heart_palette = [
Color(255, 255, 255),
Color(0, 0, 0),
Color(255, 0, 0),
Color(46, 1, 1),
Color(255, 128, 0),
Color(255, 191, 0),
Color(255, 255, 0),
Color(185, 246, 30),
Color(0, 255, 0),
Color(185, 255, 255),
Color(0, 255, 255),
Color(0, 0, 255),
Color(145, 0, 211),
Color(157, 48, 118),
Color(255, 0, 255),
Color(204, 27, 126)
]
        self.heart_fps = 24