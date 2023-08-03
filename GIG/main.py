from library.lib import *


win_size = [8*30,8*20]
win = Window(size=win_size,flag=Flags.win_scales)
global_pos = [0,0]

test_map = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,5,0,0,0,0,0,0,5,0,0,0,0,0,0],
    [0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0],
    [0,0,0,0,0,0,0,4,4,4,4,4,4,4,4,4,0,0,0,0,0],
    [0,0,0,5,0,0,0,1,1,4,4,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0],
    [0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,0,0],
    [0,0,0,0,0,0,5,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]
rects = []
jump_busts = []

def rectinizer(mapping):
    global rects
    x = 0
    y = 0
    for i in range(len(mapping)):
        
        rect_start = False
        rect_width = 0
        y = i*8
        
        for j in range(len(mapping[i])):
            #if mapping[i][j] == 4:
            #    rects.append(Collider(j*8,i*8,8,8))
            
            if mapping[i][j]==1 and rect_start == False:
                rect_start = True
                x = j*8
            
            if rect_start and mapping[i][j]==1:
                rect_width +=8
                
            try:
                if rect_start and mapping[i][j+1]!=1:
                    rects.append(Collider(x,y,rect_width,8))
                    rect_start = False
                    rect_width = 0
            except:
                ...
    

                
            
garss_images = load_block_cheat('data\grass_tiles.png',4,[8,8])
def map_create(mapping):
    
    surf = pygame.Surface([len(mapping[0])*8,len(mapping)*8]).convert_alpha()
    surf.set_colorkey((0,0,0))
    
    for i in range(len(mapping)):
        for j in range(len(mapping[i])):
            
            if j+1==len(mapping[0]):j-=1
            if i+1==len(mapping):i-=1
            if mapping[i][j] == 1 and mapping[i-1][j] != 1:
                
                if mapping[i][j-1] == 1 and mapping[i][j+1] ==1:
                    garss_images['top_middle'].center = [j*8+4,i*8+4]
                    garss_images['top_middle'].draw_surf(surf)
                if mapping[i][j-1] != 1 and mapping[i][j+1] ==1:
                    garss_images['top_left'].center = [j*8+4,i*8+4]
                    garss_images['top_left'].draw_surf(surf)
                if mapping[i][j-1] == 1 and mapping[i][j+1] !=1:
                    garss_images['top_right'].center = [j*8+4,i*8+4]
                    garss_images['top_right'].draw_surf(surf)
                
                if mapping[i][j-1] != 1 and mapping[i][j+1] !=1:
                    garss_images['top_vertical'].center = [j*8+4,i*8+4]
                    garss_images['top_vertical'].draw_surf(surf)
                    
                if mapping[i][j-1] == 1 and mapping[i][j+1] ==1 and mapping[i+1][j] !=1:
                    garss_images['center_horizontal'].center = [j*8+4,i*8+4]
                    garss_images['center_horizontal'].draw_surf(surf)
                    
                if mapping[i][j-1] == 1 and mapping[i][j+1] !=1 and mapping[i+1][j] !=1:
                    garss_images['right_horizontal'].center = [j*8+4,i*8+4]
                    garss_images['right_horizontal'].draw_surf(surf)
                    
                if mapping[i][j-1] != 1 and mapping[i][j+1] == 1 and mapping[i+1][j] !=1:
                    garss_images['left_horizontal'].center = [j*8+4,i*8+4]
                    garss_images['left_horizontal'].draw_surf(surf)
                
                    
            elif mapping[i][j]==1 and mapping[i-1][j] == 1 and mapping[i+1][j]!=1:
                if mapping[i][j-1] == 1 and mapping[i][j+1] == 1:
                    garss_images['down_middle'].center = [j*8+4,i*8+4]
                    garss_images['down_middle'].draw_surf(surf)
                if mapping[i][j-1] != 1 and mapping[i][j+1] ==1:
                    garss_images['down_left'].center = [j*8+4,i*8+4]
                    garss_images['down_left'].draw_surf(surf)
                if mapping[i][j-1] == 1 and mapping[i][j+1] !=1:
                    garss_images['down_right'].center = [j*8+4,i*8+4]
                    garss_images['down_right'].draw_surf(surf)
                    
                if mapping[i][j-1] != 1 and mapping[i][j+1] !=1:
                    garss_images['down_vertical'].center = [j*8+4,i*8+4]
                    garss_images['down_vertical'].draw_surf(surf)
                    
            elif mapping[i][j]==1 and mapping[i-1][j] == 1 and mapping[i+1][j]==1 and mapping[i][j-1] != 1 and mapping[i][j+1]!=1 :
                garss_images['center_vertical'].center = [j*8+4,i*8+4]
                garss_images['center_vertical'].draw_surf(surf)
                
            if mapping[i][j]==1 and mapping[i+1][j]==1 and mapping[i-1][j]==1 and mapping[i][j+1]==1 and mapping[i][j-1]==1:
                garss_images['center_middle'].center = [j*8+4,i*8+4]
                garss_images['center_middle'].draw_surf(surf)
                if mapping[i-1][j-1]!=1:
                    garss_images['left_up'].center = [j*8+4,i*8+4]
                    garss_images['left_up'].draw_surf(surf)
                elif mapping[i-1][j+1]!=1:
                    garss_images['right_up'].center = [j*8+4,i*8+4]
                    garss_images['right_up'].draw_surf(surf)
                    
                if mapping[i+1][j-1]!=1:
                    garss_images['left_down'].center = [j*8+4,i*8+4]
                    garss_images['left_down'].draw_surf(surf)
                elif mapping[i+1][j+1]!=1:
                    garss_images['right_down'].center = [j*8+4,i*8+4]
                    garss_images['right_down'].draw_surf(surf)
            
            if mapping[i][j]==1 and mapping[i+1][j]==1 and mapping[i-1][j]==1 and mapping[i][j+1]!=1 and mapping[i][j-1]==1:
                garss_images['center_right'].center = [j*8+4,i*8+4]
                garss_images['center_right'].draw_surf(surf)
            if mapping[i][j]==1 and mapping[i+1][j]==1 and mapping[i-1][j]==1 and mapping[i][j+1]==1 and mapping[i][j-1]!=1:
                garss_images['center_left'].center = [j*8+4,i*8+4]
                garss_images['center_left'].draw_surf(surf)
            
            if mapping[i][j]==1 and mapping[i+1][j]!=1 and mapping[i-1][j]!=1 and mapping[i][j+1]!=1 and mapping[i][j-1]!=1:
                garss_images['one'].center = [j*8+4,i*8+4]
                garss_images['one'].draw_surf(surf)
                
    return surf
                
m = map_create(test_map)

class Person:
    def __init__(self) -> None:
        self.stay_anim = AnimatedSprite('data\person\person_stay.png',20)
        self.run_anim = AnimatedSprite('data\person\person_run.png',5)
        self.jump_anim = AnimatedSprite('data\person\person_jamp.png',10)
        self.stay_anim.start()
        self.run_anim.start()
        self.napr = False
        self.move = False
        self.collider = Collider(8,8,6,7,gravity=Vector2(0,0.1),trenie=Vector2(0.5,0.01), air_resistance=Vector2(0.7,1))
        
        
    def render(self,win):
        pos = copy([self.collider.center[0],self.collider.center[1]])
        self.stay_anim.center = pos
        self.run_anim.center = pos
        self.jump_anim.center = pos
        self.stay_anim.update()
        self.run_anim.update()
        if self.collider.collides['down']:
            if self.move:
                self.run_anim.render(win)
            else:
                self.stay_anim.render(win)
        else:
            self.jump_anim.render(win)
            
    def set_pos(self,pos):
        self.collider.center = [pos[0],pos[1]]
        
    def update(self):
        global rects
        self.run_anim.set_mirror(self.napr)
        self.stay_anim.set_mirror(self.napr)
        self.jump_anim.set_mirror(self.napr)
        
        self.move = False
        if Keyboard.key_pressed('up') and self.collider.collides['down']:
            self.collider.sy = -2
        if Keyboard.key_pressed('left'):
            self.collider.sx = -1.5 
            self.napr = True
            self.move = True
        if Keyboard.key_pressed('right'):
            self.collider.sx = 1.5  
            self.napr = False
            self.move = True
            
        self.collider.collide_rect_list(rects,True)
p = Person()
class Jump_bust:
    def __init__(self) -> None:
        self.image_no_jump = Sprite(load_image( r'data\jump_ponj\nopr_jump.png' ))
        self.image_jump = Sprite( load_image( r'data\jump_ponj\press_jump.png'))
        self.pos = [0,0]
        self.pressed = False
    
    def set_pos(self, pos):
        self.pos = pos
        self.collder = Collider(self.pos[0],self.pos[1]-5+8,8,3)
        self.image_no_jump.center = [self.pos[0]+4,self.pos[1]+4]
        self.image_jump.center = [self.pos[0]+4,self.pos[1]+4]
        self.timer = 0
    
    def render(self, win):
        global p
        if not self.pressed:
            self.image_no_jump.draw(win)
        else:
            self.image_jump.draw(win)
            
        if p.collider.collide_rect(self.collder):
            p.collider.sy=-3
            self.timer = 5
        
        if self.timer!=0:
            self.pressed = True
            self.timer-=0.1

        if self.timer<0:
            self.pressed = False
            self.timer = 0
            
        #self.collder.draw(win._win)
          
class Air_Jump_bust:
    def __init__(self) -> None:
        self.image_no_jump = AnimatedSprite( r'data\jump_ponj\air_not_jump.png' )
        self.image_jump = AnimatedSprite( r'data\jump_ponj\air_jump.png')
        self.image_jump.start()
        self.image_no_jump.start()
        self.pos = [0,0]
        self.pressed = False
        self.press_timer = 0
        self.tt = 5
    
    def set_pos(self, pos):
        self.pos = pos
        self.collder = Collider(self.pos[0],self.pos[1]-5+8,8,3)
        self.image_no_jump.center = [self.pos[0]+4,self.pos[1]-7]
        self.image_jump.center = [self.pos[0]+4,self.pos[1]-7]
        self.timer = 0
    
    def render(self, win):
        global p
        self.press_timer+=0.1
        self.image_no_jump.center[1]+=sin(self.press_timer)/self.tt
        self.image_jump.center[1]+=sin(self.press_timer)/self.tt
        self.image_jump.update()
        self.image_no_jump.update()
        if not self.pressed:
            self.image_no_jump.render(win)
        else:
            self.image_jump.render(win)
            
        #self.collder.draw(win._win)
            
        if p.collider.collide_rect(self.collder):
            p.collider.sy=-3
            self.timer = 5
            self.tt = 1
            self.press_timer = 0
        
        if self.timer!=0:
            self.pressed = True
            self.timer-=0.1
            self.tt = 1

        if self.timer<0:
            self.pressed = False
            self.timer = 0  
            self.tt = 5  
        
        self.image_no_jump.center[1] -= (self.image_no_jump.center[1]- self.collder.center[1]+10)/10
        self.image_jump.center[1] -= (self.image_jump.center[1]- self.collder.center[1]+10)/10
        
           
def create_jump_busts(mapping):
    global jump_busts
    for i in range(len(mapping)):
        for j in range(len(mapping[i])):
            if j+1==len(mapping[0]):j-=1
            if i+1==len(mapping):i-=1
            if mapping[i][j] == 5 and mapping[i+1][j]!=0:
                jb = Jump_bust()
                jb.set_pos([j*8,i*8])
                jump_busts.append(jb)
            if mapping[i][j]==5 and mapping[i+1][j]==0:
                jb = Air_Jump_bust()
                jb.set_pos([j*8,i*8])
                jump_busts.append(jb)
            if mapping[i+1][j]==-1:
                p.set_pos([j*8+5,i*8+16])
            

create_jump_busts(test_map)         
        
stones = []
class Stone:
    def __init__(self) -> None:
        self.animation = AnimatedSprite('data\stone\stone.png',6,True)
    
    def set_pos(self, pos):
        global p
        self.colider = Collider(pos[0],pos[1],8,8)
        self.up_collider = Collider(pos[0],pos[1]-2,8,8)
        self.animation.center = self.colider.center

        
        
    def render(self,win):
        global p,rects
        self.animation.update()
        self.animation.render(win)
        if self.up_collider.collide_rect(p.collider):
            self.animation.start()
        if not self.animation._render:
            self.colider.colliding = False
                 
def create_stones(mapping):
    global stones, rects
    for i in range(len(mapping)):
        for j in range(len(mapping[i])):
            if mapping[i][j] == 4:
                jb = Stone()
                jb.set_pos([j*8,i*8])
                rects.append(jb.colider)
                stones.append(jb)
create_stones(test_map)    
    
class Key:
    def __init__(self) -> None:
        self.image = AnimatedSprite('data\key_and_dor\key_anim.png',5)     
        self.image.start()
        self.timer = 0
        self.uped = False
        self.dor_open = False
        self.kill_timer = 50
        self.key_particles = (
        Particle()
        .set_color((189,174,18))
        .set_shape(Shapes.RECT)
        .set_size([4,4])
        .set_size_deller(0.1)
        .set_move_duration(180)
        .set_move_adding(0.8)
        )
        self.particle_space = ParticleSpace([0,0],win_size,win)
        self.spavner = Spavner(spavner_size_=[1,1])
    
    def set_pos(self, pos):
        self.collider = Collider(pos[0],pos[1], 8,8)   
        
    def render(self, win):
        self.timer+=1
        self.image.center = self.collider.center
        self.image.center[1]+=sin(self.timer/10)
        self.image.update()
        self.image.render(win)
        #self.collider.draw(win._win)
        if p.collider.collide_rect(self.collider):
            self.uped = True
        if not self.dor_open:
            if self.uped:
                
                dx = self.collider.center[0]-p.collider.center[0]
                dy = self.collider.center[1]-p.collider.center[1]+15
                
                self.collider.center = [
                    self.collider.center[0]-dx*0.03,
                    self.collider.center[1]-dy*0.03
                ]
        else:
            dx = self.collider.center[0]-d.collider.center[0]
            dy = self.collider.center[1]-d.collider.center[1]
                
            self.collider.center = [
                    self.collider.center[0]-dx*0.1,
                    self.collider.center[1]-dy*0.1
            ]
            self.kill_timer-=1
        
        if self.kill_timer==0:
            print('yes')
            self.spavner.pos = self.collider.center
            
            self.image._render = False
            self.particle_space.add(self.key_particles, self.spavner, 5,1)
        
        
        self.particle_space.update()
        self.particle_space.draw()

k:Key


def create_key(mapping):
    global k
    for i in range(len(mapping)):
        for j in range(len(mapping[i])):
            if mapping[i][j] == 3:
                k = Key()
                k.set_pos([j*8,i*8])
                
create_key(test_map)
    
class Dor:
    def __init__(self) -> None:
        self.dor_anim = AnimatedSprite('data\key_and_dor\dor_anim.png',5,True)   
        
    def set_pos(self,pos):
        self.collider = Collider(pos[0],pos[1], 16,16) 
        self.detect_collider = Collider(pos[0]-10,pos[1]-10, 36,36)
        
    def render(self, win):
        self.dor_anim.center = self.collider.center
        self.dor_anim.update()
        self.dor_anim.render(win)
        
        if k.uped:
            if p.collider.collide_rect(self.detect_collider):
                self.dor_anim.start()
                k.dor_open = True
                
        if not self.dor_anim._render:
            self.collider.colliding = False
            
        
        
d:Dor        
def create_dor(mapping):
    global d, rects
    for i in range(len(mapping)):
        for j in range(len(mapping[i])):
            if mapping[i][j] == 6:
                d = Dor()
                d.set_pos([j*8,i*8])   
                rects.append(d.collider)  
                   

create_dor(test_map)  
        

rectinizer(test_map)

while win.update(fps=60, fps_view=1, base_color='white'):
    win._win.blit(m,global_pos)
    p.render(win)
    [s.render(win) for s in stones]
    p.update()
    
    
    d.render(win)
    k.render(win)
    #[r.draw(win._win) for r in rects]
    #[r.collder.draw(win._win) for r in jump_busts]
    #[s.up_collider.draw(win._win) for s in stones]
    ms = Mouse.speed
    if Mouse.press():
        global_pos[0]+=ms[0]
        global_pos[1]+=ms[1]
    [b.render(win) for b in jump_busts]
    
    
    