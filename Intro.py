import streamlit as st
from PIL import Image

st.set_page_config(page_title="Hub de Aplicaciones de IA", layout="wide")

st.title("Hub de Aplicaciones y Proyectos de Inteligencia Artificial")

with st.sidebar:
    st.subheader("Aplicaciones con Inteligencia Artificial")
    parrafo = (
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos."
    )
    st.write(parrafo)

# Portal general de ejercicios
url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios generales: [Portal de Ejercicios]({url_ia})")

st.divider()

# Lista horizontal de los 12 Proyectos

# Proyecto 1
with st.container():
    c1, c2 = st.columns([1, 4])
    with c1:
        st.image(Image.open('imagenes/txt_to_audio2.png'), width=180)
    with c2:
        st.subheader("Proyecto 1: Prueba de Streamlit")
        st.write("Creación de un archivo de prueba inicial para evaluar y desplegar aplicaciones en Streamlit.")
        url1 = "https://introca-prueba.streamlit.app/"
        st.write(f"Enlace a la app: [Probar App]({url1})")

st.divider()

# Proyecto 2
with st.container():
    c1, c2 = st.columns([1, 4])
    with c1:
        st.image(Image.open('imagenes/txt_to_audio.png'), width=180)
    with c2:
        st.subheader("Proyecto 2: Clasificación de Frutas")
        st.write("Despliegue de aplicación en Streamlit para clasificar frutas definiendo peso, diámetro y dulzor, calculando la distancia matemática con nuevos registros.")
        url2 = "https://clasfruta-yqnz6jhwmu9vgwc7xedzpj.streamlit.app/"
        st.write(f"Enlace a la app: [Clasificación Frutas]({url2})")

st.divider()

# Proyecto 3
with st.container():
    c1, c2 = st.columns([1, 4])
    with c1:
        st.image(Image.open('imagenes/OIG5.jpg'), width=180)
    with c2:
        st.subheader("Proyecto 3: Descenso de Gradiente y Optimización")
        st.write("Exploración de derivadas y gradientes para transformar un problema matemático en un proceso computacional de búsqueda de mínimos e iteración de parámetros.")
        url3 = "https://scriptgradiente-nh6bc7quqjqwq8rbyd7fpj.streamlit.app/"
        st.write(f"Enlace a la app: [Script Gradiente]({url3})")

st.divider()

# Proyecto 4
with st.container():
    c1, c2 = st.columns([1, 4])
    with c1:
        st.image(Image.open('imagenes/OIG8.jpg'), width=180)
    with c2:
        st.subheader("Proyecto 4: Lógica, Complejidad (Big-O) y Vectorización")
        st.write("Análisis de la cadena causal entre lógica de negocios, escalabilidad computacional (Big-O) y optimización mediante vectorización.")
        url4 = "https://scriptbig0-9ewesadfzcnjekvdqkduam.streamlit.app/"
        st.write(f"Enlace a la app: [Big-O y Vectorización]({url4})")

st.divider()

# Proyecto 5
with st.container():
    c1, c2 = st.columns([1, 4])
    with c1:
        st.image(Image.open('imagenes/data_analisis.png'), width=180)
    with c2:
        st.subheader("Proyecto 5: Preparación y Análisis de Datos")
        st.write("Técnicas de preparación de datos: conversión de tipos (category), filtrado de outliers mediante IQR, normalización/estandarización, splits aleatorios vs. cronológicos y análisis de correlación.")
        url5 = "https://cbynrvaqgzanktxpvnzdrv.streamlit.app/"
        st.write(f"Enlace a la app: [Preparación de Datos]({url5})")

st.divider()

# Proyecto 6
with st.container():
    c1, c2 = st.columns([1, 4])
    with c1:
        st.image(Image.open('imagenes/OIG3.jpg'), width=180)
    with c2:
        st.subheader("Proyecto 6: Monitoreo Ambiental CRISP-DM (Cornare)")
        st.write("Procesamiento de datos ambientales reales de estaciones de monitoreo de Cornare (MARCO) bajo la metodología CRISP-DM y construcción del Índice de Calidad de Datos (ICD).")
        url6 = "https://pronosticocornare-s2nrwe4eug8vkt9usekfy9.streamlit.app/"
        st.write(f"Enlace a la app: [Pronóstico Cornare]({url6})")

st.divider()

# Proyecto 7
with st.container():
    c1, c2 = st.columns([1, 4])
    with c1:
        st.image(Image.open('imagenes/Chat_pdf.png'), width=180)
    with c2:
        st.subheader("Proyecto 7: Regresión Lineal Simple y Múltiple")
        st.write("Modelado predictivo continuo, análisis de la función de costo, tasa de aprendizaje (learning rate) y métricas de evaluación (MSE, R²).")
        url7 = "https://appregresion-dpkyxgzgkkuisyvq56kgfx.streamlit.app/"
        st.write(f"Enlace a la app: [Regresión Lineal]({url7})")

st.divider()

# Proyecto 8
with st.container():
    c1, c2 = st.columns([1, 4])
    with c1:
        st.image(Image.open('imagenes/OIG4.jpg'), width=180)
    with c2:
        st.subheader("Proyecto 8: Pronóstico de Series de Tiempo")
        st.write("Análisis de tendencia, estacionalidad y ruido en series temporales aplicando modelos estadísticos potentes como ARIMA, SARIMA y Suavizado Exponencial (Holt-Winters).")
        url8 = "https://series-tiempo-imjnyqe8crxw2vjqfznsfr.streamlit.app/"
        st.write(f"Enlace a la app: [Series de Tiempo]({url8})")

st.divider()

# Proyecto 9
with st.container():
    c1, c2 = st.columns([1, 4])
    with c1:
        st.image(Image.open('imagenes/OIG6.jpg'), width=180)
    with c2:
        st.subheader("Proyecto 9: Captura y Procesamiento de Datos IoT")
        st.write("Obtención e integración de datos térmicos y de humedad en tiempo real con dispositivos físicos de sensores IoT.")
        url9 = "https://appthermal-n5ju3pkcxb2ckbgkfylkrn.streamlit.app/"
        st.write(f"Enlace a la app: [Captura Thermal IoT]({url9})")

st.divider()

# Proyecto 10
with st.container():
    c1, c2 = st.columns([1, 4])
    with c1:
        st.image(Image.open('imagenes/txt_to_audio2.png'), width=180)
    with c2:
        st.subheader("Proyecto 10: Transición de Regresión Lineal a Regresión Logística")
        st.write("Evolución de modelos predictivos desde la estimación de variables numéricas continuas hacia la clasificación por categorías.")
        url10 = "https://appregresion-dpkyxgzgkkuisyvq56kgfx.streamlit.app/"
        st.write(f"Enlace a la app: [Regresión Logística]({url10})")

st.divider()

# Proyecto 11
with st.container():
    c1, c2 = st.columns([1, 4])
    with c1:
        st.image(Image.open('imagenes/OIG5.jpg'), width=180)
    with c2:
        st.subheader("Proyecto 11: Clasificación con K-Vecinos más Cercanos (KNN)")
        st.write("Estudio del algoritmo KNN para capturar fronteras no lineales, detección de anomalías y búsqueda por similitud.")
        st.info("Desarrollado con interfaz HTML provista en clase.")

st.divider()

# Proyecto 12
with st.container():
    c1, c2 = st.columns([1, 4])
    with c1:
        st.image(Image.open('imagenes/OIG8.jpg'), width=180)
    with c2:
        st.subheader("Proyecto 12: Clasificación de Fertilidad de Suelos (KNN & AGROSAVIA)")
        st.write("Aplicación práctica del algoritmo KNN para clasificar el nivel de fertilidad de suelos (baja, media, alta) a partir de análisis químicos.")
        url12 = "https://suelos-aaanaqm72uokr8cfseyxna.streamlit.app/"
        st.write(f"Enlace a la app: [Clasificación de Suelos]({url12})")
