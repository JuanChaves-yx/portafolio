import streamlit as st
from PIL import Image

# Configuración de página ancha para acomodar las 4 columnas cómodamente
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

# Distribuimos las 12 aplicaciones en 4 columnas (3 tarjetas por columna)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("1. Prueba Streamlit")
    image = Image.open('imagenes/txt_to_audio2.png')
    st.image(image, width=180)
    st.write("Creación de archivo inicial de prueba y despliegue básico en la plataforma.") 
    url1 = "https://introca-prueba.streamlit.app/"
    st.write(f"App Prueba: [Enlace]({url1})")

    st.subheader("2. Clasificación Frutas")
    image = Image.open('imagenes/txt_to_audio.png')
    st.image(image, width=180)
    st.write("Agrega frutas (peso, diámetro, dulzor) y calcula distancia entre características.") 
    url2 = "https://clasfruta-yqnz6jhwmu9vgwc7xedzpj.streamlit.app/"
    st.write(f"Clasificación: [Enlace]({url2})")

    st.subheader("3. Descenso de Gradiente")
    image = Image.open('imagenes/OIG5.jpg')
    st.image(image, width=180)
    st.write("Transformación matemática para optimización, derivadas y búsqueda de mínimos.") 
    url3 = "https://scriptgradiente-nh6bc7quqjqwq8rbyd7fpj.streamlit.app/"
    st.write(f"Gradiente: [Enlace]({url3})")

with col2: 
    st.subheader("4. Lógica & Big-O")
    image = Image.open('imagenes/OIG8.jpg')
    st.image(image, width=180)
    st.write("Análisis de complejidad algorítmica, reglas de negocio y vectorización.") 
    url4 = "https://scriptbig0-9ewesadfzcnjekvdqkduam.streamlit.app/"
    st.write(f"Big-O & Vectorización: [Enlace]({url4})")

    st.subheader("5. Preparación de Datos")
    image = Image.open('imagenes/data_analisis.png')
    st.image(image, width=180)
    st.write("Conversión a category, IQR para outliers, Z-score y splits aleatorio vs. cronológico.") 
    url5 = "https://cbynrvaqgzanktxpvnzdrv.streamlit.app/"
    st.write(f"Prep. Datos: [Enlace]({url5})")

    st.subheader("6. Datos Ambientales")
    image = Image.open('imagenes/OIG3.jpg')
    st.image(image, width=180)
    st.write("Análisis CRISP-DM con datos de Cornare MARCO e Índice de Calidad de Datos (ICD).") 
    url6 = "https://pronosticocornare-s2nrwe4eug8vkt9usekfy9.streamlit.app/"
    st.write(f"Datos Cornare: [Enlace]({url6})")

with col3: 
    st.subheader("7. Regresión Lineal")
    image = Image.open('imagenes/Chat_pdf.png')
    st.image(image, width=180)
    st.write("Modelos simple/múltiple, función de costo, learning rate y métricas (MSE, R²).") 
    url7 = "https://appregresion-dpkyxgzgkkuisyvq56kgfx.streamlit.app/"
    st.write(f"Regresión Lineal: [Enlace]({url7})")

    st.subheader("8. Series de Tiempo")
    image = Image.open('imagenes/OIG4.jpg')
    st.image(image, width=180)
    st.write("Análisis de tendencia y estacionalidad con ARIMA, SARIMA y Holt-Winters.") 
    url8 = "https://series-tiempo-imjnyqe8crxw2vjqfznsfr.streamlit.app/"
    st.write(f"Series de Tiempo: [Enlace]({url8})")

    st.subheader("9. Captura IoT")
    image = Image.open('imagenes/OIG6.jpg')
    st.image(image, width=180)
    st.write("Procesamiento de datos en tiempo real (humedad, temperatura) con sensores IoT.") 
    url9 = "https://appthermal-n5ju3pkcxb2ckbgkfylkrn.streamlit.app/"
    st.write(f"Sistema IoT: [Enlace]({url9})")

with col4: 
    st.subheader("10. Regresión Logística")
    image = Image.open('imagenes/txt_to_audio2.png')
    st.image(image, width=180)
    st.write("Transición de predicción de variables continuas a clasificación por categorías.") 
    url10 = "https://appregresion-dpkyxgzgkkuisyvq56kgfx.streamlit.app/"
    st.write(f"Regresión Logística: [Enlace]({url10})")

    st.subheader("11. Clasificación KNN")
    image = Image.open('imagenes/OIG5.jpg')
    st.image(image, width=180)
    st.write("Algoritmo K-Vecinos más Cercanos, fronteras no lineales y búsqueda por similitud.") 
    st.info("Desarrollado con HTML local en clase.")

    st.subheader("12. KNN Suelos AGROSAVIA")
    image = Image.open('imagenes/OIG8.jpg')
    st.image(image, width=180)
    st.write("Clasificación de fertilidad de suelos (baja, media, alta) según análisis químicos.") 
    url12 = "https://suelos-aaanaqm72uokr8cfseyxna.streamlit.app/"
    st.write(f"KNN Suelos: [Enlace]({url12})")
