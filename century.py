from read_data_game import *
from init_game import *
from Player import *


class Century():

    def __init__(self):
        self.coins = {'gold': 10, 'silver': 10}
        self.all_card_normal, self.all_card_point = initGame(*readDataGame())
        self.card_point_close = self.all_card_point[5:]
        self.card_normal_close = self.all_card_normal[6:]
        self.card_normal_open = self.all_card_normal[:6]
        self.card_point_open = setBonus(self.all_card_point[:5], self.coins)
        self.turn = 1

    @property
    def run(self):
        data_player = []
        for id in range(1, 6):
            data_player.append(Player(id))

        while not stop_game(data_player):
            print("Turn: ", self.turn)
            for player in data_player:
                card_normal = self.card_normal_open.copy()
                card_point = self.card_point_open.copy()
                coins = self.coins.copy()

                action_player = player.action(card_normal, card_point, coins)
                # print(action_player)

                if type(action_player) == type('string'):
                    action_player = [action_player]

                if not check_action(action_player):
                    print(action_player)
                    raise Exception(f'NGƯỜI CHƠI {player.id} OUTPUT RA SAI SỬA ĐI')

                if action_player[0] == "relax":
                    player.relax

                elif action_player[0] == "get_card_point":
                    player.get_card_point(action_player[1].copy())

                    if action_player[1]['bonus'] == 1:
                        self.coins['silver'] -= 1

                    if action_player[1]['bonus'] == 3:
                        self.coins['gold'] -= 1

                    self.card_point_open.remove(action_player[1])
                    self.card_point_open += [self.card_point_close[-1]]
                    self.card_point_close.pop()

                    self.card_point_open = setBonus(self.card_point_open, self.coins)

                elif action_player[0] == "get_card_normal":
                    if len(self.card_normal_open) == 0:
                        raise Exception(f"DÙ ĐÃ HẾT THẺ NORMAL NHƯNG NGƯỜI CHƠI {player.id} VẪN ACTION LẤY THẺ")

                    card = action_player[1].copy()
                    material_giveback = action_player[2].copy()
                    all_card = self.card_normal_open.copy()
                    pos = self.card_normal_open.index(card)

                    player.get_card_normal(card, material_giveback, all_card, pos)

                    self.card_normal_open.remove(card)

                    if len(self.card_normal_close) != 0:
                        self.card_normal_open.append(self.card_normal_close[-1])
                        self.card_normal_close.pop()

                elif action_player[0] == "card_update":
                    card = action_player[1].copy()
                    material_giveback = action_player[2].copy()
                    material_recevie = action_player[3].copy()

                    player.use_card_upgrade(card, material_giveback, material_recevie)

                elif action_player[0] == "card_get_material":
                    card = action_player[1].copy()
                    material_remove = action_player[2].copy()

                    player.use_card_get_material(card, material_remove)

                elif action_player[0] == "card_exchange":
                    card = action_player[1].copy()
                    times = action_player[2]
                    material_remove = action_player[3].copy()

                    player.use_card_exchange(card, times, material_remove)

                else:
                    raise Exception(
                        'Không có action nào để đọc'
                    )
            self.turn += 1

            if self.turn == 500:
                data_player[0].count_card = 5
                data_player[0].count_point = 40

        id_win = check_player_win(data_player)
        show_point_players(data_player, id_win)
        # print(data_player[2].material)


game = Century()
game.run

