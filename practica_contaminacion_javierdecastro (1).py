import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime



# Exploración archivo

data=pd.read_csv("calidad-del-aire-datos-historicos-diarios.csv", delimiter=";")
#print(data.head(10)) 
#print(type(data)) 
#print(data.shape) 
#print(data.columns)

data['Fecha'] = pd.to_datetime(data['Fecha'], format='%Y-%m-%d')
data_2020 = data[data['Fecha'].dt.year == 2020]
#print(data_2020)



# Obtener las medias de cada uno de los valores por provincia, durante el año 2020. Si no se tienen valores sustituir por -1

columnas_valores_aire= ['NO (ug/m3)', 'NO2 (ug/m3)', 'SO2 (ug/m3)', 'O3 (ug/m3)', 'CO (mg/m3)']
data_medias_provincia=data_2020.groupby("Provincia")[columnas_valores_aire].mean().reset_index()
data_medias_provincia.fillna(-1, inplace=True)
print(data_medias_provincia)



# Graficar la evolución del NO en toda la comunidad a lo largo de Agosto del 2020

'''data['Fecha'] = pd.to_datetime(data['Fecha'], format='%Y-%m-%d')
data["Mes"] = data["Fecha"].dt.month
data["Año"] = data["Fecha"].dt.year

NO_agosto_2020 = data[(data["Año"] == 2020) & (data["Mes"] == 8)]
evolucion_NO = NO_agosto_2020.groupby("Fecha")["NO (ug/m3)"].mean().reset_index()

plt.plot(evolucion_NO["Fecha"], evolucion_NO["NO (ug/m3)"])
plt.title("Evolución del NO en agosto de 2020")
plt.xlabel("Fecha")
plt.ylabel("Valor de NO")
plt.xticks(rotation=45)
plt.show()'''



# Evolución del NO en la ciudad de León a lo largo del año 2020

'''data['Fecha'] = pd.to_datetime(data['Fecha'], format='%Y-%m-%d')
data["Año"] = data["Fecha"].dt.year
data["Provincia"] = data["Provincia"].str.title() 

NO_2020_leon = data[(data["Año"] == 2020) & (data["Provincia"] == "León")] 
evolucion_NO_leon = NO_2020_leon.groupby("Fecha")["NO (ug/m3)"].mean().reset_index()

plt.plot(evolucion_NO_leon["Fecha"], evolucion_NO_leon["NO (ug/m3)"])
plt.title("Evolución del NO en León durante 2020")
plt.xlabel("Fecha")
plt.ylabel("Valor de NO")
plt.xticks(rotation=45)
plt.show()'''


#Gráfica múltiple donde se miden el NO, O3 y SO2

fig, ax = plt.subplots(2,2)

labelx = ['NO (ug/m3)', 'O3 (ug/m3)', 'SO2 (ug/m3)']
Avila = [3.098901,61.975000,2.301105]
Burgos= [4.304047,55.509447,2.677905]
Leon = [2.873876,51.694713,3.929156]
Palencia= [3.765262,52.577454,4.291298]
Salamanca= [3.520510,66.616963,2.299868]
Segovia = [2.983607,63.674863,3.084699]
Soria = [6.639344,58.293629,2.131148]
Valladolid= [6.639344,49.740148,5.814388]
Zamora= [6.549180,55.294766,2.224044]

'''ax.set_xlabel('variables a medir')
ax.set_ylabel('valores')

ax.bar(labelx, Avila, label='Avila')
ax.bar(labelx, Burgos, label='Burgos')
ax.bar(labelx, Leon, label='Leon')
ax.bar(labelx, Palencia, label='Palencia')
ax.bar(labelx, Salamanca, label='Salamanca')
ax.bar(labelx, Segovia, label='Segovia')
ax.bar(labelx, Soria, label='Soria')
ax.bar(labelx, Valladolid, label='Valladolid')
ax.bar(labelx, Zamora, label='Zamora')

ax.legend()
plt.show()'''

# Comparativa de los niveles de NO por provincias 
'''NO = [Avila[0],Burgos[0],Leon[0],Palencia[0],Salamanca[0],Segovia[0],Soria[0],Valladolid[0],Zamora[0]]
Provincias = ['Avila','Burgos','Leon','Palencia','Salamanca','Segovia','Soria','Valladolid','Zamora']

ax.set_xlabel('Provincias')
ax.set_ylabel('valores')
ax.bar(Provincias,NO,label="NO")
ax.legend()
plt.show()'''


#Gráfica múltiple 

NO = [Avila[0],Burgos[0],Leon[0],Palencia[0],Salamanca[0],Segovia[0],Soria[0],Valladolid[0],Zamora[0]]
O3 = [Avila[1],Burgos[1],Leon[1],Palencia[1],Salamanca[1],Segovia[1],Soria[1],Valladolid[1],Zamora[1]]
SO2 = [Avila[2],Burgos[2],Leon[2],Palencia[2],Salamanca[2],Segovia[2],Soria[2],Valladolid[2],Zamora[2]]
Provincias = ['Avila','Burgos','Leon','Palencia','Salamanca','Segovia','Soria','Valladolid','Zamora']
ax[0,0].set_xlabel('Provincias')
ax[0,0].set_ylabel('Valores')
ax[0,0].plot(Provincias,NO, label= 'NO')
ax[0,0].legend()

ax[0,1].set_xlabel('Provincias')
ax[0,1].set_ylabel('Valores')
ax[0,1].bar(Provincias,O3, label= 'O3')
ax[0,1].legend()

ax[1,0].set_xlabel('Provincias')
ax[1,0].set_ylabel('Valores')
ax[1,0].scatter(Provincias,SO2, label= 'SO2')
ax[1,0].legend()

plt.show()






































