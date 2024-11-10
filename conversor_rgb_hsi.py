import tkinter as tk
from math import acos, sqrt, pi
from tkinter import messagebox


def rgb_para_hsi(r, g, b):

    r, g, b = r / 255, g / 255, b / 255

    # Calcular a intensidade
    intensidade = (r + g + b) / 3

    min_rgb = min(r, g, b)
    if intensidade > 0:
        saturacao = 1 - min_rgb / intensidade
    else:
        saturacao = 0

    if saturacao == 0:
        matiz = 0  # Se não houver cor, matiz é indefinido, então definimos como 0
    else:
        num = 0.5 * ((r - g) + (r - b))
        denom = sqrt((r - g)**2 + (r - b) * (g - b))
        theta = acos(num / denom) if denom != 0 else 0

        if b <= g:
            matiz = theta * (180 / pi)
        else:
            matiz = 360 - theta * (180 / pi)

    return round(matiz, 2), round(saturacao, 2), round(intensidade, 2)


def atualizar_cores():
    try:
        r = int(entrada_r.get())
        g = int(entrada_g.get())
        b = int(entrada_b.get())

        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            raise ValueError("Valores de R, G, B devem estar entre 0 e 255.")

        # Atualizar o retângulo de cor RGB
        cor_rgb = f'#{r:02x}{g:02x}{b:02x}'
        rgb_canvas.create_rectangle(0, 0, 100, 100, fill=cor_rgb, outline="")

        # Converter para HSI e atualizar o retângulo de cor HSI
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
    # Limpar entradas e valores de HSI
    entrada_r.delete(0, tk.END)
    entrada_g.delete(0, tk.END)
    entrada_b.delete(0, tk.END)
    
    # Limpar a cor exibida nos retângulos
    rgb_canvas.delete("all")
    hsi_canvas.delete("all")
    
    # Redefinir os valores dos rótulos HSI
    label_matiz_valor.config(text="Hue: ")
    label_sat_valor.config(text="Saturação: ")
    label_int_valor.config(text="Intensidade: ")
    
root = tk.Tk()
root.title("Conversor RGB para HSI")

# Entradas e rótulos RGB
tk.Label(root, text="R:").grid(row=1, column=0)
tk.Label(root, text="G:").grid(row=2, column=0)
tk.Label(root, text="B:").grid(row=3, column=0)

entrada_r = tk.Entry(root, width=5, fg="red") 
entrada_r.grid(row=1, column=1)
entrada_g = tk.Entry(root, width=5, fg="green")  
entrada_g.grid(row=2, column=1)
entrada_b = tk.Entry(root, width=5, fg="blue")  
entrada_b.grid(row=3, column=1)

# Exibir cor RGB
rgb_canvas = tk.Canvas(root, width=100, height=100)
rgb_canvas.grid(row=0, column=1)
tk.Label(root, text="Modelo RGB").grid(row=0, column=0)

# Exibir cor HSI
hsi_canvas = tk.Canvas(root, width=100, height=100)
hsi_canvas.grid(row=0, column=3)
tk.Label(root, text="Modelo HSI").grid(row=0, column=2)


label_matiz_valor = tk.Label(root, text="Hue: ")
label_matiz_valor.grid(row=1, column=2)
label_sat_valor = tk.Label(root, text="Saturação: ")
label_sat_valor.grid(row=2, column=2)
label_int_valor = tk.Label(root, text="Intensidade: ")
label_int_valor.grid(row=3, column=2)


botao_converter = tk.Button(root, text="Converter", command=atualizar_cores)
botao_converter.grid(row=4, column=1)
botao_limpar = tk.Button(root, text="Limpar", command=limpar_campos)
botao_limpar.grid(row=4, column=2)

root.mainloop()
