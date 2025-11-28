import streamlit as st
import pandas as pd
from src.image_gen import PokemonGenerator
from src.lore_gen import generate_fusion_lore

# Page Config
st.set_page_config(page_title="PokéFusion AI", page_icon="🧬")

# Title and Style
st.title("🧬 Pokémon Fusion Lab")
st.markdown("Mix the DNA of two Pokémon and see what happens!")

# 1. Load Resources (Cached)
@st.cache_resource
def load_engine():
    return PokemonGenerator()

@st.cache_data
def load_pokemon_list():
    # Ensure the path matches your CSV location
    df = pd.read_csv("dataset/pokemon_full.csv")
    names = df['english_name'].sort_values().unique().tolist()
    return names

# Initialize
try:
    gen = load_engine()
    pokemon_list = load_pokemon_list()
except Exception as e:
    st.error(f"Error loading engine: {e}")
    st.stop()

# --- SIDEBAR (CONTROLS) ---
with st.sidebar:
    st.header("⚗️ DNA Mixer")
    
    col1, col2 = st.columns(2)
    with col1:
        poke_a = st.selectbox("Parent 1 (Base)", pokemon_list, index=0)
    with col2:
        # Tries to set index 4 (Charmander) if available, otherwise 1
        default_index = 4 if len(pokemon_list) > 4 else 0
        poke_b = st.selectbox("Parent 2 (Modifier)", pokemon_list, index=default_index)

    # Fusion Slider
    alpha = st.slider("Genetic Dominance", 0.0, 1.0, 0.5, 0.1)
    st.caption("Left: More like Parent 1 | Right: More like Parent 2")

    btn_fusion = st.button("🧬 FUSE NOW", type="primary")

# --- MAIN AREA ---
if btn_fusion:
    col_img, col_txt = st.columns([1, 1.5])
    
    with col_img:
        with st.spinner("🎨 Generating pixel art..."):
            # Call Visual Brain
            image = gen.generate_fusion(poke_a, poke_b, alpha)
            st.image(image, caption="Fusion Result", use_container_width=True)

    with col_txt:
        with st.spinner("📜 Writing new Pokedex entry..."):
            # Call Narrative Brain
            lore = generate_fusion_lore(poke_a, poke_b)
            
            if lore:
                st.subheader(f"{lore['name']}")
                st.markdown(f"**Type:** {lore['type']}")
                st.markdown(f"**Ability:** {lore['ability']}")
                st.info(f"_{lore['description']}_")
            else:
                st.error("Error generating lore (Check API Key).")

else:
    st.info("👈 Select two Pokémon from the sidebar and click FUSE NOW!")