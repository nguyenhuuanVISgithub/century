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

def can_buy(player,card):
    mua = True
    target = list(card["give_back"].values())
    for nl in range(4):
        if target[nl] > list(player.material.values())[nl]:
            mua = False
            break
    return mua

def sapmua(player,card):
    # sắp mua khi nâng cấp
    thua = []
    thieu = []
    for nl in card['give_back'].keys():
        thua_1 = (player.material[nl] - card['give_back'][nl])*(player.material[nl] > card['give_back'][nl])
        thua.append(thua_1)
        thieu_1 = card['give_back'][nl]- (player.material[nl] )*(card['give_back'][nl] > player.material[nl])
        thieu.append(thieu_1)
    if sum(thieu) <3:
        # print("thừa",thua,"thiếu",thieu)
        if sum(thieu) == 1:
            # print(thieu.index(max(thieu)))
            for idnl in range(thieu.index(max(thieu))):
                if thua[idnl] > 0:
                    return 1
        if sum(thieu) == 2:
            # print(thua,thieu)
            if thieu[0] > 0:
                return None
            else:
                for idnl in range(1,4):
                    if thieu[idnl] > thua[idnl-1]:
                        return None
                return 2
    # return False

def future(player,card)


def action(player, card_normal, card_point, conis):
    # target = [int(i) for i in card_point[0]["give_back"].split("-")]
    target = list(card_point[4]["give_back"].values())
    mua = True
    for card in card_point:
        if sapmua(player,card) != None:
            target = list(card["give_back"].values())
        if can_buy(player,card):
            # print("lấy điểm",target,player.material)
            print(card_point.index(card))
            return 'get_card_point',card
    # print(target,player.material)
    trong_tay = list(player.material.values())
    so_luong = sum(target) - sum(trong_tay)
    # print(target,trong_tay,so_luong)
    if so_luong > 0:
        state = "lay_nl"
    else:
        state = "upgrade"
    # print(state)
    if state == "lay_nl":
        for card in player.card_close:
            if (sum(card["receive"].values())) == 2:
                # print("lấy 2 vàng")
                return "card_get_material", card, convert("0-0-0-0")
    else:
        #nâng cấp
        use = None
        for card in player.card_close:
            if (sum(card["receive"].values())) == 0:
                use = card
    # nâng cấp cái gì
        if use != None:
            list_nang_cap = [0,0,0,0]
            for nl in range(4):
                if trong_tay[nl] > target[nl]:
                    for a in range(trong_tay[nl] - target[nl]):
                        list_nang_cap[nl] += 1
                        if sum(list_nang_cap) == 2:
                            break
                    break
            list_nhan_ve = [0]
            for nl in range(3):
                list_nhan_ve.append(list_nang_cap[nl])
            # print(list_nang_cap,list_nhan_ve)
            give_back = "-".join(map(str,list_nang_cap))
            receive = "-".join(map(str,list_nhan_ve))
            # print(give_back,receive)
            # print("nâng cấp 2 lần",give_back,receive,target,trong_tay)
            return 'card_update', use, convert(give_back), convert(receive)
        else:
            for card in player.card_close:
                if (sum(card["receive"].values())) == 2 and sum(trong_tay) <6:
                    # print("lấy 2 vàng")
                    return "card_get_material", card, convert("0-0-0-0")
            # print("nghỉ 1")
            return "relax"
    # print("nghỉ 2")
    return "relax"
            
