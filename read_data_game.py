import pandas as pd
import numpy as np
from init_game import convert

def readDataGame():
    data = pd.read_excel('data_card/card_normal.xlsx', sheet_name='exchange', engine='openpyxl')
    data = dict(data)
    attribute = list(data.keys())

    data_card_normal = []
    for i in range(len(data['times'])):
        df_dict = {}

        for att in attribute:
            if att[0] in ['g', 'r']:
                df_dict[att] = convert(data[att][i])
            else:
                df_dict[att] = int(data[att][i])

        data_card_normal.append(df_dict.copy())
    
    data = pd.read_excel('data_card/card_point.xlsx', engine='openpyxl')

    data_card_point = [
        {'give_back': data['card_point'][i], 'receive': data['ponit'][i]}
        for i in range(len(data))
    ]

    return data_card_normal, data_card_point