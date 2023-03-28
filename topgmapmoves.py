# Control ball position with the arrow keys

import simplegui
import math
import random

# initialize state
width = 750
height = 300
position = [75,height/2]
radius = 23
position2 = [width-radius, 30]
x_pos= width/2
velx= 0
vely= 0
velx2 = -7
vely2 = 1
time = 0
message = ""
test = 0
image = simplegui.load_image('https://raw.githubusercontent.com/Edodo06/Phytontopg/main/policecarAF1.jpg')
imageroad = simplegui.load_image('https://raw.githubusercontent.com/Edodo06/Phytontopg/test/stradapre2.png')
imagetopg = simplegui.load_image('https://raw.githubusercontent.com/Edodo06/Phytontopg/main/pixil-frame-0%2520%25282%2529.png')


counter = 0
EXPLOSION_CENTER = [50, 50]
EXPLOSION_SIZE = [100, 100]
EXPLOSION_DIM = [9, 9]
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/explosion.hasgraphics.png")

def scontro():
    global velx2
    global vely2
    
    dist = math.sqrt(pow(position[0]-position2[0],2)+pow(position[1]- position2[1],2))
    if (dist <= 2*radius):
       
        timer.stop()
        velx2 = 0
        vely2 = 0
        return True 
# event handlers
def keydown(key):
    global velx
    global vely
    global scontro
    if key == simplegui.KEY_MAP['a']:
        print("ciao")
        
    if (not scontro()):
        
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
        
 

       

    
def draw(canvas):
    global velx
    global vely
    global velx2
    global vely2
    global message
    global counter
    global x_pos
   
    
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
    canvas.draw_image(imageroad, (1935/4, 571/2), (1935/2,571),(x_pos,height/2),(width*1.75,height))
    
    
    #primo piano 
    
    canvas.draw_image(image, (999/2 , 694/2 ), (999, 694), position2, (radius*3, radius*3))
    canvas.draw_image(imagetopg, (1000/2 , 1000/2 ), (1000,1000), position, (radius*3, radius*3))
    if (scontro()):
        #esplosione da qui
        explosion_index = [counter % EXPLOSION_DIM[0], counter // EXPLOSION_DIM[0]]
        canvas.draw_image(explosion_image, 
                    [EXPLOSION_CENTER[0] + explosion_index[0] * EXPLOSION_SIZE[0], 
                     EXPLOSION_CENTER[1] + explosion_index[1] * EXPLOSION_SIZE[1]], 
                     EXPLOSION_SIZE, [position[0]-(position[0] - position2[0])/2,
                                      position[1]-(position[1] - position2[1])/2],[100,100])
        counter = (counter + 1) % (EXPLOSION_DIM[0] * EXPLOSION_DIM[1])
        #esplosione fino qui
        timer.stop()
        canvas.draw_text("Game Over", [50,112], 48, "Red")    
    
    
    #layout
    canvas.draw_text(message,(660,30),30,"White") 
        
def timer_strada():       
    global x_pos
    
        
    x_pos=x_pos-6
    if (x_pos < 350):
        x_pos = 600
       
    if (scontro()):
        
        timerstrada.stop()
    
    
    
    
    
def timer_handler():       
    global time
    global position2
    global velx2
    global test
    global message
    
    test = test +1
    
    message = str(test)
    
    time = time +1
   
    if time%500 == 0:
        velx2 = velx2-random.randint(-3,3)
        print(velx2)
frame = simplegui.create_frame("Key Handling", width, height)

timer = simplegui.create_timer(10, timer_handler)
timerstrada = simplegui.create_timer(30, timer_strada)

# register event handlers
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

timerstrada.start()
timer.start()

# start frame
frame.start()
