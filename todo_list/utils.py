def retorna_o_maior_id_de_uma_list(list: list):
    maior_id = 0
    for item in list:
        if item['id'] > maior_id:
            maior_id = item['id']
    
    return maior_id
