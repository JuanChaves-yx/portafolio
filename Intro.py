import streamlit as st
from PIL import Image

# Nuevo Título Principal
st.title("Hub de Proyectos y Aplicaciones de Inteligencia Artificial")

with st.sidebar:
    st.subheader("Aplicaciones con Inteligencia Artificial")
    parrafo = (
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos."
    )
    st.write(parrafo)

# Enlace a páginas/ejercicios generales y Proyecto 1 (Prueba de Streamlit)
url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
url_prueba = "https://introca-prueba.streamlit.app/"

st.subheader("Páginas de Referencia y Primera Prueba")
st.write(f"• Material de clase y ejercicios: [Ver Portal]({url_ia})")
st.write(f"• Proyecto 1 (Prueba inicial de Streamlit): [Ver App]({url_prueba})")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Clasificación de Frutas")
    image = Image.open('imagenes/txt_to_audio2.png')
    st.image(image, width=190)
    st.write("Clasificación evaluando peso, diámetro, dulzor y cálculo de distancia.") 
    url = "https://clasfruta-yqnz6jhwmu9vgwc7xedzpj.streamlit.app/"
    st.write(f"Clasificación Frutas: [Enlace]({url})")

    st.subheader("Optimización y Gradiente")
    image = Image.open('imagenes/txt_to_audio.png')
    st.image(image, width=200)
    st.write("Derivadas, cálculo de gradiente y descenso de gradiente.") 
    url = "https://scriptgradiente-nh6bc7quqjqwq8rbyd7fpj.streamlit.app/"
    st.write(f"Descenso de Gradiente: [Enlace]({url})")

    st.subheader("Complejidad y Vectorización")
    image = Image.open('imagenes/OIG5.jpg')
    st.image(image, width=200)
    st.write("Análisis de complejidad algorítmica (Big-O) y vectorización.") 
    url = "https://scriptbig0-9ewesadfzcnjekvdqkduam.streamlit.app/"
    st.write(f"Big-O & Vectorización: [Enlace]({url})")

with col2: 
    st.subheader("Preparación de Datos")
    image = Image.open('imagenes/OIG8.jpg')
    st.image(image, width=200)
    st.write("Tratamiento de outliers (IQR), normalización, estandarización y splits.") 
    url = "https://cbynrvaqgzanktxpvnzdrv.streamlit.app/"
    st.write(f"Preparación de Datos: [Enlace]({url})")

    st.subheader("Monitoreo Ambiental (MARCO)")
    image = Image.open('imagenes/data_analisis.png')
    st.image(image, width=190)
    st.write("Datos ambientales de Cornare y cálculo del Índice de Calidad de Datos (ICD).") 
    url = "https://pronosticocornare-s2nrwe4eug8vkt9usekfy9.streamlit.app/"
    st.write(f"Datos Cornare: [Enlace]({url})")

    st.subheader("Regresión Lineal y Logística")
    image = Image.open('imagenes/OIG3.jpg')
    st.image(image, width=200)
    st.write("Modelos de regresión simple, múltiple y transición a logística.") 
    url_reg = "https://appregresion-dpkyxgzgkkuisyvq56kgfx.streamlit.app/"
    st.write(f"Regresión: [Enlace]({url_reg})")

with col3: 
    st.subheader("Análisis de Series de Tiempo")
    image = Image.open('imagenes/Chat_pdf.png')
    st.image(image, width=190)
    st.write("Pronóstico de tendencia y estacionalidad con modelos ARIMA y Suavizado.") 
    url = "https://series-tiempo-imjnyqe8crxw2vjqfznsfr.streamlit.app/"
    st.write(f"Series de Tiempo: [Enlace]({url})")

    st.subheader("Sistema IoT & Sensores")
    image = Image.open('imagenes/OIG4.jpg')
    st.image(image, width=200)
    st.write("Captura y procesamiento de datos de temperatura y humedad en tiempo real.") 
    url = "https://appthermal-n5ju3pkcxb2ckbgkfylkrn.streamlit.app/"
    st.write(f"Captura IoT: [Enlace]({url})")
    
    st.subheader("Clasificación de Suelos (KNN)")
    image = Image.open('imagenes/OIG6.jpg')
    st.image(image, width=200)
    st.write("Estimación de fertilidad de suelos (AGROSAVIA) con algoritmos KNN.") 
    url = "https://suelos-aaanaqm72uokr8cfseyxna.streamlit.app/"
    st.write(f"KNN Suelos: [Enlace]({url})")
