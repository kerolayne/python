import pygame

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

'''
def Boneco(screen, x, y):
    pygame.draw.ellipse(screen, , [35+x, 0+y, 25,25])

'''
def draw_sphere(color, pos, radius=2):
    gl.glColor(*color)

    gl.glPushMatrix()

    x, y = pos
    gl.glTranslate(x, y, 3)

    q = glu.gluNewQuadric()
    glu.gluSphere(q, radius, 20, 20)
    glu.gluDeleteQuadric(q)

    gl.glPopMatrix()
    
def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)
    glRotatef(0, 0, 0, 0)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw_sphere()
        #Boneco()
        pygame.display.flip()
        pygame.time.wait(10)

main()