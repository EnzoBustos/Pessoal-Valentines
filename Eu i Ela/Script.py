from PIL import Image
import os
from pathlib import Path

# Diretório onde estão as imagens
pasta = r"c:\Users\enzo\Downloads\Eu i Ela"

# Listar todos os arquivos JPEG
arquivos_jpeg = sorted([f for f in os.listdir(pasta) if f.lower().endswith('.jpeg') or f.lower().endswith('.jpg')])

print(f"Encontrados {len(arquivos_jpeg)} arquivos JPEG")

# Converter e renomear
for idx, arquivo in enumerate(arquivos_jpeg, 1):
    caminho_original = os.path.join(pasta, arquivo)
    caminho_avif = os.path.join(pasta, f"{idx}.avif")
    
    try:
        # Abrir a imagem
        img = Image.open(caminho_original)
        
        # Converter para RGB se necessário (AVIF precisa de RGB)
        if img.mode in ('RGBA', 'LA', 'P'):
            rgb_img = Image.new('RGB', img.size, (255, 255, 255))
            rgb_img.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
            img = rgb_img
        elif img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Salvar como AVIF
        img.save(caminho_avif, 'AVIF', quality=85)
        
        # Deletar arquivo original
        os.remove(caminho_original)
        
        print(f"✓ {idx} - Convertido e renomeado: {arquivo} → {idx}.avif")
    
    except Exception as e:
        print(f"✗ Erro ao converter {arquivo}: {e}")

print("\nConversão e renomeação concluída!")
