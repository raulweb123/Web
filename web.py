
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import base64



st.set_page_config(
    page_title="Ropa y calzado",
    layout="wide"
)

path_css="style_sheet.css"
def load_css(path_css):
    with open(path_css) as f: 
        return st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
load_css(path_css)


def btn_b_callback():
    st.session_state.display_result=False
    st.session_state.reset=False


def display_image(path_principal, path_producto, path_final):
    with open(path_principal + path_producto + path_final, "rb") as f:
        data_uri = base64.b64encode(f.read()).decode("utf-8")
        markdown = f"""
        <div class="image">
        <img src="data:image/png;base64, {data_uri}" alt="image" width="200" height="300"/>
        </div>
        """
        return(st.markdown(markdown, unsafe_allow_html=True))


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



path_principal="Productos/"

if selected=="Cazadoras y abrigos":
    st.header("Cazadoras y abrigos")
    # st.slider("Precio del producto:", 0, 100, step=2)
    path_producto="Cazadoras y Abrigos/"
    left, center, right = st.columns((1,1,1))
    with left:
        st.write("***Cazadora de cuero***")
        display_image(path_principal, path_producto, "/Cazadora/Cazadora1.jpg")
        st.write("199,99€")
        def html_ref():
            href=f"""<a href="Productos/Cazadoras y Abrigos/Cazadora/Producto1.html"><button>INFO</button></a>"""
            return(href)
        mas_info_cazadora = st.button('Más información', key=1)
        if mas_info_cazadora:
            st.write(f"""
                                <title>CAZADORA PIEL CUELLO COMBINADO</title>
                                <h1>CAZADORA PIEL CUELLO COMBINADO</h1>""", unsafe_allow_html=True)
            display_image(path_principal, path_producto, "/Cazadora/Cazadora1.jpg")
            st.write("")
            display_image(path_principal, path_producto, "/Cazadora/Cazadora2.jpg")
            st.write("""<p class="Precio">199,00 EUR</p>
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
            menos_info_cazadora = st.button("Menos información",key=2, on_click=btn_b_callback)
                    
        with center:
            st.write("***Abrigo de paño***")
            display_image(path_principal, path_producto, "Abrigo/abrigo1.jpg")
            st.write("199,99€")
            if 'display_result' not in st.session_state:
                st.session_state.display_result = False
            if 'reset' not in st.session_state:
                st.session_state.reset = False

            mas_info = st.button('Más información', key=3)
            if mas_info:
                st.write(f"""
                            <title>Abrigo de paño</title>
                            <h1>Abrigo de paño con cuello solapas y manga larga</h1>
                            <h2>Cierre botonadura frontal. Bolsillos delanteros.</h2>""", unsafe_allow_html=True)
                display_image(path_principal, path_producto, "Abrigo/abrigo1.jpg")
                st.write(f"""
                            <p class="Precio">29,99 EUR</p>
                            <h2>COMPOSICIÓN</h2>
                            <p>Trabajamos con programas de seguimiento para garantizar el cumplimiento de nuestros estándares sociales, 
                                medioambientales y de seguridad y salud de nuestros productos. Para evaluar su cumplimiento hemos desarrollado un 
                                programa de auditorías y planes de mejora continua.
                                <ul>
                                    <li>100% poliéster</li>
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
                menos_info = st.button("Menos información", key=4, on_click=btn_b_callback)
    with right:
        st.write("Imagen3")
        display_image("", "", "Ropa_ejemplo.jfif")

if selected=="Deportes":
    st.header("Deportes")
    path_producto="Deportes/"
    left, center, right = st.columns((1,1,1))
    with left:
        st.write("***Camiseta de Baloncesto Ja Morant***")
        display_image(path_principal, path_producto, "Camiseta Ja morant/Camiseta1.jpg")
        st.write("99,99€")
    with center:
        st.write("Imagen2")
        display_image("", "", "Ropa_ejemplo.jfif")
    with right:
        st.write("Imagen3")
        display_image("", "", "Ropa_ejemplo.jfif")

if selected=="Pantalones":
    st.header("Pantalones")
    left, center, right = st.columns((1,1,1))
    with left:
        st.write("Imagen1")
        display_image("", "", "Ropa_ejemplo.jfif")
    with center:
        st.write("Imagen2")
        display_image("", "", "Ropa_ejemplo.jfif")
    with right:
        st.write("Imagen3")
        display_image("", "", "Ropa_ejemplo.jfif")
if selected=="Calzado":
    path_producto="Calzado/"
    st.header("Calzado")
    left, center, right = st.columns((1,1,1))
    with left:
        st.write("Retro 4 Bred")
        display_image(path_principal, path_producto, "retro 4 red bred/retro4.jpg")
        st.write("500€") 
        mas_info=st.button("Mas información", key=12)
        if mas_info: 
        
            st.write(f"""
                        <title>Camiseta "Jordan Retro4 Bred"<em><strong>3 en stock<strong/></em></title>""", unsafe_allow_html=True)
            display_image(path_principal, path_producto, "retro 4 red bred/retro4.jpg")
            st.write(f"""<h2>CUIDADOS</h2>
                        <p>Lavar unicamente con productos especializados para calzado
                        <div>""", unsafe_allow_html=True)
            menos_info = st.button("Menos información", key=8, on_click=btn_b_callback)
    with center:
        st.write("Imagen2")
        display_image("", "", "Ropa_ejemplo.jfif")
    with right:
        st.write("Imagen3")
        display_image("", "", "Ropa_ejemplo.jfif")
if selected=="Camisetas":
    path_producto="Camisetas/"
    st.header("Camisetas")
    left, center, right = st.columns((1,1,1))
    with left:
        st.write(f"""<p><strong>Camiseta "OFF White"<strong/></p>
                 <p><em><strong>Exclusiva<strong/></em></p>""", unsafe_allow_html=True)
        display_image(path_principal, path_producto, "Camiseta1/camiseta1.jpg")
        st.write("300€") 
        mas_info=st.button("Mas información", key=6)
        if mas_info: 
        
            st.write(f"""
                        <title>Camiseta "OFF white"<em><strong>Exclusiva<strong/></em></title>""", unsafe_allow_html=True)
            display_image(path_principal, path_producto, "Camiseta1/camiseta.jpg")
            st.write(f"""<h2>COMPOSICIÓN</h2>
                        <p> Camiseta Big Bookish Skate Negro y blanco, algodón, estampado del logo en la parte delantera, cuello redondo y manga corta.</p>
                        <ul>
                        <li>Algodón 100%</li>
                        <h2>CUIDADOS</h2>
                        <p>Lavar en lavadora
                        <div>""", unsafe_allow_html=True)
            menos_info = st.button("Menos información", key=4, on_click=btn_b_callback)
    with center:
        st.write("Imagen2")
        display_image("", "", "Ropa_ejemplo.jfif")
          
    with right:
        st.write("Imagen3")
        display_image("", "", "Ropa_ejemplo.jfif")