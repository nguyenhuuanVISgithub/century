'''
    Nghỉ Ngơi: return 'relax'
    Lấy thẻ có điểm: 'get_card_point', card
    Lấy thẻ không có điểm: 'get_card_normal', card, material_giveback
    Sử dụng thẻ:
        - update: 'card_update', card, material_giveback, material_recevie
        - get_material: 'card_get_material', card, material_remove
        - exchange: 'card_exchange', card, times, material_remove
    Note:
        - material_giveback: Nguyên liệu trả cho bàn chơi
        - material_recevie: Nguyên liệu nhận lại
        - material_remove: Nguyên liệu bỏ đi khi tổng số nguyên liệu > 10
        !IMPORTANT
        - Tất cả các biến trên đều có dạng là một dict
            các key là các màu của nguyên liệu(yellow,...)
            value là số nguyên liệu tương ứng
'''
from init_game import convert

def action(player, card_normal, card_ponit, conis):
    card = player.card_close[0]
    a = {'yellow': 0, 'red': 0, 'green': 0, 'brown': 0}
    c = 1
    if c == 1:
        a['yellow'] = 2

    return 'card_update', card, convert(f'{c}-0-0-0'), convert('0-2-0-0')
    #return 'relax'


                 


            
