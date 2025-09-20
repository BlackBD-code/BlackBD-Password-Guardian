# BlackBD Password Guardian
# Gift for 69k Community by BlackBD Cyber Security

import re
import secrets
import stri#!/usr/bin/env python3
ng
from tkinter import *
from tkinter import ttk, messagebox

class BlackBDPasswordGuardian:
    def __init__(self):
        self.root = Tk()
        self.root.title("BlackBD Password Guardian - Free Gift")
        self.root.geometry("500x600")
        self.root.configure(bg="#1a1a1a")
        
        # Header
        header = Label(self.root, text="🛡️ BlackBD Password Guardian", 
                      font=("Arial", 18, "bold"), fg="#00ff00", bg="#1a1a1a")
        header.pack(pady=20)
        
        subtitle = Label(self.root, text="Free Gift for 69k Community Members", 
                        font=("Arial", 10), fg="#888888", bg="#1a1a1a")
        subtitle.pack()
        
        # Password Check Section
        check_frame = Frame(self.root, bg="#1a1a1a")
        check_frame.pack(pady=20, padx=20, fill="x")
        
        Label(check_frame, text="🔍 Check Password Strength:", 
              font=("Arial", 12, "bold"), fg="white", bg="#1a1a1a").pack(anchor="w")
        
        self.password_entry = Entry(check_frame, font=("Arial", 10), width=40, show="*")
        self.password_entry.pack(pady=5, fill="x")
        self.password_entry.bind("<KeyRelease>", self.check_password)
        
        self.strength_label = Label(check_frame, text="Password strength will appear here...", 
                                   font=("Arial", 10), fg="#888888", bg="#1a1a1a")
        self.strength_label.pack(anchor="w", pady=5)
        
        # Progress Bar
        self.progress = ttk.Progressbar(check_frame, length=300, mode='determinate')
        self.progress.pack(pady=5, fill="x")
        
        # Generate Section
        gen_frame = Frame(self.root, bg="#1a1a1a")
        gen_frame.pack(pady=20, padx=20, fill="x")
        
        Label(gen_frame, text="🎲 Generate Secure Password:", 
              font=("Arial", 12, "bold"), fg="white", bg="#1a1a1a").pack(anchor="w")
        
        options_frame = Frame(gen_frame, bg="#1a1a1a")
        options_frame.pack(fill="x", pady=5)
        
        Label(options_frame, text="Length:", fg="white", bg="#1a1a1a").grid(row=0, column=0, sticky="w")
        self.length_var = IntVar(value=12)
        length_spinbox = Spinbox(options_frame, from_=8, to=64, textvariable=self.length_var, width=5)
        length_spinbox.grid(row=0, column=1, padx=5)
        
        self.include_symbols = BooleanVar(value=True)
        Checkbutton(options_frame, text="Symbols", variable=self.include_symbols, 
                   fg="white", bg="#1a1a1a", selectcolor="#333333").grid(row=0, column=2, padx=5)
        
        self.include_numbers = BooleanVar(value=True)
        Checkbutton(options_frame, text="Numbers", variable=self.include_numbers, 
                   fg="white", bg="#1a1a1a", selectcolor="#333333").grid(row=0, column=3, padx=5)
        
        generate_btn = Button(gen_frame, text="🎯 Generate Password", 
                             command=self.generate_password, bg="#00aa00", fg="white", 
                             font=("Arial", 10, "bold"))
        generate_btn.pack(pady=10)
        
        self.generated_password = Text(gen_frame, height=3, font=("Courier", 10))
        self.generated_password.pack(fill="x", pady=5)
        
        copy_btn = Button(gen_frame, text="📋 Copy to Clipboard", 
                         command=self.copy_password, bg="#0066cc", fg="white")
        copy_btn.pack(pady=5)
        
        # Footer
        footer = Label(self.root, text="Made with ❤️ for BlackBD Community | Stay Secure!", 
                      font=("Arial", 8), fg="#666666", bg="#1a1a1a")
        footer.pack(side="bottom", pady=10)
        
    def check_password(self, event=None):
        password = self.password_entry.get()
        if not password:
            self.strength_label.config(text="Password strength will appear here...", fg="#888888")
            self.progress['value'] = 0
            return
        
        score = 0
        feedback = []
        
        # Length check
        if len(password) >= 12:
            score += 25
        elif len(password) >= 8:
            score += 15
            feedback.append("Consider longer password")
        else:
            feedback.append("Too short (minimum 8 characters)")
        
        # Character variety
        if re.search(r'[a-z]', password):
            score += 15
        else:
            feedback.append("Add lowercase letters")
            
        if re.search(r'[A-Z]', password):
            score += 15
        else:
            feedback.append("Add uppercase letters")
            
        if re.search(r'\d', password):
            score += 15
        else:
            feedback.append("Add numbers")
            
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            score += 20
        else:
            feedback.append("Add special characters")
        
        # Common patterns
        if re.search(r'(.)\1{2,}', password):
            score -= 10
            feedback.append("Avoid repeated characters")
        
        # Update display
        self.progress['value'] = min(score, 100)
        
        if score >= 80:
            status = "🛡️ Very Strong"
            color = "#00ff00"
        elif score >= 60:
            status = "💪 Strong"
            color = "#88ff00"
        elif score >= 40:
            status = "⚠️ Moderate"
            color = "#ffaa00"
        else:
            status = "❌ Weak"
            color = "#ff4444"
        
        result_text = f"{status} ({score}/100)"
        if feedback:
            result_text += f" | Tips: {', '.join(feedback[:2])}"
        
        self.strength_label.config(text=result_text, fg=color)
    
    def generate_password(self):
        length = self.length_var.get()
        chars = string.ascii_letters
        
        if self.include_numbers.get():
            chars += string.digits
        if self.include_symbols.get():
            chars += "!@#$%^&*(),.?\":{}|<>"
        
        password = ''.join(secrets.choice(chars) for _ in range(length))
        
        self.generated_password.delete(1.0, END)
        self.generated_password.insert(1.0, f"Generated Password:\n{password}\n\nSave this securely!")
    
    def copy_password(self):
        try:
            content = self.generated_password.get(1.0, END)
            password_line = content.split('\n')[1]
            self.root.clipboard_clear()
            self.root.clipboard_append(password_line)
            messagebox.showinfo("Success", "Password copied to clipboard!")
        except:
            messagebox.showwarning("Error", "No password to copy!")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = BlackBDPasswordGuardian()
    app.run()
