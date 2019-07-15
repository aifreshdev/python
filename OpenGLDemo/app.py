import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

# pip install PyOpenGL PyOpenGL_accelerate PyGame
# square
verticies = (
	(1, -1, -1), # 1 side
	(1, 1, -1), # 2 side
	(-1, 1, -1), # 3 side
	(-1, -1, -1), # 4 side
	(1, -1, 1), # 5 side
	(1, 1, 1), # 6 side
	(-1, -1, 1), # 7 side
	(-1, 1, 1) # 8 side
	)

edges = ( # total 12 line
	(0, 1), # 1 line
	(0, 3), # 2 line
	(0, 4), # 3 line
	(2, 1), # 4 line
	(2, 3), # 5 line
	(2, 7), # 6 line
	(6, 3), # 7 line
	(6, 4), # 8 line
	(6, 7), # 9 line
	(5, 1), # 10 line
	(5, 4), # 11 line
	(5, 7) # 12 line
	)


def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()
