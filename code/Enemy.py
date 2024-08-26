#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    #Movimento vertical Enemy 3
        self.movement_vertical = name == 'Enemy3'
        if self.movement_vertical:
            self.inicio_y = position [1]
            #Velocidade do enemy 3
            self.y_velocidade = 2
            self.direction = 1
            self.y_max = position[1] + 100
            self.y_min = position[1] - 100

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        #Movimento do enemy 3 na vertical
        if self.movement_vertical:
            if self.rect.centery >= self.y_max or self.rect.centery <= self.y_min:
                self.direction *= -1 # para inverter a direção
            self.rect.centery += self.y_velocidade * self.direction

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
