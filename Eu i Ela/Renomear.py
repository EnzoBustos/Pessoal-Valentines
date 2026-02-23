import os

pasta = r"c:\Users\enzo\Downloads\Eu i Ela"

# Listar todos os arquivos AVIF em ordem
arquivos_avif = sorted([f for f in os.listdir(pasta) if f.lower().endswith('.avif')])

print(f"Renomeando {len(arquivos_avif)} arquivos AVIF de 1 a {len(arquivos_avif)}...\n")

# Primeira passagem: renomear para temporário
for idx, arquivo in enumerate(arquivos_avif, 1):
    caminho_original = os.path.join(pasta, arquivo)
    caminho_temp = os.path.join(pasta, f"temp_{idx:03d}.avif")
    
    try:
        os.rename(caminho_original, caminho_temp)
    except Exception as e:
        print(f"✗ Erro ao renomear {arquivo}: {e}")

# Segunda passagem: renomear do temporário para o final
for idx in range(1, len(arquivos_avif) + 1):
    caminho_temp = os.path.join(pasta, f"temp_{idx:03d}.avif")
    caminho_final = os.path.join(pasta, f"{idx}.avif")
    
    try:
        os.rename(caminho_temp, caminho_final)
        print(f"✓ {idx}.avif")
    except Exception as e:
        print(f"✗ Erro ao renomear temp_{idx:03d}.avif: {e}")

print(f"\nRenomeação concluída! Agora temos {len(arquivos_avif)} imagens de 1.avif a {len(arquivos_avif)}.avif")
