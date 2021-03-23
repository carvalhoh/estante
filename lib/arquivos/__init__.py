from os import mkdir

def arquivoExiste(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(name, local):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print(f'ERRO! Ao criar o arquivo.')
    else:
        print('Arquivo criado com sucesso!')
