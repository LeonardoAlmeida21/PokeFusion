import os
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
import json

# 1. Setup
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("❌ ERROR: API Key not found. Please check your .env file!")

genai.configure(api_key=api_key)


model = genai.GenerativeModel('gemini-2.5-flash')

def get_pokemon_info(pokemon_name, csv_path="dataset/pokemon_full.csv"):
    
    try:
        df = pd.read_csv(csv_path)
        
        pokemon_name = pokemon_name.lower().strip()
        
        
        row = df[df['english_name'] == pokemon_name].iloc[0]
        
        info = f"Name: {row['english_name']}, Type 1: {row['primary_type']}"
        if pd.notna(row['secondary_type']):
            info += f", Type 2: {row['secondary_type']}"
        info += f", Description: {row['description']}"
        return info
    except IndexError:
        return f"Name: {pokemon_name} (Data not found in CSV)"
    except Exception as e:
        return f"Error reading data: {e}"

def generate_fusion_lore(pokemon_a, pokemon_b):
        
    
    info_a = get_pokemon_info(pokemon_a)
    info_b = get_pokemon_info(pokemon_b)

    
    prompt = f"""
    You are an expert Pokemon Professor specializing in genetic fusion.
    I have fused two Pokemon:
    1. {info_a}
    2. {info_b}

    Create a new Pokedex entry for this fusion.
    Format your response strictly as a JSON object with these keys:
    - "name": A creative mixed name (e.g., Charstoise).
    - "type": The new typing (can be a mix).
    - "description": A short, clever pokedex entry (max 2 sentences) combining their behaviors and biology.
    - "ability": A creative name for a mixed ability.

    Response must be ONLY valid JSON.
    """

    # 3. Call API
    try:
        response = model.generate_content(prompt)
        
        clean_text = response.text.replace("```json", "").replace("```", "").strip()
        data = json.loads(clean_text)
        return data
    except Exception as e:
        print(f"❌ API Error: {e}")
        return None

