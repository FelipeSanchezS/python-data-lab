import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
archivo_excel = "C:\\Users\\pipe-\\Documents\\Prueba-Ing-Datos\\4.Dataset\\base_datos.xlsx"
dfs = pd.read_excel(archivo_excel, sheet_name=None)

# Verificar qué hojas existen
print(dfs.keys()) 
hoja_ventas = dfs['ventas']  
hoja_clientes = dfs['clientes']  
hoja_productos = dfs['productos']  


# Preprocesar las hojas, si es necesario (por ejemplo, convertir fechas)
hoja_ventas['fecha_venta'] = pd.to_datetime(hoja_ventas['fecha_venta'])

# Crear la figura y los ejes para la cuadrícula de subgráficas (2 filas, 3 columnas)
fig, axs = plt.subplots(2, 3, figsize=(15, 10))  # Ajustar el tamaño de la figura
axs = axs.flatten() 

# Los 5 productos más vendidos
productos_mas_vendidos = hoja_ventas.groupby('id_producto')['cantidad'].sum().sort_values(ascending=False).head(5)
sns.barplot(x=productos_mas_vendidos.index, y=productos_mas_vendidos.values, ax=axs[0])
axs[0].set_xlabel('ID del Producto')
axs[0].set_ylabel('Cantidad Vendida')
axs[0].set_title('Los 5 Productos Más Vendidos')
axs[0].tick_params(axis='x')

# Gráfica de total de ventas por mes
ventas_por_mes = hoja_ventas.groupby(hoja_ventas['fecha_venta'].dt.month)['precio_unitario'].sum()
sns.barplot(x=ventas_por_mes.index, y=ventas_por_mes.values, ax=axs[1], palette=['y','r', 'y','r', 'y','r', 'y','r','y','r','y','r'])
axs[1].set_xlabel('Mes')
axs[1].set_ylabel('Total de Ventas')
axs[1].set_title('Total de Ventas por Mes')
axs[1].set_xticks(range(1, 13))

# Evolución de ventas en el tiempo
ventas_por_fecha = hoja_ventas.groupby('fecha_venta')['precio_unitario'].sum()
sns.lineplot(x=ventas_por_fecha.index, y=ventas_por_fecha.values, ax=axs[2], color='green')
axs[2].set_xlabel('Fecha de Venta')
axs[2].set_ylabel('Total de Ventas')
axs[2].set_title('Evolución de Ventas en el Tiempo')

# Categoría que genera más ingresos
hoja_ventas = hoja_ventas.merge(hoja_productos[['id_producto', 'categoria']], on='id_producto', how='left')  
hoja_ventas.rename(columns={'categoria': 'categoria_productos'}, inplace=True)
ingresos_por_categoria = hoja_ventas.groupby('categoria_productos')['precio_unitario'].sum()
sns.barplot(x=ingresos_por_categoria.index, y=ingresos_por_categoria.values, ax=axs[3], palette='viridis')
axs[3].set_xlabel('Categoría de Producto')
axs[3].set_ylabel('Total de Ingresos')
axs[3].set_title('Ingresos por Categoría de Producto')
axs[3].tick_params(axis='x', rotation=45)

# Clientes que más compran
clientes_que_mas_compran = hoja_ventas.groupby('id_cliente')['id_cliente'].count().sort_values(ascending=False).head(5)
sns.barplot(x=clientes_que_mas_compran.index, y=clientes_que_mas_compran.values, ax=axs[4], palette='viridis')
axs[4].set_xlabel('ID del Cliente')
axs[4].set_ylabel('Cantidad de Compras')
axs[4].set_title('Clientes que más Compran')
axs[4].tick_params(axis='x', rotation=45)

# Desviación estándar de las ventas
sns.histplot(hoja_ventas['precio_unitario'], bins=20, kde=True, color='blue', ax=axs[5])
axs[5].set_xlabel('Precio Unitario')
axs[5].set_ylabel('Frecuencia')
axs[5].set_title('Distribución de Precios Unitarios')

# Ajustar el layout para evitar que las gráficas se superpongan
fig.tight_layout()

# Mostrar la gráfica
plt.show()
