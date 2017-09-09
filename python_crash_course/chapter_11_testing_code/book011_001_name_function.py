def get_nome_completo(firt_name, last_name, middle=''):
    """Formatar nome completo"""
    if  middle:
        full_name = firt_name + ' ' + middle + ' ' + last_name
    else:
        full_name = firt_name + ' ' + last_name
    return full_name.title()