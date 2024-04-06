
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import base64
# from streamlit_gsheets import GSheetsConnection
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader


st.set_page_config(
    page_title="Ropa y calzado",
    layout="wide"
)

with open('credentials.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
)


# ocultar_registro = st.button("Volver a iniciar sesión",key=2, on_click=btn_b_callback)

authenticator.login(fields={"Form name":"Iniciar sesion", "Username":"Nombre de usuario", "Password":"Contraseña", "Login":"Iniciar sesión"})
if st.session_state["authentication_status"]:
    left, center, right =st.columns((2,2,1))
    with right:
        authenticator.logout("Cerrar sesión")
        st.write("")
    path_css="style_sheet.css"
    def load_css(path_css):
        with open(path_css) as f: 
            return st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
    load_css(path_css)

    def btn_b_callback():
        st.session_state.display_result=False
        st.session_state.reset=False
    precios = pd.read_excel("Productos.xlsx", sheet_name="Precios")



    def display_image(path_principal, path_producto, path_final):
        with open(path_principal + path_producto + path_final, "rb") as f:
            data_uri = base64.b64encode(f.read()).decode("utf-8")
            markdown = f"""
            <div class="image">
            <img src="data:image/png;base64, {data_uri}" alt="image" width="200" height="300"/>
            </div>
            """
            return(st.markdown(markdown, unsafe_allow_html=True))

    # url = "https://docs.google.com/spreadsheets/u/1/d/1l2mDj4D8EYfOBfGef99IE3t7DPiy3QIlm8ne9KVn-tE/edit?usp=drive_open&ouid=109996259176322594398"

    # conn = st.experimental_connection("gsheets", type=GSheetsConnection)

    # data = conn.read(spreadsheet=url, usecols=list(range(2)), ttl=5)
    # st.dataframe(data)



    selected = option_menu(
        menu_title=None,  # required
        options=["Cazadoras y abrigos","Camisetas", "Deportes","Pantalones", "Calzado"],  # Dropdown menu
        icons=[None],  # Icons for dropdown menu
        menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal",
        styles={
            "container": {"padding": "0px!important", "background-color": "#fff0e0"},
            "icon": {"color": "#afad9f", "font-size": "17px"},
            "nav-link": {
                "font-size": "17px",
                "text-align": "center",
                "font-weight": "bold",
                "color":"black",
                "margin": "0px",
                "--hover-color": "#fff0e0",
                "background-color": "#fff0e0"
                },
            "nav-link-selected": {"background-color": "#afad9f"},
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
            # buy_button = st.button('Añadir al carrito', key=0.1)
            # if buy_button:

            mas_info_cazadora = st.button('Más información', key=1)
            if mas_info_cazadora:
                st.write(f"""
                                    <title>{"Cazadora de cuero"}</title>
                                    <h1>CAZADORA PIEL CUELLO COMBINADO</h1>""", unsafe_allow_html=True)
                display_image(path_principal, path_producto, "/Cazadora/Cazadora1.jpg")
                st.write("")
                display_image(path_principal, path_producto, "/Cazadora/Cazadora2.jpg")
                st.write(f"""<p class="Precio">{precios[precios["producto"]=="Cazadora de cuero"]["Precio"].values[0]}€</p>
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
                st.write(f"""{precios[precios["producto"]=="Abrigo de paño"]["Precio"].values[0]}€""")
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
                                <p class="Precio">{precios[precios["producto"]=="Abrigo de paño"]["Precio"].values[0]}€</p>
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
            st.write(f"""{precios[precios["producto"]=="Camiseta de Baloncesto Ja Morant"]["Precio"].values[0]}€""")
            if 'display_result' not in st.session_state:
                    st.session_state.display_result = False
            if 'reset' not in st.session_state:
                st.session_state.reset = False

            mas_info = st.button('Más información', key=3)
            if mas_info:
                st.write(f"""
                            <title>Camiseta de Baloncesto Ja Morant</title>
                            <h1>Camiseta Ja morant edicion jugador</h1>""", unsafe_allow_html=True)
                
                display_image(path_principal, path_producto, "Camiseta Ja morant/camiseta1.jpg")
                st.write(f"""
                            <p class="Precio">{precios[precios["producto"]=="Camiseta de Baloncesto Ja Morant"]["Precio"].values[0]}€</p>
                        </html>""", unsafe_allow_html=True)
                menos_info = st.button("Menos información", key=4, on_click=btn_b_callback)
        with center:
            st.write("Imagen2")
            display_image("", "", "Ropa_ejemplo.jfif")
        with right:
            st.write("Imagen3")
            display_image("", "", "Ropa_ejemplo.jfif")

    if selected=="Pantalones":
        st.header("Pantalones")
        path_producto="pantalones/"
        left, center, right = st.columns((1,1,1))
        with left:
            st.write("Nike x Off-White")
            st.write(f"""{precios[precios["producto"]=="Nike x Off-White"]["Precio"].values[0]}€""")
            display_image(path_principal, path_producto, "Nike/nike1.png")
            if 'display_result' not in st.session_state:
                    st.session_state.display_result = False
            if 'reset' not in st.session_state:
                st.session_state.reset = False

            mas_info = st.button('Más información', key=3)
            if mas_info:
                st.write(f"""
                            <title>Nike x Off-White</title>
                            <h1>Nike x Off-White Coleccion partes de abajo</h1>
                            <p>Este pantalón amplio e impecable de tejido Woven repelente al agua está diseñado para hacer frente al mal tiempo y ofrece mucho espacio 
                        para moverte libremente. La cintura elástica con el logotipo Off-White™ mantiene los pantalones en su sitio. 
                        Además, los cordones regulables de la rodilla y el dobladillo te permiten cambiar el ajuste alrededor de las zapatillas.</p>""", unsafe_allow_html=True)
                display_image(path_principal, path_producto, "Nike/nike2.png")
                st.write(f"""
                            <p class="Precio">{precios[precios["producto"]=="Nike x Off-White"]["Precio"].values[0]}€</p>
                        </html>""", unsafe_allow_html=True)
                menos_info = st.button("Menos información", key=4, on_click=btn_b_callback)
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
            st.write(f"""{precios[precios["producto"]=="Retro 4 Bred"]["Precio"].values[0]}€""")
            mas_info=st.button("Mas información", key=12)
            if mas_info: 
            
                st.write(f"""
                            <title>"Jordan Retro4 Bred"<em><strong>3 en stock<strong/></em></title>""", unsafe_allow_html=True)
                display_image(path_principal, path_producto, "retro 4 red bred/retro4.jpg")
                st.write(f"""<p>{precios[precios["producto"]=="Retro 4 Bred"]["Precio"].values[0]}€</p>
                        <h2>CUIDADOS</h2>
                            <p>Lavar unicamente con productos especializados para calzado</p>""", unsafe_allow_html=True)
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
            st.write(f"""{precios[precios["producto"]=='Camiseta "OFF White"']["Precio"].values[0]}€""")
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
elif st.session_state["authentication_status"] is False:
    st.error('Usuario o contraseña incorrecta')
    if authenticator.reset_password(st.session_state["username"]):
        st.success('Contraseña modificada correctamente')


elif st.session_state["authentication_status"] is None:
    st.warning('Porfavor, entra tu usuario y contraseña')
    try:
        email_n, email_n2, name_n = authenticator.register_user(preauthorization=False, fields={"Form name":"Registrate", "Repeat password":"Repetir contraseña", "Password":"Contraseña", "Name":"Nombre y Apellidos","Email":"Email","Username":"Usuario", "Register":"Crear cuenta"})
        if email_n:
            with open("credentials.yaml", "w") as file:
                yaml.dump(config, file, default_flow_style=False)
            st.success("Usuario registrado correctamente")
    except Exception as e:
        st.error(e)
