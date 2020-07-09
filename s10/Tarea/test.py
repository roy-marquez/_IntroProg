def prop_update (prop):
    answer = 'Actualizar {} ? : [S = si] / [N = no]'.format(prop)
    if (input(answer.lower()) == 's'):
        return True
    else:
        return False


print( 'Acualizar id_num: ', prop_update('id_num'))
print( 'Acualizar nombre: ', prop_update('nombre'))
print( 'Acualizar email: ', prop_update('email'))
print( 'Acualizar curso: ', prop_update('curso'))
