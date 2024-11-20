#!/usr/bin/python
# -*- coding: utf-8 -*-
from teste.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT, WIN_WIDTH
from teste.EnemyShot import EnemyShot
from teste.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.speed_y = 0
        self.direction_y = 0

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        ### Adição da movimentação e velocidade do inimigo 3.
        if self.name == 'Enemy3':
            self.rect.centery += self.speed_y * self.direction_y

            if self.rect.bottom >= WIN_HEIGHT:
                self.direction_y = -1

            elif self.rect.top <= 0:
                self.direction_y = 1
                self.speed_y =2
        ###

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
