import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

diretorio = "C:\\Users\\mneto\\git_test_repo\\ADA_classes\\DS-PY-Data-Science\\DS-PY-004 TÉCNICAS DE PROGRAMAÇÃO I (PY)\\Material do Aluno\\datasets"

base1 = pd.read_csv(os.path.join(diretorio, 'base1.csv'), sep=',')
base2 = pd.read_csv(os.path.join(diretorio, 'base2.csv'), sep=',')

dados_concatenados = pd.concat([base1, base2], ignore_index=True)

dados_concatenados_sem_duplicatas = dados_concatenados.drop_duplicates()

dados_tratados = dados_concatenados_sem_duplicatas.dropna()


plt.figure(figsize=(10, 6))
sns.boxplot(data=dados_tratados)
plt.title('Boxplot dos Dados Tratados')
plt.show()

#teste
#teste