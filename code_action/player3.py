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
import numpy as np

def state_to_states(state):
    states = []
    for idnl in range(3):
        s = state.copy()
        if s[idnl] > 0:
            s[idnl] -= 1
            s[idnl+1] += 1
            states.append(s)
    return states
def full_upgrade(state,upgrade):
    states = [state]
    full = []
    while upgrade > 0:
        temp = []
        for state in states:
            temp += state_to_states(state)
        full += temp
        states = temp.copy()
        upgrade -=1
    return full

def can_buy(state,card):
    c = np.array(list(card['give_back'].values()))
    return min(state-c) >= 0


def future(start_items,targets):
    items = []
    for it in start_items:
        fn = it[0]
        cards = it[1]
        for f in fn:
            for the in cards:
                states = []
                if the['upgrade'] == 0:
                    card = [np.array(list(the['give_back'].values())),np.array(list(the['receive'].values())),0]
                    max = the['times']
                    for idnl in range(4):
                        if card[0][idnl] > 0:
                            times = f[idnl]//card[0][idnl]
                            if times < max:
                                max = times
                    # lần = 0
                    for lan in range(max):
                        state = f - card[0]*(lan+1) + card[1]*(lan+1)
                        while sum(state) > 10:
                            thua = sum(state) - 10
                            for idnl in range(4):
                                state[idnl] -= min(thua,state[idnl])
                        states.append(state)
                else:
                    times = the['upgrade']
                    states = full_upgrade(f,times)
                new_cards = [car for car in cards if car != the]
                item = [states,new_cards]
                items.append(item)
    for item in items:
        for state in item[0]:
            for target in targets:
                if can_buy(state,target):
                    return target['receive']
    for item in items:
        if len(item[1]) == 0:
            return 0
    return future(items,targets)

def first_gen(f,the):
    states = []
    if the['upgrade'] == 0:
        card = [np.array(list(the['give_back'].values())),np.array(list(the['receive'].values())),0]
        max = the['times']
        for idnl in range(4):
            if card[0][idnl] > 0:
                times = f[idnl]//card[0][idnl]
                if times < max:
                    max = times
        # lần = 0
        for lan in range(max):
            state = f - card[0]*(lan+1) + card[1]*(lan+1)
            while sum(state) > 10:
                thua = sum(state) - 10
                for idnl in range(4):
                    state[idnl] -= min(thua,state[idnl])
            states.append(state)
    else:
        times = the['upgrade']
        states = full_upgrade(f,times)
    return states


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
    diem = 5
    card_n = None
    for card in card_normal:
        cost = card_normal.index(card)
        if cost <= player.material["yellow"]:
            ctype,score = phanloai(card)
            if score > diem:
                diem = score
                card_n = card
    #nếu có thẻ normal đẹp thì lấy
    if card_n != None:
        fee = str(card_normal.index(card_n)) + "-0-0-0"
        print("lấy thẻ đổi",list(card_n['give_back'].values()),"lấy",list(card_n['receive'].values()))
        return 'get_card_normal', card_n, convert(fee)
    else:
    #     # nếu không thì chạy engine
    #     for card in player.card_close:
    #         print(card)
        fn = [np.array(list(player.material.values()))]
        cards = player.card_close
        tuonglai = future([[fn,cards]],card_point)
        print(tuonglai)
        # for nhanh in tuonglai:
        #     for nhanh_nho in nhanh[0]:
        #         print(nhanh_nho)
        # for target in card_point:
        #     print(target['receive'])
    return 'relax'

                 


            
