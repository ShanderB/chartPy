import pandas as pd
import collections
import matplotlib.pyplot as plt

excel_data = pd.read_excel('Ouvido.xlsx')
data = pd.DataFrame(excel_data, columns=['Data'])
dados = collections.defaultdict(list)
dias = []
quantidades = []

for index, element in data.iterrows():
    dados[element['Data']].append(element['Data'])
    # if element['Data'] not in dias:
        # dias.append(element['Data'])

    # if element['Horário'] not in horarios:
        # horarios.append(element['Horário'].strftime('%H:%M'))

# for element in dados:
#     print(dados[element])

for element in dados:
    quantidades.append(len(dados[element]))

for element in dados:
    dias.append(element)

plt.plot(dias, quantidades, color='red', marker='o')
# plt.title('Quantidade por dia', fontsize=14)
# plt.text(1, 7, "Revok")
# plt.gca().add_patch(plt.Circle((1, 7), radius=0.3, clip_on=True, fill=False, edgecolor='red', linewidth=2))
plt.gca().add_patch(plt.Rectangle((3, 1), 2, 6, fill=True, color='#f5b3b3'))
plt.gca().add_patch(plt.Rectangle((10, 1), 2, 6, fill=True, color='#f5b3b3'))
plt.gca().add_patch(plt.Rectangle((16, 1), 2, 6, fill=True, color='#f5b3b3'))
plt.gca().add_patch(plt.Rectangle((23, 1), 1, 6, fill=True, color='#f5b3b3'))
plt.xlabel('Data', fontsize=6)
plt.ylabel('Quantidade', fontsize=6)
plt.grid(True)
plt.show()