import qrcode
from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog, messagebox

# Function to generate the QR code
def generate_qr():
    try:
        # Get user inputs
        user_input = text_entry.get()
        box_size = int(box_size_entry.get())
        border = int(border_entry.get())
        fill_color = fill_color_var.get()
        back_color = back_color_var.get()
        error_level = error_level_var.get()

        # Set error correction level
        error_correction_map = {
            "L (7%)": qrcode.constants.ERROR_CORRECT_L,
            "M (15%)": qrcode.constants.ERROR_CORRECT_M,
            "Q (25%)": qrcode.constants.ERROR_CORRECT_Q,
            "H (30%)": qrcode.constants.ERROR_CORRECT_H
        }

        # Create QR code object with customization
        qr = qrcode.QRCode(
            version=1,
            error_correction=error_correction_map[error_level],
            box_size=box_size,
            border=border
        )
        qr.add_data(user_input)
        img = qr.make_image(fill_color=fill_color, back_color=back_color)

        # Ask where to save the image
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
        if file_path:
            img.save(file_path)
            messagebox.showinfo("Success", "QR Code saved successfully!")
        else:
            messagebox.showwarning("Cancelled", "Saving QR Code was cancelled.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to choose fill color
def choose_fill_color():
    color = colorchooser.askcolor(title="Choose Fill Color")
    if color[1]:
        fill_color_var.set(color[1])

# Function to choose background color
def choose_back_color():
    color = colorchooser.askcolor(title="Choose Background Color")
    if color[1]:
        back_color_var.set(color[1])

# Create GUI window
root = Tk()
root.title("Ultra Simple QR Code Generator")

# Labels and entry for text
Label(root, text="Enter Your Text:").grid(row=0, column=0, padx=10, pady=10)
text_entry = Entry(root, width=30)
text_entry.grid(row=0, column=1, padx=10, pady=10)

# Label and entry for box size
Label(root, text="Box Size:").grid(row=1, column=0, padx=10, pady=10)
box_size_entry = Entry(root, width=10)
box_size_entry.insert(0, "20")
box_size_entry.grid(row=1, column=1, padx=10, pady=10)

# Label and entry for border size
Label(root, text="Border Size:").grid(row=2, column=0, padx=10, pady=10)
border_entry = Entry(root, width=10)
border_entry.insert(0, "6")
border_entry.grid(row=2, column=1, padx=10, pady=10)

# Option menu for error correction level
Label(root, text="Error Correction:").grid(row=3, column=0, padx=10, pady=10)
error_level_var = StringVar()
error_level_var.set("L (7%)")
error_level_menu = OptionMenu(root, error_level_var, "L (7%)", "M (15%)", "Q (25%)", "H (30%)")
error_level_menu.grid(row=3, column=1, padx=10, pady=10)

# Button and entry for fill color
Label(root, text="Fill Color:").grid(row=4, column=0, padx=10, pady=10)
fill_color_var = StringVar()
fill_color_var.set("red")
fill_color_button = Button(root, text="Choose Fill Color", command=choose_fill_color)
fill_color_button.grid(row=4, column=1, padx=10, pady=10)

# Button and entry for background color
Label(root, text="Background Color:").grid(row=5, column=0, padx=10, pady=10)
back_color_var = StringVar()
back_color_var.set("black")
back_color_button = Button(root, text="Choose Background Color", command=choose_back_color)
back_color_button.grid(row=5, column=1, padx=10, pady=10)

# Generate button
generate_button = Button(root, text="Generate QR Code", command=generate_qr)
generate_button.grid(row=6, column=0, columnspan=2, pady=20)

# Run the GUI loop
root.mainloop()
