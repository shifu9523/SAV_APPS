import streamlit as st
 
# ============================================================
# CONFIGURACIÓN DE PÁGINA
# ============================================================
st.set_page_config(
    page_title="Portafolio SAV",       # 👈 CAMBIA: Nombre de tu portafolio
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)
 
# ============================================================
# CSS PERSONALIZADO — aquí vive toda la magia visual
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Sans:wght@300;400;500&display=swap');
 
/* Fondo oscuro general */
.stApp {
    background: #0a0a0f;
    color: #e8e4f0;
}
 
/* Sidebar */
[data-testid="stSidebar"] {
    background: #0f0d1a !important;
    border-right: 1px solid #1e1a30;
}
[data-testid="stSidebar"] * {
    color: #c8c0e8 !important;
}
 
/* Títulos principales */
h1 {
    font-family: 'Syne', sans-serif !important;
    font-size: 2.4rem !important;
    font-weight: 800 !important;
    background: linear-gradient(135deg, #a89cf7, #6c5ce7, #8e7cf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -1px;
}
 
h2, h3 {
    font-family: 'Syne', sans-serif !important;
    color: #d4cef5 !important;
}
 
/* Tarjetas de aplicación */
.app-card {
    background: #12101e;
    border: 1px solid #2a2440;
    border-radius: 16px;
    padding: 1.4rem;
    margin-bottom: 1.2rem;
    transition: border-color 0.3s ease, transform 0.2s ease;
    position: relative;
    overflow: hidden;
}
.app-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, #534AB7, #8e7cf8, #534AB7);
}
.app-card:hover {
    border-color: #534AB7;
    transform: translateY(-3px);
}
.card-title {
    font-family: 'Syne', sans-serif;
    font-size: 1rem;
    font-weight: 700;
    color: #d4cef5;
    margin-bottom: 0.5rem;
}
.card-desc {
    font-size: 0.82rem;
    color: #8a84a8;
    font-weight: 300;
    line-height: 1.6;
    margin-bottom: 0.8rem;
}
.card-link {
    display: inline-block;
    padding: 6px 16px;
    background: #1e1a35;
    border: 1px solid #534AB7;
    border-radius: 20px;
    color: #a89cf7 !important;
    font-size: 0.78rem;
    font-weight: 500;
    text-decoration: none;
    transition: background 0.2s;
}
.card-link:hover {
    background: #534AB7;
    color: #fff !important;
}
 
/* Badge de categoría */
.badge {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 12px;
    font-size: 0.72rem;
    font-weight: 500;
    margin-bottom: 0.6rem;
}
.badge-nlp   { background: #1a1035; color: #a89cf7; border: 1px solid #3d3470; }
.badge-vision{ background: #0f1e1a; color: #5dcaa5; border: 1px solid #1d6e56; }
.badge-audio { background: #1a1020; color: #d4c0f5; border: 1px solid #6a4f9a; }
.badge-data  { background: #1a150f; color: #ef9f27; border: 1px solid #854f0b; }
.badge-iot   { background: #1a0f12; color: #f09595; border: 1px solid #993556; }
 
/* Hero banner */
.hero-banner {
    background: linear-gradient(135deg, #0f0d1a 0%, #1a1035 100%);
    border: 1px solid #2a2440;
    border-radius: 20px;
    padding: 2rem 2.5rem;
    margin-bottom: 2.5rem;
    position: relative;
    overflow: hidden;
}
.hero-banner::after {
    content: '🤖';
    position: absolute;
    right: 2rem; top: 50%;
    transform: translateY(-50%);
    font-size: 5rem;
    opacity: 0.12;
}
.hero-name {
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    color: #f0eeff;
}
.hero-role {
    font-size: 0.95rem;
    color: #7c76a0;
    margin-top: 0.3rem;
    font-weight: 300;
}
.hero-desc {
    font-size: 0.88rem;
    color: #a09ab8;
    margin-top: 0.8rem;
    max-width: 600px;
    line-height: 1.7;
}
.hero-links {
    display: flex;
    gap: 10px;
    margin-top: 1.2rem;
    flex-wrap: wrap;
}
.hero-link {
    padding: 7px 18px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 500;
    text-decoration: none;
    border: 1px solid #3a3060;
    color: #b8b0d8;
    background: #1a1635;
    transition: all 0.2s;
}
.hero-link:hover {
    border-color: #534AB7;
    color: #d4cef5;
}
 
/* Sección título */
.section-label {
    font-size: 0.72rem;
    font-weight: 500;
    letter-spacing: 2px;
    color: #534AB7;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
}
.section-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.3rem;
    font-weight: 700;
    color: #d4cef5;
    margin-bottom: 1.5rem;
}
 
/* Separador */
.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, #2a2440, transparent);
    margin: 2rem 0;
}
</style>
""", unsafe_allow_html=True)
 
 
# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:
    st.markdown("## 🤖 Sobre este portafolio")
    st.markdown("""
    <div style='font-size:0.85rem; color:#9a94b8; line-height:1.7; margin-top:0.5rem;'>
    Portafolio de clase.
    </div>
    """, unsafe_allow_html=True)
 
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.markdown("### 🔗 Recursos")
 
    # 👈 CAMBIA: tu enlace de recursos generales
  
 
 


 
 
# ============================================================
# HERO BANNER
# ============================================================
st.markdown("""
<div class='hero-banner'>
    <div class='hero-name'>Samuel Acevedo V.</div>  <!-- 👈 CAMBIA: tu nombre -->
    <div class='hero-role'>Estudiante de diseño intercativo · Universidad EAFIT</div>  <!-- 👈 CAMBIA: tu rol y universidad -->
    <div class='hero-desc'>
        PORTAFOLIO
    </div>
    <div class='hero-links'>
        <a class='hero-link' href='https://www.linkedin.com/in/samuel-acevedo-velásquez-a5a410335/' target='_blank'>💼 LinkedIn</a>
        <!-- 👆 CAMBIA: tus links reales arriba -->
    </div>
</div>
""", unsafe_allow_html=True)
 
 
# ============================================================
# DATOS DE LAS APPS — EDITA AQUÍ TUS PROYECTOS
# ============================================================
# Estructura: (título, descripción, url, badge_tipo, emoji)
# badge_tipo puede ser: nlp, vision, audio, data, iot
 
apps = [
    {
        "titulo": "Conversión de Texto a Voz",
        "desc": "Transforma cualquier texto en audio natural usando modelos de síntesis de voz de última generación.",
        "url": "https://multisav.streamlit.app",     # 👈 CAMBIA por tu URL real
        "badge": "audio",
        "emoji": "🔊"
    },
    {
        "titulo": "Conoce sobre Waterpolo",
        "desc": "Con esta herramienta puedes aprender lo que quieras de waterpolo",
        "url": "https://chatpdfsav.streamlit.app",    # 👈 CAMBIA por tu URL real
        "badge": "vision",
        "emoji": "👁️"
    },
    {
        "titulo": "Control por voz",
        "desc": "Habla y observa la magia.",
        "url": "https://ctrlvoicesav.streamlit.app",  # 👈 CAMBIA
        "badge": "vision",
        "emoji": "🧠"
    },
    {
        "titulo": "Tablero inteligente",
        "desc": "Dibuja y analiza tu imagen.",
        "url": "https://drawrecogsav.streamlit.app",   # 👈 CAMBIA
        "badge": "audio",
        "emoji": "🎙️"
    },
    {
        "titulo": "Recocnocimiento de digitos escritos a mano",
        "desc": "Dibuja tus digitos y deja que la palicación los identifique.",
        "url": "https://handwsav.streamlit.app",   # 👈 CAMBIA
        "badge": "data",
        "emoji": "📊"
    },
    {
        "titulo": "Mi primera APP",
        "desc": "Explórala",
        "url": "https://introsamu.streamlit.app",  # 👈 CAMBIA
        "badge": "audio",
        "emoji": "🎬"
    },
    {
        "titulo": "APP de presentación",
        "desc": "Mi pagina de presentación",
        "url": "https://introsav.streamlit.app",   # 👈 CAMBIA
        "badge": "nlp",
        "emoji": "📄"
    },
    {
        "titulo": "Reconocimiento óptico de caracteres",
        "desc": "escucha los textos tus imagenes en tiempo real",
        "url": "https://ocr-audiosav.streamlit.app",  # 👈 CAMBIA
        "badge": "vision",
        "emoji": "🖼️"
    },
    {
        "titulo": "Reconocimiento óptico de caracteres 2",
        "desc": "Reconoce tus fotos desde tu cámara",
        "url": "https://ocrsav.streamlit.app",  # 👈 CAMBIA por URL correcta
        "badge": "iot",
        "emoji": "⚙️"
    },

    {
        "titulo": "Lector sensor MQTT",
        "desc": "MQTT",
        "url": "https://recepmqttshifu.streamlit.app",  # 👈 CAMBIA por URL correcta
        "badge": "iot",
        "emoji": "⚙️"
    },

    {
        "titulo": "Analisis de sentimientos",
        "desc": "Analiza tus sentimientos con un texto",
        "url": "https://sentimentanuel.streamlit.app",  # 👈 CAMBIA por URL correcta
        "badge": "iot",
        "emoji": "⚙️"
    },

    {
        "titulo": "Reconocimiento de imágenes",
        "desc": "Reconoce si samu está o no en tus fotos",
        "url": "https://tm95nvds.streamlit.app",  # 👈 CAMBIA por URL correcta
        "badge": "iot",
        "emoji": "⚙️"
    },

    {
        "titulo": "Traductor",
        "desc": "Escucho lo que quieres traducir.",
        "url": "https://visionappsav.streamlit.app",  # 👈 CAMBIA por URL correcta
        "badge": "iot",
        "emoji": "⚙️"
    },

    {
        "titulo": "WordCloud Studio",
        "desc": "Haz tus nubes de palabras",
        "url": "https://wordcloudsav.streamlit.app",  # 👈 CAMBIA por URL correcta
        "badge": "iot",
        "emoji": "⚙️"
    },

    {
        "titulo": "Analisis de imagen",
        "desc": "Clave KPI",
        "url": "https://traductordim.streamlit.app",  # 👈 CAMBIA por URL correcta
        "badge": "iot",
        "emoji": "⚙️"
    },

    {
        "titulo": "Detección de objetos",
        "desc": "Detecta objetos en tus imágenes",
        "url": "https://yolov5aa.streamlit.app",  # 👈 CAMBIA por URL correcta
        "badge": "iot",
        "emoji": "⚙️"
    },
]
 
badge_labels = {
    "nlp":    ("badge-nlp",    "NLP"),
    "vision": ("badge-vision", "Visión"),
    "audio":  ("badge-audio",  "Audio"),
    "data":   ("badge-data",   "Datos"),
    "iot":    ("badge-iot",    "IoT"),
}
 
 
# ============================================================
# GRILLA DE TARJETAS — 3 columnas
# ============================================================
st.markdown("<div class='section-label'>Proyectos</div>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>Aplicaciones de IA</div>", unsafe_allow_html=True)
 
cols = st.columns(3)
 
for i, app in enumerate(apps):
    badge_class, badge_text = badge_labels[app["badge"]]
    with cols[i % 3]:
        st.markdown(f"""
        <div class='app-card'>
            <div class='badge {badge_class}'>{badge_text}</div>
            <div class='card-title'>{app['emoji']} {app['titulo']}</div>
            <div class='card-desc'>{app['desc']}</div>
            <a class='card-link' href='{app['url']}' target='_blank'>Abrir app →</a>
        </div>
        """, unsafe_allow_html=True)
 
 
# ============================================================
# FOOTER
# ============================================================
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align:center; font-size:0.78rem; color:#4a4468; padding: 1rem 0;'>
    Hecho con 🤖 + Python · Streamlit · 2025 &nbsp;·&nbsp;
    <!-- 👈 CAMBIA: pon tu nombre abajo -->
    <span style='color:#534AB7;'>Tu Nombre</span>
</div>
""", unsafe_allow_html=True)

