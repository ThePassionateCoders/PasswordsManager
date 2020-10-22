from tkinter import *
import tkinter.messagebox as msg
import json

passvalue=""
plattvalue=""
plattf=""
keyvalue=""
keyvaluef=""
confpass=""
oldkey=""
newkey=""
confirmkey=""

def encrypt(cleartext):
	alpha = """0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()-_=+[]\{}|;':",./<>? ¡™€₹×±✓£¢∞§¶•ªº–≠œ∑®†¥øπ“‘«åß∂ƒ©˙∆˚¬…æΩ≈ç√∫µ≤≥÷"""
	cyphertext=""
	for char in cleartext:
		if char in alpha:
			newpos=(alpha.find(char)+71)%142
			cyphertext += alpha[newpos]
		else:
			cyphertext += char
	return cyphertext

def getkey():
	try:
		with open("key.txt") as f:
			return encrypt(f.read())
	except:
		return "root"
	
def changekey():
	if newkey.get()=="" or oldkey.get()=="" or confirmkey.get()=="":
		msg.showerror("Feild Empty", "Please fill all details!")
	elif oldkey.get() != getkey():
		msg.showerror("Error", "Secret Key is wrong! ")
		oldkey.set("")
	elif confirmkey.get() != newkey.get():
		msg.showerror("Error", "Keys didn't matched!")
		confirmkey.set("")
		newkey.set("")
	elif newkey.get() == oldkey.get():
		msg.showerror("Error", "Please choose a different key!")
		confirmkey.set("")
		newkey.set("")
	else:
		with open("key.txt", "w") as f:
			f.write(encrypt(newkey.get()))
		msg.showinfo("Success", "Your Secret Key has been updated successfully!")
		confirmkey.set("")
		newkey.set("")
		oldkey.set("")
	
	
def submit():
	try:
		with open("passwords.json") as f:
			passwords=json.loads(f.read())
	except:
		passwords={}
	passwords[plattvalue.get().lower()]=encrypt(passvalue.get())
	if plattvalue.get()=="" or passvalue.get()=="" or keyvalue.get()=="" or confpass.get()=="":
		msg.showerror("Feild Empty", "Please fill all details!")
	elif confpass.get() != passvalue.get():
		msg.showerror("Error", "Passwords didn't matched!")
		passvalue.set("")
		confpass.set("")
	else:
		if keyvalue.get() != getkey():
			msg.showerror("Error", "Secret key is wrong!")
			keyvalue.set("")
			return
		passwords=json.dumps(passwords)
		with open("passwords.json", "w") as f:
			f.write(passwords)
		msg.showinfo("Success", "Password saved successfully!")
		plattvalue.set("")
		passvalue.set("")
		keyvalue.set("")
		confpass.set("")


def getpass():
	try:
		with open("passwords.json") as f:
			passwords=json.loads(f.read())
	except:
		msg.showerror("Error", "You have not saved any password yet!")
		return addpass()
	if plattf.get()=="" or keyvaluef.get()=="":
		msg.showerror("Feild Empty", "Any Field Can't Be Empty!")
		return
	else:
		try:
			if keyvaluef.get() != getkey():
				msg.showerror("Error", "Secret key is wrong!")
				keyvaluef.set("")
				return
			msg.showinfo(f"{plattf.get().upper()} PASSWORD", f"Your {plattf.get()} password:\n{encrypt(passwords[plattf.get().lower()])}")
			plattf.set("")
			keyvaluef.set("")
		except:
			msg.showerror("Error", "Password for this plattform is not saved yet.")
			addpass(passedplattvalue=plattf.get())
			
			

	
			
def fetch():
	global root
	global plattf
	global keyvaluef
	root.destroy()
	root=Tk()
	root.configure(background="blue")
	root.geometry("350x155")
	root.minsize(350,155)
	root.maxsize(350,155)
	root.title("Fetch Password")
	
	mymenu=Menu(root)
	mymenu.add_command(label="Home", command=home)
	mymenu.add_command(label="Add", command=addpass)
	mymenu.add_command(label="Fecth", command=fetch)
	mymenu.add_command(label="Settings", command=setting)
	mymenu.add_command(label="Help", command=help)
	root.config(menu=mymenu)
	
	Label(root, text="Plattform", borderwidth="5", relief=SUNKEN, pady="5", padx="5", fg="red", bg="yellow").grid(row="0", column="0", pady="5", padx="5")
	Label(root, text="Secret Key", borderwidth="5", relief=SUNKEN, pady="5", padx="5", fg="red", bg="yellow").grid(row="1", column="0", pady="5", padx="5")
	
	plattf=StringVar()
	keyvaluef=StringVar()
	
	Entry(root, text=plattf, fg="blue", bg="yellow").grid(row="0", column="1", pady="5", padx="5")
	Entry(root, text=keyvaluef, show="*", fg="blue", bg="yellow").grid(row="1", column="1", pady="5", padx="5")
	
	Button(text="Fetch", borderwidth="5", relief=SUNKEN, pady="5", padx="5", command=getpass, bg="grey", fg="white").grid(row="2", column="1", sticky="w", pady="5", padx="5")
	
	root.mainloop()
	
	


def help():
	msg.showinfo("Help", "This is a password manager created by Hammad Ali")
		
	
def addpass(passedplattvalue=False):
	global root
	global passvalue
	global plattvalue
	global keyvalue
	global confpass
	root.destroy()
	root=Tk()
	root.configure(background="blue")
	# width x height
	root.geometry("350x255")
	root.title("Add Password")
	
	# width,height
	root.minsize(350,255)
	root.maxsize(350,255)
	
	mymenu=Menu(root)
	mymenu.add_command(label="Home", command=home)
	mymenu.add_command(label="Add", command=addpass)
	mymenu.add_command(label="Fecth", command=fetch)
	mymenu.add_command(label="Settings", command=setting)
	mymenu.add_command(label="Help", command=help)
	root.config(menu=mymenu)
	
	Label(root, text="Plattform", borderwidth="5", relief=SUNKEN, pady="5", padx="5", fg="red", bg="yellow").grid(row="0", column="0", pady="5", padx="5")
	Label(root, text="Password", borderwidth="5", relief=SUNKEN, pady="5", padx="5", fg="red", bg="yellow").grid(row="1", column="0", pady="5", padx="5")
	Label(root, text="Confirm", borderwidth="5", relief=SUNKEN, pady="5", padx="5", fg="red", bg="yellow").grid(row="2", column="0", pady="5", padx="5")
	Label(root, text="Secret Key", borderwidth="5", relief=SUNKEN, pady="5", padx="5", fg="red", bg="yellow").grid(row="3", column="0", pady="5", padx="5")

	passvalue=StringVar()
	plattvalue=StringVar()
	keyvalue=StringVar()
	confpass=StringVar()
	if passedplattvalue:
		plattvalue.set(passedplattvalue)
		
	Entry(root, text=plattvalue, fg="blue", bg="yellow").grid(row="0", column="1", pady="5", padx="5")
	Entry(root, text=passvalue, show="*", fg="blue", bg="yellow").grid(row="1", column="1", pady="5", padx="5")
	Entry(root, text=confpass, show="*", fg="blue", bg="yellow").grid(row="2", column="1", pady="5", padx="5")
	Entry(root, text=keyvalue, show="*", fg="blue", bg="yellow").grid(row="3", column="1", pady="5", padx="5")
	
	Button(text="Submit", borderwidth="5", relief=SUNKEN, pady="5", padx="5", command=submit, bg="grey", fg="white").grid(row="4", column="1", pady="5", padx="5", sticky="w")
	
	root.mainloop()
	
def setting():
	global root
	global newkey
	global oldkey
	global confirmkey
	
	root.destroy()
	root=Tk()
	root.configure(background="blue")
	# width x height
	root.geometry("350x210")
	root.title("Add Password")
	
	# width,height
	root.minsize(350,210)
	root.maxsize(350,210)
	
	mymenu=Menu(root)
	mymenu.add_command(label="Home", command=home)
	mymenu.add_command(label="Add", command=addpass)
	mymenu.add_command(label="Fecth", command=fetch)
	mymenu.add_command(label="Settings", command=setting)
	mymenu.add_command(label="Help", command=help)
	root.config(menu=mymenu)
	
	Label(root, text="Old Key", borderwidth="5", relief=SUNKEN, pady="5", padx="5", fg="red", bg="yellow").grid(row="0", column="0", pady="5", padx="5")
	Label(root, text="New Kew", borderwidth="5", relief=SUNKEN, pady="5", padx="5", fg="red", bg="yellow").grid(row="1", column="0", pady="5", padx="5")
	Label(root, text="Confirm", borderwidth="5", relief=SUNKEN, pady="5", padx="5", fg="red", bg="yellow").grid(row="2", column="0", pady="5", padx="5")
	
	oldkey=StringVar()
	newkey=StringVar()
	confirmkey=StringVar()
	
	Entry(root, text=oldkey, show="*", fg="blue", bg="yellow").grid(row="0", column="1", pady="5", padx="5")
	Entry(root, text=newkey, show="*", fg="blue", bg="yellow").grid(row="1", column="1", pady="5", padx="5")
	Entry(root, text=confirmkey, show="*", fg="blue", bg="yellow").grid(row="2", column="1", pady="5", padx="5")
	
	Button(text="Change", borderwidth="5", relief=SUNKEN, pady="5", padx="5", command=changekey, bg="grey", fg="white").grid(row="3", column="1", pady="5", padx="5", sticky="w")
	
	root.mainloop()

def home():
	global root
	try:
		root.destroy()
	except:
		pass		
	root=Tk()
	root.configure(background="yellow")
	root.geometry("360x75")
	root.minsize(360,75)
	root.maxsize(360,75)
	root.title("Passwords Manager")
		
	mymenu=Menu(root)
	mymenu.add_command(label="Home", command=home)
	mymenu.add_command(label="Add", command=addpass)
	mymenu.add_command(label="Fecth", command=fetch)
	mymenu.add_command(label="Settings", command=setting)
	mymenu.add_command(label="Help", command=help)
	root.config(menu=mymenu)
	
	Label(root, text="Welcome to Passwords Manager!\n This is a software to manage your passwords\n Created by Hammad Ali", fg="Red", bg="yellow").pack()
	
	root.mainloop()

if __name__=="__main__":	
	home()