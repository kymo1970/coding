import tkinter as tk


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("920x540")
        self.root.resizable(width=False, height=False)
        self.root.title("KD - Budget App")
        self.lblHeading = tk.Label(text="Monthly Budget App",
                                   font=("sans-serif", 24),
                                   bg="#444444", fg="aquaMarine",
                                   width=45)
        self.lblHeading.grid(row=0, column=0, padx=30, pady=10)
        self.draw("Monthly Budget App")
        
        self.root.mainloop()
    
    def draw(self, msg):
        self.textBox = tk.Text(width=50, height=19, bg="#444444", fg="aquaMarine")
        self.textBox.insert(1.0, msg)
        self.textBox.grid(row=1, column=0, padx=10, pady=10)
        
    
    def button(self):
        self.frame = tk.Frame(self.root, height=1, width=50)
        self.frame.grid(row=1, column=1)
        self.entAmount = tk.Entry(self.frame, font=12)
        self.entAmount.grid(row=0, column=0)
        self.btnCalculate = tk.Button(self.frame, text="Calculate")
        self.btnCalculate.grid(row=0, column=1)

if __name__ == "__main__":
    MainWindow()