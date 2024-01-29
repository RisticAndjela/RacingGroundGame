import pygame
import sys
from Rectangle import RectangleWithDots
from Road import Road
from Car import Car
from level import*
from Message import *

level=chose_level()

pygame.init()
car = Car()
roads = []
original_road = Road(max_height=150, initial_points=[],car=car, pygame=pygame ,newCar= True )
roads.append(original_road)
rect_with_dots = RectangleWithDots(original_road,difficulty=int(level))
smaller_rectangles = rect_with_dots.smallerRectangles()

# Create a list to store instances of EmptyRoad
# Print the dots in each smaller rectangle
# print(f"{[f'({dot.x}, {dot. y})' for dot in rect_with_dots.dots]}")
for i, smaller_rectangle in enumerate(smaller_rectangles):
    # print(f"Smaller Rectangle {i + 1} Dots: {[f'({dot.x}, {dot.y})' for dot in smaller_rectangle.dots ]} and the width is from {smaller_rectangle.x} to {smaller_rectangle.width} and the height is from {smaller_rectangle.y} to {smaller_rectangle.height}")
    road = Road(max_height=150, initial_points=smaller_rectangle.dots,car=car, pygame=pygame ,newCar= False)
    roads.append(road)

current_road_index = 0
change_time = pygame.time.get_ticks() + 5  # Initial change time set to 2 seconds
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Check for key press to advance to the next road
            if event.key == pygame.K_SPACE:
                current_road_index += 1

    # Check if it's time to change the road
    if pygame.time.get_ticks() > change_time:
        current_road_index = (current_road_index + 1) % len(roads)
        change_time = pygame.time.get_ticks() + 5  # Set next change time

    # Clear the screen
    pygame.display.get_surface().fill((255, 255, 255))

    # Draw the current road
    roads[current_road_index].draw_road()

    # Update the display
    pygame.display.flip()

    if current_road_index == len(roads) - 1:
        running = False
    if current_road_index < len(roads) - 1:
        roads[current_road_index+1].height=roads[current_road_index].height 
    # Control the frame  
    clock.tick(30)  # Adjust the value to control the speed

send_message("You succsefuly finished the game")
pygame.quit()
sys.exit()
