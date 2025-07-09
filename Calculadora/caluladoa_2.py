import customtkinter as ctk

class FlatCalculator(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora Flat")
        self.geometry("300x400")
        ctk.set_appearance_mode("light")  # ou "darck"
        ctk.set_default_color_theme("dark-blue")

        self.expression = ""

        # Display
        self.display = ctk.CTkEntry(self, font=("Arial", 24), justify="right")
        self.display.pack(padx=10, pady=20, fill="both")

        # Grade de botões
        btn_frame = ctk.CTkFrame(self)
        btn_frame.pack(expand=True, fill="both")

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]

        for row in buttons:
            row_frame = ctk.CTkFrame(btn_frame)
            row_frame.pack(expand=True, fill="both")
            for char in row:
                btn = ctk.CTkButton(row_frame, text=char, font=("Arial", 18),
                                    command=lambda c=char: self.on_click(c))
                btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)

    def on_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "=":
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Erro"
        else:
            self.expression += str(char)
        self.display.delete(0, "end")
        self.display.insert("end", self.expression)

if __name__ == "__main__":
    app = FlatCalculator()
    app.mainloop()
