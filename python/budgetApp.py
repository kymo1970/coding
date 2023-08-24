import tkinter as tk


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.config(bg="#333333")
        self.root.geometry("920x540")
        self.root.resizable(width=False, height=False)
        self.root.title("KD - Budget App")
        self.lblHeading = tk.Label(self.root, text="Monthly Budget App",
                                   font=("sans-serif", 24),
                                   bg="#333333", fg="aquaMarine",
                                   width=45)
        self.lblHeading.grid(row=0, column=0, columnspan=2, pady=50)
        self.draw()
        self.button()
        
        self.root.mainloop()
        
    def calculateBudget(self):
        pass
    
    def draw(self):
        self.textBox = tk.Text(width=20, height=20, bg="#333333", fg="aquaMarine", bd="2px", relief="solid")
        self.textBox.grid(row=2, column=0)
        self.lblTextBox = tk.Label(self.root, text="Accounts", font=("sans-serif", 18), bg="#333333", fg="aquaMarine")
        self.lblTextBox.grid(row=1, column=0)
        
    
    def button(self):
        self.frame = tk.Frame(self.root, height=1, width=50, bg="#333333")
        self.frame.grid(row=1, column=1, sticky="W")
        self.entAmount = tk.Entry(self.frame, font=12, bg="#333333", fg="aquaMarine", relief="solid")
        self.entAmount.grid(row=0, column=0, padx="10px")
        self.entAmount.focus()
        self.btnCalculate = tk.Button(self.frame, text="Calculate Budget", font=("sans-serif", 12), bg="#333333", fg="aquaMarine", command=self.calculateBudget)
        self.btnCalculate.grid(row=0, column=1, ipadx="15px", ipady="5px")

if __name__ == "__main__":
    MainWindow()