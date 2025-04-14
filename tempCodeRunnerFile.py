import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import pandas as pd
import json

class CSVtoJSONApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor CSV para JSON")
        self.root.geometry("600x400")

        # Botão para carregar CSV
        self.btn_load = tk.Button(root, text="Selecionar CSV", command=self.load_csv)
        self.btn_load.pack(pady=10)

        # Área de visualização dos dados
        self.text_area = scrolledtext.ScrolledText(root, width=70, height=15)
        self.text_area.pack()

        # Botão para exportar JSON
        self.btn_export = tk.Button(root, text="Exportar como JSON", command=self.export_json, state=tk.DISABLED)
        self.btn_export.pack(pady=10)

        self.df = None  # onde vamos armazenar os dados lidos

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                self.df = pd.read_csv(file_path)
                self.text_area.delete('1.0', tk.END)  # limpa a área de texto
                self.text_area.insert(tk.END, self.df.head().to_string())  # mostra as primeiras linhas
                self.btn_export.config(state=tk.NORMAL)  # ativa o botão de exportar
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível ler o arquivo CSV.\n{str(e)}")

    def export_json(self):
        if self.df is not None:
            file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
            if file_path:
                try:
                    self.df.to_json(file_path, orient='records', indent=4)
                    messagebox.showinfo("Sucesso", "Arquivo JSON exportado com sucesso!")
                except Exception as e:
                    messagebox.showerror("Erro", f"Não foi possível salvar o arquivo JSON.\n{str(e)}")

# Executa o app
if __name__ == "__main__":
    root = tk.Tk()
    app = CSVtoJSONApp(root)
    root.mainloop()
