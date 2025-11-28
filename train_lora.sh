export MODEL_NAME="runwayml/stable-diffusion-v1-5"
export DATASET_DIR="./dataset/images"  # A pasta onde puseste as imagens e os txts
export OUTPUT_DIR="./models/pokemon-lora"

accelerate launch train_text_to_image_lora.py \
  --pretrained_model_name_or_path=$MODEL_NAME \
  --train_data_dir=$DATASET_DIR \
  --dataloader_num_workers=0 \
  --resolution=512 \
  --center_crop \
  --random_flip \
  --train_batch_size=1 \
  --gradient_accumulation_steps=4 \
  --max_train_steps=1500 \
  --learning_rate=1e-04 \
  --max_grad_norm=1 \
  --lr_scheduler="cosine" \
  --lr_warmup_steps=0 \
  --output_dir=$OUTPUT_DIR \
  --checkpointing_steps=500 \
  --validation_prompt="pixel_art style, pikachu hybrid" \
  --seed=1337 \
  --mixed_precision="fp16" \
  --use_8bit_adam