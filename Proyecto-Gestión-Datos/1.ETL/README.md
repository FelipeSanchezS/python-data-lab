Librerías necesarias para su ejecución: 

    - Pandas: Se una con la finalidad de tratar los conjuntos de datos, en este caso, la base de datos.

    - mysql_connector: Se usa como conector entre el script de python y la base de datos creada, para esta ocasión sera MySQL

    - re: Tiene la finalidad de trabajar el tema de expresiones regulares

Pasos para ejecutar el Script: 

    Para realizar esto se requiere unicamente contar con la ruta del archivo excel actualizada, tener la base de datos creada y conectada de forma correcta en cuando a usuario, servidor y contraseña, que la estructura coincida con la establecida en el script y las librerías requeridas instaladas. Una vez hecho esto basta con ejecutar el Script y este ira mostrando en pantalla mensajes de la limpieza de datos y la inserción de registros en cada tabla. Una vez finalizado enviará un mensaje diciendo que todos los datos fueron insertados de forma correcta

Explicación transformaciones aplicadas:

        En este ejercicio directamente dentro del Script del ETL, dentro del Transform se realizan trasformaciones específicamente a las columnas de nombre, categoría, correo y fecha.

            - Nombre: Para este caso se transforma de tal manera que los datos Tengan en mayúscula la primera letra.

             - Categoría: Para este caso al no crearse una tabla y relacionarla dado que según la cantidad de datos y la estructura no lo vi necesario, se procedió a establecer toda la palabra en mayúscula para que logre distinguir una de la otra

             - Correo: Para esta variable se impuso una validación de que el correo debe tener la siguiente: Contener antes y después del signo @ caracteres alfanuméricos y especiales, adicionalmente después de los caracteres que van posterior al @ debe ir un . continuando con caracteres alfanuméricos, dando asi cumplimiento a la estructura básica que tienen los correos electrónicos.

             - Fecha: Para esta variable unicamente se estableció que el formato debía ser YYYY-MM-DD