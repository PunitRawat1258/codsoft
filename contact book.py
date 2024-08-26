#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
root = Tk()
root.geometry('600x400')
root.title ('Guardian Directory')
root.config (bg = 'light grey')
root.resizable (0,0)


GuardianDirectory = [
    ['Drew', 'DeLeon', '4567891', 'address4', 'drew@deleon.com'],
    ['Apple', 'Appleby', '1234567', 'address1', 'apple@appleby.com'],
    ]

FirstName = StringVar()
LastName = StringVar()
ContactNumber = StringVar()
Address = StringVar()
Email = StringVar()

frame = Frame(root)
frame.pack (side = RIGHT)

scroll = Scrollbar(frame, orient = VERTICAL)
select = Listbox (frame, yscrollcommand = scroll.set, height =15,)
scroll.config (command = select.yview)
scroll.pack(side = RIGHT, fill = Y)
select.pack(side = LEFT, fill = BOTH, expand = 1)


def selected():
    return int(select.curselection()[0])

def add():
    GuardianDirectory.append([FirstName.get(), LastName.get(),
    ContactNumber.get(), Address.get(), Email.get()])
    selectset()
    print(f"Contact added.")

def delete ():
    del GuardianDirectory[selected()]
    selectset()

def search():
    FirstName = FirstName_entry.get()
    if FirstName in GuardianDirectory:
        ContactNumber.delete(0,tk.END)
        ContactNumber.insert(0,GuardianDirectory[FirstName])
    else:
        ContactNumber.delete(0, tk.END)

def view():
    FIRSTNAME, LASTNAME, CONTACTNNUMBER, ADDRESS, EMAIL = GuardianDirectory[Selected()]
    FirstName.set(FIRSTNAME)
    LastName.set(LASTNAME)
    ContactNumber.set(CONTACTNNUMBER)
    Address.set(ADDRESS)
    Email.set(EMAIL)
def selectset():
    GuardianDirectory.sort()
    select.delete (0,END)
    for FirstName, LastName, ContactNumber, Address, Email in GuardianDirectory:
        select.insert (END, FirstName)
selectset()

def search():
    GuardianDirectory.search()
    FirstName.get()

def exit():
    root.destroy()

Label(root, text = 'First Name', font = 'arial 12 bold', bg = 'white') .place (x=30, y=20)
Entry(root, textvariable = FirstName).place (x=130, y=20)

Label(root, text = 'Last Name', font = 'arial 12 bold', bg = 'white') .place (x=30, y=70)
Entry(root, textvariable = LastName).place (x=130, y=70)

Label(root, text = 'Contact Number', font = 'arial 12 bold', bg = 'white') .place (x=30, y=120)
Entry(root, textvariable = ContactNumber).place (x=130, y=120)

Label(root, text = 'Address', font = 'arial 12 bold', bg = 'white') .place (x=30, y=170)
Entry(root, textvariable = Address).place (x=130, y=170)

Label(root, text = 'Email', font = 'arial 12 bold', bg = 'white') .place (x=30, y=220)
Entry(root, textvariable = Email).place (x=130, y=220)

Button(root, text = 'Add Contact', font = 'arial 12 bold', bg = 'white', command = add).place(x=70,y=280)
Button(root, text = 'Delete Contact', font = 'arial 12 bold', bg = 'white', command = delete).place(x=200, y=280)
Button(root, text = 'Search Contact', font = 'arial 12 bold', bg = 'white', command = view).place(x=70, y=330)
Button(root, text = 'Sort Contact', font = 'arial 12 bold', bg = 'white', command = selectset).place(x=200, y=330)
Button(root, text = 'Exit', font = 'arial 12 bold', bg = 'grey', command = exit).place(x=470, y=330)

root.mainloop()


# In[ ]:




