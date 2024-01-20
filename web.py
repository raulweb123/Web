
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import base64



st.set_page_config(
    page_title="Ropa y calzado",
    layout="wide"
)

path_css="C:/Users/Raúl/Desktop/Web Raul/style_sheet.css"
def load_css(path_css):
    with open(path_css) as f: 
        return st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
load_css(path_css)

selected = option_menu(
    menu_title=None,  # required
    options=["Cazadoras y abrigos","Camisetas", "Deportes","Pantalones", "Calzado"],  # Dropdown menu
    icons=[None],  # Icons for dropdown menu
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="horizontal",
    styles={
        "container": {"padding": "0px!important", "background-color": "#72e9f2"},
        "icon": {"color": "white", "font-size": "17px"},
        "nav-link": {
            "font-size": "17px",
            "text-align": "center",
            "font-weight": "bold",
            "color":"black",
            "margin": "20px",
            "--hover-color": "#72e9f2",
            "background-color": "#72e9f2"
            },
        "nav-link-selected": {"background-color": "#e8b20e"},
        })

path_principal="C:/Users/Raúl/Desktop/Web Raul/Productos/"

if selected=="Cazadoras y abrigos":
    st.header("Cazadoras y abrigos")
    # st.slider("Precio del producto:", 0, 100, step=2)
    path_producto="Cazadoras y Abrigos/"
    left, center, right = st.columns((1,1,1))
    with left:
        st.write("***Cazadora de cuero***")
        with open(path_principal + path_producto + "/Cazadora/Cazadora1.jpg", "rb") as f:
            data_uri = base64.b64encode(f.read()).decode("utf-8")
            markdown = f"""
            <div class="image">
            <img src="data:image/png;base64, {data_uri}" alt="image" width="200" height="300"/>
            </div>
            """
            st.markdown(markdown, unsafe_allow_html=True)
            st.write("199,99€")
            def html_ref():
                href=f"""<a href="C:/Users/Raúl/Desktop/Web Raul/Productos/Cazadoras y Abrigos/Cazadora/Producto1.html"><button>INFO</button></a>"""
                return(href)
            st.link_button("Info","www.google.es")
            st.button("INFO", type="primary")
            if st.button("show info"):
                st.write(f"""
                                    <body>
                                        <div class="dot dot1"> </div>
                                        <div class="dot dot2"> </div>
                                        <div class="dot dot3"> </div>
                                    </body>
                                    <head>
                                        <meta charset="UTF-8">
                                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                        <link rel="stylesheet" href="C:/Users/Raúl/Desktop/Web Raul/style_sheet.css">
                                    </head>
                                    <title>CAZADORA PIEL CUELLO COMBINADO</title>
                                    <h1>CAZADORA PIEL CUELLO COMBINADO</h1>
                                    <img src="C:/Users/Raúl/Desktop/Web Raul/Productos/Cazadoras y Abrigos/Cazadora/Cazadora1.jpg" alt="Foto cazadora" width="200" height="300">
                                    <img src="C:/Users/Raúl/Desktop/Web Raul/Productos/Cazadoras y Abrigos/Cazadora/Cazadora2.jpg" alt="Foto Cazadora2" width="200" height="300">
                                    <p class="Precio">199,00 EUR</p>
                                    <h2>COMPOSICIÓN</h2>
                                    <p>Trabajamos con programas de seguimiento para garantizar el cumplimiento de nuestros estándares sociales, 
                                        medioambientales y de seguridad y salud de nuestros productos. Para evaluar su cumplimiento hemos desarrollado un 
                                        programa de auditorías y planes de mejora continua.
                                        <div><strong>EXTERIOR CUELLO</strong></div>
                                        <ul>
                                            <li>100% piel con pelo de cordero</li>
                                        </ul>
                                        <div><strong>MATERIAL PRINCIPAL</strong></div>
                                        <ul>
                                            <li>100% piel de cordero</li>
                                        </ul>
                                        <div><strong>FORRO</strong></div>
                                        <ul>
                                            <li>100% poliéster</li>
                                        </ul>
                                    </p>
                                        <h2>CUIDADOS</h2>
                                        <p>Cuidar de tus prendas es cuidar del medioambiente. Para mantener limpias tus chaquetas y abrigos sólo tienes que ventilarlas
                                            y pasarles un paño o un cepillo para la ropa. Si la limpieza en seco es necesaria intenta buscar tintorerías que utilicen 
                                            tecnologías respetuosas con el medioambiente.
                                        <div>
                                            <figure>
                                                <figcaption>
                                                <img src="https://static.zara.net/photos///contents/cm/product-cares-9-icon_0.svg?ts=1604343299129" alt="No lavar"> 
                                                No lavar</figcaption>
                                            </figure>
                                        </div>  
                                        <div>
                                            <figure>
                                                <figcaption>
                                                <img src="https://static.zara.net/photos///contents/cm/product-cares-14-icon_0.svg?ts=1604343289322" width="32" height="32" alt="No lavar">
                                                No usar lejia o blanqueador</figcaption>
                                            </figure>
                                        </div>  
                                        <div>
                                            <figure>
                                                <figcaption>
                                                <img src="https://static.zara.net/photos///contents/cm/product-cares-19-icon_0.svg?ts=1604343282915" width="32" height="32" alt="No lavar"> 
                                                No planchar</figcaption>
                                            </figure>
                                        </div>  
                                        <figure>
                                            <figcaption>
                                            <img src="https://static.zara.net/photos///contents/cm/product-cares-28-icon_0.svg?ts=1604343290530" width="32" height="32" alt="No lavar"> 
                                            No limpieza en seco</figcaption>
                                        </figure>
                                    </div>
                                    </div>  
                                    <figure>
                                        <figcaption>
                                            <img src="https://static.zara.net/photos///contents/cm/product-cares-35-icon_0.svg?ts=1604343281266" width="32" height="32" alt="No lavar"> 
                                        No usar secadora</figcaption>
                                    </figure>
                                    </div>  
                                        </p>
                                </html>""", unsafe_allow_html=True)
            else:
                st.write("")
                
    with center:
        st.write("***Abrigo de paño***")
        with open("C:/Users/Raúl/Desktop/Web Raul/Productos/Cazadoras y Abrigos/Abrigo/abrigo1.jpg", "rb") as f:
            data_uri = base64.b64encode(f.read()).decode("utf-8")
            markdown = f"""
            <div class="image">
            <img src="data:image/png;base64, {data_uri}" alt="image" width="200" height="300"/>
            </div>
            """
            st.markdown(markdown, unsafe_allow_html=True)
            st.write("199,99€")
    with right:
        st.write("Imagen3")
        with open("Ropa_ejemplo.jfif", "rb") as f:
            data_uri = base64.b64encode(f.read()).decode("utf-8")
            markdown = f"""
            <div class="image">
            <img src="data:image/png;base64, {data_uri}" alt="image" width="200" height="300"/>
            </div>
            """
            
            st.markdown(markdown, unsafe_allow_html=True)
if selected=="Deportes":
    st.header("Deportes")
    path_producto="Deportes/"
    left, center, right = st.columns((1,1,1))
    with left:
        st.write("***Camiseta de Baloncesto Ja Morant***")
        with open(path_principal + path_producto + "Camiseta ja Morant/Camiseta1.jpg", "rb") as f:
            data_uri = base64.b64encode(f.read()).decode("utf-8")
            markdown = f"""
            <div class="image">
            <img src="data:image/png;base64, {data_uri}" alt="image" width="250" height="250"/>
            </div>
            """
            st.markdown(markdown, unsafe_allow_html=True)
            st.write("99,99€")
    with center:
        st.write("Imagen2")
        with open("Ropa_ejemplo.jfif", "rb") as f:
            data_uri = base64.b64encode(f.read()).decode("utf-8")
            markdown = f"""
            <div class="image">
            <img src="data:image/png;base64, {data_uri}" alt="image" />
            </div>
            """
            st.markdown(markdown, unsafe_allow_html=True)
    with right:
        st.write("Imagen3")
        with open("Ropa_ejemplo.jfif", "rb") as f:
            data_uri = base64.b64encode(f.read()).decode("utf-8")
            markdown = f"""
            <div class="image">
            <img src="data:image/png;base64, {data_uri}" alt="image" />
            </div>
            """
            st.markdown(markdown, unsafe_allow_html=True)

if selected=="Pantalones":
    st.header("Pantalones")
    left, center, right = st.columns((1,1,1))
    with left:
        st.write("Imagen1")
        with open("Ropa_ejemplo.jfif", "rb") as f:
            data_uri = base64.b64encode(f.read()).decode("utf-8")
            markdown = f"""
            <div class="image">
            <img src="data:image/png;base64, {data_uri}" alt="image" />
            </div>
            """
            st.markdown(markdown, unsafe_allow_html=True)
    with center:
        st.write("Imagen2")
        with open("Ropa_ejemplo.jfif", "rb") as f:
            data_uri = base64.b64encode(f.read()).decode("utf-8")
            markdown = f"""
            <div class="image">
            <img src="data:image/png;base64, {data_uri}" alt="image" />
            </div>
            """
            st.markdown(markdown, unsafe_allow_html=True)
    with right:
        st.write("Imagen3")
        with open("Ropa_ejemplo.jfif", "rb") as f:
            data_uri = base64.b64encode(f.read()).decode("utf-8")
            markdown = f"""
            <div class="image">
            <img src="data:image/png;base64, {data_uri}" alt="image" />
            </div>
            """
            st.markdown(markdown, unsafe_allow_html=True)
if selected=="Calzado":
    st.header("Calzado")
    left, center, right = st.columns((1,1,1))
    with left:
        st.write("Imagen1")
        with open("Ropa_ejemplo.jfif", "rb") as f:
            data_uri = base64.b64encode(f.read()).decode("utf-8")
            markdown = f"""
            <div class="image">
            <img src="data:image/png;base64, {data_uri}" alt="image" />
            </div>
            """
            st.markdown(markdown, unsafe_allow_html=True)
    with center:
        st.write("Imagen2")
        with open("Ropa_ejemplo.jfif", "rb") as f:
            data_uri = base64.b64encode(f.read()).decode("utf-8")
            markdown = f"""
            <div class="image">
            <img src="data:image/png;base64, {data_uri}" alt="image" />
            </div>
            """
            st.markdown(markdown, unsafe_allow_html=True)
    with right:
        st.write("Imagen3")
        with open("Ropa_ejemplo.jfif", "rb") as f:
            data_uri = base64.b64encode(f.read()).decode("utf-8")
            markdown = f"""
            <div class="image">
            <img src="data:image/png;base64, {data_uri}" alt="image" />
            </div>
            """
            st.markdown(markdown, unsafe_allow_html=True)
