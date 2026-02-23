import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from pathlib import Path

class CropadorImagens:
    def __init__(self, root):
        self.root = root
        self.root.title("Cropador de Imagens - Centralizador de Rostos")
        self.root.geometry("1200x800")
        
        self.pasta = r"c:\Users\enzo\Downloads\Eu i Ela"
        self.arquivos_avif = sorted([f for f in os.listdir(self.pasta) 
                                     if f.lower().endswith('.avif')])
        
        self.indice_atual = 0
        self.imagem_original = None
        self.imagem_tk = None
        self.tamanho_quadrado = 500
        self.pos_x = 0
        self.pos_y = 0
        self.arrastando = False
        self.redimensionando = False
        
        # Frame principal
        self.frame_controles = tk.Frame(root, bg="lightgray", height=100)
        self.frame_controles.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        
        # Rótulo de informações
        self.label_info = tk.Label(self.frame_controles, text="", bg="lightgray", font=("Arial", 10))
        self.label_info.pack(anchor=tk.W, padx=5, pady=5)
        
        # Frame para controles
        self.frame_botoes = tk.Frame(self.frame_controles, bg="lightgray")
        self.frame_botoes.pack(anchor=tk.W, padx=5, pady=5)
        
        tk.Button(self.frame_botoes, text="◀ Anterior", command=self.anterior, width=12).pack(side=tk.LEFT, padx=2)
        tk.Button(self.frame_botoes, text="Próximo ▶", command=self.proximo, width=12).pack(side=tk.LEFT, padx=2)
        tk.Button(self.frame_botoes, text="✔ Salvar Crop", command=self.salvar_crop, width=12, bg="lightgreen").pack(side=tk.LEFT, padx=2)
        tk.Button(self.frame_botoes, text="⊘ Pular", command=self.pular, width=12).pack(side=tk.LEFT, padx=2)
        
        # Frame para ajustes
        self.frame_ajustes = tk.Frame(self.frame_controles, bg="lightgray")
        self.frame_ajustes.pack(anchor=tk.W, padx=5, pady=5)
        
        tk.Label(self.frame_ajustes, text="Tamanho Quadrado:", bg="lightgray").pack(side=tk.LEFT, padx=5)
        self.scale_tamanho = tk.Scale(self.frame_ajustes, from_=100, to=1200, orient=tk.HORIZONTAL, 
                                       command=self.atualizar_tamanho, length=200)
        self.scale_tamanho.set(500)
        self.scale_tamanho.pack(side=tk.LEFT, padx=5)
        self.label_tamanho = tk.Label(self.frame_ajustes, text=f"500x500", 
                                       bg="lightgray", width=12)
        self.label_tamanho.pack(side=tk.LEFT, padx=5)
        
        # Canvas para exibir imagem
        self.canvas = tk.Canvas(root, bg="black", cursor="crosshair")
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.canvas.bind("<Motion>", self.movimento_mouse)
        self.canvas.bind("<Button-1>", self.inicio_arrasto)
        self.canvas.bind("<B1-Motion>", self.durante_arrasto)
        self.canvas.bind("<ButtonRelease-1>", self.fim_arrasto)
        
        self.carregar_imagem()
    
    def carregar_imagem(self):
        if self.indice_atual < len(self.arquivos_avif):
            caminho = os.path.join(self.pasta, self.arquivos_avif[self.indice_atual])
            self.imagem_original = Image.open(caminho)
            
            # Obter dimensões
            largura, altura = self.imagem_original.size
            tamanho_maximo = min(largura, altura)
            
            # Atualizar o máximo do scale
            self.scale_tamanho.config(to=tamanho_maximo)
            
            # Definir tamanho inicial (máximo disponível)
            self.tamanho_quadrado = tamanho_maximo
            self.scale_tamanho.set(self.tamanho_quadrado)
            
            # Centralizar no corpo (aproximadamente)
            self.pos_x = (largura - self.tamanho_quadrado) // 2
            self.pos_y = (altura - self.tamanho_quadrado) // 2
            
            self.atualizar_canvas()
            self.atualizar_info()
        else:
            messagebox.showinfo("Concluído", "Todas as imagens foram processadas!")
            self.root.quit()
    
    def atualizar_tamanho(self, valor):
        self.tamanho_quadrado = int(valor)
        self.label_tamanho.config(text=f"{self.tamanho_quadrado}x{self.tamanho_quadrado}")
        
        if self.imagem_original is None:
            return
        
        # Reposicionar se necessário
        largura, altura = self.imagem_original.size
        if self.pos_x + self.tamanho_quadrado > largura:
            self.pos_x = max(0, largura - self.tamanho_quadrado)
        if self.pos_y + self.tamanho_quadrado > altura:
            self.pos_y = max(0, altura - self.tamanho_quadrado)
        
        self.atualizar_canvas()
    
    def atualizar_canvas(self):
        if self.imagem_original is None:
            return
        
        # Redimensionar imagem para caber no canvas
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        if canvas_width < 2 or canvas_height < 2:
            self.root.after(100, self.atualizar_canvas)
            return
        
        # Validar posições
        if self.pos_x is None or self.pos_y is None:
            self.pos_x = 0
            self.pos_y = 0
        
        # Calcular escala
        scale_x = canvas_width / self.imagem_original.width
        scale_y = canvas_height / self.imagem_original.height
        scale = min(scale_x, scale_y)
        
        # Redimensionar imagem
        nova_largura = int(self.imagem_original.width * scale)
        nova_altura = int(self.imagem_original.height * scale)
        imagem_redimensionada = self.imagem_original.resize((nova_largura, nova_altura), Image.Resampling.LANCZOS)
        
        # Criar imagem com retângulo de seleção
        imagem_copia = imagem_redimensionada.copy()
        
        # Desenhar retângulo de seleção
        from PIL import ImageDraw
        draw = ImageDraw.Draw(imagem_copia)
        
        x1 = int(self.pos_x * scale)
        y1 = int(self.pos_y * scale)
        x2 = int((self.pos_x + self.tamanho_quadrado) * scale)
        y2 = int((self.pos_y + self.tamanho_quadrado) * scale)
        
        # Desenhar retângulo verde brilhante
        draw.rectangle([x1, y1, x2, y2], outline="lime", width=3)
        
        # Desenhar alças nos cantos
        tamanho_alca = 8
        for px, py in [(x1, y1), (x2, y1), (x1, y2), (x2, y2)]:
            draw.ellipse([px-tamanho_alca, py-tamanho_alca, px+tamanho_alca, py+tamanho_alca], 
                        fill="lime", outline="white")
        
        self.imagem_tk = ImageTk.PhotoImage(imagem_copia)
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.imagem_tk, anchor="nw")
        
        # Armazenar escala para cálculos de mouse
        self.escala_canvas = scale
        self.offset_x = 0
        self.offset_y = 0
    
    def atualizar_info(self):
        info = f"Imagem {self.indice_atual + 1}/{len(self.arquivos_avif)} - {self.arquivos_avif[self.indice_atual]} | " \
               f"Original: {self.imagem_original.width}x{self.imagem_original.height} | " \
               f"Clique e arraste para mover | Duplo clique para redimensionar"
        self.label_info.config(text=info)
    
    def movimento_mouse(self, event):
        if self.imagem_original is None or not hasattr(self, 'escala_canvas'):
            return
        
        x_real = event.x / self.escala_canvas
        y_real = event.y / self.escala_canvas
        
        # Detectar se está perto de uma alça para redimensionar
        distancia_alca = 10 / self.escala_canvas
        
        canto_esq_sup = abs(x_real - self.pos_x) < distancia_alca and abs(y_real - self.pos_y) < distancia_alca
        canto_dir_inf = abs(x_real - (self.pos_x + self.tamanho_quadrado)) < distancia_alca and \
                        abs(y_real - (self.pos_y + self.tamanho_quadrado)) < distancia_alca
        
        if canto_esq_sup or canto_dir_inf:
            self.canvas.config(cursor="fleur")
        else:
            self.canvas.config(cursor="crosshair")
    
    def inicio_arrasto(self, event):
        if self.imagem_original is None or not hasattr(self, 'escala_canvas'):
            return
        
        x_real = event.x / self.escala_canvas
        y_real = event.y / self.escala_canvas
        
        # Verificar se está dentro do retângulo
        if (self.pos_x <= x_real <= self.pos_x + self.tamanho_quadrado and 
            self.pos_y <= y_real <= self.pos_y + self.tamanho_quadrado):
            self.arrastando = True
            self.mouse_inicio_x = x_real
            self.mouse_inicio_y = y_real
            self.drag_inicio_x = self.pos_x
            self.drag_inicio_y = self.pos_y
    
    def durante_arrasto(self, event):
        if not self.arrastando or self.imagem_original is None or not hasattr(self, 'escala_canvas'):
            return
        
        x_real = event.x / self.escala_canvas
        y_real = event.y / self.escala_canvas
        
        dx = x_real - self.mouse_inicio_x
        dy = y_real - self.mouse_inicio_y
        
        novo_x = self.drag_inicio_x + dx
        novo_y = self.drag_inicio_y + dy
        
        # Limitar dentro da imagem
        novo_x = max(0, min(novo_x, self.imagem_original.width - self.tamanho_quadrado))
        novo_y = max(0, min(novo_y, self.imagem_original.height - self.tamanho_quadrado))
        
        self.pos_x = int(novo_x)
        self.pos_y = int(novo_y)
        
        self.atualizar_canvas()
    
    def fim_arrasto(self, event):
        self.arrastando = False
    
    def salvar_crop(self):
        if self.imagem_original is None:
            return
        
        try:
            # Crop
            img_croppada = self.imagem_original.crop((
                self.pos_x, self.pos_y,
                self.pos_x + self.tamanho_quadrado,
                self.pos_y + self.tamanho_quadrado
            ))
            
            # Salvar
            caminho = os.path.join(self.pasta, self.arquivos_avif[self.indice_atual])
            img_croppada.save(caminho, 'AVIF', quality=85)
            
            messagebox.showinfo("Sucesso", f"Crop salvo para {self.arquivos_avif[self.indice_atual]}")
            self.proximo()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar: {e}")
    
    def pular(self):
        self.proximo()
    
    def proximo(self):
        self.indice_atual += 1
        self.carregar_imagem()
    
    def anterior(self):
        if self.indice_atual > 0:
            self.indice_atual -= 1
            self.carregar_imagem()

if __name__ == "__main__":
    root = tk.Tk()
    app = CropadorImagens(root)
    root.mainloop()
