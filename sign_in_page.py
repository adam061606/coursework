# adam wrote all of this
# import tkinter modules
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import tkinter.messagebox

# globally declare wb and sheet variable
root = Tk()

# setting the windows size
root.geometry("400x200")
# setting the app name
root.title("sign in")

# declaring string variable
# for storing name and password
name_sign=tk.StringVar()
passw_sign=tk.StringVar()


# a function that will get the name and password and store them in a text file
def signIn():
    name=name_sign.get()
    password=passw_sign.get()
    
    file1 = open("account_username.txt", "r")
    usernames = file1.readlines()
    #print(usernames)
    file1.close()
    username_list =[]
    for i in usernames:
        i = i.strip()
        i = i[5:]
        username_list.append(i)
    print(username_list)

    file2 = open("account_password.txt", "r")
    passwords = file2.readlines()
    #print(passwords)
    file2.close()
    password_list =[]
    for i in passwords:
        i = i.strip()
        i = i[9:]
        password_list.append(i)
    print(password_list)

    print(name)
    print(password)


    for i in username_list:
        if name == i:
            a = username_list.index(name)
            if password == password_list[a]:
                root.destroy()
                import main_page
                break
            else :
                #tkMessageBox.showinfo(title="error", message="wrong password")
                print ("password is wrong")
                break
        else :
            #tkMessageBox.showinfo(title="error", message="username not found, register a new account.")
            print ("username not found")
            break
            #root.destroy()
            #import register_page

def reg():
    root.destroy()
    import register_page

# creating a label for name
name_label_sign = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))
# creating a input text box
name_entry_sign = tk.Entry(root,textvariable = name_sign, font=('calibre',10,'normal'))
# creating a label for password
passw_label_sign = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))
# creating a input text box for password
passw_entry_sign =tk.Entry(root, textvariable = passw_sign, font = ('calibre',10,'normal'), show = '*')
# creating a button that will call the submit function
signIn_btn=tk.Button(root,text = 'Sign In', command = signIn)
# creating a button that will call the sign-in function
reg_btn=tk.Button(root,text = 'Dont have an account? Register now!', command = reg)

name_label_sign.grid(row=0,column=0)
name_entry_sign.grid(row=0,column=1)
passw_label_sign.grid(row=1,column=0)
passw_entry_sign.grid(row=1,column=1)
signIn_btn.grid(row=2,column=1)
reg_btn.grid(row=3,column=1)

# performing an infinite loop
# for the window to display
root.mainloop()



    



