import torch
from diffusers import StableDiffusionPipeline
from PIL import Image

# Global Configuration
BASE_MODEL = "runwayml/stable-diffusion-v1-5"
LORA_PATH = "models/pokemon-lora" # Ensure this path exists!

class PokemonGenerator:
    def __init__(self):
        print("🔌 Starting Fusion Engine...")
        self.pipe = StableDiffusionPipeline.from_pretrained(
            BASE_MODEL, 
            torch_dtype=torch.float16
        )
        print(f"🎨 Loading LoRA weights from: {LORA_PATH}")
        self.pipe.load_lora_weights(LORA_PATH)
        self.pipe.to("cuda")
        
        # Memory optimization
        self.pipe.enable_attention_slicing()

    def generate_fusion(self, pokemon_a, pokemon_b, alpha=0.5):
        """
        alpha: 0.0 (ONLY Pokemon A) <---> 1.0 (ONLY Pokemon B)
        """
        # Fusion Math (Weighting)
        # alpha 0.5 -> Weights (1.0, 1.0)
        # alpha 0.0 -> Weights (1.5, 0.5) - A Dominates
        # alpha 1.0 -> Weights (0.5, 1.5) - B Dominates
        weight_a = 1.5 - alpha
        weight_b = 0.5 + alpha
        
        # Advanced Prompt Engineering
        prompt = (
            f"pixel_art style, "
            f"hybrid of ({pokemon_a}:{weight_a:.2f}) and ({pokemon_b}:{weight_b:.2f}), "
            f"white background, simple background, 2d game sprite"
        )
        
        negative_prompt = "3d render, realistic, shadows, dark background, text, watermark, human"
        
        print(f"🚀 Generating Prompt: {prompt}")
        
        # Generate
        image = self.pipe(
            prompt, 
            negative_prompt=negative_prompt, 
            width=512, 
            height=512,
            num_inference_steps=40,
            guidance_scale=8.0
        ).images[0]
        
        # Pixel Crunch (Post-Processing)
        # Resize to 96x96 to force pixel look
        final_image = image.resize((96, 96), resample=Image.NEAREST)
        
        # Scale back up for display (4x zoom)
        display_image = final_image.resize((384, 384), resample=Image.NEAREST)
        
        return display_image