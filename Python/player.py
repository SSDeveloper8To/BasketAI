import pygame
import numpy as np


class Player:
    mass = 1.4
    gravity = 750
    radius = 30
    jump_force = 750
    wall_collision_slowdown = 0.7
    img = pygame.image.load('smily.png')
    w, h = img.get_size()
    scale_factor = 2 * radius / w
    scaled_image = pygame.transform.scale_by(img, scale_factor)

    def __init__(self, x, y, game):
        self.pos = np.array([x, y], dtype=float)
        self.vel = np.array([0, 0], dtype=float)
        self.acc = np.array([0, Player.gravity], dtype=float)
        self.game = game

    def update(self):
        self.pos += self.vel * self.game.dt
        self.vel += self.acc * self.game.dt
        self.check_boundaries()

    def check_boundaries(self):
        if self.pos[0] + Player.radius >= self.game.width:
            self.pos[0] = self.game.width - Player.radius
            self.vel[0] *= -Player.wall_collision_slowdown
        if self.pos[0] - Player.radius <= 0:
            self.pos[0] = Player.radius
            self.vel[0] *= -Player.wall_collision_slowdown
        if self.pos[1] - Player.radius <= 0:
            self.pos[1] = Player.radius
            self.vel[1] *= -Player.wall_collision_slowdown

    def push(self, target_pos):
        direction = target_pos - self.pos
        direction = direction / np.linalg.norm(direction)  # Normalize the vector
        self.vel = direction * Player.jump_force

    def draw(self, surface):
        surface.blit(self.scaled_image, (self.pos[0] - Player.radius, self.pos[1] - Player.radius))