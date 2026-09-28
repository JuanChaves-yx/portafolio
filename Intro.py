import streamlit as st
from PIL import Image

# Título Principal
st.title("Aplicaciones de Inteligencia Artificial.")

with st.sidebar:
    st.subheader("Aplicaciones con Inteligencia Artificial.")
    parrafo = (
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos."
    )
    st.write(parrafo)

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")

# Manteniendo la estructura de 3 columnas horizontales
col1, col2, col3 = st.columns(3)

with col1:
    # Proyecto 1
    st.subheader("1. Prueba Inicial Streamlit")
    image1 = Image.open('imagenes/txt_to_audio2.png')
    st.image(image1, width=190)
    st.write("En el siguiente enlace probaremos la creación y despliegue básico en Streamlit.") 
    url1 = "https://introca-prueba.streamlit.app/"
    st.write(f"Prueba Streamlit: [Enlace]({url1})")

    # Proyecto 4
    st.subheader("4. Lógica y Complejidad (Big-O)")
    image4 = Image.open('imagenes/OIG5.jpg')
    st.image Christopher = st.image(image4, width=200) if 'image4' in locals() else None
    st.image(image4, width=200)
    st.write("En el siguiente enlace veremos cómo optimizar la complejidad algorítmica y vectorización.") 
    url4 = "https://scriptbig0-9ewesadfzcnjekvdqkduam.streamlit.app/"
    st.write(f"Big-O & Vectorización: [Enlace]({url4})")

    # Proyecto 7
    st.subheader("7. Regresión Lineal")
    image7 = Image.open('imagenes/Chat_pdf.png')
    st.image(image7, width=190)
    st.write("En el siguiente enlace estudiaremos modelos de regresión lineal simple y múltiple.") 
    url7 = "https://appregresion-dpkyxgzgkkuisyvq56kgfx.streamlit.app/"
    st.write(f"Regresión Lineal: [Enlace]({url7})")

    # Proyecto 10
    st.subheader("10. Regresión Logística")
    image10 = Image.open('imagenes/txt_to_audio2.png')
    st.image(image10, width=190)
    st.write("En el siguiente enlace veremos la transición de predecir números a clasificación de clases.") 
    url10 = "https://appregresion-dpkyxgzgkkuisyvq56kgfx.streamlit.app/"
    st.write(f"Regresión Logística: [Enlace]({url10})")


with col2: 
    # Proyecto 2
    st.subheader("2. Clasificación de Frutas")
    image2 = Image.open('imagenes/txt_to_audio.png')
    st.image(image2, width=200)
    st.write("En el siguiente enlace evaluaremos características de frutas y cálculo de distancias.") 
    url2 = "https://clasfruta-yqnz6jhwmu9vgwc7xedzpj.streamlit.app/"
    st.write(f"Clasificación Frutas: [Enlace]({url2})")

    # Proyecto 5
    st.subheader("5. Preparación de Datos")
    image5 = Image.open('imagenes/OIG8.jpg')
    st.image(image5, width=200)
    st.write("En el siguiente enlace veremos manejo de outliers (IQR), escalado y splits de datasets.") 
    url5 = "https://cbynrvaqgzanktxpvnzdrv.streamlit.app/"
    st.write(f"Preparación de Datos: [Enlace]({url5})")

    # Proyecto 8
    st.subheader("8. Series de Tiempo")
    image8 = Image.open('imagenes/OIG4.jpg')
    st.image(image8, width=200)
    st.write("En el siguiente enlace analizaremos tendencia, estacionalidad y modelos ARIMA/SARIMA.") 
    url8 = "https://series-tiempo-imjnyqe8crxw2vjqfznsfr.streamlit.app/"
    st.write(f"Series de Tiempo: [Enlace]({url8})")

    # Proyecto 11
    st.subheader("11. Clasificación KNN")
    image11 = Image.open('imagenes/OIG5.jpg')
    st.image(image11, width=200)
    st.write("Exploración teórica del algoritmo K-Vecinos más Cercanos y fronteras no lineales.") 
    st.caption("Trabajado con archivo HTML local en clase.")


with col3: 
    # Proyecto 3
    st.subheader("3. Descenso de Gradiente")
    image3 = Image.open('imagenes/OIG5.jpg')
    st.image(image3, width=200)
    st.write("En el siguiente enlace exploraremos derivadas y gradientes para búsqueda de mínimos.") 
    url3 = "https://scriptgradiente-nh6bc7quqjqwq8rbyd7fpj.streamlit.app/"
    st.write(f"Descenso Gradiente: [Enlace]({url3})")

    # Proyecto 6
    st.subheader("6. Monitoreo Ambiental (CRISP-DM)")
    image6 = Image.open('imagenes/data_analisis.png')
    st.image(image6, width=190)
    st.write("En el siguiente enlace analizaremos datos de Cornare y el Índice de Calidad de Datos.") 
    url6 = "https://pronosticocornare-s2nrwe4eug8vkt9usekfy9.streamlit.app/"
    st.write(f"Datos Cornare: [Enlace]({url6})")

    # Proyecto 9
    st.subheader("9. Sistema de IoT")
    image9 = Image.open('imagenes/OIG6.jpg')
    st.image(image9, width=200)
    st.write("En el siguiente enlace veremos la captura y procesamiento de datos térmicos con sensores.") 
    url9 = "https://appthermal-n5ju3pkcxb2ckbgkfylkrn.streamlit.app/"
    st.write(f"Captura IoT: [Enlace]({url9})")

    # Proyecto 12
    st.subheader("12. Clasificación Suelos (KNN)")
    image12 = Image.open('imagenes/OIG8.jpg')
    st.image(image12, width=200)
    st.write("En el siguiente enlace estimaremos la fertilidad de suelos utilizando datos de AGROSAVIA.") 
    url12 = "https://suelos-aaanaqm72uokr8cfseyxna.streamlit.app/"
    st.write(f"KNN Suelos: [Enlace]({url12})")
