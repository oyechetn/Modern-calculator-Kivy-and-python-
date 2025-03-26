import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ok Calculator")
        self.root.geometry("300x400")
        self.root.configure(bg="black")  
        
        self.display = tk.Entry(root, font=("Arial", 20), bd=5, insertwidth=4, 
                                width=14, borderwidth=4, justify="right", bg="black", fg="white")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['⌫', '0', '=', '+'],
            ['Clear']
        ]
        
        for i, row in enumerate(buttons):
            for j, label in enumerate(row):
                button = tk.Button(root, text=label, padx=20, pady=20, font=("Arial", 18), 
                                   command=lambda lbl=label: self.on_button_press(lbl), 
                                   bg="black", fg="white", activebackground="grey", activeforeground="white")
                button.grid(row=i+1, column=j, sticky="nsew")
        
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            root.grid_columnconfigure(j, weight=1)

        root.bind("<Key>", self.on_keypress)

    def on_button_press(self, label):
        current = self.display.get()
        
        if label == 'Clear':  
            self.display.delete(0, tk.END)
        elif label == '=':  
            try:
                result = eval(current)  
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif label == '⌫':  
            self.display.delete(len(current) - 1, tk.END)
        else:  
            self.display.insert(tk.END, label)

    def on_keypress(self, event):
        key = event.char
        if key.isdigit() or key in "+-*/=":
            self.on_button_press(key)
        elif key == "\r":  # Enter key
            self.on_button_press("=")
        elif key == "\x08":  # Backspace key
            self.on_button_press("⌫")

# Run
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
