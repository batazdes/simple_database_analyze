import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('sales.csv')
print ('Первые 5 строк\n', df.head())
print ('\nТипы данных и пропуски\n', df.info())
print ('\nСтатистика по числовым столбцам\n', df.describe())

average_price = df.groupby('product')['price'].mean().reset_index()
print ('\nСредняя цена продуктов:\n',average_price)

df['total'] = df['price']*df['quantity']
print ('\nДанные с учетом общей выручки:\n', df)

max_benefit = df.nlargest(1, 'total')
print ('\nТовар с максимальной выручкой:\n',str(list(max_benefit['product']))[2:-2])

dates = df[df['total']>500]
print ('\nДаты, в которых выручка была больше 500:\n', list(dates['date']))

summ = df.sum(axis = 0)
print ('\nОбщая сумма продаж\n', summ['quantity'])
print ('\nОбщая выручка\n', summ['total'])

average_product_benefit = df.groupby('product')['total'].sum().reset_index()
print('\nВыручка по каждому типу товаров\n', average_product_benefit,'\n')

numpy_task = np.array(df['total'])
print (numpy_task)
print ('\nСреднее значение всех продаж\n',round(np.mean(numpy_task),2))
print ('\nМедиана всех продаж\n',round(np.median(numpy_task),2))

average_product_benefit.plot (kind = 'bar', title = '\nВыручка по каждому типу товаров\n')
plt.ylabel('Выручка')
plt.xlabel('Товар')
plt.grid(True)
plt.show()

df.to_csv('final_dataset.csv')
