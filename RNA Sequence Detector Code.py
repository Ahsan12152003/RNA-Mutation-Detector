import tkinter as tk
from tkinter import messagebox

def find_mutations(seq1, seq2):
    mutations = []
    min_len = min(len(seq1), len(seq2))
    
    for i in range(min_len):
        if seq1[i] != seq2[i]:
            mutations.append(f"Position {i+1}: {seq1[i]} → {seq2[i]}")
    
    if len(seq1) != len(seq2):
        mutations.append("Sequences have different lengths.")
    
    return "\n".join(mutations) if mutations else "No mutations detected."

def detect_mutations():
    seq1 = entry_seq1.get("1.0", tk.END).strip().upper()
    seq2 = entry_seq2.get("1.0", tk.END).strip().upper()
    
    if not seq1 or not seq2:
        messagebox.showerror("Input Error", "Both sequences must be provided.")
        return
    
    result = find_mutations(seq1, seq2)
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, result)

def clear_fields():
    entry_seq1.delete("1.0", tk.END)
    entry_seq2.delete("1.0", tk.END)
    text_output.delete("1.0", tk.END)

# GUI Setup
root = tk.Tk()
root.title("RNA Mutation Detector")
root.geometry("500x400")

# Labels & Text Areas
tk.Label(root, text="RNA Sequence 1:").pack()
entry_seq1 = tk.Text(root, height=3, width=50)
entry_seq1.pack()

tk.Label(root, text="RNA Sequence 2:").pack()
entry_seq2 = tk.Text(root, height=3, width=50)
entry_seq2.pack()

# Buttons
detect_button = tk.Button(root, text="Detect Mutations", command=detect_mutations)
detect_button.pack()

clear_button = tk.Button(root, text="Clear", command=clear_fields)
clear_button.pack()

# Output
tk.Label(root, text="Mutations:").pack()
text_output = tk.Text(root, height=5, width=50)
text_output.pack()

# Run GUI
root.mainloop()
