import time

from game_eng.game_model import GameModel
from game_eng.team_ders.team_a import TeamA
from game_eng.team_ders.team_b import TeamB
from game_eng.team_ders.team_c import TeamC
from game_eng.player import Player
from game_vc.grid_vc import GridVC
from objects.base import DrawObject


class GameVC(DrawObject):
    def __init__(self, game):
        super().__init__(game)
        self.__turn_start_time = time.time()
        self.model = create_hardcoded_game_model()
        self.grid = self.model.grid
        self.grid_vc = GridVC(self.grid, self.game)

    def process_logic(self):
        self.grid_vc.process_logic()
        if time.time() - self.__turn_start_time >= self.model.player_turn_period:
            self.__next_turn()  # TODO: переписать для сетевой игры (потребуется асинхронная синхронизация)
            self.__turn_start_time = time.time()

    @property
    def is_current_scene_map(self) -> bool:
        scene = type(self.game.current_scene).__name__
        return scene.startswith("Map")

    def process_event(self, event):
        if self.is_current_scene_map:
            self.grid_vc.process_event(event)

    def process_draw(self):
        if self.is_current_scene_map:
            self.grid_vc.process_draw()

    def __next_turn(self):
        self.model.next_player_turn()
        self.game.current_scene.toolbar.update_tools()


def create_hardcoded_game_model() -> GameModel:
    teams = [TeamA(0), TeamB(1), TeamC(2)]
    for i in range(len(teams)):
        team = teams[i]
        team.add_player(create_hardcoded_player(f"P{i}A", team))
        team.add_player(create_hardcoded_player(f"P{i}B", team))
    game = GameModel(teams, title="Hardcoded session", grid_width=6, grid_height=6,
                     player_turn_period=30, teams_money_limit=999)
    for team in teams:
        team.set_game_model(game)
    game.grid.tiles[0][0].conquer(teams[0])
    game.grid.tiles[1][0].conquer(teams[1])
    game.grid.tiles[2][0].conquer(teams[2])
    return game


def create_hardcoded_player(name, team) -> Player:
    player = Player(name, team)
    from game_eng.pressure_tool_set_ders.ddos_pts import DDosPTSet
    from game_eng.pressure_tool_set_ders.dos_pts import DosPTSet
    player.add_pressure_tools(DDosPTSet, 1)
    player.add_pressure_tools(DosPTSet, 2)
    return player
