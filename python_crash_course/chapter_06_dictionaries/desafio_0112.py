# 112: Crie um script com um dicionário nele vai ter duas chaves,cada chave vai ser o nome de uma pessoa,
# e vai receber um dicionário, com primeiro nome, ultimo nome, e localização,
# em seguida faça um loop for ao qual mostre as informações de cada pessoa, nome completo, localização ..
# use items() explique.

pessoas = {
    'Jon': {
        'primeiro_nome': 'Jon',
        'ultimo_nome': 'Snow',
        'localizacao': 'Winterfell'
    },
    'Daenerys': {
        'primeiro_nome': 'Daenerys',
        'ultimo_nome': 'Targaryen',
        'localizacao': 'Dragonstone'
    },
    'Cersei': {
        'primeiro_nome': 'Cersei',
        'ultimo_nome': 'Lannister',
        'localizacao': 'Kingsland'
    }
}

for pessoa, dados in pessoas.items():
    print('--> Nome:', pessoa.title())
    print('\t - Nome completo:', dados['primeiro_nome'], dados['ultimo_nome'])
    print('\t - Localização:', dados['localizacao'])
    print()