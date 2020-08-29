import pygame

class Car:
    def __init__(self):
        self.location = (x, y)
        self.speed_multiplier = 1
        self.heading = 90
        self.acceleration = 0
        self.environmental_deceleration = -10 * speed_multiplier
        self.velocity = 0
    
    def change_acceleration(self, change_amount):
        self.acceleration += change_amount
        self.velocity -= self.environmental_deceleration
        self.velocity += 

    def update_location():
        """
        should be called once per display tick
        """
