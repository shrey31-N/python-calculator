import tkinter as tk

# Format result to remove .0 if not needed
def format_result(result):
    return int(result) if isinstance(result, float) and result.is_integer() else result

# Evaluate expression with support for sqrt and discount
def evaluate_expression(expr):
    try:
        if "√" in expr:
            num = float(expr.replace("√", ""))
            return format_result(num ** 0.5)
        elif "disc" in expr:
            parts = expr.split("disc")
            price = float(parts[0])
            discount_percent = float(parts[1])
            discount_amount = (discount_percent / 100) * price
            final_price = price - discount_amount
            return f"₹{format_result(final_price)} (Saved ₹{format_result(discount_amount)})"
        else:
            return format_result(eval(expr))
    except Exception:
        return "Error"

# Handle button click
def on_click(event):
    text = event.widget.cget("text")
    
    if text == "=":
        expr = entry.get()
        result = evaluate_expression(expr)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    elif text == "AC":
        entry.delete(0, tk.END)
    elif text == "←":
        entry.delete(len(entry.get())-1)
    elif text == "√":
        entry.insert(tk.END, "√")
    elif text == "Disc":
        entry.insert(tk.END, "disc")
    else:
        entry.insert(tk.END, text)

# Create main window
root = tk.Tk()
root.title("Smart Calculator")
root.configure(bg="black")

# Entry box
entry = tk.Entry(root, font="Arial 20", bd=8, insertwidth=2, width=16, borderwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Button layout
buttons = [
    ["AC", "←", "Disc", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

# Create and bind buttons
for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        btn = tk.Button(root, text=buttons[i][j], padx=20, pady=20, font="Arial 18", bg="black", fg="orange")
        btn.grid(row=i+1, column=j, sticky="nsew")
        btn.bind("<Button-1>", on_click)

# Make layout responsive
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Run the application
root.mainloop()
