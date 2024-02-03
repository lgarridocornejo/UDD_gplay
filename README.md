# UDD_gplay
Proyecto 7 Data Science &amp; IA

# Análisis de Sentimientos en Reseñas de Google Play usando SVM

Este proyecto utiliza máquinas de vectores de soporte (SVM) para predecir el sentimiento de las reseñas de las aplicaciones en Google Play Store. El objetivo es desarrollar un modelo de aprendizaje automático que pueda clasificar automáticamente las reseñas como positivas o negativas.

## Objetivo

El objetivo principal de este proyecto es demostrar la eficacia de utilizar SVM para la clasificación de sentimientos en grandes volúmenes de reseñas de aplicaciones en Google Play Store. Al predecir el sentimiento de las reseñas, las empresas pueden comprender mejor la percepción de los usuarios sobre sus aplicaciones y tomar decisiones informadas para mejorar la experiencia del usuario.

## Conjunto de Datos

El conjunto de datos utilizado en este proyecto consiste en reseñas de aplicaciones recopiladas de Google Play Store. Cada reseña está etiquetada con un sentimiento: positivo o negativo. El conjunto de datos se divide en un conjunto de entrenamiento y un conjunto de prueba para evaluar el rendimiento del modelo.

## Implementación

El proyecto está implementado en Python utilizando la biblioteca scikit-learn para el entrenamiento y la evaluación del modelo SVM. Se siguen los siguientes pasos principales:

1. Preprocesamiento de Datos: Limpiar y preprocesar las reseñas de las aplicaciones, incluida la tokenización y eliminación de palabras irrelevantes.
2. Extracción de Características: Convertir las reseñas preprocesadas en vectores numéricos para que puedan ser utilizadas como entrada para SVM.
3. Entrenamiento del Modelo: Utilizar SVM para entrenar un modelo en el conjunto de datos de entrenamiento.
4. Evaluación del Modelo: Evaluar el rendimiento del modelo utilizando el conjunto de datos de prueba y métricas como precisión, recall y F1-score.


## Uso

Para utilizar este proyecto, sigue estos pasos:

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias necesarias especificadas en `requirements.txt`.
3. Ejecuta el script principal para entrenar y evaluar el modelo.

## Contenido

1. data: Carpeta donde se almacenan los set de datos
2. lib: Carpeta que contiene un par de librerias personales
3. story: Carpeta con la presentación del proyecto, con y sin notas del autor.

<pre>
├── github.url
├── LICENSE
├── README.md
├── UDD_Proyecto_M7.ipynb
├── requirement.txt
├── svc.pkl
└── data
    ├── googleplaystore.csv
    ├── googleplaystore_user_reviews.csv
    ├── license.txt
    └── play.png
├── lib
    ├── examinar.py
    └── normalizacion.py
├── story
    ├── google_play_notas.pdf
    └── google_play.pdf

</pre>

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir a este proyecto, sigue estos pasos:

1. Realiza un fork del repositorio.
2. Crea una nueva rama para tu contribución.
3. Haz tus cambios y realiza un pull request para que sean revisados.

## Contacto

Para cualquier pregunta o sugerencia, no dudes en ponerte en contacto con [Luis Garrido Cornejo](https://github.com/lgarridocornejo).

## Licencia

Este proyecto está bajo la [GNU General Public License v3.0](LICENSE).
