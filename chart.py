import pandas as pd
import collections
import matplotlib.pyplot as plt

excel_data = pd.read_excel('Ouvido.xlsx')
data = pd.DataFrame(excel_data, columns=['Horário', 'Data'])
dados = collections.defaultdict(list)
dias = []
horarios = []

for index, element in data.iterrows():
    dados[element['Data']].append(element['Horário'].strftime('%H:%M'))
    # if element['Data'] not in dias:
        # dias.append(element['Data'])

    # if element['Horário'] not in horarios:
        # horarios.append(element['Horário'].strftime('%H:%M'))

# for element in dados:
#     print(dados[element])

for element in dados:
    horarios.append(len(dados[element]))

for element in dados:
    dias.append(element)

plt.plot(dias, horarios, color='red', marker='o')
plt.title('Quantidade por dia', fontsize=14)
plt.xlabel('Data', fontsize=14)
plt.ylabel('Quantidade', fontsize=14)
plt.grid(True)
plt.show()