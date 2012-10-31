import math
ANGLE = 4
def rotate_movement(angle, x, y, dr = 1):
    angle = math.radians(angle)
    x += dr * ANGLE * math.sin(angle)
    y += dr * ANGLE * math.cos(angle)
    return [x, y]

def in_bounds(x, y, w, h, xdiff = 0, ydiff = 0):
    if 0 - xdiff > x: x = 0
    if x > w + xdiff:x = w
    if 0 - ydiff > y: y = 0
    if y > h + ydiff: y = h
    return [x,y]

def highscore(score):
    highfile = open('high.txt', 'rU')
    high = int(highfile.read())
    highfile.close()
    print high, "was the highscore"
    print "Your score was", score
    if score > high:
        print "You beat the highscore"
        highfile = open('high.txt', 'w')
        highfile.write(str(score))
        highfile.close()
        
def detect_collision(obj1, obj2):
    if obj1.x + obj1.width / 2.0 > obj2.x - obj2.width:
        if obj1.x - obj1.width / 2.0 < obj2.x + obj2.width:
            if obj1.y + obj1.height / 2.0 > obj2.y - obj2.height:
                if obj1.y - obj1.height / 2.0 < obj2.y + obj2.height:
                    return 1
    return 0
