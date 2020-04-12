import sys
import pygame

from src.desktop.scenes.final import FinalScene
from src.desktop.scenes.main import MainScene
from src.desktop.scenes.menu import MenuScene


class Game:
    MENU_SCENE_INDEX = 0
    MAIN_SCENE_INDEX = 1
    GAMEOVER_SCENE_INDEX = 2

    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.size = self.width, self.height

        self.create_window()
        self.game_over = False
        self.wall_collision_count = 0
        self.ticks = 0
        self.scenes = [MenuScene(self), MainScene(self), FinalScene(self)]
        self.current_scene = 0

    def create_window(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)

    def main_loop(self):
        while not self.game_over:
            eventlist = pygame.event.get()
            for event in eventlist:
                self.scenes[self.current_scene].process_event(event)
                if event.type == pygame.QUIT:
                    print('Пользователь нажал крестик')
                    self.game_over = True

            self.scenes[self.current_scene].process_frame(eventlist)


        sys.exit(0)