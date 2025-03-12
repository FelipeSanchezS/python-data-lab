import pandas as pd
import mysql.connector
import re

#Primero creamos el conector a la base de datos
# Configuración de la conexión
conexion = mysql.connector.connect(
    host='localhost',  # o la IP del servidor MySQL
    user='root',  # tu usuario de MySQL
    password='',  # tu contraseña de MySQL
    database='prueba2'  # nombre de tu base de datos
)

# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()

#############################################
#EXTRAEMOS LOS DATOS 
#############################################
# Leer el archivo Excel
archivo_excel = "C:\\Users\\pipe-\\Documents\\Prueba-Ing-Datos\\4.Dataset\\base_datos.xlsx"
dfs = pd.read_excel(archivo_excel, sheet_name=None)

# Mostrar los nombres de las hojas disponibles
print(dfs.keys())  # Esto te mostrará los nombres de las hojas en el archivo Excel
hoja_ventas = dfs['ventas']
hoja_clientes = dfs['clientes']
hoja_productos = dfs['productos']

#############################################
#TRANSFORMACIÓN DE DATOS
#############################################

# Normalizar nombres y categorías
hoja_clientes['nombre_cliente'] = hoja_clientes['nombre_cliente'].str.title()
hoja_productos['categoria'] = hoja_productos['categoria'].str.upper()

#Validamos los valores nulos
print('valores Nulos para la hoja ventas')
print(hoja_ventas.isna().sum())

print('valores Nulos para la hoja productos')
print(hoja_productos.isna().sum())

print('valores Nulos para la hoja clientes')
print(hoja_clientes.isna().sum())

#Para este caso manejaremos los valores nulos eliminándolos, en este caso, la totalidad de la fila 
hoja_ventas.dropna(subset=['fecha_venta', 'id_cliente', 'id_producto', 'precio_unitario'], inplace=True)  

#Validamos nuevamente todas las tablas para validar que los datos estén correctos y limpios
print('valores Nulos para la hoja ventas')
print(hoja_ventas.isna().sum())

print('valores Nulos para la hoja productos')
print(hoja_productos.isna().sum())

print('valores Nulos para la hoja clientes')
print(hoja_clientes.isna().sum())

#Validamos los correos electrónicos
# Función para validar correo electrónico
def validar_email(email):
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(patron, email))

# Aplicar la validación de correos
hoja_clientes['email_valido'] = hoja_clientes['email'].apply(validar_email)

# Filtrar solo los registros con correos electrónicos válidos
hoja_clientes_validos = hoja_clientes[hoja_clientes['email_valido'] == True]

#Transformamos las fechas en formato correcto en caso que no lo este
hoja_ventas['fecha_venta'] = pd.to_datetime(hoja_ventas['fecha_venta'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')

#############################################
#CARGUE DE DATOS
#############################################

# Cargar los datos en la tabla 'clientes'
for index, row in hoja_clientes.iterrows():
    cursor.execute('''
        INSERT INTO clientes (id_cliente, nombre_cliente, ciudad, email) 
        VALUES (%s, %s, %s, %s)
    ''', (row['id_cliente'], row['nombre_cliente'], row['ciudad'], row['email']))
print('Valores insertados correctamente de la tabla clientes')

# # Cargar los datos en la tabla 'productos'
for index, row in hoja_productos.iterrows():
    cursor.execute('''
        INSERT INTO productos (id_producto, nombre_producto, categoria, precio) 
        VALUES (%s, %s, %s, %s)
    ''', (row['id_producto'], row['nombre_producto'], row['categoria'], row['precio']))
print('Valores insertados correctamente de la tabla productos')

# # Cargar los datos en la tabla 'ventas'
for index, row in hoja_ventas.iterrows():
    cursor.execute('''
        INSERT INTO ventas (id_venta, fecha_venta, id_cliente, id_producto, cantidad, precio_unitario, total_venta) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    ''', (row['id_venta'], row['fecha_venta'], row['id_cliente'], row['id_producto'], 
        row['cantidad'], row['precio_unitario'], row['total_venta']))
print('Valores insertados correctamente de la tabla ventas')

# # Confirmar los cambios y cerrar la conexión
conexion.commit()


print("Datos cargados correctamente en la base de datos MySQL.")