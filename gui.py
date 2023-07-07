import tkinter as tk
from PIL import ImageTk, Image

def button1_click():
    print("Button 1 clicked!")

def button2_click():
    print("Button 2 clicked!")

# Create the main window
window = tk.Tk()

# Load the image
image_path = r"C:\Users\shree\Desktop\mp4\static\img.jpeg"
image = Image.open(image_path)
image = image.resize((800, 600))  # Adjust the size as needed
image_tk = ImageTk.PhotoImage(image)

# Create a label to display the image
image_label = tk.Label(window, image=image_tk)
image_label.pack()

# Create buttons with custom styling
button1 = tk.Button(window, text='Button 1', command=button1_click, bg='lightblue', fg='black', font=('Arial', 14, 'bold'))
button1.place(x=100, y=100)  # Adjust the coordinates as needed

button2 = tk.Button(window, text='Button 2', command=button2_click, bg='lightgreen', fg='black', font=('Arial', 14, 'bold'))
button2.place(x=200, y=200)  # Adjust the coordinates as needed

# Start the GUI event loop
window.mainloop()
