import tkinter as tk
from tkinter import messagebox

# Function to check eligibility and capture vote
def check_eligibility_and_vote():
    first_name = entry_fn.get()
    last_name = entry_ln.get()
    email = entry_email.get()
    phone = entry_ph.get()
    address = entry_ad.get()
    try:
        age = int(entry_age.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid age")
        return

    if age < 18:
        messagebox.showwarning("Not Eligible", "You are not eligible for voting")
        return
    else:
        messagebox.showinfo("Eligible", "You are eligible for voting")

    # Capture the vote
    vote_choice = vote_var.get()
    if vote_choice == 1:
        messagebox.showinfo("Vote", "Forcefully voted for TMC")
    elif vote_choice == 2:
        messagebox.showinfo("Vote", "You have voted for BJP")
    elif vote_choice == 3:
        messagebox.showinfo("Vote", "Voted for Rahul")
    else:
        messagebox.showerror("Error", "Wrong input, please select a candidate")

# Create the main window
root = tk.Tk()
root.title("National Voting Commission")

# First name label and entry
label_fn = tk.Label(root, text="First Name:")
label_fn.grid(row=0, column=0, padx=10, pady=5)
entry_fn = tk.Entry(root)
entry_fn.grid(row=0, column=1, padx=10, pady=5)

# Last name label and entry
label_ln = tk.Label(root, text="Last Name:")
label_ln.grid(row=1, column=0, padx=10, pady=5)
entry_ln = tk.Entry(root)
entry_ln.grid(row=1, column=1, padx=10, pady=5)

# Email label and entry
label_email = tk.Label(root, text="Email:")
label_email.grid(row=2, column=0, padx=10, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1, padx=10, pady=5)

# Phone number label and entry
label_ph = tk.Label(root, text="Phone Number:")
label_ph.grid(row=3, column=0, padx=10, pady=5)
entry_ph = tk.Entry(root)
entry_ph.grid(row=3, column=1, padx=10, pady=5)

# Address label and entry
label_ad = tk.Label(root, text="Address:")
label_ad.grid(row=4, column=0, padx=10, pady=5)
entry_ad = tk.Entry(root)
entry_ad.grid(row=4, column=1, padx=10, pady=5)

# Age label and entry
label_age = tk.Label(root, text="Age:")
label_age.grid(row=5, column=0, padx=10, pady=5)
entry_age = tk.Entry(root)
entry_age.grid(row=5, column=1, padx=10, pady=5)

# Voting options
vote_var = tk.IntVar()
label_vote = tk.Label(root, text="Vote for your candidate:")
label_vote.grid(row=6, column=0, padx=10, pady=10)

rb1 = tk.Radiobutton(root, text="Momota (TMC)", variable=vote_var, value=1)
rb1.grid(row=6, column=1, padx=10, pady=5)

rb2 = tk.Radiobutton(root, text="Modi (BJP)", variable=vote_var, value=2)
rb2.grid(row=7, column=1, padx=10, pady=5)

rb3 = tk.Radiobutton(root, text="Rahul (Congress)", variable=vote_var, value=3)
rb3.grid(row=8, column=1, padx=10, pady=5)

# Submit button
submit_btn = tk.Button(root, text="Submit", command=check_eligibility_and_vote)
submit_btn.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()
