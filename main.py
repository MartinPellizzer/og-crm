from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

lead_labels = [
    ['Business Name', 'First Name', 'Last Name', 'Address', 'Website', 'Phone', 'Email'],
]

lead_data = [
    ['Fungo Felice', 'villaggio puffi, 23', 'www.fungofelice.com', 'info@fungofelice.com', '555-555-5555'],
]

def clicked():
    print(business_name_entry.get())
    business_name_entry.delete(0, END)
    business_name_entry.insert(0, 'done')
    # messagebox.showinfo('this is my popup', 'hello there')
    response = messagebox.askokcancel('this is my popup', 'hello there')
    if response == 1:
        print('ok')
    else:
        print('cancel')

root = Tk()
root.title("OZONOGROUP CRM")
root.iconbitmap('logo.ico')

i = 0

frame1 = LabelFrame(root, text='Lead Info', padx=5, pady=5)
frame1.grid(row=i, column=0, padx=10, pady=10)

business_name_label = Label(frame1, text=f'{lead_labels[0][0]}:', width=12, anchor=E)
business_name_label.grid(row=i, column=0)
business_name_entry = Entry(frame1, width=50)
business_name_entry.grid(row=i, column=1)
i += 1

first_name_label = Label(frame1, text=f'{lead_labels[0][1]}:', width=12, anchor=E)
first_name_label.grid(row=i, column=0)
first_name_entry = Entry(frame1, width=50)
first_name_entry.grid(row=i, column=1)
i += 1

last_name_label = Label(frame1, text=f'{lead_labels[0][2]}:', width=12, anchor=E)
last_name_label.grid(row=i, column=0)
last_name_entry = Entry(frame1, width=50)
last_name_entry.grid(row=i, column=1)
i += 1

address_name_label = Label(frame1, text=f'{lead_labels[0][3]}:', width=12, anchor=E)
address_name_label.grid(row=i, column=0)
address_name_entry = Entry(frame1, width=50)
address_name_entry.grid(row=i, column=1)
i += 1

website_name_label = Label(frame1, text=f'{lead_labels[0][4]}:', width=12, anchor=E)
website_name_label.grid(row=i, column=0)
website_name_entry = Entry(frame1, width=50)
website_name_entry.grid(row=i, column=1)
i += 1

phone_name_label = Label(frame1, text=f'{lead_labels[0][5]}:', width=12, anchor=E)
phone_name_label.grid(row=i, column=0)
phone_name_entry = Entry(frame1, width=50)
phone_name_entry.grid(row=i, column=1)
i += 1

email_name_label = Label(frame1, text=f'{lead_labels[0][6]}:', width=12, anchor=E)
email_name_label.grid(row=i, column=0)
email_name_entry = Entry(frame1, width=50)
email_name_entry.grid(row=i, column=1)
i += 1

img1 = ImageTk.PhotoImage(Image.open('logo.png'))
image_label = Label(image=img1)
image_label.grid(row=i, column=0)
i += 1

button = Button(root, text='Save', width=60, command=lambda: clicked())
button.grid(row=i, column=0, columnspan=2)
i += 1

status_label = Label(root, text='status ok', bd=1, relief=SUNKEN, anchor=E)
status_label.grid(row=i, column=0, columnspan=2, sticky=W+E)
i += 1

root.mainloop()