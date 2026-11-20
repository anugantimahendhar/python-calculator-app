
import customtkinter as ctk
from calculator import add, subtract, multiply, divide, percentage

# Theme settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Calculator variables
first_number = None
operator = None
new_number = True


# Button functionality
def button_click(value):
    global first_number, operator, new_number

    current = display_var.get()

    if value == "AC":
        display_var.set("0")
        expression_var.set("Ready to calculate")
        first_number = None
        operator = None
        new_number = True

    elif value == "⌫":
        if current == "Error":
            display_var.set("0")
        else:
            display_var.set(current[:-1] or "0")

    elif value == "%":
        try:
            result = percentage(float(current))
            display_var.set(f"{result:.12g}")
        except ValueError:
            display_var.set("Error")

    elif value in ["+", "−", "×", "÷"]:
        try:
            first_number = float(current)
            operator = value
            expression_var.set(f"{current} {value}")
            new_number = True
        except ValueError:
            display_var.set("Error")

    elif value == "=":
        if first_number is None or new_number:
            return

        try:
            second_number = float(current)

            expression_var.set(
                f"{first_number:g} {operator} {current} ="
            )

            if operator == "+":
                result = add(first_number, second_number)

            elif operator == "−":
                result = subtract(first_number, second_number)

            elif operator == "×":
                result = multiply(first_number, second_number)

            elif operator == "÷":
                result = divide(first_number, second_number)

            display_var.set(f"{result:.12g}")

        except (ValueError, ZeroDivisionError):
            display_var.set("Error")

        first_number = None
        operator = None
        new_number = True

    else:
        if new_number or current == "Error":
            current = "0"
            new_number = False

        if value == ".":
            if "." not in current:
                display_var.set(current + ".")

        elif current == "0":
            display_var.set(value)

        else:
            display_var.set(current + value)


# Main window
root = ctk.CTk()
root.title("Calc Studio")
root.geometry("380x580")
root.resizable(False, False)
root.configure(fg_color="#0c1017")

display_var = ctk.StringVar(value="0")
expression_var = ctk.StringVar(value="Ready to calculate")


# Header
header = ctk.CTkFrame(root, fg_color="transparent")
header.pack(fill="x", padx=20, pady=(20, 10))

ctk.CTkLabel(
    header,
    text="Calc Studio",
    font=("Segoe UI", 25, "bold"),
    text_color="#ffffff"
).pack(anchor="w")

ctk.CTkLabel(
    header,
    text="STANDARD CALCULATOR",
    font=("Segoe UI", 11),
    text_color="#838a9b"
).pack(anchor="w")


# Modern display panel
display_frame = ctk.CTkFrame(
    root,
    fg_color="#171c27",
    corner_radius=18
)

display_frame.pack(
    fill="x",
    padx=20,
    pady=10
)

ctk.CTkLabel(
    display_frame,
    textvariable=expression_var,
    font=("Segoe UI", 14),
    text_color="#9299ad",
    anchor="e"
).pack(fill="x", padx=18, pady=(12, 0))

ctk.CTkLabel(
    display_frame,
    textvariable=display_var,
    font=("Segoe UI", 34, "bold"),
    text_color="white",
    anchor="e"
).pack(fill="x", padx=18, pady=12)

ctk.CTkFrame(
    display_frame,
    height=3,
    fg_color="#9671ff",
    corner_radius=5
).pack(fill="x", padx=18, pady=(0, 12))


# Buttons container
button_frame = ctk.CTkFrame(
    root,
    fg_color="transparent"
)

button_frame.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=5
)


# Button layout
buttons = [
    ["AC", "⌫", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "−"],
    ["1", "2", "3", "+"],
    ["0", ".", "="]
]


# Create modern buttons
for r, button_row in enumerate(buttons):

    column = 0

    for text in button_row:

        bg_color = "#1b202b"
        hover_color = "#303747"
        text_color = "#ffffff"

        if text in ["+", "−", "×", "÷"]:
            bg_color = "#27213e"
            hover_color = "#443460"
            text_color = "#bfa5ff"

        elif text == "=":
            bg_color = "#9567ed"
            hover_color = "#ad85ff"

        elif text == "AC":
            bg_color = "#392332"
            hover_color = "#59354b"
            text_color = "#ff94ae"

        elif text in ["⌫", "%"]:
            bg_color = "#292f3e"
            hover_color = "#41495b"

        span = 2 if text == "0" else 1

        button = ctk.CTkButton(
            button_frame,
            text=text,
            font=("Segoe UI", 21, "bold"),
            fg_color=bg_color,
            hover_color=hover_color,
            text_color=text_color,
            corner_radius=14,
            height=50,
            width=0,
            command=lambda x=text: button_click(x)
        )

        button.grid(
            row=r,
            column=column,
            columnspan=span,
            padx=5,
            pady=5,
            sticky="nsew"
        )

        column += span


# Configure grid
for i in range(4):
    button_frame.columnconfigure(i, weight=1)

for i in range(5):
    button_frame.rowconfigure(i, weight=1)


# Footer
ctk.CTkLabel(
    root,
    text="CALC STUDIO  •  POWERED BY PYTHON",
    font=("Segoe UI", 10),
    text_color="#767e92"
).pack(pady=(5, 12))


root.mainloop()
