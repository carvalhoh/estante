from lib.arquivos import *

try:
    arq = str(input('nome do arquivo: ')).strip()
    caminho = './armazenamento/'
    arq = f'{caminho}{arq}.txt'
except FileNotFoundError:
    print('Arquivo não encontrado.')
else:
    if not arquivoExiste(arq):
        criarArquivo(arq, caminho)
