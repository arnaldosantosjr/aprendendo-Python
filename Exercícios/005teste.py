import tkinter as tk
from tkinter import messagebox

def calcular_imc():
    try:
        nome = entry_nome.get().strip()
        genero = var_genero.get()
        peso = float(entry_peso.get().strip())
        altura = float(entry_altura.get().strip())

        if peso <= 0 or altura <= 0:
            raise ValueError("Peso e altura devem ser maiores que zero.")

        imc = peso / (altura ** 2)
        resultado = f"{nome}, o seu IMC é: {imc:.2f}\n"

        if genero == "h":
            if imc < 20:
                resultado += "Você está abaixo do peso normal"
            elif imc < 24.9:
                resultado += "Você está no peso ideal"
            elif imc < 29.9:
                resultado += "Você está com obesidade leve"
            elif imc < 39.9:
                resultado += "Você está com obesidade moderada"
            else:
                resultado += "Você está com obesidade mórbida"
        elif genero == "m":
            if imc < 19:
                resultado += "Você está abaixo do peso normal"
            elif imc < 23.9:
                resultado += "Você está no peso ideal"
            elif imc < 28.9:
                resultado += "Você está com obesidade leve"
            elif imc < 38.9:
                resultado += "Você está com obesidade moderada"
            else:
                resultado += "Você está com obesidade mórbida"
        else:
            resultado = "Selecione um gênero válido."

        messagebox.showinfo("Resultado", resultado)

    except ValueError:
        messagebox.showerror("Erro", "Insira valores válidos para peso e altura.")

# Janela principal
janela = tk.Tk()
janela.title("Calculadora de IMC")

# Nome
tk.Label(janela, text="Nome:").grid(row=0, column=0)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1)

# Gênero
tk.Label(janela, text="Gênero:").grid(row=1, column=0)
var_genero = tk.StringVar(value="h")
tk.Radiobutton(janela, text="Homem", variable=var_genero, value="h").grid(row=1, column=1, sticky="w")
tk.Radiobutton(janela, text="Mulher", variable=var_genero, value="m").grid(row=1, column=2, sticky="w")

# Peso
tk.Label(janela, text="Peso (kg):").grid(row=2, column=0)
entry_peso = tk.Entry(janela)
entry_peso.grid(row=2, column=1)

# Altura
tk.Label(janela, text="Altura (m):").grid(row=3, column=0)
entry_altura = tk.Entry(janela)
entry_altura.grid(row=3, column=1)

# Botão calcular
botao = tk.Button(janela, text="Calcular IMC", command=calcular_imc)
botao.grid(row=4, column=0, columnspan=2, pady=10)

janela.mainloop()
