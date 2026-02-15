import tkinter as tk
from tkinter import colorchooser
import colorsys

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16)/255.0 for i in (0, 2, 4))

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(
        int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255)
    )

def generate_palette(hex_color):
    base_rgb = hex_to_rgb(hex_color)
    h, l, s = colorsys.rgb_to_hls(*base_rgb)

    palettes = {}
    comp = colorsys.hls_to_rgb((h+0.5)%1, l, s)
    palettes['Complementar'] = [hex_color, rgb_to_hex(comp)]
    ana1 = colorsys.hls_to_rgb((h+0.08)%1, l, s)
    ana2 = colorsys.hls_to_rgb((h-0.08)%1, l, s)
    palettes['Análogas'] = [rgb_to_hex(ana1), hex_color, rgb_to_hex(ana2)]
    tri1 = colorsys.hls_to_rgb((h+1/3)%1, l, s)
    tri2 = colorsys.hls_to_rgb((h+2/3)%1, l, s)
    palettes['Triádicas'] = [hex_color, rgb_to_hex(tri1), rgb_to_hex(tri2)]
    tet1 = colorsys.hls_to_rgb((h+0.25)%1, l, s)
    tet2 = colorsys.hls_to_rgb((h+0.5)%1, l, s)
    tet3 = colorsys.hls_to_rgb((h+0.75)%1, l, s)
    palettes['Tetrádicas'] = [hex_color, rgb_to_hex(tet1), rgb_to_hex(tet2), rgb_to_hex(tet3)]
    return palettes

def mostrar_paletas(hex_cor):
    for widget in frame_resultados.winfo_children():
        widget.destroy()
    paletas = generate_palette(hex_cor)
    tk.Label(frame_resultados, text=f"Esquemas para {hex_cor}:", font=("Arial", 12, "bold")).pack(pady=5)
    for nome, cores in paletas.items():
        bloco = tk.Frame(frame_resultados, pady=2)
        bloco.pack(fill="x")
        tk.Label(bloco, text=nome+":", width=15, anchor="w", font=("Arial", 10)).pack(side="left")
        for c in cores:
            tk.Label(bloco, bg=c, width=10, height=2, relief="ridge").pack(side="left", padx=2)

def escolher_cor():
    cor = colorchooser.askcolor(title="Escolha uma cor")
    if cor[1]:  # cor[1] é o valor hexadecimal
        mostrar_paletas(cor[1])

root = tk.Tk()
root.title("Gerador de Esquemas de Cores")

largura = 650
altura = 450
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
pos_x = (largura_tela // 2) - (largura // 2)
pos_y = (altura_tela // 2) - (altura // 2)
root.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

root.configure(bg="#f0f0f0")

tk.Label(root, text="Gerador de Esquemas de Cores\n\nClique no botão abaixo para escolher uma cor e ver suas harmonias cromáticas:", 
         bg="#f0f0f0", font=("Arial", 12), justify="center").pack(pady=15)

tk.Button(root, text="Escolher Cor", command=escolher_cor, bg="#7b5de6", fg="white", font=("Arial", 12, "bold")).pack(pady=20)

frame_resultados = tk.Frame(root, bg="#f0f0f0")
frame_resultados.pack(pady=10, fill="both", expand=True)

root.mainloop()
