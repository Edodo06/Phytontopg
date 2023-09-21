#Control ball position with the arrow keys

import simplegui
import math
import random

# initialize state
width = 750
height = 300
position = [75,height/2]
radius = 23
position2 = [width-radius, 30]
position3 = [width-radius, 100]
x_pos= width/2
velx= 0
vely= 0
velx2 = -7
vely2 = 1
velx3 = -5
vely3 = 1
time = 0
message = ""
test = 0
start = 0
startcredit = 0
image = simplegui.load_image('https://raw.githubusercontent.com/Edodo06/Phytontopg/main/policecarA-removebg-preview.png')
imageroad = simplegui.load_image('https://raw.githubusercontent.com/Edodo06/Phytontopg/test2/prestr5.png')
imagetopg = simplegui.load_image('https://raw.githubusercontent.com/Edodo06/Phytontopg/main/pixil-frame-0%2520%25282%2529.png')
imagestart = simplegui.load_image('https://raw.githubusercontent.com/Edodo06/Phytontopg/main/start5tt.jpg')

sound = simplegui.load_sound('https://github.com/Edodo06/Phytontopg/raw/main/Indila%20-%20Tourner%20Dans%20Le%20Vide%20(Andrew%20Tate%20Version).mp3')
sound.play()
sound.set_volume(0.8)


counter = 0
EXPLOSION_CENTER = [50, 50]
EXPLOSION_SIZE = [100, 100]
EXPLOSION_DIM = [9, 9]
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/explosion.hasgraphics.png")



def scontro():
    global velx2
    global vely2
    global velx3
    global vely3
    dist12 = math.sqrt(pow(position[0]-position2[0],2)+pow(position[1]- position2[1],2))
    dist13 = math.sqrt(pow(position[0]-position3[0],2)+pow(position[1]- position3[1],2))
    if (dist12 <= 2*radius):
 
        timer.stop()
        sound.pause()
        velx2 = 0
        vely2 = 0
        velx3 = 0
        vely3 = 0
        return True
    
    if (dist13 <= 2*radius):
 
        timer.stop()
        sound.pause()
        velx2 = 0
        vely2 = 0
        velx3 = 0
        vely3 = 0
        
        return True
# event handlers
def keydown(key):
    global velx
    global vely
    global scontro
    global start
    global startcredit
    
    if key == simplegui.KEY_MAP['m']:
             sound.pause()
            
         
    if key == simplegui.KEY_MAP['g']:
        start = 1
    if key == simplegui.KEY_MAP['p']:
        start = 3
        
    if key == simplegui.KEY_MAP['c']:
        startcredit = 2   
    if key == simplegui.KEY_MAP['n']:
             sound.rewind()
             sound.play()  
             sound.set_volume(0.8)   
            
    
    if (not scontro()):
 
        if key == simplegui.KEY_MAP['s']:
            vely = vely + 5
        if key == simplegui.KEY_MAP['w']:
            vely = vely - 5
 
 
        if key == simplegui.KEY_MAP['up']:
            vely = vely - 5
        if key == simplegui.KEY_MAP['down']:
            vely = vely + 5
            

        
def keyup(key):
    global velx
    global vely        
 
 
    if key == simplegui.KEY_MAP['w']:
        vely = 0
    if key == simplegui.KEY_MAP['s']:
        vely = 0
 
 
 
    if key == simplegui.KEY_MAP['up']:
            vely = 0
    if key == simplegui.KEY_MAP['down']:
            vely = 0

 

def start_game():
    if start == 1:
        return 1
def start_game2():
    if start == 3:
        return 3    
def start_credit():
    if startcredit == 2:
        return 2
def draw(canvas):
    global velx
    global vely
    global velx2
    global vely2
    global velx3
    global vely3
    global message
    global counter
    global x_pos
    global start
    
    if start_game() != 1:
             imagestart = simplegui.load_image('https://raw.githubusercontent.com/Edodo06/Phytontopg/main/start5tt.jpg')

             canvas.draw_image(imagestart, (605 / 2, 512 / 2), (605, 512), (375,150),(750,300))
                
    if start_credit() == 2:
             imagecredit = simplegui.load_image('https://raw.githubusercontent.com/Edodo06/Phytontopg/main/pixil-frame-0.png') 

             canvas.draw_image(imagecredit, (700 / 2, 593 / 2), (605, 512), (375,150),(750,300))
                
    if start_game2() == 3:
             imagestart2 = simplegui.load_image('https://raw.githubusercontent.com/Edodo06/Phytontopg/main/start5tt.jpg')

             canvas.draw_image(imagestart2, (605 / 2, 512 / 2), (605, 512), (375,150),(750,300))       
    
    if start_game() ==  1:
        
         position[0]=position[0]+velx
         position[1]=position[1]+vely
         position2[0]=position2[0]+velx2
         position3[0]=position3[0]+velx3
 
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
 
         if position3[0] > width-radius:
              velx3 = -velx3
         if position3[0] < radius:
              position3[0] = width-radius
              position3[1] = random.randint(0+radius,height-radius)

 
 
 
 
 
 
               #background
         canvas.draw_image(imageroad, (3400/2, 3400/2), (200,3400),(100,height/2),(200,height))
         canvas.draw_image(imageroad, (3400/2, 3400/2), (3400,3400),(x_pos,height/2),(width*1.75,height))
                #canvas.draw_image(imagecredit, (700/2, 593/2), (700,593),(x_pos,height/2),(width*1.75,height))
 
                #primo piano
 
         canvas.draw_image(image, (599/2 , 416/2 ), (599, 416), position2, (radius*4, radius*4))
    
         canvas.draw_image(image, (599/2 , 416/2 ), (599, 416), position3, (radius*4, radius*4))
    
         canvas.draw_image(imagetopg, (1000/2 , 1000/2 ), (1000,1000), position, (radius*4, radius*4))
       
         if (scontro()):
                    if counter < 80:
                       #esplosione da qui
                        explosion_index = [counter % EXPLOSION_DIM[0], counter // EXPLOSION_DIM[0]]
                        canvas.draw_image(explosion_image,
                       [EXPLOSION_CENTER[0] + explosion_index[0] * EXPLOSION_SIZE[0],
                        EXPLOSION_CENTER[1] + explosion_index[1] * EXPLOSION_SIZE[1]],
                        EXPLOSION_SIZE, [position[0]-(position[0] - position3[0])/2,
                                      position[1]-(position[1] - position3[1])/2],[100,100])
                        counter = (counter + 1) % (EXPLOSION_DIM[0] * EXPLOSION_DIM[1])
            #esplosione fino qui
                        timer.stop()
                        canvas.draw_text("Game Over", [50,112], 48, "red") 
                      
           
 
 
             #layout
         canvas.draw_text(message,(660,25),30,"red")
          
    
def timer_strada():      
    global x_pos
 
 
    x_pos=x_pos-5
    if (x_pos < 100):
        x_pos = 745
 
    if (scontro()):
 
        timerstrada.stop()
 
 
 
 

   
    
    
def timer_handler():      
    global time
    global position2
    global velx2
    global position3
    global velx3
    global test
    global message
    
    
    if start_game() != 1:
         time = 0   
         
    if start_game() == 1:      
        test = test +1
 
        message = str(test)
 
        time = time +1
 
        if time%500 == 0:
            velx2 = velx2-2
        if time%1000 == 0:
            velx3= velx3-5
 
       

#frame = simplegui.create_frame("restart", width,height)
frame = simplegui.create_frame("Key Handling", width,height)

timer = simplegui.create_timer(10, timer_handler)
timerstrada = simplegui.create_timer(30, timer_strada)

# register event handlers

frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)



timerstrada.start()
timer.start()


# start frame
label4 = frame.add_label('')
label4.set_text('INSTRUCTIONS')

label = frame.add_label('')
label.set_text('Press G to start')

label8 = frame.add_label('')
label8.set_text('Press P to start menu')

label5 = frame.add_label('')
label5.set_text('Move up and down with W/S or use the arrow keys ')



label2 = frame.add_label('')
label2.set_text('Press C to go to the credits')



label6 = frame.add_label('')
label6.set_text('Press N to restart the music')

label7 = frame.add_label('')
label7.set_text('Press M to mute the music')

frame.set_draw_handler(draw)

frame.start()
