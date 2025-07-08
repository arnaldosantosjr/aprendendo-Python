import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Simples")
        master.geometry("300x400") # Define o tamanho inicial da janela
        master.resizable(False, False) # Impede que a janela seja redimensionada

        self.expression = ""
        self.input_text = tk.StringVar()

        # Display da calculadora
        self.input_frame = tk.Frame(master, bd=0, relief="flat", bg="#eee") # << Crie o frame primeiro
        self.input_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.input_field = tk.Entry(self.input_frame, font=('arial', 18, 'bold'), # << Crie o Entry depois do frame
                                    textvariable=self.input_text, width=20, bg="#eee",
                                    bd=0, justify=tk.RIGHT, state='readonly')
        self.input_field.grid(row=0, column=0, ipady=10, sticky="nsew") # << Agora configure-o
        self.input_frame.grid_columnconfigure(0, weight=1) # << E configure o peso da coluna do frame

        # Frame para os botões
        self.btns_frame = tk.Frame(master, bg="#ccc")
        self.btns_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        for i in range(4): # Temos 4 colunas de botões (0 a 3)
            self.btns_frame.grid_columnconfigure(i, weight=1)
        for i in range(5): # Temos 5 linhas de botões (0 a 4)
            self.btns_frame.grid_rowconfigure(i, weight=1)

        # Linhas de botões
        # Linha 1: C, /, *, -
        self.create_button("C", 0, 0, command=self.clear_all, bg="#f00", fg="white")
        self.create_button("/", 0, 1, command=lambda: self.button_click("/"), bg="#f7f7f7")
        self.create_button("*", 0, 2, command=lambda: self.button_click("*"), bg="#f7f7f7")
        self.create_button("-", 0, 3, command=lambda: self.button_click("-"), bg="#f7f7f7")

        # Linha 2: 7, 8, 9, +
        self.create_button("7", 1, 0, command=lambda: self.button_click("7"))
        self.create_button("8", 1, 1, command=lambda: self.button_click("8"))
        self.create_button("9", 1, 2, command=lambda: self.button_click("9"))
        self.create_button("+", 1, 3, command=lambda: self.button_click("+"), rowspan=2, bg="#f7f7f7")

        # Linha 3: 4, 5, 6
        self.create_button("4", 2, 0, command=lambda: self.button_click("4"))
        self.create_button("5", 2, 1, command=lambda: self.button_click("5"))
        self.create_button("6", 2, 2, command=lambda: self.button_click("6"))

        # Linha 4: 1, 2, 3
        self.create_button("1", 3, 0, command=lambda: self.button_click("1"))
        self.create_button("2", 3, 1, command=lambda: self.button_click("2"))
        self.create_button("3", 3, 2, command=lambda: self.button_click("3"))

        # Linha 5: 0, ., =
        self.create_button("0", 4, 0, command=lambda: self.button_click("0"), columnspan=2)
        self.create_button(".", 4, 2, command=lambda: self.button_click("."))
        self.create_button("=", 3, 3, command=self.evaluate_expression, rowspan=2, bg="#5cb85c", fg="white")

    def create_button(self, text, row, column, command, bg="#fff", fg="black", rowspan=1, columnspan=1):
        button = tk.Button(self.btns_frame, text=text, fg=fg, bg=bg,
                           command=command, height=2, width=8,
                           font=('arial', 12, 'bold'))
        button.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, padx=1, pady=1, sticky="nsew")

    def button_click(self, item):
        self.expression += str(item)
        self.input_text.set(self.expression)

    def clear_all(self):
        self.expression = ""
        self.input_text.set("")

    def evaluate_expression(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except Exception as e:
            messagebox.showerror("Erro", "Expressão Inválida")
            self.expression = ""
            self.input_text.set("")

# Iniciar a aplicação
root = tk.Tk()
my_calculator = Calculator(root)
root.mainloop()