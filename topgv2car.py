# Control ball position with the arrow keys

import simplegui
import math
import random

# initialize state
width = 750
height = 300
position = [75,height/2]
radius = 15
position2 = [width-radius, 30]

velx= 0
vely= 0
velx2 = -7
vely2 = 1
time = 0
message = ""
test = 0
image = simplegui.load_image('https://raw.githubusercontent.com/Edodo06/Phytontopg/main/policecarAF1.jpg')
imageroad = simplegui.load_image('https://raw.githubusercontent.com/MrAleSoaveCotta/Gioco/main/strada%20fin1.jpg')
imagetopg = simplegui.load_image('https://raw.githubusercontent.com/Edodo06/Phytontopg/main/pixil-frame-0%2520%25282%2529.png')

# event handlers
def keydown(key):
    global velx
    global vely
    if key == simplegui.KEY_MAP['a']:
        print("ciao")
    if key == simplegui.KEY_MAP['s']:
        vely = vely + 5
    if key == simplegui.KEY_MAP['w']:
        vely = vely - 5
def keyup(key):
    global velx
    global vely        
  
       
    if key == simplegui.KEY_MAP['w']:
        vely = 0
    if key == simplegui.KEY_MAP['s']:
        vely = 0
        

def scontro():
    global position
    global position2
    global velx
    global vely
    global velx2
    global vely2
    dx = position[0]-position2[0]
    dy = position[1]-position2[1]
    dist = math.sqrt(dx*dx+dy*dy)
    
    if (dist <= 2*radius):
        #print "scontro"
        velx= 0
        vely= 0
        velx2=0
        vely2=0
        return 1
       

def draw(canvas):
    global velx
    global vely
    global velx2
    global vely2
    global message
    if (scontro()==1):
        canvas.draw_text("Game Over", [50,112], 48, "Red")
        timer.stop()
    
    position[0]=position[0]+velx
    position[1]=position[1]+vely
    position2[0]=position2[0]+velx2
  
    if position[0] > width-radius:
        velx = -velx
    if position[0] < radius:
        velx = -velx
    if position[1] > height-radius:
        vely = -vely
    if position[1] < radius:
        vely = -vely
    if position2[0] > width-radius:
        velx2 = -velx2
    if position2[0] < radius:
        position2[0] = width-radius
        position2[1] = random.randint(0+radius,height-radius)
    #background
    canvas.draw_image(imageroad, (999/2, 599/2), (999, 599),(400, 150),(900, 300))
    
    
    #primo piano 
    ######non va la foto 2 della macchina che viene addosso
    canvas.draw_image(image, (999/2 , 694/2 ), (999, 694), position2, (radius*3, radius*3))
    canvas.draw_circle(position, radius, 2, "red", "red")
    #canvas.draw_image(imagetopg, radius, 2, "yellow", "yellow")
   
    
    
    
    #layout
    canvas.draw_text(message,(660,30),30,"White") 
    
    if (scontro()==1):
        canvas.draw_text("Game Over", [50,112], 48, "Red")
        timer.stop()
def timer_handler():       
    global time
    global position2
    global velx2
    global test
    global message
    
    test = test +1
    
    message = str(test)
    
    time = time +1
   
    if time%1000 == 0:
        velx2 = velx2-1
       
frame = simplegui.create_frame("Key Handling", width, height)

timer = simplegui.create_timer(10, timer_handler)
timer.start()

# register event handlers
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)


# start frame
frame.start()
