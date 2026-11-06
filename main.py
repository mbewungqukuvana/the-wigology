
import streamlit as st
import bcrypt
import hmac


st.set_page_config(
    page_title="The Wigology",
    page_icon="✨",
    layout="wide"
)


st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Bodoni+Moda:wght@400;500&family=Tenor+Sans&family=Manrope:wght@400;500;600&display=swap');




[data-testid="stSidebar"], [data-testid="stSidebar"] > div,
[data-testid="stSidebarContent"], [data-testid="stSidebarUserContent"] {
 background:#FFFFFF!important; color:#26211D!important;
}
[data-testid="stSidebar"] *, [data-testid="stSidebar"] label,
[data-testid="stSidebar"] p, [data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2 {color:#26211D!important;}
[data-testid="stSidebar"] [data-testid="stRadio"] label,
[data-testid="stSidebar"] [role="radiogroup"] label {
 background:#FFFEFC!important; border:1px solid #DED4CA!important;
 padding:.75rem .8rem!important; border-radius:2px!important; margin:.35rem 0!important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked),
[data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {
 background:#EDE5DC!important; border-color:#9B8773!important;
}
[data-testid="stSidebar"] input[type="radio"] {accent-color:#8A7662!important;}
[data-testid="stSidebar"] [data-testid="stBaseButton-secondary"] {
 background:#FFFEFC!important; border:1px solid #BFB0A1!important;
 color:#29231F!important; border-radius:2px!important;
}
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] a {color:#6F5F50!important;}
@keyframes wigology-dashboard-reveal {
 from {opacity:0;transform:translateY(16px)}
 to {opacity:1;transform:translateY(0)}
}
.wigology-dashboard-welcome {animation:wigology-dashboard-reveal 1.65s ease-out both;}



[data-testid="stSidebar"],
[data-testid="stSidebar"] > div,
[data-testid="stSidebarContent"],
[data-testid="stSidebarUserContent"] { background: #FFFFFF !important; }
[data-testid="stSidebar"] [data-testid="stTextInput"] input,
[data-testid="stSidebar"] [data-baseweb="input"] input,
[data-testid="stSidebar"] [data-baseweb="input"] > div,
[data-testid="stSidebar"] [data-testid="stSelectbox"] [data-baseweb="select"] > div {
    background: #FFFFFF !important;
    color: #201B18 !important;
    -webkit-text-fill-color: #201B18 !important;
    border-color: #D7C9BA !important;
}
[data-testid="stSidebar"] input::placeholder { color: #84796E !important; -webkit-text-fill-color: #84796E !important; }
[data-testid="stSidebar"] [data-testid="stSelectbox"] *,
[data-testid="stSidebar"] [data-testid="stTextInput"] label { color: #201B18 !important; }
[data-testid="stSidebar"] [data-testid="stSelectbox"] svg { fill: #201B18 !important; }
[data-testid="stSidebar"] [data-testid="stForm"] { background: #FFFFFF !important; border-color: #E4DAD0 !important; }


[data-testid="stSidebar"] [data-testid="stTextInput"] div[data-baseweb="input"],
[data-testid="stSidebar"] [data-testid="stTextInput"] div[data-baseweb="input"] > div,
[data-testid="stSidebar"] [data-testid="stTextInput"] input,
[data-testid="stSidebar"] [data-testid="stSelectbox"] div[data-baseweb="select"] > div,
[data-testid="stSidebar"] [data-testid="stSelectbox"] div[data-baseweb="select"] input {
 background-color:#FFFFFF !important; background:#FFFFFF !important;
 color:#201B18 !important; -webkit-text-fill-color:#201B18 !important;
 border-color:#D7C9BA !important; box-shadow:none !important;
}
[data-testid="stSidebar"] [data-testid="stSelectbox"] div[data-baseweb="select"] span,
[data-testid="stSidebar"] [data-testid="stSelectbox"] div[data-baseweb="select"] [data-testid="stMarkdownContainer"] {
 color:#201B18 !important; -webkit-text-fill-color:#201B18 !important;
}
[data-testid="stSidebar"] [data-testid="stSelectbox"] svg { fill:#7C6A59 !important; color:#7C6A59 !important; }

body [data-baseweb="popover"] [data-baseweb="menu"],
body [data-baseweb="popover"] [role="listbox"],
body [data-baseweb="popover"] [role="option"],
body [data-baseweb="popover"] li,
body [data-baseweb="menu"] {
 background:#FFFFFF !important; color:#201B18 !important;
}
body [data-baseweb="popover"] [role="option"]:hover,
body [data-baseweb="popover"] [aria-selected="true"] {
 background:#F3EEE8 !important; color:#201B18 !important;
}
body [data-baseweb="popover"] span,
body [data-baseweb="popover"] div { color:#201B18 !important; }
[data-testid="stSidebar"] [data-testid="stFormSubmitButton"] button {
 background:#FFFFFF !important; color:#201B18 !important;
 border:1px solid #BEB5AB !important; border-radius:2px !important;
}
[data-testid="stSidebar"] [data-testid="stFormSubmitButton"] button:hover {
 background:#F3EEE8 !important; color:#201B18 !important;
}




[data-testid="stMainBlockContainer"] {
    padding-top: 2rem !important;
    max-width: 1250px;
}





[data-testid="stApp"],
[data-testid="stMain"],
[data-testid="stMainBlockContainer"] {
    background-color: #FFFFFF !important;
    color: #111111 !important;
}


[data-testid="stMain"] h1,
[data-testid="stMain"] h2,
[data-testid="stMain"] h3,
[data-testid="stMain"] p,
[data-testid="stMain"] [data-testid="stCaptionContainer"] {
    color: #111111 !important;
}


.wigology-collection-heading h2,
.wigology-collection-heading p {
    color: #111111 !important;
}


[data-testid="stMain"] .stButton button {
    background-color: #FFFFFF !important;
    color: #111111 !important;
    border: 1px solid #111111 !important;
    border-radius: 0 !important;
}


[data-testid="stMain"] .stButton button:hover {
    background-color: #111111 !important;
    color: #FFFFFF !important;
    border-color: #111111 !important;
}


.wigology-hero-start {
    height: 12vh;
}


.wigology-section-space {
    height: 20vh;
}


.wigology-collection-heading {
    text-align: center;
    margin-bottom: 3rem;
}

.wigology-collection-heading h2 {
    font-family: 'Tenor Sans', sans-serif;
    font-weight: 400;
    font-size: clamp(2rem, 4vw, 3.5rem);
    margin-bottom: 1rem;
}

.wigology-collection-heading p {
    font-family: 'Manrope', sans-serif;
    font-size: 1rem;
    line-height: 1.7;
}


[data-testid="stMain"] h1 {
    font-size: clamp(2.5rem, 4vw, 4rem) !important;
    line-height: 1.2 !important;
}


[data-testid="stMain"] .stButton button {
    min-height: 3.4rem;
    border-radius: 0 !important;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}


@media (max-width: 768px) {
    .wigology-hero-start {
        height: 5vh;
    }

    .wigology-section-space {
        height: 10vh;
    }
}


[data-testid="stMainBlockContainer"] {
    padding-top: 1.5rem !important;
}


[data-testid="stMain"] h1 {
    margin-bottom: 0.8rem !important;
}





[data-testid="stMainBlockContainer"] {
    padding-top: 2rem !important;
    max-width: 1250px;
}


[data-testid="stMain"] h1 {
    font-size: clamp(2.8rem, 5vw, 5rem) !important;
    line-height: 1.15 !important;
    letter-spacing: 0.02em;
}


[data-testid="stMain"] h2 {
    font-size: 2.5rem !important;
    font-weight: 400 !important;
}


[data-testid="stMain"] .stButton button {
    min-height: 3.4rem;
    border-radius: 0 !important;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}


[data-testid="stMain"] [data-testid="stImage"] img {
    display: block;
    width: 100%;
}


html, body,
[data-testid="stApp"],
[data-testid="stApp"] p,
[data-testid="stApp"] label,
[data-testid="stApp"] button,
[data-testid="stApp"] input,
[data-testid="stApp"] textarea,
[data-testid="stApp"] select {
    font-family: 'Tenor Sans', sans-serif !important;
}


[data-testid="stApp"] h1,
[data-testid="stApp"] h2,
[data-testid="stApp"] h3 {
    font-family: 'Bodoni Moda', Georgia, serif !important;
    font-weight: 400 !important;
    letter-spacing: -0.5px;
}


[data-testid="stMain"] h1 {
    font-size: 3.5rem !important;
}


[data-testid="stMain"] p {
    line-height: 1.7;
}


[data-testid="stApp"] button {
    font-weight: 500;
}



[data-testid="stMain"] [data-baseweb="select"] > div {
    background: #ffffff !important;
    color: #111111 !important;
    border: 1px solid #c9c3bc !important;
    border-radius: 2px !important;
    box-shadow: none !important;
    min-height: 3.3rem;
}
[data-testid="stMain"] [data-baseweb="select"] span,
[data-testid="stMain"] [data-baseweb="select"] input {
    color: #111111 !important;
}
[data-testid="stMain"] [data-baseweb="select"] svg {
    fill: #111111 !important;
}
[data-testid="stMain"] [role="radiogroup"] {
    gap: 1.3rem;
    margin: 0.6rem 0 1.2rem;
}
[data-testid="stMain"] [data-testid="stRadio"] label {
    color: #111111 !important;
}



.wigology-home-copy { text-align: center; margin-bottom: 1.2rem; }
.wigology-home-copy h1 { margin: 0 0 0.8rem !important; }
.wigology-home-copy p { font-size: 0.78rem; letter-spacing: 0.19em; margin: 0; }



[data-testid="stSidebar"] [data-testid="stSelectbox"] [data-baseweb="select"],
[data-testid="stSidebar"] [data-testid="stSelectbox"] [data-baseweb="select"] > div,
[data-testid="stSidebar"] [data-testid="stSelectbox"] input,
[data-testid="stSidebar"] [data-testid="stTextInput"] [data-baseweb="input"],
[data-testid="stSidebar"] [data-testid="stTextInput"] input {
  background:#fff !important; background-color:#fff !important;
  color:#25201C !important; -webkit-text-fill-color:#25201C !important;
  caret-color:#25201C !important; box-shadow:none !important;
}
[data-testid="stSidebar"] [data-testid="stSelectbox"] [data-baseweb="select"] > div,
[data-testid="stSidebar"] [data-testid="stTextInput"] [data-baseweb="input"] {
  border:1px solid #CBBEAF !important; border-radius:2px !important;
}
[data-testid="stSidebar"] input:-webkit-autofill,
[data-testid="stSidebar"] input:-webkit-autofill:focus {
  -webkit-box-shadow:0 0 0 1000px white inset !important;
  -webkit-text-fill-color:#25201C !important;
}
[data-testid="stSidebar"] [data-testid="stSelectbox"] svg { fill:#7C6A59 !important; }
[data-testid="stSidebar"] [data-testid="stSelectbox"] span,
[data-testid="stSidebar"] [data-testid="stSelectbox"] div[role="combobox"] {
  color:#25201C !important; -webkit-text-fill-color:#25201C !important;
}

div[data-baseweb="popover"], div[data-baseweb="popover"] [data-baseweb="menu"],
div[data-baseweb="popover"] [role="listbox"],
div[data-baseweb="popover"] [role="option"],
div[data-baseweb="popover"] li {
  background:#fff !important; background-color:#fff !important;
  color:#25201C !important;
}
div[data-baseweb="popover"] [role="option"] *,
div[data-baseweb="popover"] li * {
  color:#25201C !important; -webkit-text-fill-color:#25201C !important;
}
div[data-baseweb="popover"] [role="option"]:hover,
div[data-baseweb="popover"] [aria-selected="true"] {
  background:#F2ECE5 !important; background-color:#F2ECE5 !important;
}

</style>
""", unsafe_allow_html=True)


st.markdown("""
<style>
[class*="st-key-wig_tile_"] button {
    border: 1px solid #BEB5AB !important;
    background: #FFFFFF !important;
    color: #161616 !important;
    border-radius: 2px !important;
    min-height: 4rem !important;
    text-transform: none !important;
    letter-spacing: .025em !important;
}
[class*="st-key-wig_tile_"] button:hover {
    border-color: #111111 !important;
    background: #F3EEE8 !important;
    color: #111111 !important;
}
[class*="st-key-wig_tile_"] button[kind="primary"],
[class*="st-key-wig_tile_"] button[kind="primary"]:hover {
    background: #171717 !important;
    color: #FFFFFF !important;
    border-color: #171717 !important;
}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<style>
:root {
  --wig-ivory: #F8F4EC;
  --wig-cream: #EEE5D8;
  --wig-chocolate: #38251F;
  --wig-walnut: #624333;
  --wig-olive: #3C442D;
  --wig-olive-soft: #E5E7DC;
  --wig-black: #201B18;
  --wig-line: #D8CCBD;
}

[data-testid="stApp"], [data-testid="stMain"],
[data-testid="stMainBlockContainer"] {
  background: var(--wig-ivory) !important;
  color: var(--wig-black) !important;
}
[data-testid="stMain"] h1, [data-testid="stMain"] h2,
[data-testid="stMain"] h3, [data-testid="stMain"] p,
[data-testid="stMain"] [data-testid="stCaptionContainer"] {
  color: var(--wig-chocolate) !important;
}

[data-testid="stMain"] .stButton button {
  background: transparent !important;
  color: var(--wig-chocolate) !important;
  border: 1px solid var(--wig-walnut) !important;
  border-radius: 2px !important;
  box-shadow: none !important;
  transition: background .2s ease, color .2s ease, border-color .2s ease;
}
[data-testid="stMain"] .stButton button:hover,
[data-testid="stMain"] .stButton button:focus-visible,
[data-testid="stMain"] .stButton button[kind="primary"] {
  background: var(--wig-chocolate) !important;
  color: #FFF9F0 !important;
  border-color: var(--wig-chocolate) !important;
}
[data-testid="stMain"] .stButton button:hover *,
[data-testid="stMain"] .stButton button:focus-visible *,
[data-testid="stMain"] .stButton button[kind="primary"] * {
  color: #FFF9F0 !important;
  -webkit-text-fill-color: #FFF9F0 !important;
}

[data-testid="stMain"] [class*="st-key-homepage_build"] button {
  background: var(--wig-chocolate) !important;
  color: #FFF9F0 !important;
  border-color: var(--wig-chocolate) !important;
}
[data-testid="stMain"] [class*="st-key-homepage_build"] button * {
  color: #FFF9F0 !important;
  -webkit-text-fill-color: #FFF9F0 !important;
}
[data-testid="stMain"] [class*="st-key-homepage_build"] button:hover {
  background: var(--wig-walnut) !important;
  border-color: var(--wig-walnut) !important;
}

[class*="st-key-wig_tile_"] button[kind="primary"],
[class*="st-key-shop_tile_"] button[kind="primary"] {
  background: var(--wig-olive) !important;
  color: #FFF9F0 !important;
  border-color: var(--wig-olive) !important;
}
[class*="st-key-wig_tile_"] button[kind="primary"] *,
[class*="st-key-shop_tile_"] button[kind="primary"] * {
  color: #FFF9F0 !important;
  -webkit-text-fill-color: #FFF9F0 !important;
}
[class*="st-key-wig_tile_"] button:not([kind="primary"]),
[class*="st-key-shop_tile_"] button:not([kind="primary"]) {
  background: var(--wig-ivory) !important;
  color: var(--wig-chocolate) !important;
  border-color: var(--wig-line) !important;
}
.wigology-home-copy h1 { color: var(--wig-chocolate) !important; }
.wigology-home-copy p { color: var(--wig-olive) !important; }

.wigology-home-copy::after {
  content: "";
  display: block;
  width: 62px;
  height: 2px;
  margin: 20px auto 0;
  background: var(--wig-olive);
  opacity: .8;
}

[data-testid="stMain"]:has(.wigology-home-copy) [data-testid="stImage"] img {
  mix-blend-mode: multiply;
}
.wig-science-hero, .wigology-shop-intro,
.wig-research-hero, .wig-science-story.wig-science-warm {
  background: var(--wig-cream) !important;
}
.wig-science-story { background: var(--wig-ivory) !important; }
.wig-science-eyebrow, .wig-research-eyebrow,
.wig-profile-head .eyebrow, .wig-science-story .eyebrow,
.wigology-science-label { color: var(--wig-olive) !important; }
.wig-science-links a { color: var(--wig-olive) !important; }
.wig-profile-photo { background: var(--wig-cream) !important; border-color: var(--wig-line) !important; }
.wig-fact, .wig-profile-section, .wig-research-card { border-color: var(--wig-line) !important; }
.wig-builder-summary { background: var(--wig-cream) !important; border-color: var(--wig-line) !important; }
.wig-builder-summary .price { color: var(--wig-chocolate) !important; }
[data-testid="stSidebar"], [data-testid="stSidebar"] > div,
[data-testid="stSidebarContent"], [data-testid="stSidebarUserContent"] {
  background: var(--wig-ivory) !important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] label,
[data-testid="stSidebar"] [role="radiogroup"] label {
  background: #FFF9F0 !important;
  border-color: var(--wig-line) !important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked),
[data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {
  background: var(--wig-olive-soft) !important;
  border-color: var(--wig-olive) !important;
}
[data-testid="stMain"] [data-baseweb="select"] > div {
  background: #FFF9F0 !important;
  border-color: var(--wig-line) !important;
}
@media (max-width: 768px) {
  .wigology-home-copy { margin-bottom: 1.4rem; }
}
</style>
""", unsafe_allow_html=True)


HAIR = {
    'Indian': {
        'Wavy': {
            'about': 'Naturally flowing waves with soft bends and movement. The exact wave pattern and fullness vary between bundles.',
            'appearance': 'Soft, flowing waves',
            'sew_in': 'Suitable for sew-ins when the leave-out can be styled to complement the waves.',
            'wig': 'Suitable for a custom wig with a flowing, wavy finish.',
            'care': 'Detangle gently, avoid excessive heat and handle the waves with care.'
        },
        'Curly': {
            'about': 'Natural curls with shape and volume. Curl size and definition can vary from one bundle to another.',
            'appearance': 'Curls and natural volume',
            'sew_in': 'Suitable for sew-ins when the curl pattern complements the desired style.',
            'wig': 'Suitable for a custom wig with a curly finish.',
            'care': 'Detangle carefully and avoid rough brushing that separates the curls.'
        }
    },
    'Filipino': {
        'Straight': {
            'about': 'Naturally straight hair with movement and body. Natural straight hair does not need to be perfectly flat or pin-straight.',
            'appearance': 'Straight with natural movement',
            'sew_in': 'Suitable for sew-ins when the leave-out can be styled to blend with the hair.',
            'wig': 'Suitable for a custom wig with a naturally straight finish.',
            'care': 'Use heat carefully and reduce friction to help maintain a smooth appearance.'
        },
        'Wavy': {
            'about': 'Soft natural waves with movement. The exact size and shape of the waves vary between bundles.',
            'appearance': 'Soft, natural waves',
            'sew_in': 'Suitable for sew-ins when the chosen wave pattern complements the desired style.',
            'wig': 'Suitable for a custom wig with a soft, wavy finish.',
            'care': 'Detangle gently; brushing and heat styling may temporarily change the wave pattern.'
        }
    }
}

hair_information = {
    origin: {
        "country": "India" if origin == "Indian" else "the Philippines",
        "textures": {texture: {"about": details["about"], "sew_ins": details["sew_in"], "wigs": details["wig"], "care": details["care"], "appearance": details["appearance"]} for texture, details in textures.items()},
        "colouring": "Professional colouring should be assessed on the actual hair after confirming its processing history."
    } for origin, textures in HAIR.items()
}


hair_origins = ["Indian", "Filipino"]

hair_textures = ["Straight", "Wavy", "Curly"]

hair_lengths = list(range(8, 27, 2))

closure_sizes = ["6x6", "7x7", "9x6"]


from pathlib import Path
from html import escape
import base64
import json
import streamlit.components.v1 as components

HAIR_PHOTOS = {
    "Indian Wavy": "images/indian_wavy.jpg",
    "Indian Curly": "images/indian_curly.jpg",
    "Filipino Straight": "images/filipino_straight.jpg",
    "Filipino Wavy": "images/filipino_wavy.jpg",
}

WIG_VIEW_IMAGES = {
    "Indian Wavy": ["indian_wavy_front.jpg", "indian_wavy_side.jpg", "indian_wavy_back.jpg"],
    "Filipino Straight": ["filipino_straight_front.jpg", "filipino_straight_side.jpg", "filipino_straight_back.jpg"],
}


@st.cache_data(show_spinner=False, max_entries=24)
def _wig_view_image_data(path_string, modified_ns):
    """Cache the encoded image; modified_ns invalidates cache on file changes."""
    return "data:image/jpeg;base64," + base64.b64encode(Path(path_string).read_bytes()).decode("ascii")


def show_wig_angle_viewer(name):
    """Drag/swipe a three-photo wig viewer. This is not a true 3D model."""
    filenames = WIG_VIEW_IMAGES.get(name)
    if not filenames:
        return False
    paths = [Path(__file__).resolve().parent / "images" / file for file in filenames]
    if not all(path.is_file() for path in paths):
        return False
    images = [_wig_view_image_data(str(path), path.stat().st_mtime_ns) for path in paths]

    html = r'''<!doctype html><html><head><meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
      *{box-sizing:border-box}body{margin:0;background:#fff;color:#302820;font-family:Arial,sans-serif}
      .viewer{position:relative;overflow:hidden;border:1px solid #e9e2da;background:#fff;touch-action:none;user-select:none;cursor:pointer;height:420px}
      .viewer.dragging{cursor:grabbing}
      .frame{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;pointer-events:none;will-change:opacity}
      .hint{position:absolute;bottom:13px;left:50%;transform:translateX(-50%);background:rgba(255,255,255,.92);padding:9px 13px;white-space:nowrap;font-size:10px;letter-spacing:.12em;color:#5d5149;pointer-events:none}
      .controls{display:flex;align-items:center;justify-content:center;gap:9px;margin-top:13px;flex-wrap:wrap}
      button{border:1px solid #d7cfc5;background:#fff;color:#44382f;padding:10px 14px;letter-spacing:.1em;font-size:10px;cursor:pointer}
      button[aria-pressed="true"]{background:#29221e;color:white;border-color:#29221e}
      .sub{font-size:10px;color:#8b7b6c;letter-spacing:.1em;text-align:center;margin-top:10px}
      @media(max-width:500px){.viewer{height:340px}.hint{font-size:9px}.controls{gap:5px}button{padding:10px 11px}}
    </style></head><body>
    <div class="viewer" id="viewer" role="button" tabindex="0" aria-pressed="false" aria-label="Pause the automatically rotating wig views. Click to pause or play.">
      <div id="frames"></div>
    </div>
    <div class="controls" id="controls"></div>
    <script>
      const photos=__IMAGES__,labels=['FRONT','SIDE','BACK'];
      const viewer=document.getElementById('viewer'),frames=document.getElementById('frames'),controls=document.getElementById('controls');
      const imgs=photos.map((src,i)=>{const el=document.createElement('img');el.src=src;el.alt=labels[i].toLowerCase()+' view';el.className='frame';el.draggable=false;frames.appendChild(el);return el});
      const sequence=[0,1,2,1];
      const prefersReduced=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      let phase=0,playing=!prefersReduced,lastTime=null,dragging=false,moved=false,lastX=0,pointer=null;
      const buttons=labels.map((label,i)=>{const b=document.createElement('button');b.type='button';b.textContent=label;b.addEventListener('click',()=>{playing=false;phase=sequence.indexOf(i);sync();paint()});controls.appendChild(b);return b});
      const playButton=document.createElement('button');playButton.type='button';playButton.addEventListener('click',()=>{playing=!playing;sync()});controls.appendChild(playButton);
      function sync(){playButton.textContent=playing?'PAUSE':'PLAY';playButton.setAttribute('aria-pressed',String(playing));viewer.setAttribute('aria-pressed',String(!playing));viewer.setAttribute('aria-label',playing?'Pause rotating wig views':'Play rotating wig views')}
      function paint(){const n=sequence.length;const p=((phase%n)+n)%n;const j=Math.floor(p),t=p-j;
        const blend=t*t*(3-2*t),first=sequence[j],second=sequence[(j+1)%n];
        imgs.forEach((img,i)=>{img.style.opacity=(first===second&&i===first?1:i===first?1-blend:i===second?blend:0).toFixed(4)});
        buttons.forEach((b,i)=>b.setAttribute('aria-pressed',String(i===(blend<.5?first:second))));
      }
      function tick(now){if(lastTime!==null&&playing&&!dragging){const elapsed=Math.min(80,now-lastTime);phase+=elapsed/2500;}
        lastTime=now;paint();requestAnimationFrame(tick)}
      viewer.addEventListener('pointerdown',e=>{if(e.pointerType==='mouse'&&e.button!==0)return;pointer=e.pointerId;dragging=true;moved=false;lastX=e.clientX;viewer.setPointerCapture(pointer);viewer.classList.add('dragging')});
      viewer.addEventListener('pointermove',e=>{if(!dragging||e.pointerId!==pointer)return;const dx=e.clientX-lastX;lastX=e.clientX;if(Math.abs(dx)>1){moved=true;playing=false;phase-=dx/190;sync();paint()}});
      function end(e){if(!dragging||e.pointerId!==pointer)return;dragging=false;pointer=null;viewer.classList.remove('dragging');if(!moved){playing=!playing;sync()}}
      viewer.addEventListener('pointerup',end);viewer.addEventListener('pointercancel',e=>{dragging=false;pointer=null;viewer.classList.remove('dragging')});
      viewer.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();playing=!playing;sync()}else if(e.key==='ArrowLeft'||e.key==='ArrowRight'){e.preventDefault();playing=false;phase+=(e.key==='ArrowRight'?.25:-.25);sync();paint()}});
      document.addEventListener('visibilitychange',()=>{lastTime=null});
      sync();paint();requestAnimationFrame(tick);
    </script></body></html>'''
    html = html.replace("__IMAGES__", json.dumps(images))
    components.html(html, height=515, scrolling=False)
    return True


st.markdown("""<style>

.wig-profile-head {text-align:center;padding:2.2rem 1rem 1.3rem;}
.wig-profile-head .eyebrow,.wig-research-eyebrow {font-family:'Manrope',sans-serif;letter-spacing:.2em;font-size:.7rem;color:#76685b;}
.wig-profile-head h2 {font-family:'Bodoni Moda',Georgia,serif;margin:.8rem 0;}
.wig-profile-photo {height:350px;display:flex;align-items:center;justify-content:center;background:#F7F4F0;border:1px solid #E5DCD2;text-align:center;color:#75675D;padding:1.5rem;}
.wig-fact {border-bottom:1px solid #E9E1D9;padding:.7rem 0;display:flex;justify-content:space-between;gap:1rem;font-size:.88rem;}
.wig-fact strong {font-weight:600;}
.wig-research-hero {background:#F3EEE8;text-align:center;padding:3rem 1.5rem;margin:1rem 0 3rem;}
.wig-research-card {padding:1.8rem 0;border-bottom:1px solid #E5DFD8;}
.wig-profile-section {padding:1rem 0;border-bottom:1px solid #E5DFD8;}
</style>""",unsafe_allow_html=True)

def available_textures(origin):
    return list(hair_information[origin]["textures"])

def show_hair_profile(origin, texture):
    """Show product-specific information before customers customise their wig."""
    if not origin or texture not in hair_information[origin]["textures"]:
        st.info("Choose an available origin and texture.")
        return
    details = hair_information[origin]["textures"][texture]
    name = f"{origin} {texture}"
    st.markdown(
        f'<div class="wig-profile-head"><div class="eyebrow">THE WIGOLOGY / HAIR INTELLIGENCE</div>'
        f'<h2>{escape(name)}</h2><p>Get to know your selected hair.</p></div>',
        unsafe_allow_html=True,
    )
    photo_col, info_col = st.columns([1, 1.15], gap="large")
    with photo_col:
        if not show_wig_angle_viewer(name):
            photo = Path(HAIR_PHOTOS[name])
            if photo.is_file():
                st.image(str(photo), use_container_width=True)
            else:
                st.markdown('<div class="wig-profile-photo">YOUR HAIR PHOTOGRAPH<br>COMING SOON</div>',
                            unsafe_allow_html=True)
    with info_col:
        st.markdown("#### Your Hair Profile")


        profile_intro = {
            ("Indian", "Wavy"): (
                "Our Indian Wavy collection features naturally flowing waves, visible body "
                "and a fuller-looking finish. The soft bends give this hair movement "
                "without a perfectly uniform wave pattern."
            ),
            ("Indian", "Curly"): (
                "Our Indian Curly collection features defined curls, natural body and "
                "a voluminous finish. Its textured appearance creates fullness while "
                "allowing the curls to move naturally."
            ),
            ("Filipino", "Straight"): (
                "Our Filipino Straight collection has a naturally straight appearance "
                "with soft movement and subtle body. It offers a smooth, polished look "
                "without needing to be completely pin-straight."
            ),
            ("Filipino", "Wavy"): (
                "Our Filipino Wavy collection features gentle, flowing waves and a "
                "relaxed finish. Its soft texture creates movement and dimension "
                "without an overly structured wave pattern."
            ),
        }
        st.write(profile_intro[(origin, texture)])
        facts = [
            ("Origin", hair_information[origin]["country"]),
            ("Texture", texture),
            ("Strand feel", "Medium to coarse"),
            ("Processing", "No chemical processing"),
        ]
        for label, value in facts:
            st.markdown(
                f'<div class="wig-fact"><strong>{escape(label)}</strong>'
                f'<span>{escape(value)}</span></div>',
                unsafe_allow_html=True,
            )

    behaviour = {
        ("Indian", "Wavy"): (
            "Its flowing waves create movement and natural fullness. The wave pattern may "
            "look more defined after washing and softer after brushing or heat styling. "
            "Humidity can also affect the finished style."
        ),
        ("Indian", "Curly"): (
            "Curls naturally create volume and definition. The hair may appear shorter "
            "when the curls contract, and the curl pattern can vary between bundles. "
            "Water and humidity may change the amount of curl definition and fullness."
        ),
        ("Filipino", "Straight"): (
            "Naturally straight hair can still have body, soft bends and movement rather "
            "than a pin-straight finish. Washing and humid conditions may bring out "
            "some natural fullness, while styling can temporarily smooth the hair."
        ),
        ("Filipino", "Wavy"): (
            "Soft waves create movement and shape. Washing can make the natural wave "
            "pattern more visible; brushing and heat styling may temporarily relax "
            "its definition. Humidity may also affect the overall finish."
        ),
    }
    st.markdown("#### How This Hair Behaves")
    st.write(behaviour[(origin, texture)])


RESEARCH = [
    {
        "title": "Raw vs Virgin Hair",
        "eyebrow": "01 / UNDERSTANDING HAIR",
        "intro": "You've probably heard the terms raw hair and virgin hair used as though they represent different levels of quality.",
        "question": "But are they really different?",
        "paragraphs": [
            "<strong>Scientifically, the important distinction is whether the hair has undergone chemical processing, not whether it is labelled raw or virgin.</strong> Both terms are commonly used to describe human hair that has not been chemically treated, such as through colouring, relaxing or perming.",
            "Raw hair is largely a commercial marketing term, often used to suggest a more natural or premium product rather than a separate scientifically defined hair category. Different suppliers may use the terms differently.",
            "Another common misconception is that raw hair must come from a single donor. The number of donors does not determine whether hair is chemically unprocessed. Whether collected from one donor or several, hair can still be virgin if it has not undergone chemical processing.",
            "At The Wigology, we believe the real distinction lies in the hair's processing history, condition and quality — not simply the label used to sell it.",
        ],
        "links": [
            ("Explore hair processing research", "https://pubmed.ncbi.nlm.nih.gov/?term=human+hair+chemical+processing"),
            ("Explore hair fibre research", "https://pubmed.ncbi.nlm.nih.gov/?term=human+hair+fibre+properties"),
        ],
    },
    {
        "title": "Humidity & Styling",
        "eyebrow": "02 / EVERYDAY HAIR SCIENCE",
        "intro": "Ever noticed your perfectly styled hair becoming fuller or losing its shape on a humid day?",
        "question": None,
        "paragraphs": [
            "Human hair naturally absorbs moisture from the air. When humidity rises, that moisture can affect the temporary bonds that help hold a hairstyle in place. As a result, a sleek finish may become fuller, or natural waves and curls may become more noticeable.",
            "This change does not automatically mean the hair is damaged. It is part of how human hair responds to its environment.",
        ],
        "links": [("Explore the research", "https://pubmed.ncbi.nlm.nih.gov/?term=human+hair+humidity+water+sorption")],
    },
    {
        "title": "Tangling & Care",
        "eyebrow": "03 / CARING FOR YOUR HAIR",
        "intro": "The way you handle your hair matters just as much as the way you style it.",
        "question": None,
        "paragraphs": [
            "Daily brushing, rubbing against clothing and repeated heat styling can gradually wear the hair's outer surface. Increased friction can make strands catch against one another, leading to more tangling and making detangling difficult.",
            "Gentle detangling, careful storage and limiting unnecessary heat can help your bundles and wigs maintain a smoother appearance.",
        ],
        "links": [("Explore the research", "https://pubmed.ncbi.nlm.nih.gov/?term=human+hair+cuticle+damage+friction+heat")],
    },
    {
        "title": "Sunlight & Hair",
        "eyebrow": "04 / PROTECTING YOUR HAIR",
        "intro": "Your human hair extensions respond to sunlight, too.",
        "question": None,
        "paragraphs": [
            "Over time, prolonged ultraviolet exposure can affect the colour and condition of human hair. The effects depend on the hair and its processing history.",
            "When you're not wearing your wig, storing it away from direct sunlight can help preserve its appearance.",
        ],
        "links": [("Explore the research", "https://pubmed.ncbi.nlm.nih.gov/?term=human+hair+ultraviolet+photodamage")],
    },
]


@st.cache_data(show_spinner=False, max_entries=4)
def _science_pattern_data(path_string, modified_ns):
    return "data:image/jpeg;base64," + base64.b64encode(Path(path_string).read_bytes()).decode("ascii")


def show_science_library():

    from pathlib import Path
    import base64
    pattern_file = Path(__file__).resolve().parent / "images" / "burgundy_pattern.jpg"
    if pattern_file.exists():
        pattern_url = _science_pattern_data(str(pattern_file), pattern_file.stat().st_mtime_ns)
    else:
        st.warning("Science background image missing: place burgundy_pattern.jpg inside the images folder beside main.py.")
        pattern_url = ""


    st.markdown("""
    <style>
    .wig-science-hero {background:#F3EEE8;text-align:center;padding:clamp(3rem,7vw,6rem) 1.5rem;margin:.8rem 0 3.5rem;}
    .wig-science-eyebrow {font-family:'Manrope',sans-serif;letter-spacing:.22em;font-size:.7rem;color:#76685B;margin-bottom:1.3rem;}
    .wig-science-hero h1 {font-family:'Bodoni Moda',Georgia,serif;font-weight:400;font-size:clamp(2.6rem,5vw,4.7rem)!important;line-height:1.13;margin:0 0 1.5rem;}
    .wig-science-hero p {font-family:'Tenor Sans',sans-serif;font-size:clamp(.94rem,1.5vw,1.07rem);line-height:1.9;max-width:660px;margin:auto;}
    .wig-science-story {padding:clamp(2rem,4vw,3.5rem) clamp(1.1rem,3vw,3rem);margin:0 0 2rem;background:#FFFFFF;}
    .wig-science-story.wig-science-warm {background:#F7F3EE;}
    .wig-science-story .eyebrow {font-family:'Manrope',sans-serif;font-size:.67rem;letter-spacing:.19em;color:#806F60;margin-bottom:1.25rem;}
    .wig-science-story h2 {font-family:'Bodoni Moda',Georgia,serif;font-size:clamp(2rem,3.4vw,3rem)!important;line-height:1.18;margin:0 0 1.6rem;}
    .wig-science-story .opening {font-size:1.05rem;line-height:1.95;max-width:680px;margin:0 0 1.5rem;}
    .wig-science-story .question {font-family:'Bodoni Moda',Georgia,serif;font-size:clamp(1.5rem,2.7vw,2.25rem);font-weight:500;text-align:center;margin:2.2rem auto 2.5rem;line-height:1.4;}
    .wig-science-story .copy {max-width:690px;margin:0 auto;}
    .wig-science-story .copy p {font-size:.98rem;line-height:2.05;margin:0 0 1.65rem;}
    .wig-science-story .copy strong {font-weight:600;}
    .wig-science-links {display:flex;flex-wrap:wrap;gap:.65rem 1.8rem;margin:1.8rem auto 0;max-width:690px;}
    .wig-science-links a {font-family:'Manrope',sans-serif;color:#6D5A4C!important;font-size:.75rem;letter-spacing:.045em;text-decoration:underline;text-underline-offset:5px;}
    @media(max-width:768px){.wig-science-hero{margin-bottom:2rem}.wig-science-story{margin-bottom:1rem}.wig-science-story .question{margin:1.8rem auto 2rem}}


    [data-testid="stApp"]:has(.wig-science-pattern-stage),
    [data-testid="stMain"]:has(.wig-science-pattern-stage),
    [data-testid="stMainBlockContainer"]:has(.wig-science-pattern-stage) {
        background-color:#F2E5D3 !important;
        background-image:url("__WIGOLOGY_PATTERN_URL__") !important;
        background-repeat:repeat !important;
        background-position:center top !important;
        background-size:clamp(560px, 76vw, 1080px) auto !important;
    }

    [data-testid="stMain"]:has(.wig-science-pattern-stage) .stButton button {
        background:#FFF9F0 !important;
        color:#39251F !important;
        border:1px solid #634235 !important;
    }
    [data-testid="stMain"]:has(.wig-science-pattern-stage) .stButton button:hover {
        background:#39251F !important;
        color:#FFF9F0 !important;
    }

    [data-testid="stMain"]:has(.wig-science-pattern-stage) .wig-science-story {
        background:#F8F4ED !important;
    }
    [data-testid="stMain"]:has(.wig-science-pattern-stage) .wig-science-story.wig-science-warm {
        background:#EFE6DA !important;
    }


    .wig-science-pattern-stage {
        background:transparent !important;
        padding:clamp(105px,10vw,160px) 0 0;
        margin:.8rem 0 3.5rem;
        width:100%;
        overflow:hidden;
    }
    [data-testid="stMain"] .wig-science-pattern-stage .wig-science-hero {
        background:#253222 !important;
        border-radius:50% 50% 0 0 / 43% 43% 0 0 !important;
        padding:clamp(6rem,11vw,10rem) clamp(1.3rem,5vw,5rem) clamp(3rem,6vw,5rem) !important;
        margin:0 !important;
        min-height:450px;
        display:flex;
        flex-direction:column;
        justify-content:center;
        text-align:center;
        position:relative;
        z-index:1;
        box-shadow:none !important;
        overflow:hidden;
    }
    [data-testid="stMain"] .wig-science-pattern-stage .wig-science-hero::before,
    [data-testid="stMain"] .wig-science-pattern-stage .wig-science-hero::after {content:none !important;}
    [data-testid="stMain"] .wig-science-pattern-stage .wig-science-hero h1,
    [data-testid="stMain"] .wig-science-pattern-stage .wig-science-hero p,
    [data-testid="stMain"] .wig-science-pattern-stage .wig-science-hero .wig-science-eyebrow {
        color:#FFF9EF !important;
        -webkit-text-fill-color:#FFF9EF !important;
    }
    [data-testid="stMain"] .wig-science-pattern-stage .wig-science-hero h1 {
        max-width:980px;
        margin:1.3rem auto 1.2rem !important;
    }
    [data-testid="stMain"] .wig-science-pattern-stage .wig-science-hero p {margin:0 auto;}
    @media(max-width:768px){
        .wig-science-pattern-stage {padding-top:85px;margin-bottom:2rem;}
        [data-testid="stMain"] .wig-science-pattern-stage .wig-science-hero {
            min-height:355px;
            border-radius:50% 50% 0 0 / 20% 20% 0 0 !important;
            padding:6rem 1.2rem 3rem !important;
        }
    }
    </style>
    <div class="wig-science-pattern-stage">
      <section class="wig-science-hero">
        <div class="wig-science-eyebrow">THE WIGOLOGY / HAIR INTELLIGENCE</div>
        <h1>The Science Behind Wigology.</h1>
        <p>Explore the hair science behind human hair through research.</p>
      </section>
    </div>
    """.replace("__WIGOLOGY_PATTERN_URL__", pattern_url), unsafe_allow_html=True)


    _, centre, _ = st.columns([.5, 3.5, .5], gap="small")
    with centre:
        for index, item in enumerate(RESEARCH):
            opening = escape(item["intro"])
            if index == 0:
                opening = opening.replace("raw hair", "<em>raw hair</em>").replace("virgin hair", "<em>virgin hair</em>")
            paragraphs = "".join(f"<p>{paragraph}</p>" for paragraph in item["paragraphs"])
            question = (f'<div class="question">{escape(item["question"])}</div>'
                        if item["question"] else "")
            links = "".join(
                f'<a href="{escape(url, quote=True)}" target="_blank" rel="noopener noreferrer">{escape(label)}</a>'
                for label, url in item["links"]
            )
            warm = " wig-science-warm" if index % 2 else ""
            st.markdown(
                f'<section class="wig-science-story{warm}">'
                f'<div class="eyebrow">{escape(item["eyebrow"])}</div>'
                f'<h2>{escape(item["title"])}</h2>'
                f'<p class="opening">{opening}</p>'
                f'{question}<div class="copy">{paragraphs}</div>'
                f'<div class="wig-science-links">{links}</div></section>',
                unsafe_allow_html=True,
            )


def show_hair_science(origin, texture):
    show_hair_profile(origin, texture)


def show_wig_builder():

    from pricing_studio import (
        INDIAN_BUNDLES, FILIPINO_SAMPLE_BUNDLES,
        INDIAN_CLOSURES, FILIPINO_CLOSURES,
    )

    st.markdown(
        "<h1 class='wig-builder-title'>Build Your Dream Wig</h1>",
        unsafe_allow_html=True,
    )
    st.markdown("""
    <style>
    [class*="st-key-wig_tile_"] button {
        background:#FFFFFF !important; color:#111111 !important;
        border:1px solid #BEB5AB !important; border-radius:2px !important;
        min-height:4rem !important; text-transform:none !important;
    }
    [class*="st-key-wig_tile_"] button[kind="primary"] {
        background:#F3EEE8 !important; color:#111111 !important;
        border:2px solid #8C7967 !important;
    }
    [class*="st-key-wig_tile_"] button:hover {
        background:#EAE1D7 !important; color:#111111 !important;
    }
    .wig-builder-title {
        text-align:center !important;
        word-spacing:0 !important;
        letter-spacing:-0.025em !important;
        font-size:clamp(2.2rem, 4.5vw, 4rem) !important;
        line-height:1.12 !important;
        margin:0 auto 1rem !important;
        max-width:100%;
    }
    .wig-builder-label {text-align:center;letter-spacing:.12em;font-size:.8rem;margin:1.6rem 0 1rem;}
    .wig-builder-summary {border:1px solid #D8CFC5;background:#FFFFFF;padding:1.5rem;margin:1.5rem 0;text-align:center;}
    .wig-builder-summary .price {font:400 clamp(2rem,4vw,3.2rem) Georgia,serif;margin:.7rem 0;}
    </style>
    """, unsafe_allow_html=True)
    _, centre, _ = st.columns([1, 2.4, 1], gap="small")
    with centre:
        st.markdown("<p style='text-align:center;'>Your hair. Your vision. Made for you.</p>", unsafe_allow_html=True)
        if "wig_selected_origin" not in st.session_state:
            st.session_state.wig_selected_origin = None
        if "wig_selected_texture" not in st.session_state:
            st.session_state.wig_selected_texture = None

        def tile_group(label, choices, state_key, prefix):
            st.markdown(f'<div class="wig-builder-label">{label}</div>', unsafe_allow_html=True)
            if not choices:
                return
            cols = st.columns(len(choices), gap="small")
            for col, option in zip(cols, choices):
                with col:
                    active = st.session_state.get(state_key) == option
                    if st.button(f"✓ {option}" if active else option,
                                 key=f"wig_tile_{prefix}_{option}",
                                 type="primary" if active else "secondary",
                                 use_container_width=True):
                        st.session_state[state_key] = option
                        st.rerun()

        tile_group("01 — SELECT YOUR HAIR ORIGIN", hair_origins, "wig_selected_origin", "origin")
        if st.session_state.wig_selected_origin and st.session_state.wig_selected_texture not in available_textures(st.session_state.wig_selected_origin):
            st.session_state.wig_selected_texture = None
        tile_group("02 — SELECT YOUR HAIR TEXTURE", available_textures(st.session_state.wig_selected_origin) if st.session_state.wig_selected_origin else [], "wig_selected_texture", "texture")
        origin = st.session_state.wig_selected_origin
        texture = st.session_state.wig_selected_texture
        if not (origin and texture):
            return

        st.write("")
        show_hair_profile(origin, texture)
        st.write("")
        st.markdown("<p class='wig-builder-label'>CONTINUE BUILDING YOUR WIG</p>", unsafe_allow_html=True)

        curly_price_on_request = origin == "Indian" and texture == "Curly"
        if origin == "Indian":
            bundle_prices = ({length: None for length in hair_lengths}
                             if curly_price_on_request
                             else {length: row["Straight / Wavy"] for length, row in INDIAN_BUNDLES.items()})
            closure_prices = INDIAN_CLOSURES
        else:
            bundle_prices = FILIPINO_SAMPLE_BUNDLES
            closure_prices = FILIPINO_CLOSURES


        def number_tiles(caption, options, state_key, tile_prefix, default, columns=5):
            st.markdown(f'<div class="wig-builder-label">{escape(caption)}</div>',
                        unsafe_allow_html=True)
            values = list(options)
            if not values:
                return None
            if st.session_state.get(state_key) not in values:
                st.session_state[state_key] = default if default in values else values[0]
            for start in range(0, len(values), columns):
                row_options = values[start:start + columns]
                row_columns = st.columns(len(row_options), gap="small")
                for column, option in zip(row_columns, row_options):
                    with column:
                        active = st.session_state[state_key] == option
                        text = f"{option}″" if tile_prefix.startswith("length") else str(option)
                        if st.button(f"✓ {text}" if active else text,
                                     key=f"wig_tile_{tile_prefix}_{option}",
                                     type="primary" if active else "secondary",
                                     use_container_width=True):
                            st.session_state[state_key] = option
                            st.rerun()
            return st.session_state[state_key]

        st.markdown('<div class="wig-builder-label">03 — CHOOSE YOUR BUNDLES</div>',
                    unsafe_allow_html=True)
        count = number_tiles("NUMBER OF BUNDLES", range(1, 6),
                             "wig_builder_choice_count", "count", 3)
        chosen = []
        for i in range(int(count)):
            length = number_tiles(f"BUNDLE {i + 1} LENGTH (INCHES)", bundle_prices.keys(),
                                  f"wig_builder_choice_length_{i}", f"length_bundle_{i}", 20)
            chosen.append(length)

        st.markdown('<div class="wig-builder-label">04 — CHOOSE YOUR CLOSURE</div>',
                    unsafe_allow_html=True)
        tile_group("SELECT YOUR CLOSURE SIZE", closure_sizes,
                   "wig_builder_closure_size", "closure_size")
        closure_size = st.session_state.get("wig_builder_closure_size")
        closure_length = number_tiles("CLOSURE LENGTH (INCHES)", closure_prices.keys(),
                                      "wig_builder_choice_closure_length", "length_closure", 18)

        if not closure_size:
            st.caption("Select a closure size to see your wig estimate.")
            return

        st.divider()
        st.markdown('<div class="wig-builder-label">05 — YOUR DREAM WIG</div>', unsafe_allow_html=True)
        st.markdown(f"**Hair:** {origin} {texture}")
        st.markdown("**Bundles:** " + ", ".join(f'{length}″' for length in chosen))
        st.markdown(f"**Closure:** {closure_size} · {closure_length}″")


        if curly_price_on_request:
            st.markdown('<div class="wig-builder-summary"><div>ESTIMATED WIG PRICE</div>'
                        '<div class="price">Price on request</div></div>', unsafe_allow_html=True)
            st.caption("Indian Curly supplier pricing must be confirmed before a quotation can be provided.")
            return


        closure_quote = closure_prices[closure_length].get(closure_size.replace("x", "×"))
        if closure_quote is None:
            st.markdown('<div class="wig-builder-summary"><div>ESTIMATED WIG PRICE</div>'
                        '<div class="price">Price on request</div></div>', unsafe_allow_html=True)
            st.caption("This closure size and length needs a confirmed supplier quote before we can calculate a price.")
            return


        supplier_usd = sum(bundle_prices[length] for length in chosen) + float(closure_quote)
        exchange_rate = 18.00
        shipping_usd = 65.00
        customs_zar = 200.00
        making_zar = 330.00
        gross_margin = 35.0
        estimated_cost = (supplier_usd + shipping_usd) * exchange_rate + customs_zar + making_zar
        estimated_price = estimated_cost / (1 - gross_margin / 100)
        st.markdown(
            f'<div class="wig-builder-summary"><div>ESTIMATED WIG PRICE</div>'
            f'<div class="price">R {estimated_price:,.2f}</div>'
            '<div>Made to order · Estimate only</div></div>',
            unsafe_allow_html=True,
        )
        st.caption("Illustrative estimate based on supplier quotes and Pricing Studio defaults: "
                   "R18/USD, $65 shipping, R200 customs, R330 wig making and 35% gross margin. "
                   "Final pricing is subject to confirmation; no payment is collected here.")
        if origin == "Filipino":
            st.caption("Filipino supplier quotes are samples; confirm the selected texture and current availability.")


def show_individual_hair_shop():
    """Shop individual bundles and closures; education belongs in the wig builder."""
    if "shop_selected_origin" not in st.session_state:
        st.session_state.shop_selected_origin = None
    if "shop_selected_texture" not in st.session_state:
        st.session_state.shop_selected_texture = None

    st.markdown("""
    <style>
    .wigology-shop-intro {
        background: #F3EEE8; text-align: center;
        padding: 2.5rem 1rem; margin: .8rem 0 2rem;
    }
    .wigology-shop-intro .eyebrow {
        font-size: .75rem; letter-spacing: .18em; text-transform: uppercase;
    }
    .wigology-shop-intro h1 {
        font-family: Georgia, serif; font-size: clamp(2rem,4vw,3.3rem) !important;
        margin: .7rem 0;
    }
    .wigology-shop-intro p {font-size: .94rem; margin: 0;}
    .wigology-science-label {
        letter-spacing: .16em; text-transform: uppercase;
        font-size: .72rem; margin-top: 1.4rem; color: #6A6056;
    }
    .wigology-science-divider {border-top:1px solid #E5DFD8; margin:1.4rem 0;}

    [class*="st-key-shop_tile_"] button {
        border: 1px solid #BEB5AB !important;
        background: #FFFFFF !important;
        color: #161616 !important;
        border-radius: 2px !important;
        min-height: 4rem !important;
        font-size: 1rem !important;
        letter-spacing: .025em !important;
        text-transform: none !important;
    }
    [class*="st-key-shop_tile_"] button:hover {
        border-color: #111111 !important;
        background: #F3EEE8 !important;
        color: #111111 !important;
    }
    [class*="st-key-shop_tile_"] button[kind="primary"] {
        background: #F3EEE8 !important;
        color: #111111 !important;
        border: 2px solid #8C7967 !important;
    }
    [class*="st-key-shop_tile_"] button[kind="primary"]:hover {
        background: #EAE1D7 !important;
        color: #111111 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="wigology-shop-intro">
      <div class="eyebrow">THE WIGOLOGY COLLECTION</div>
      <h1>Shop Bundles &amp; Closures.</h1>
    </div>
    """, unsafe_allow_html=True)

    _, centre, _ = st.columns([1, 2.4, 1], gap="small")
    with centre:
        st.markdown("<p style='text-align:center;letter-spacing:.12em;font-size:.8rem;'>01 — SELECT YOUR HAIR ORIGIN</p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center;color:#948F89;font-size:.78rem;margin:-.25rem 0 1rem;'>Select your hair origin to see available textures.</p>", unsafe_allow_html=True)
        for col, option in zip(st.columns(2, gap="small"), hair_origins):
            with col:
                active = st.session_state.shop_selected_origin == option
                if st.button(f"✓ {option}" if active else option, key=f"shop_tile_origin_{option}",
                             type="primary" if active else "secondary", use_container_width=True):
                    if st.session_state.shop_selected_origin != option:
                        st.session_state.shop_selected_texture = None
                    st.session_state.shop_selected_origin = option
                    st.rerun()

        st.write("")
        st.markdown("<p style='text-align:center;letter-spacing:.12em;font-size:.8rem;'>02 — SELECT YOUR HAIR TEXTURE</p>", unsafe_allow_html=True)
        origin = st.session_state.shop_selected_origin
        options = available_textures(origin) if origin else []
        if st.session_state.shop_selected_texture not in options:
            st.session_state.shop_selected_texture = None
        if options:
            for col, option in zip(st.columns(len(options), gap="small"), options):
                with col:
                    active = st.session_state.shop_selected_texture == option
                    if st.button(f"✓ {option}" if active else option, key=f"shop_tile_texture_{option}",
                                 type="primary" if active else "secondary", use_container_width=True):
                        st.session_state.shop_selected_texture = option
                        st.rerun()

        st.markdown(
            "<p style='text-align:center;font-size:.87rem;line-height:1.9;margin:1.8rem 0 2rem;'>"
            "Not sure which hair is right for you? Discover your perfect match in <strong>Build Your Dream Wig</strong>, "
            "or explore <strong>The Science of Hair</strong>.</p>",
            unsafe_allow_html=True,
        )
        if not (origin and st.session_state.shop_selected_texture):
            return

        st.markdown("<p style='text-align:center;letter-spacing:.12em;font-size:.8rem;'>03 — SELECT YOUR COLLECTION</p>", unsafe_allow_html=True)
        collection_cols = st.columns(2, gap="small")
        for col, option in zip(collection_cols, ["Bundles", "Closures"]):
            with col:
                selected = st.session_state.get("shop_product_type", "Bundles") == option
                if st.button(f"✓ {option}" if selected else option,
                             key=f"shop_tile_collection_{option}",
                             type="primary" if selected else "secondary",
                             use_container_width=True):
                    st.session_state.shop_product_type = option
                    st.rerun()

        product_type = st.session_state.get("shop_product_type", "Bundles")
        if product_type == "Bundles":
            st.write("")
            st.markdown("<p style='text-align:center;letter-spacing:.12em;font-size:.8rem;'>04 — BUNDLE QUANTITY</p>", unsafe_allow_html=True)
            quantity = st.number_input("Number of Bundles", min_value=1, max_value=5,
                                       value=1, step=1, key="shop_bundle_quantity")
            st.write("")
            st.markdown("<p style='text-align:center;letter-spacing:.12em;font-size:.8rem;'>05 — BUNDLE LENGTHS</p>", unsafe_allow_html=True)
            selected_lengths = []
            for number in range(1, int(quantity) + 1):
                length = st.select_slider(f"Bundle {number} Length (inches)",
                                          options=hair_lengths,
                                          value=20, key=f"shop_bundle_length_{number}")
                selected_lengths.append(length)

            origin = st.session_state.get("shop_selected_origin")
            texture = st.session_state.get("shop_selected_texture")
            if origin and texture:
                st.divider()
                st.markdown("### Your Selection")
                with st.container(border=True):
                    st.write(f"**Hair:** {origin} {texture}")
                    st.write(f"**Bundle Quantity:** {quantity}")
                    for number, length in enumerate(selected_lengths, 1):
                        st.write(f"Bundle {number}: {length} inches")
        else:
            st.write("")
            st.markdown("<p style='text-align:center;letter-spacing:.12em;font-size:.8rem;'>04 — CLOSURE SIZE</p>", unsafe_allow_html=True)
            size_cols = st.columns(len(closure_sizes), gap="small")
            for col, option in zip(size_cols, closure_sizes):
                with col:
                    selected = st.session_state.get("shop_selected_closure_size") == option
                    if st.button(f"✓ {option}" if selected else option,
                                 key=f"shop_tile_closure_size_{option}",
                                 type="primary" if selected else "secondary",
                                 use_container_width=True):
                        st.session_state.shop_selected_closure_size = option
                        st.rerun()
            st.write("")
            st.markdown("<p style='text-align:center;letter-spacing:.12em;font-size:.8rem;'>05 — CLOSURE LENGTH</p>", unsafe_allow_html=True)
            closure_length = st.select_slider("Closure Length (inches)",
                                               options=hair_lengths, value=18,
                                               key="shop_closure_length")
            closure_size = st.session_state.get("shop_selected_closure_size")
            if closure_size:
                st.divider()
                st.markdown("### Your Selection")
                with st.container(border=True):
                    st.write(f"**Closure Size:** {closure_size}")
                    st.write(f"**Closure Length:** {closure_length} inches")
            else:
                st.caption("Select a closure size to complete your selection.")


def show_homepage():




    st.markdown('<div class="wigology-hero-start"></div>',
                unsafe_allow_html=True)

    text_col, image_col = st.columns(
        [1.1, 1],
        gap="large",
        vertical_alignment="center"
    )

    with text_col:
        st.markdown("""
        <div class="wigology-home-copy">
            <h1>The Wigology.</h1>
            <p>THE ART &amp; SCIENCE OF HAIR</p>
        </div>
        """, unsafe_allow_html=True)


        st.write("")

        st.button(
            "BUILD YOUR DREAM WIG",
            use_container_width=True,
            key="homepage_build",
            on_click=navigate_to_customer_page,
            args=("Build Your Dream Wig",),
        )

        st.button(
            "EXPLORE THE SCIENCE OF HAIR",
            use_container_width=True,
            key="homepage_science",
            on_click=navigate_to_customer_page,
            args=("The Science of Hair",),
        )

        st.button(
            "SHOP NOW",
            use_container_width=True,
            key="homepage_shop",
            on_click=navigate_to_customer_page,
            args=("Shop Now",),
        )

    with image_col:
        if Path("images/homepage_wig.png").is_file():
            st.image("images/homepage_wig.png", use_container_width=True)
        else:
            st.markdown('<div class="wig-profile-photo">HOMEPAGE PHOTOGRAPH</div>', unsafe_allow_html=True)


CUSTOMER_PAGE_SLUGS = {
    "Home": "home",
    "Shop Now": "shop",
    "Build Your Dream Wig": "build-your-dream-wig",
    "The Science of Hair": "science-of-hair",
}
SLUG_TO_CUSTOMER_PAGE = {slug: name for name, slug in CUSTOMER_PAGE_SLUGS.items()}


def navigate_to_customer_page(page):
    """Switch customer views with one Streamlit widget-triggered rerun."""
    st.session_state.customer_page = page
    if page in ("Home", "Shop Now"):
        st.session_state.shop_step = "Choose"


def show_storefront():
    # Do not rewrite query parameters on every click: that can cause
    # additional browser URL updates and extra page work on hosted Streamlit.
    if "customer_page" not in st.session_state:
        requested_page = SLUG_TO_CUSTOMER_PAGE.get(st.query_params.get("page", "home"))
        st.session_state.customer_page = requested_page or "Home"

    page = st.session_state.customer_page

    # A single placeholder owns the customer view so Streamlit can replace
    # its contents as one block when the destination view is ready.
    customer_view = st.empty()
    with customer_view.container():
        if page != "Home":
            st.button(
                "← Back to Home",
                on_click=navigate_to_customer_page,
                args=("Home",),
                key="customer_back_home",
            )

        if page == "Home":
            show_homepage()
        elif page == "Shop Now":
            show_individual_hair_shop()
        elif page == "Build Your Dream Wig":
            show_wig_builder()
        elif page == "The Science of Hair":
            show_science_library()


st.markdown("""
<style>
[data-testid="stMain"] [class*="st-key-wig_tile_"] button {
    background: #F8F4EC !important;
    color: #38251F !important;
    border: 1px solid #CEBEAE !important;
    border-radius: 2px !important;
    box-shadow: none !important;
    min-height: 3.6rem !important;
    text-transform: none !important;
    letter-spacing: .02em !important;
    font-family: 'Tenor Sans', sans-serif !important;
}
[data-testid="stMain"] [class*="st-key-wig_tile_"] button[kind="primary"],
[data-testid="stMain"] [class*="st-key-wig_tile_"] button[kind="primary"]:hover {
    background: #38251F !important;
    border-color: #38251F !important;
    color: #FFF9F0 !important;
}
[data-testid="stMain"] [class*="st-key-wig_tile_"] button[kind="primary"] * {
    color: #FFF9F0 !important;
    -webkit-text-fill-color: #FFF9F0 !important;
}
[data-testid="stMain"] [class*="st-key-wig_tile_"] button:not([kind="primary"]):hover {
    background: #EEE5D8 !important;
    border-color: #624333 !important;
    color: #38251F !important;
}
</style>
""", unsafe_allow_html=True)


def show_owner_dashboard():
    st.markdown("""
    <div class="wigology-dashboard-welcome" style="background:#F3EEE8; padding:2.1rem 1.5rem; text-align:center; margin-bottom:1.8rem;">
      <div style="letter-spacing:.2em; font-size:.72rem; color:#766A5E;">THE WIGOLOGY / PRIVATE STUDIO</div>
      <div style="font:400 clamp(2rem,4vw,3rem) Georgia,serif; color:#201B18; margin:.6rem 0;">Welcome to Dashboard</div>
    </div>
    """, unsafe_allow_html=True)
    section = st.radio(
        "Owner tools",
        ["Overview", "Pricing Studio"],
        horizontal=True,
        key="owner_dashboard_section",
    )
    if section == "Pricing Studio":
        from pricing_studio import show_pricing_studio
        show_pricing_studio()
    else:
        st.info("Inventory, orders and business analytics are coming next.")


if not st.session_state.get("owner_logged_in", False):
    st.sidebar.markdown("<div style='font:400 1.7rem Georgia,serif; text-align:center; padding:.6rem 0 1rem;'>The Wigology.</div>", unsafe_allow_html=True)

import os

try:
    owner_email = os.getenv("OWNER_EMAIL") or st.secrets["owner"]["email"]
    owner_password_hash = os.getenv("OWNER_PASSWORD_HASH") or st.secrets["owner"]["password_hash"]
except Exception:
    owner_email = None
    owner_password_hash = None

if "owner_logged_in" not in st.session_state:
    st.session_state.owner_logged_in = False


if st.session_state.owner_logged_in:

    st.sidebar.markdown("""
    <div style="background:#FFFFFF; color:#312B25; border:1px solid #D7C9BA;
      padding:1.15rem 1rem; text-align:center; margin:1rem 0 1.4rem;">
      <div style="font:400 1.25rem Georgia,serif;">The Wigology.</div>
      <div style="font-size:.69rem; letter-spacing:.19em; margin-top:.55rem; color:#75675C;">PRIVATE OWNER ACCESS</div>
      <div style="border-top:1px solid #D7C9BA; margin-top:.9rem; padding-top:.7rem;
        font-size:.82rem;">✦ &nbsp; OWNER SIGNED IN</div>
    </div>
    """, unsafe_allow_html=True)

    if st.sidebar.button("Log out"):
        st.session_state.owner_logged_in = False
        st.rerun()

    page = st.sidebar.selectbox(
        "Select a page",
        ["Customer Storefront", "Owner Dashboard"],
        index=1,
        key="owner_page_selector",
    )

    if page == "Owner Dashboard":
        show_owner_dashboard()
    else:
        show_storefront()

else:

    show_storefront()

    with st.sidebar.expander("Owner Login"):

        with st.form("owner_login_form"):

            email = st.text_input("Email")

            password = st.text_input(
                "Password",
                type="password"
            )

            submitted = st.form_submit_button(
                "Log in"
            )

        if submitted:
            if not owner_email or not owner_password_hash:
                st.error("Owner login is not configured in Streamlit secrets.")
                st.stop()

            email_matches = hmac.compare_digest(
                email.strip().lower(),
                owner_email.strip().lower()
            )

            password_matches = bcrypt.checkpw(
                password.encode(),
                owner_password_hash.encode()
            )

            if email_matches and password_matches:
                st.session_state.owner_logged_in = True
                st.rerun()
            else:
                st.error("Incorrect email or password.")


st.markdown("""
<style>
:root {
 --wig-ivory:#F7F3EB;
 --wig-cream:#EEE5D8;
 --wig-brown:#38251F;
 --wig-brown-hover:#52392F;
 --wig-soft-white:#FFF9F0;
 --wig-line:#CEBEAE;
}

[data-testid="stApp"], [data-testid="stMain"],
[data-testid="stMainBlockContainer"] { background:#F7F3EB !important; color:#38251F !important; }
[data-testid="stMain"] h1,[data-testid="stMain"] h2,
[data-testid="stMain"] h3,[data-testid="stMain"] p,
[data-testid="stMain"] label,[data-testid="stMain"] [data-testid="stCaptionContainer"] {
 color:#38251F !important;
}
.wigology-home-copy p,
.wig-science-eyebrow,.wig-science-story .eyebrow,
.wig-profile-head .eyebrow,.wigology-science-label {
 color:#755C4C !important;
}
.wigology-home-copy::after { background:#755C4C !important; opacity:.7 !important; }

[data-testid="stMain"] [class*="st-key-homepage_build"] button,
[data-testid="stMain"] [class*="st-key-homepage_build"] button:hover {
 background:#38251F !important; border:1px solid #38251F !important;
 color:#FFF9F0 !important;
}
[data-testid="stMain"] [class*="st-key-homepage_science"] button,
[data-testid="stMain"] [class*="st-key-homepage_shop"] button {
 background:transparent !important; border:1px solid #735B4D !important;
 color:#38251F !important;
}
[data-testid="stMain"] [class*="st-key-homepage_science"] button:hover,
[data-testid="stMain"] [class*="st-key-homepage_shop"] button:hover {
 background:#38251F !important; border-color:#38251F !important;
 color:#FFF9F0 !important;
}
[data-testid="stMain"] [class*="st-key-homepage_build"] button *,
[data-testid="stMain"] [class*="st-key-homepage_build"] button:hover *,
[data-testid="stMain"] [class*="st-key-homepage_science"] button:hover *,
[data-testid="stMain"] [class*="st-key-homepage_shop"] button:hover * {
 color:#FFF9F0 !important; -webkit-text-fill-color:#FFF9F0 !important;
}
[data-testid="stMain"] [class*="st-key-homepage_science"] button:not(:hover) *,
[data-testid="stMain"] [class*="st-key-homepage_shop"] button:not(:hover) * {
 color:#38251F !important; -webkit-text-fill-color:#38251F !important;
}

[data-testid="stMain"] [class*="st-key-wig_tile_"] button,
[data-testid="stMain"] [class*="st-key-shop_tile_"] button {
 background:#F7F3EB !important; color:#38251F !important;
 border:1px solid #C9B7A6 !important; border-radius:2px !important;
 box-shadow:none !important;
 min-height:3.7rem !important;
}
[data-testid="stMain"] [class*="st-key-wig_tile_"] button[kind="primary"],
[data-testid="stMain"] [class*="st-key-shop_tile_"] button[kind="primary"],
[data-testid="stMain"] [class*="st-key-wig_tile_"] button[kind="primary"]:hover,
[data-testid="stMain"] [class*="st-key-shop_tile_"] button[kind="primary"]:hover {
 background:#38251F !important; border:1px solid #38251F !important;
 color:#FFF9F0 !important;
}
[data-testid="stMain"] [class*="st-key-wig_tile_"] button[kind="primary"] *,
[data-testid="stMain"] [class*="st-key-shop_tile_"] button[kind="primary"] * {
 color:#FFF9F0 !important; -webkit-text-fill-color:#FFF9F0 !important;
}
[data-testid="stMain"] [class*="st-key-wig_tile_"] button:not([kind="primary"]):hover,
[data-testid="stMain"] [class*="st-key-shop_tile_"] button:not([kind="primary"]):hover {
 background:#EEE5D8 !important; color:#38251F !important;
 border-color:#735B4D !important;
}

[data-testid="stMain"] [data-testid="stNumberInput"] [data-baseweb="input"],
[data-testid="stMain"] [data-testid="stNumberInput"] [data-baseweb="input"] > div,
[data-testid="stMain"] [data-testid="stNumberInput"] input {
 background:#FFF9F0 !important; background-color:#FFF9F0 !important;
 color:#38251F !important; -webkit-text-fill-color:#38251F !important;
 box-shadow:none !important;
}
[data-testid="stMain"] [data-testid="stNumberInput"] [data-baseweb="input"] {
 border:1px solid #CEBEAE !important; border-radius:2px !important;
 overflow:hidden;
}
[data-testid="stMain"] [data-testid="stNumberInput"] button,
[data-testid="stMain"] [data-testid="stNumberInput"] button:hover {
 background:#EEE5D8 !important; background-color:#EEE5D8 !important;
 border-color:#CEBEAE !important; border-radius:0 !important;
 color:#38251F !important;
}
[data-testid="stMain"] [data-testid="stNumberInput"] button svg,
[data-testid="stMain"] [data-testid="stNumberInput"] button svg * {
 fill:#38251F !important; stroke:#38251F !important; color:#38251F !important;
}

[data-testid="stMain"] [data-testid="stSelectbox"] div[data-baseweb="select"],
[data-testid="stMain"] [data-testid="stSelectbox"] div[data-baseweb="select"] > div,
[data-testid="stMain"] [data-baseweb="select"] > div {
 background:#FFF9F0 !important; background-color:#FFF9F0 !important;
 border-color:#CEBEAE !important; border-radius:2px !important;
 box-shadow:none !important; color:#38251F !important;
}
[data-testid="stMain"] [data-baseweb="select"] input,
[data-testid="stMain"] [data-baseweb="select"] span,
[data-testid="stMain"] [data-baseweb="select"] [role="combobox"] {
 color:#38251F !important; -webkit-text-fill-color:#38251F !important;
}
[data-testid="stMain"] [data-baseweb="select"] svg {
 fill:#38251F !important; color:#38251F !important;
}

body [data-baseweb="popover"] [role="listbox"],
body [data-baseweb="popover"] [role="option"],
body [data-baseweb="popover"] [data-baseweb="menu"] {
 background:#FFF9F0 !important; color:#38251F !important;
}
body [data-baseweb="popover"] [role="option"]:hover,
body [data-baseweb="popover"] [aria-selected="true"] {
 background:#EEE5D8 !important; color:#38251F !important;
}

[data-testid="stMain"] [data-testid="stSlider"] [role="slider"],
[data-testid="stMain"] [data-testid="stSelectSlider"] [role="slider"] {
 background:#38251F !important; border-color:#38251F !important;
}
.wig-science-hero,.wigology-shop-intro,.wig-research-hero,
.wig-science-story.wig-science-warm,.wig-builder-summary {
 background:#EEE5D8 !important;
}
.wig-science-story {background:#F7F3EB !important;}
.wig-science-links a {color:#624333 !important;}

[data-testid="stMain"]:has(.wigology-home-copy) [data-testid="stImage"],
[data-testid="stMain"]:has(.wigology-home-copy) [data-testid="stImage"] > div,
[data-testid="stMain"]:has(.wigology-home-copy) [data-testid="stImage"] picture {
 background: transparent !important;
}
[data-testid="stMain"]:has(.wigology-home-copy) [data-testid="stImage"] img {
 display: block !important;
 mix-blend-mode: multiply !important;
 background: transparent !important;
}
</style>
""",unsafe_allow_html=True)


st.markdown("""
<style>

[data-testid="stMain"] [data-testid="stSelectbox"] [data-baseweb="select"],
[data-testid="stMain"] [data-testid="stSelectbox"] [data-baseweb="select"] > div,
[data-testid="stMain"] [data-testid="stSelectbox"] [data-baseweb="select"] div,
[data-testid="stMain"] [data-testid="stSelectbox"] div[role="combobox"],
[data-testid="stMain"] [data-testid="stSelectbox"] [role="combobox"],
[data-testid="stMain"] [data-testid="stSelectbox"] [data-baseweb="select"] input {
  background: #FFF9F0 !important;
  background-color: #FFF9F0 !important;
  color: #38251F !important;
  -webkit-text-fill-color: #38251F !important;
  box-shadow: none !important;
}
[data-testid="stMain"] [data-testid="stSelectbox"] [data-baseweb="select"] > div:first-child,
[data-testid="stMain"] [data-testid="stSelectbox"] div[role="combobox"] {
  border: 1px solid #CEBEAE !important;
  border-radius: 3px !important;
  min-height: 3.2rem !important;
}
[data-testid="stMain"] [data-testid="stSelectbox"] [data-baseweb="select"] span,
[data-testid="stMain"] [data-testid="stSelectbox"] [data-baseweb="select"] p,
[data-testid="stMain"] [data-testid="stSelectbox"] [data-baseweb="select"] svg,
[data-testid="stMain"] [data-testid="stSelectbox"] [data-baseweb="select"] svg * {
  color: #38251F !important;
  fill: #38251F !important;
  stroke: #38251F !important;
  -webkit-text-fill-color: #38251F !important;
}

[data-testid="stMain"] [data-testid="stSelectbox"] [data-baseweb="input"],
[data-testid="stMain"] [data-testid="stSelectbox"] [data-baseweb="input"] div,
[data-testid="stMain"] [data-testid="stSelectbox"] [data-baseweb="input"] input {
  background: #FFF9F0 !important;
  color: #38251F !important;
  -webkit-text-fill-color: #38251F !important;
}

[data-baseweb="popover"] [role="listbox"],
[data-baseweb="popover"] [role="option"],
[data-baseweb="popover"] [data-baseweb="menu"] {
  background: #FFF9F0 !important;
  color: #38251F !important;
}
[data-baseweb="popover"] [role="option"]:hover,
[data-baseweb="popover"] [aria-selected="true"] {
  background: #EEE5D8 !important;
}
</style>
""", unsafe_allow_html=True)

