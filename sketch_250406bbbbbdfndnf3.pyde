x=1
w=100
def setup():
    size(600,400)
    colorMode(HSB,360,100,100)
def draw():
    global x
    global w
    fill(237,232,208)
    ellipse(230,200,150,210)
    fill(100,100,w)
    ellipse(200,190,50,50)
    fill(100,x,100)
    ellipse(260,190,50,50)
    x=x+1
    w=w-1
    
