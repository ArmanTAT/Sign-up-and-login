import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Sign Up/Login")

# Create the frames for the sign up and login forms
signup_frame = tk.Frame(window)
login_frame = tk.Frame(window)

# Create the widgets for the sign up form
signup_label = tk.Label(signup_frame, text="Sign Up")
signup_username_label = tk.Label(signup_frame, text="Username:")
signup_password_label = tk.Label(signup_frame, text="Password:")
signup_username_entry = tk.Entry(signup_frame)
signup_password_entry = tk.Entry(signup_frame, show="*")
signup_button = tk.Button(signup_frame, text="Sign Up")

# Create the widgets for the login form
login_label = tk.Label(login_frame, text="Login")
login_username_label = tk.Label(login_frame, text="Username:")
login_password_label = tk.Label(login_frame, text="Password:")
login_username_entry = tk.Entry(login_frame)
login_password_entry = tk.Entry(login_frame, show="*")
login_button = tk.Button(login_frame, text="Login")

# Function to handle the sign up button press
def signup():
  # Get the values entered in the sign up form
  username = signup_username_entry.get()
  password = signup_password_entry.get()

  # Write the username and password to a file
  with open("credentials.txt", "a") as f:
    f.write(f"{username},{password}\n")

  # Clear the sign up form
  signup_username_entry.delete(0, "end")
  signup_password_entry.delete(0, "end")

# Function to handle the login button press
def login():
  # Get the values entered in the login form
  username = login_username_entry.get()
  password = login_password_entry.get()

  # Read the credentials from the file
  with open("credentials.txt", "r") as f:
    for line in f:
      # Check if the username and password match
      if line.strip() == f"{username},{password}":
        # Login successful
        print("Login successful!")
        return

  # If we get here, the login was not successful
  print("Invalid username or password")

# Attach the button press functions to the buttons
signup_button.config(command=signup)
login_button.config(command=login)
# Layout the widgets in the sign up frame
signup_label.pack()
signup_username_label.pack()
signup_username_entry.pack()
signup_password_label.pack()
signup_password_entry.pack()
signup_button.pack()

# Layout the widgets in the login frame
login_label.pack()
login_username_label.pack()
login_username_entry.pack()
login_password_label.pack()
login_password_entry.pack()
login_button.pack()

# Display the sign up frame
signup_frame.pack()

# Create a button to switch to the login frame
switch_button = tk.Button(signup_frame, text="Already have an account? Login here", command=lambda: switch_frames(login_frame))
switch_button.pack()

# Function to switch between the sign up and login frames
def switch_frames(frame):
  signup_frame.pack_forget()
  frame.pack()

# Run the main loop
window.mainloop()
