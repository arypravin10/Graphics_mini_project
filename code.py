import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glShadeModel(GL_SMOOTH)
    
def draw_sphere(radius):
    quadric = gluNewQuadric()
    gluQuadricNormals(quadric, GLU_SMOOTH)
    gluQuadricTexture(quadric, GL_TRUE)
    gluSphere(quadric, radius, 32, 32)
    gluDeleteQuadric(quadric)

def draw_planet(radius, distance_from_sun, orbit_speed, rotation_speed, color):
    glPushMatrix()
    glColor3f(*color)
    glRotatef(orbit_speed * pygame.time.get_ticks() / 1000.0, 0.0, 1.0, 0.0)
    glTranslatef(distance_from_sun, 0.0, 0.0)
    glRotatef(rotation_speed * pygame.time.get_ticks() / 1000.0, 0.0, 1.0, 0.0)
    draw_sphere(radius)
    glPopMatrix()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    init()
    fov = 45.0
    aspect_ratio = display[0] / float(display[1])
    near = 0.1
    far = 100.0
    gluPerspective(fov, aspect_ratio, near, far)
    glTranslatef(0.0, 0.0, -10.0)
    clock = pygame.time.Clock()
    sun_color = (1.0, 1.0, 0.0)
    sun_radius = 1.0
    mercury_color = (0.5, 0.5, 0.5)
    mercury_radius = 0.2
    mercury_distance_from_sun = 3.0
    mercury_orbit_speed = 5.0
    mercury_rotation_speed = 10.0
    venus_color = (0.5, 0.5, 1.0)
    venus_radius = 0.3
    venus_distance_from_sun = 5.0
    venus_orbit_speed = 3.0
    venus_rotation_speed = 6.0
    earth_color = (0.0, 1.0, 0.0)
    earth_radius = 0.4
    earth_distance_from_sun = 7.0
    earth_orbit_speed = 2.0
    earth_rotation_speed = 4.0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw_planet(sun_radius, 0.0, 0.0, 0.0, sun_color)
        draw_planet(mercury_radius, mercury_distance_from_sun, mercury_orbit_speed, mercury_rotation_speed, mercury_color)
        draw_planet(venus_radius, venus_distance_from_sun, venus_orbit_speed, venus_rotation_speed, venus_color)
        draw_planet(earth_radius,earth_distance_from_sun, earth_orbit_speed, earth_rotation_speed, earth_color)
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()
