import tkinter as tk
from tkinter import messagebox

# Define a list of positive response words
pr = ['happy', 'delighted', 'fine', 'well']

# Function to process the user input
def check_response():
    ur = entry.get()  # Get the input from the entry field
    wrd = ur.split()
    k = 0
    for i in wrd:
        if i.lower() in pr:  # Check if the word matches any in the list (case insensitive)
            k = 1
    if k == 1:
        messagebox.showinfo("Response", "Even I am doing well!")  # Display a message box with the positive response
    else:
        messagebox.showerror("Response", "Sorry, I couldn't understand")  # Display an error message box

# Create the main application window
root = tk.Tk()
root.title("Barbie Theme - How Are You?")
root.geometry("400x300")

# Set the background color to a Barbie-inspired pink
root.configure(bg="#FFC0CB")

# Create a label with a Barbie-style font and pink color scheme
label = tk.Label(root, text="How are you?", font=("Comic Sans MS", 20, "bold"), bg="#FFC0CB", fg="#FF69B4")
label.pack(pady=20)

# Create an entry widget with Barbie-like style
entry = tk.Entry(root, width=30, font=("Comic Sans MS", 14), bg="#FFF0F5", fg="#FF69B4", bd=3, relief="ridge")
entry.pack(pady=10)

# Create a button with a Barbie-themed color and style
button = tk.Button(root, text="Submit", command=check_response, font=("Comic Sans MS", 14), bg="#FF69B4", fg="white", bd=3, relief="raised")
button.pack(pady=20)

# Add a stylish border around the window
frame = tk.Frame(root, bg="#FFB6C1", bd=5, relief="sunken")
frame.place(relwidth=1, relheight=1)

# Run the Tkinter event loop
root.mainloop()
