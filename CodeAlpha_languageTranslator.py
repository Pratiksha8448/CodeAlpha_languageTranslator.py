import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# Function to handle translation
def translate_text():
    source_text = text_input.get("1.0", tk.END).strip()
    target_lang = lang_box.get()
    
    if not source_text:
        messagebox.showwarning("Warning", "Please enter some text to translate.")
        return
        
    # Mapping display names to language codes
    lang_mapping = {"Spanish": "es", "French": "fr", "German": "de", "Hindi": "hi", "Arabic": "ar"}
    lang_code = lang_mapping.get(target_lang, "en")

    try:
        # Automatically detects source language, translates to target
        translated = GoogleTranslator(source='auto', target=lang_code).translate(source_text)
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, translated)
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {e}")

# Setup the main UI Window
root = tk.Tk()
root.title("CodeAlpha Language Translator")
root.geometry("500x450")

# Input Label & Text Box
tk.Label(root, text="Enter Text (Auto-detect Language):", font=("Arial", 10, "bold")).pack(pady=5)
text_input = tk.Text(root, height=6, width=55)
text_input.pack(pady=5)

# Target Language Selection
tk.Label(root, text="Select Target Language:", font=("Arial", 10, "bold")).pack(pady=5)
languages = ["Spanish", "French", "German", "Hindi", "Arabic"]
lang_box = ttk.Combobox(root, values=languages, state="readonly")
lang_box.set("Spanish")
lang_box.pack(pady=5)

# Translate Button
translate_btn = tk.Button(root, text="Translate", command=translate_text, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
translate_btn.pack(pady=10)

# Output Label & Text Box
tk.Label(root, text="Translated Text:", font=("Arial", 10, "bold")).pack(pady=5)
text_output = tk.Text(root, height=6, width=55)
text_output.pack(pady=5)

root.mainloop()