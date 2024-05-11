import pygame
import random
import datetime

pygame.init()

screen = pygame.display.set_mode( [600, 800] )

smallFont = pygame.font.SysFont('tahoma', 60)
font = pygame.font.SysFont('tahoma', 100)
bigFont = pygame.font.SysFont('tahoma', 120)

Numbers = [1,2,3,4,5,6,7,8]
random.shuffle( Numbers )
Numbers.append(0)

Tiles = [ Numbers[0:3],
          Numbers[3:6],
          Numbers[6:]]

SelectedTileI = 0
SelectedTileJ = 0

StartTime = datetime.datetime.now()

def swap( tiles, fromI, fromJ, toI, toJ ):
    print( f'swap ({fromI},{fromJ}) to ({toI},{toJ})')

    if fromI < 0 or fromI > 2 or toI < 0 or toI > 2 or fromJ < 0 or fromJ > 2 or toJ < 0 or toJ > 2:
        return

    sumChanges = abs(fromI - toI + fromJ - toJ )
    if sumChanges == 1 and tiles[ toI ][ toJ ] == 0:
        tmp = tiles[ toI ][ toJ ]
        tiles[ toI ][ toJ ] = tiles[fromI][ fromJ ]
        tiles[ fromI ][ fromJ ] = tmp

    print( tiles )
    

while True:

    screen.fill( [0,0,0 ])

    currentTime = datetime.datetime.now()

    elapseTime = (currentTime - StartTime).seconds


    elapseTimeLabel = smallFont.render( f'Time: {elapseTime}', True, [255,255,255 ])
    screen.blit( elapseTimeLabel, [50, 50] )
    
    for i in range( 3 ):
        for j in range(3):
            if Tiles[i][j] == 0:
                num = font.render( f' ', True, [255,255,255 ])
            else:
                if SelectedTileI == i and SelectedTileJ == j:
                    num = bigFont.render( f'{Tiles[i][j]}', True, [255,0,255 ])
                else:
                    num = font.render( f'{Tiles[i][j]}', True, [255,255,255 ])

            x = 150+j*120
            y = 200+i*140
            
            screen.blit( num, [x, y] )


    #   events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        elif event.type == pygame.KEYDOWN:

            if event.mod & pygame.KMOD_LALT:
                if event.key == pygame.K_UP:
                    swap( Tiles, SelectedTileI, SelectedTileJ, SelectedTileI-1, SelectedTileJ )
                elif event.key == pygame.K_DOWN:
                    swap( Tiles, SelectedTileI, SelectedTileJ, SelectedTileI+1, SelectedTileJ )
                elif event.key == pygame.K_LEFT:
                    swap( Tiles, SelectedTileI, SelectedTileJ, SelectedTileI, SelectedTileJ-1 )
                elif event.key == pygame.K_RIGHT:
                    swap( Tiles, SelectedTileI, SelectedTileJ, SelectedTileI, SelectedTileJ+1 )

            if event.key == pygame.K_UP:
                SelectedTileI = max( 0, SelectedTileI-1 )
            elif event.key == pygame.K_DOWN:
                SelectedTileI = min( 2, SelectedTileI+1 )
            elif event.key == pygame.K_RIGHT:
                SelectedTileJ = min( 2, SelectedTileJ+1 )
            elif event.key == pygame.K_LEFT:
                SelectedTileJ = max( 0, SelectedTileJ-1 )
                
##            if event.key == pygame.K_KP1:
##                numI = 2
##                numJ = 0
##            elif event.key == pygame.K_KP2:
##                numI = 2
##                numJ = 1
##            elif event.key == pygame.K_KP3:
##                numI = 2
##                numJ = 2
##            elif event.key == pygame.K_KP4:
##                numI = 1
##                numJ = 0
##            elif event.key == pygame.K_KP5:
##                numI = 1
##                numJ = 1
##            elif event.key == pygame.K_KP6:
##                numI = 1
##                numJ = 2
##            elif event.key == pygame.K_KP7:
##                numI = 0
##                numJ = 0
##            elif event.key == pygame.K_KP8:
##                numI = 0
##                numJ = 1
##            elif event.key == pygame.K_KP9:
##                numI = 0
##                numJ = 2

            #   select or swap
            #if numI != None and numJ != None:
            #   if SelectedTileI != None and SelectedTileJ != None:
            #        swap( Tiles, SelectedTileI, SelectedTileJ, numI, numJ )

             #   SelectedTileI = numI
             #   SelectedTileJ = numJ

           
                    
##            if event.key == pygame.K_UP:
##                selectedI, selectedJ = SelectedTile
##                nextI = selectedI-1
##                nextJ = selectedJ
##                print( f'move ({selectedI},{selectedJ}) to ({nextI},{nextJ})')
##                if nextI>=0 and Tiles[ nextI ][ nextJ ] == 0:
##                    print( f'move ({selectedI},{selectedJ}) to ({nextI},{nextJ})')
##                    swap( Tiles, selectedI, selectedJ, nextI, nextJ )
##
##            elif event.key == pygame.K_DOWN:
##                selectedI, selectedJ = SelectedTile
##                nextI = selectedI+1
##                nextJ = selectedJ
##                print( f'move ({selectedI},{selectedJ}) to ({nextI},{nextJ})')
##                if nextI<3 and Tiles[ nextI ][ nextJ ] == 0:
##                    print( f'move ({selectedI},{selectedJ}) to ({nextI},{nextJ})')
##                    swap( Tiles, selectedI, selectedJ, nextI, nextJ )
##
##            elif event.key == pygame.K_LEFT:
##                selectedI, selectedJ = SelectedTile
##                nextI = selectedI
##                nextJ = selectedJ-1
##                print( f'move ({selectedI},{selectedJ}) to ({nextI},{nextJ})')
##                if nextJ>0 and Tiles[ nextI ][ nextJ ] == 0:
##                    print( f'move ({selectedI},{selectedJ}) to ({nextI},{nextJ})')
##                    swap( Tiles, selectedI, selectedJ, nextI, nextJ )
##
##            elif event.key == pygame.K_RIGHT:
##                selectedI, selectedJ = SelectedTile
##                nextI = selectedI
##                nextJ = selectedJ+1
##                print( f'move ({selectedI},{selectedJ}) to ({nextI},{nextJ})')
##                if nextJ<3 and Tiles[ nextI ][ nextJ ] == 0:
##                    swap( Tiles, selectedI, selectedJ, nextI, nextJ )
            
    pygame.display.update()
