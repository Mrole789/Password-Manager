from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pw():
    """Generates and returns password."""
    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","U","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    nums = ["0","1","2","3","4","5","6","7","8","9"]
    syms = ["!","#","$","%","&","(",")","*","+"]

    cl = random.randint(6, 10)
    cn = random.randint(2, 4)
    cs = random.randint(2, 4)

    p = []
    for x in range(cl):
        a = random.choice(letters)
        p.append(a)

    for y in range(cn):
        b = random.choice(nums)
        p.append(b)

    for z in range(cs):
        c = random.choice(syms)
        p.append(c)

    fp = ""
    for a in range(1, (len(p) + 1)):
        b = random.choice(p)
        fp += b
        p.remove(b)
        
    pw_input.insert(index="end", string=fp)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Saves details and password in a file"""
    p_data = {
        w_input.get(): {
            "email": u_input.get(),
            "password": pw_input.get(),
            }
        }
    
    if len(w_input.get()) == 0 or len(pw_input.get()) == 0:
        messagebox.showerror(title="Oops", message="Don't leave any field empty.")
    else:
        #read old data
        try:
            with open("data.json",mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            #or create new one if file is not created
            with open("data.json",mode="w") as file:
                json.dump(p_data, file, indent=4)
        else:
            #update new data with old data
            data.update(p_data)
            
            #save updated data
            with open("data.json",mode="w") as file:
                json.dump(data, file, indent=4)
            
        w_input.delete(0, "end")
        u_input.delete(0, "end")
        pw_input.delete(0, "end")
        
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_pw():
    try:
        with open("data.json",mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data file found.")
    else:
        web = w_input.get()
        if web in data or web.lower in data:
            em = data[web]["email"]
            pw = data[web]["password"]
            messagebox.showinfo(title=web, message=f"Email/Username: {em}\nPassword: {pw}")
        else:
            messagebox.showerror(title="Oops", message="No details for website exists.")
                
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40,pady=40)

canvas = Canvas(width=200,height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo)
canvas.grid(column=1, row=0)

w_label = Label(text="Website:")
w_label.grid(column=0,row=1)

u_label = Label(text="Email/Username:")
u_label.grid(column=0,row=2)

pw_label = Label(text="Password:")
pw_label.grid(column=0,row=3)

w_input = Entry(width=30)
w_input.insert(index="end", string="")
w_input.focus() #so cursor appears here when the program starts
w_input.grid(column=1,row=1, sticky="w")

u_input = Entry(width=35)
u_input.insert(index="end", string="")
u_input.grid(column=1,row=2,columnspan=2, sticky="ew")

pw_input = Entry(width=30)
pw_input.insert(index="end", string="")
pw_input.grid(column=1,row=3, sticky="w")

fp_button = Button(width=14,text="Search", command=find_pw)
fp_button.grid(column=2,row=1, sticky="e")

gp_button = Button(text="Generate Password", command=generate_pw)
gp_button.grid(column=2,row=3, sticky="e")

add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1,row=5,columnspan=2, sticky="ew")

window.mainloop()