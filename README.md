# YouTube_travel_analysis

En este proyecto se nutre un dataset con datos procedentes de una API y de Web Scrapping.

Sobre un DataFrame de vídeos de YouTube categorizados, selección de país y año para conocer cuántas visualizaciones han tenido los vídeos de ese país publicados en esa fecha.

1. Descarga de un dataset de vídeos de YouTube de Kaggle.com
2. Creación y limpieza del DataFrame:
    A) Revisión del estado del DataFrame. Columnas: Título, URL, Categoría y Descripción
    B) Filtrado del DataFrame por la categoría de vídeo "travel blog"
    C) Consulta a la API de YouTube mediante Key del número de visualizaciones
    D) Creación de una columna con los jsons procedentes de los requests a la API
    E) Iteración sobre la columna para extraer las visualizaciones de cada vídeos
    F) Consulta a la API de YouTube mediante Key de la fecha de publicación del vídeo
    G) Iteración sobre la columna para extraer la fecha de publicación. Regex para extraer el año
    H) Web Scrapping de la Wikipedia para extraer un listado de países en español y en inglés
    I) Creación de un listado con los países en español y en inglés
    J) Iteración sobre la columna Descripción para saber si se menciona algún país de la lista. Solo se clasifica una pequeña parte de los países. La mayoría de los vídeos no mencionan el país
    K) Casteo de la columna Visualizaciones para tratarla como int.
    H) Creación de un csv a partir del DataFrame limpio

3. Creación de una función para filtrar el DataFrame creado desde el csv limpio, por país y año
    A) Devuelve el número de visualizaciones que registraron los vídeos de ese país publicados ese año

4. Creación de una función para filtrar el DataFrame creado desde el csv limpio, por país agrupado por año
    A) Devuelve un gráfico con el número de visualizaciones que los vídeos del país han registrado cada año

5. Creación de una función para generar un PDF con el gráfico de la función descrita en el apartado 4

6. Creación del archivo main.py donde se define ArgumentParse para ejecutar desde terminal incluyendo el país y el año

#Devuelve un error de que no encuentra el archivo csv limpio en la carpeta. 

