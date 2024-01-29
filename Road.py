import pygame
import sys
from Dot import Dot
from Car import Car
from Bump import Bump
from Message import *


class Road:
    def __init__(self,height=600, max_height=300, initial_points=None, pygame=None,car =Car(),newCar=True):
        self.pygame = pygame
        width = 800
        self.width = width
        self.height = 100
        self.max_height = max_height
        self.angle_speed = 0.1
        self.scale_factor = 25
        
        # Start road parallel to up and down window sides
        self.x = width // 2
        self.y = height // 2
        
        self.car=car
        if newCar:
            self.car.y = self.y + self.height / 2 - self.car.height / 2
            self.car.x = self.x
        
        self.bumps=[]
        for dot in initial_points:
            self.bumps.append(Bump(dot,self))

        self.screen = self.pygame.display.set_mode((width, height))
        self.pygame.display.set_caption("Naginjuća Ravan")

        self.white = (255, 255, 255)

    

    def draw_road(self):
        self.screen.fill(self.white)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and self.height < self.max_height:
            self.height += self.angle_speed * self.scale_factor
            self.car.y = self.y + self.height / 2 - self.car.height / 2
            self.car.height-= self.angle_speed * self.scale_factor/4
            for i in self.bumps:
                i.height -= self.angle_speed * self.scale_factor / 4


            
        elif keys[pygame.K_DOWN] and self.height > 90:
            self.height -= self.angle_speed * self.scale_factor
            self.car.y = self.y + self.height / 2 - self.car.height / 2
            self.car.height+= self.angle_speed * self.scale_factor/4
            for i in self.bumps:
                i.height += self.angle_speed * self.scale_factor / 4


            
        elif keys[pygame.K_LEFT] and self.car.x>0:
            self.car.x-=1/self.height *300
        
        elif keys[pygame.K_RIGHT] and self.car.x< self.width:
            self.car.x+=1/self.height *300
        
        # Draw the road trapezoid
        self.pygame.draw.polygon(self.screen, (0, 0, 255), [
            (self.x - self.width / 2, self.y - self.height / 2),
            (self.x + self.width / 2, self.y - self.height / 2),
            (self.x + self.width / 2, self.y + self.height / 2),
            (self.x - self.width / 2, self.y + self.height / 2)
        ])

        # Draw the car rectangle
        self.pygame.draw.polygon(self.screen, self.car.color, [
            (self.car.x - self.car.width / 2, self.car.y - self.car.height / 2),
            (self.car.x + self.car.width / 2, self.car.y - self.car.height / 2),
            (self.car.x + self.car.width / 2, self.car.y + self.car.height / 2),
            (self.car.x - self.car.width / 2, self.car.y + self.car.height / 2)
        ])

        # Check for collisions with bumps
        car_rect = self.pygame.Rect(
            self.car.x - self.car.width / 2,
            self.car.y - self.car.height / 2,
            self.car.width,
            self.car.height
        )

        for bump in self.bumps:
            line_rect = self.pygame.Rect(
                bump.x - bump.width / 2,
                bump.y + self.y - self.height / 2 - bump.height,
                bump.width,
                bump.height
            )

            if car_rect.colliderect(line_rect):
                
                send_message("Collision with bump!")
                pygame.quit()
                sys.exit()

        # Draw the bump lines
        for bump in self.bumps:
            y1 = bump.y + self.y - self.height / 2
            if y1 <= self.y + self.height - bump.height:
                self.pygame.draw.line(self.screen, bump.color, (bump.x, y1), (bump.x, y1 - self.car.height), width=5)

        self.pygame.display.flip()

    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.draw_road()

            # Control the frame rate
            clock.tick(30)  # Adjust the value to control the speed

        pygame.quit()
        sys.exit()

            
            
    
    
if __name__ == "__main__":
    initial_points = [Dot(250, 100,name=1), Dot(200, 200,name=2), Dot(100, 300,name=3)]  # Example initial positions for points
    
    road = Road(max_height=300, initial_points=initial_points,pygame=pygame)
    road.run()
