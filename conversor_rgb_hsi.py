import tkinter as tk
from math import acos, sqrt, pi
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw
import numpy as np

def rgb_para_hsi(r, g, b):
    r, g, b = r / 255, g / 255, b / 255

    intensidade = (r + g + b) / 3
    min_rgb = min(r, g, b)
    if intensidade > 0:
        saturacao = 1 - min_rgb / intensidade
    else:
        saturacao = 0

    if saturacao == 0:
        matiz = 0
    else:
        num = 0.5 * ((r - g) + (r - b))
        denom = sqrt((r - g)**2 + (r - b) * (g - b))
        theta = acos(num / denom) if denom != 0 else 0

        if b <= g:
            matiz = theta * (180 / pi)
        else:
            matiz = 360 - theta * (180 / pi)

    return round(matiz, 2), round(saturacao, 2), round(intensidade, 2)

def criar_ciclo_de_cores():
    size = 200
    image = Image.new("RGBA", (size, size), (0, 0, 0, 0))  # Transparente
    draw = ImageDraw.Draw(image)

    for x in range(size):
        for y in range(size):
            dx, dy = x - size / 2, y - size / 2
            distance = sqrt(dx * dx + dy * dy)
            if distance <= size / 2:
                angle = (np.arctan2(dy, dx) + pi) / (2 * pi)
                sat = distance / (size / 2)
                r, g, b = hsv_para_rgb(angle, sat, 1)
                draw.point((x, y), (int(r * 255), int(g * 255), int(b * 255), 255))

    return ImageTk.PhotoImage(image), image

def hsv_para_rgb(h, s, v):
    i = int(h * 6)
    f = h * 6 - i
    p, q, t = v * (1 - s), v * (1 - f * s), v * (1 - (1 - f) * s)
    i = i % 6
    if i == 0: return v, t, p
    if i == 1: return q, v, p
    if i == 2: return p, v, t
    if i == 3: return p, q, v
    if i == 4: return t, p, v
    if i == 5: return v, p, q

def selecionar_cor(event):
    x, y = event.x, event.y
    if 0 <= x < 200 and 0 <= y < 200:
        rgb = ciclo_de_cores_image.getpixel((x, y))
        if rgb[3] > 0:  # Somente se o pixel não for transparente
            r, g, b = rgb[0], rgb[1], rgb[2]

            entrada_r.delete(0, tk.END)
            entrada_r.insert(0, str(r))
            entrada_g.delete(0, tk.END)
            entrada_g.insert(0, str(g))
            entrada_b.delete(0, tk.END)
            entrada_b.insert(0, str(b))

            atualizar_cores()

def atualizar_cores():
    try:
        r = int(entrada_r.get())
        g = int(entrada_g.get())
        b = int(entrada_b.get())

        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            raise ValueError("Valores de R, G, B devem estar entre 0 e 255.")

        cor_rgb = f'#{r:02x}{g:02x}{b:02x}'
        rgb_canvas.create_rectangle(0, 0, 100, 100, fill=cor_rgb, outline="")

        matiz, saturacao, intensidade = rgb_para_hsi(r, g, b)
        hsi_canvas.create_rectangle(0, 0, 100, 100, fill=cor_rgb, outline="")

        label_matiz_valor.config(text=f"Hue: {matiz}")
        label_sat_valor.config(text=f"Saturação: {saturacao}")
        label_int_valor.config(text=f"Intensidade: {intensidade}")

    except ValueError:
        messagebox.showerror(
            "Erro de Entrada", "Por favor, insira valores inteiros entre 0 e 255 para R, G e B.")
        limpar_campos()

def limpar_campos():
    entrada_r.delete(0, tk.END)
    entrada_g.delete(0, tk.END)
    entrada_b.delete(0, tk.END)

    rgb_canvas.delete("all")
    hsi_canvas.delete("all")

    label_matiz_valor.config(text="Hue: ")
    label_sat_valor.config(text="Saturação: ")
    label_int_valor.config(text="Intensidade: ")

root = tk.Tk()
root.title("Conversor RGB para HSI")
root.geometry("650x600")
root.config(bg="#f0f0f0")

# Título
titulo_label = tk.Label(root, text="Conversor RGB para HSI", font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#333")
titulo_label.grid(row=0, column=3, columnspan=5, pady=20)

# Ciclo de cores
ciclo_de_cores_photo, ciclo_de_cores_image = criar_ciclo_de_cores()
ciclo_canvas = tk.Canvas(root, width=200, height=200, highlightthickness=0, bg=root.cget('bg'))
ciclo_canvas.grid(row=1, column=3)
ciclo_canvas.create_image(0, 0, anchor=tk.NW, image=ciclo_de_cores_photo)
ciclo_canvas.bind("<Button-1>", selecionar_cor)

# Labels e entradas
tk.Label(root, text="R:", font=("Arial", 12), bg="#f0f0f0").grid(row=2, column=0, )
tk.Label(root, text="G:", font=("Arial", 12), bg="#f0f0f0").grid(row=2, column=2,)
tk.Label(root, text="B:", font=("Arial", 12), bg="#f0f0f0").grid(row=2, column=4, )



entrada_r = tk.Entry(root, width=5, fg="red", font=("Arial", 12))
entrada_r.grid(row=2, column=1)
entrada_g = tk.Entry(root, width=5, fg="green", font=("Arial", 12))
entrada_g.grid(row=2, column=3)
entrada_b = tk.Entry(root, width=5, fg="blue", font=("Arial", 12))
entrada_b.grid(row=2, column=5)

# Canvas para mostrar cores
rgb_canvas = tk.Canvas(root, width=100, height=100, bg="#ffffff")
rgb_canvas.grid(row=1, column=7, padx=10, pady=5)
tk.Label(root, text="Modelo RGB", font=("Arial", 12), bg="#f0f0f0").grid(row=1, column=8)

hsi_canvas = tk.Canvas(root, width=100, height=100, bg="#ffffff")
hsi_canvas.grid(row=2, column=7, padx=10, pady=5)
tk.Label(root, text="Modelo HSI", font=("Arial", 12), bg="#f0f0f0").grid(row=2, column=8)

# Labels para valores
label_matiz_valor = tk.Label(root, text="Hue: ", font=("Arial", 12), bg="#f0f0f0")
label_matiz_valor.grid(row=4, column=0, columnspan=2, pady=5)
label_sat_valor = tk.Label(root, text="Saturação: ", font=("Arial", 12), bg="#f0f0f0")
label_sat_valor.grid(row=5, column=0, columnspan=2, pady=5)
label_int_valor = tk.Label(root, text="Intensidade: ", font=("Arial", 12), bg="#f0f0f0")
label_int_valor.grid(row=6, column=0, columnspan=2, pady=5)

# Botões
botao_converter = tk.Button(root, text="Converter", command=atualizar_cores, font=("Arial", 12), bg="#4CAF50", fg="white")
botao_converter.grid(row=4, column=3, padx=10, pady=20)
botao_limpar = tk.Button(root, text="Limpar", command=limpar_campos, font=("Arial", 12), bg="#f44336", fg="white")
botao_limpar.grid(row=5, column=3, padx=10, pady=5)

root.mainloop()
