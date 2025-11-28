# 🧬 PokéFusion

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)

**PokéFusion** is a tool that creates unique Pokémon fusions using a “Two-Brain” AI architecture:

1. **Visual Brain (LoRA):** Uses Stable Diffusion (v1.5) fine-tuned on pixel-art sprites to generate the fusion image.  
2. **Narrative Brain (LLM):** Uses Google Gemini API to analyze the parents’ biology and generate a new name, appropriate typing and Pokédex entry.

![Demo Screenshot](assets/demo.png)  
*(Note: You can add a screenshot of your app running here!)*


## 🛠️ Installation & Setup

Follow these steps to set up the project on your local machine.

### 1. Prerequisites

- **Python 3.10+**  
- **Git**  
- **NVIDIA GPU (8GB VRAM recommended)**  

### 2. Clone the Repository

```bash
git clone https://github.com/LeonardoAlmeida21/PokeFusion.git
cd PokeFusion
```

### 3. Create a Virtual Environment (Recommended)

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 API Key Setup (Security)

The Gemini API key is required for text generation.


1. In the project root, rename `.env.example` → `.env`

2. Open `.env` and paste your key:

```ini
GOOGLE_API_KEY=AIzaSy...PasteYourKeyHere
```

⚠️ *Do NOT use quotes.*  
⚠️ *Never commit the `.env` file to Git.*

---


## 🚀 Usage

Launch the web interface:

```bash
streamlit run app.py
```

It will open automatically ! Have fun ! 


---

## 📂 Project Structure

```
src/                # Core logic: image generation + lore generation
utils/              # Helper scripts (CSV → .txt, processing, etc.)
dataset/            # Master CSV + zipped training images
models/             # Pretrained LoRA weights (you need to add these)
app.py              # Streamlit UI
README.md           # Project documentation
```

---

## 🤝 Contributing

Pull requests and issues are welcome!

---

## 📜 License


This project is for **educational and portfolio purposes**.  
Pokémon is a trademark of Nintendo / Creatures Inc. / GAME FREAK.

---


