from transformers import pipeline
import torch

# Modelo
model_id = "gpt2"

# Crear pipeline
pipe = pipeline(
    "text-generation",
    model=model_id,
    torch_dtype="auto",
    device_map="auto",
)

# Mensaje como string, no lista
prompt = "Explain quantum mechanics clearly and concisely."

# Generar texto
outputs = pipe(
    prompt,
    max_new_tokens=256,
    do_sample=True,
    temperature=0.7
)

# Mostrar resultado
print(outputs[0]["generated_text"])

