import streamlit as st
from PIL import Image

# Título Principal
st.title("Hub de Proyectos y Aplicaciones de Inteligencia Artificial")

with st.sidebar:
    st.subheader("Aplicaciones con Inteligencia Artificial")
    parrafo = (
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos."
    )
    st.write(parrafo)

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")

st.divider()


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("1. Prueba Inicial")
    image = Image.open('imagenes/txt_to_audio2.png')
    st.image(image, width=150)
    st.write("Archivo de prueba inicial desarrollado para probar la plataforma Streamlit.") 
    url = "https://introca-prueba.streamlit.app/"
    st.write(f"App Prueba: [Enlace]({url})")

    st.subheader("2. Clasificación de Frutas")
    image = Image.open('imagenes/txt_to_audio.png')
    st.image(image, width=150)
    st.write("Clasificación evaluando peso, diámetro, dulzor y cálculo de distancias.") 
    url = "https://clasfruta-yqnz6jhwmu9vgwc7xedzpj.streamlit.app/"
    st.write(f"Frutas: [Enlace]({url})")

    st.subheader("3. Optimización y Gradiente")
    image = Image.open('imagenes/OIG5.jpg')
    st.image(image, width=150)
    st.write("Exploración de derivadas y descenso de gradiente para optimización.") 
    url = "https://scriptgradiente-nh6bc7quqjqwq8rbyd7fpj.streamlit.app/"
    st.write(f"Gradiente: [Enlace]({url})")


with col2: 
    st.subheader("4. Complejidad y Vectorización")
    image = Image.open('imagenes/OIG8.jpg')
    st.image(image, width=150)
    st.write("Análisis de complejidad algorítmica (Big-O), lógica y vectorización.") 
    url = "https://scriptbig0-9ewesadfzcnjekvdqkduam.streamlit.app/"
    st.write(f"Big-O: [Enlace]({url})")

    st.subheader("5. Preparación de Datos")
    image = Image.open('imagenes/data_analisis.png')
    st.image(image, width=150)
    st.write("Tratamiento de outliers (IQR), normalización, estandarización y splits.") 
    url = "https://cbynrvaqgzanktxpvnzdrv.streamlit.app/"
    st.write(f"Prep. Datos: [Enlace]({url})")

    st.subheader("6. Monitoreo Ambiental")
    image = Image.open('imagenes/OIG3.jpg')
    st.image(image, width=150)
    st.write("Datos ambientales de Cornare (MARCO) e Índice de Calidad de Datos (ICD).") 
    url = "https://pronosticocornare-s2nrwe4eug8vkt9usekfy9.streamlit.app/"
    st.write(f"Cornare: [Enlace]({url})")


with col3: 
    st.subheader("7. Regresión Lineal")
    image = Image.open('imagenes/Chat_pdf.png')
    st.image(image, width=150)
    st.write("Modelos de regresión simple y múltiple, función de costo y métricas.") 
    url = "https://appregresion-dpkyxgzgkkuisyvq56kgfx.streamlit.app/" # (reutilizando link de regresión)
    st.write(f"Regresión: [Enlace]({url})")

    st.subheader("8. Series de Tiempo")
    image = Image.open('imagenes/OIG4.jpg')
    st.image(image, width=150)
    st.write("Pronóstico de tendencia y estacionalidad mediante ARIMA y Suavizado Exponencial.") 
    url = "https://series-tiempo-imjnyqe8crxw2vjqfznsfr.streamlit.app/"
    st.write(f"Series Tiempo: [Enlace]({url})")

    st.subheader("9. Sistema de IoT")
    image = Image.open('imagenes/OIG6.jpg')
    st.image(image, width=150)
    st.write("Captura y procesamiento de datos térmicos y de humedad en tiempo real con sensores.") 
    url = "https://appthermal-n5ju3pkcxb2ckbgkfylkrn.streamlit.app/"
    st.write(f"Captura IoT: [Enlace]({url})")


with col4:
    st.subheader("10. Regresión Logística")
    image = Image.open('imagenes/txt_to_audio2.png')
    st.image(image, width=150)
    st.write("Transición conceptual de la predicción numérica a la clasificación de clases.") 
    url = "https://appregresion-dpkyxgzgkkuisyvq56kgfx.streamlit.app/"
    st.write(f"Reg. Logística: [Enlace]({url})")

    st.subheader("11. Clasificación KNN (HTML)")
    image = Image.open('imagenes/OIG8.jpg')
    st.image(image, width=150)
    st.write("Fundamentos del algoritmo KNN y fronteras no lineales (Trabajo local con HTML).") 
    st.write("*Desarrollado en HTML local*")

    st.subheader("12. KNN Suelos")
    image = Image.open('imagenes/data_analisis.png')
    st.image(image, width=150)
    st.write("Clasificación de la fertilidad de suelos (AGROSAVIA) con K-Vecinos Más Cercanos.") 
    url = "https://suelos-aaanaqm72uokr8cfseyxna.streamlit.app/"
    st.write(f"KNN Suelos: [Enlace]({url})")
