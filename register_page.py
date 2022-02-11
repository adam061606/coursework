# adam wrote all of this
# import tkinter modules and easygui
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import tkinter.messagebox

# globally declare wb and sheet variable
root = Tk()

# setting the windows size
root.geometry("400x200")
# setting the app name
root.title("register")

# declaring string variable
# for storing name and password
name_var=tk.StringVar()
passw_var=tk.StringVar()
username_available = False
  
# a function that will get the name and password and store them in a text file
def createAccount():
    name=name_var.get()
    password=passw_var.get()

    file0 = open("account_username.txt", "r")
    usernames = file0.readlines()
    file0.close()
    
    for i in usernames :
        if name == i:
            #tkMessageBox.showinfo(title="error", message="username taken, please sign in instead")
            username_available == False
            name_var.set("")
            passw_var.set("")
            root.destroy()
            import sign_in_page
            break
        else : username_available = True
    if username_available == True:
        file1 = open("account_username.txt", "a")
        file1.write("user:" + name + "\n")
        file1.close()

        file2 = open("account_password.txt", "a")
        file2.write("password:" + password + "\n")
        file2.close()
        print("The name is : " + name)
        print("The password is : " + password)
        name_var.set("")
        passw_var.set("")
    
# a function that will get the name and password and store them in a text file
def signIn():
    root.destroy()
    import sign_in_page

    
# creating a label for name
name_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))
  
# creating a input text box
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
  
# creating a label for password
passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))
  
# creating a input text box for password
passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
  
# creating a button that will call the submit function
sub_btn=tk.Button(root,text = 'Submit', command = createAccount)

# creating a button that will call the sign-in function
sign_btn=tk.Button(root,text = 'Already have an account? Sign In !', command = signIn)
  
# placing the label and entry in
# the required position using grid
# method
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
passw_label.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)
sign_btn.grid(row=3,column=1)
  
# performing an infinite loop
# for the window to display
root.mainloop()
