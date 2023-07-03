import tkinter as tk


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("920x540")
        self.root.resizable(width=False, height=False)
        self.root.title("KD - Budget App")
        self.lblHeading = tk.Label(self.root, text="Monthly Budget App",
                                   font=("sans-serif", 24),
                                   bg="#444444", fg="aquaMarine",
                                   width=45)
        self.lblHeading.grid(row=0, column=0, columnspan=2)
        self.draw("Monthly Budget App")
        self.button()
        
        self.root.mainloop()
    
    def draw(self, msg):
        self.textBox = tk.Text(width=50, height=19, bg="#333333", fg="aquaMarine", bd="5px", relief="flat")
        self.textBox.insert(1.0, msg)
        self.textBox.grid(row=1, column=0, pady=50)
        
    
    def button(self):
        self.frame = tk.Frame(self.root, height=1, width=50)
        self.frame.grid(row=1, column=1, sticky="W")
        self.entAmount = tk.Entry(self.frame, font=12, bg="#333333", fg="aquaMarine")
        self.entAmount.grid(row=0, column=0)
        self.entAmount.focus()
        self.btnCalculate = tk.Button(self.frame, text="Calculate Budget", bg="#333333", fg="aquaMarine")
        self.btnCalculate.grid(row=0, column=1)

if __name__ == "__main__":
    MainWindow()