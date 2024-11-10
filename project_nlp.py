import tkinter as tk
import ttkbootstrap as ttk
from googletrans import Translator

# Initialize the Translator
translator = Translator()

# Function to translate text to Hindi 
def translate_to_Hindi():
    input_text = input_text_box.get("1.0", tk.END).strip()
    translation = translator.translate(input_text, dest='hi')
    translated_text_box.config(state=tk.NORMAL) 
    translated_text_box.delete("1.0", tk.END)
    translated_text_box.insert(tk.END, translation.text)
    translated_text_box.config(state=tk.DISABLED)  

# Set up the main GUI window
root = ttk.Window(themename="darkly")
root.title("English to Hindi Translator")
root.geometry("400x300")

# Input
input_label = ttk.Label(root, text="Enter text in English:")
input_label.pack(pady=10)

input_text_box = ttk.Text(root, height=5, width=40)
input_text_box.pack(pady=5)

# Translate button
translate_button = ttk.Button(root, text="Translate to Hindi", command=translate_to_Hindi)
translate_button.pack(pady=10)

# Output
output_label = ttk.Label(root, text="Translation in Hindi:")
output_label.pack(pady=10)

translated_text_box = ttk.Text(root, height=5, width=40, state=tk.DISABLED)
translated_text_box.pack(pady=5)

# Run the application
root.mainloop()
