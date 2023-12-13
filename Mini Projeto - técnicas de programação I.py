import numpy as np

def simulador_de_dados():
    primeiro_dado = np.random.randint(1, 7)
    segundo_dado = np.random.randint(1, 7)
    return primeiro_dado + segundo_dado

simulador_de_dados()

rodadas = np.array([simulador_de_dados() for i in range(1000)])
print(f'Array criado {rodadas}')
print(f'Soma dos resultados {rodadas.sum()}')


media = rodadas.mean()
maximo = rodadas.max()
minimo = rodadas.min()
unicos, contagem = np.unique(rodadas, return_counts=True)
frequencia = dict(zip(unicos, contagem))

print(f'Média dos resultados: {media} \n'
     f'Lançamento máximo: {maximo}\n'
     f'Lançamento mínimo: {minimo}\n'
     f'Número de vezes que cada possível lançamento ocorreu:{frequencia}')

