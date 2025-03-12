# Proyecto de Tratamiento de Datos con Python y Visualización

Este proyecto se centra en el tratamiento de un archivo `.xlsx` utilizando Python, con el objetivo de crear una base de datos y visualizar los datos procesados. El proyecto está dividido en varias fases, las cuales cubren todo el proceso desde la extracción de datos hasta la visualización de los resultados. Además, cada fase posee un README.md independiente para que pueda ser entendido de una mejor forma. Las fases son las siguientes:

## Estructura del Proyecto

El proyecto está dividido en las siguientes carpetas y fases:

1. **ETL (Extract, Transform, Load)**  
   En esta fase, se realizan las tareas de **extracción**, **transformación** y **carga** de los datos provenientes del archivo `.xlsx` a una base de datos. Se emplean bibliotecas de Python como `pandas` y `openpyxl` para manipular y limpiar los datos antes de ser insertados en la base de datos.

2. **SQL**  
   Esta fase contiene el esquema de la base de datos, así como el **dump** de la base de datos, que incluye los registros procesados. El esquema de la base de datos es entregado mediante archivos SQL, y el dump proporciona un respaldo con los datos ya cargados.

3. **Dashboard**  
   En esta fase se crea un **dashboard interactivo** utilizando bibliotecas como `matplotlib`, `seaborn` o `plotly` para visualizar gráficas que permitan analizar los datos de forma clara y eficaz. El archivo ejecutable `.py` genera las visualizaciones a partir de los datos procesados.

4. **Dataset**  
   Esta fase contiene el archivo original `.xlsx` con los datos iniciales que fueron tratados en el proyecto.

## Requisitos

Asegúrate de tener las siguientes dependencias instaladas:

- Python 3.x
- Pandas
- SQLAlchemy
- Matplotlib / Seaborn / Plotly (dependiendo de la herramienta de visualización utilizada)
- openpyxl


## Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
