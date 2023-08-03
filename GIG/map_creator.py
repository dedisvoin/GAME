from library.lib import *


win_size = [8*30,8*20]
win = Window(size=win_size,flag=Flags.win_scales)
garss_images = load_block_cheat('data\grass_tiles.png',4,[8,8])

vabor = 1
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
                    
                if mapping[i+1][j-1]!=1 and mapping[i+1][j+1]!=1:
                    garss_images['left_right_down'].center = [j*8+4,i*8+4]
                    garss_images['left_right_down'].draw_surf(surf)
                    
                if mapping[i-1][j-1]!=1 and mapping[i-1][j+1]!=1:
                    garss_images['left_right_up'].center = [j*8+4,i*8+4]
                    garss_images['left_right_up'].draw_surf(surf)
            
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


map = []
for i in range(20+1):
    m = []
    for j in range(30+1):
        m.append(0)
    map.append(m)

def viev_map():
    for i in range(len(map)):
        for j in range(len(map[i])):
            ...
                
                
def map_setter():
    global map
    mouse_coord = Mouse.position()
    mouse_coord[0]-=mouse_coord[0]%8
    mouse_coord[1]-=mouse_coord[1]%8
    dx = mouse_coord[0]//8
    dy = mouse_coord[1]//8
    if Mouse.press():
        map[dy][dx] = 1
    if Mouse.press(Mouse.right):
        map[dy][dx] = 0

while win.update(fps_view=0,fps='max'):
    map_setter()
    viev_map()
    surf = map_create(map)
    win._win.blit(surf,[0,0])