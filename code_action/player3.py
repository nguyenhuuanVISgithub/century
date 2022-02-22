'''
    Nghỉ Ngơi: return 'relax'
    Lấy thẻ có điểm: 'get_card_point', card
    Lấy thẻ không có điểm: 'get_card_normal', card, material_giveback
    Sử dụng thẻ:
        - update: 'card_update', card, material_giveback, material_receive
        - get_material: 'card_get_material', card, material_remove
        - exchange: 'card_exchange', card, times, material_remove
    Note:
        - material_giveback: Nguyên liệu trả cho bàn chơi
        - material_receive: Nguyên liệu nhận lại
        - material_remove: Nguyên liệu bỏ đi khi tổng số nguyên liệu > 10
        !IMPORTANT
        - Tất cả các biến trên đều có dạng là một dict
            các key là các màu của nguyên liệu(yellow,...)
            value là số nguyên liệu tương ứng
'''
from init_game import convert

def phanloai(card):
    if card["upgrade"] >0:
        return "finisher",card["upgrade"]*10
    if sum(card["give_back"].values()) == 1:
        score = 0
        for idnl in range(4):
            score += (1+idnl)*(list(card["receive"].values())[idnl]-list(card["give_back"].values())[idnl])
        return "crawler",score
    if sum(card["give_back"].values()) == 0:
        score = 0
        for idnl in range(4):
            score += (1+idnl)*(list(card["receive"].values())[idnl])
        return "birth",score*5
    if sum(card['give_back'].values()) == sum(card['receive'].values()):
        for idnl in range(4):
            if list(card['give_back'].values())[idnl] > 0:
                score = 4-idnl
                return "trader",score*2
    return None, 0

def action(player, card_normal, card_point, conis):
    # diem = 2
    # card_n = None
    # for card in card_normal:
    #     cost = card_normal.index(card)
    #     if cost <= player.material["yellow"]:
    #         ctype,score = phanloai(card)
    #         if score > diem:
    #             diem = score
    #             card_n = card
    # #nếu có thẻ normal đẹp thì lấy
    # if card_n != None:
    #     fee = str(card_normal.index(card_n)) + "-0-0-0"
    #     # print(fee,card_normal.index(card))
    #     return 'get_card_normal', card_n, convert(fee)
    # else:
    #     # nếu không thì chạy engine
    #     for card in player.card_close:
    #         print(card)
    return 'relax'

                 


            
