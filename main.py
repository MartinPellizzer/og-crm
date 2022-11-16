from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3

lead_labels = [
    ['Business Name', 'First Name', 'Last Name', 'Address', 'Website', 'Phone', 'Email'],
]

lead_data = [
    ['Fungo Felice', 'villaggio puffi, 23', 'www.fungofelice.com', 'info@fungofelice.com', '555-555-5555'],
]


def save():
    print(business_name_entry.get())
    business_name_entry.delete(0, END)
    business_name_entry.insert(0, 'done')
    messagebox.showinfo('this is my popup', 'hello there')
    response = messagebox.askokcancel('this is my popup', 'hello there')
    if response == 1:
        print('ok')
    else:
        print('cancel')


def submit():
	conn = sqlite3.connect('database.db')
	c = conn.cursor()

	# insert into
	c.execute('insert into leads values (:date_first_added, :date_last_updated, :first_name, :last_name, :business_name, :business_address, :website, :phone, :email, :status)',
		{
			'date_first_added': '2022/09/11', 
			'date_last_updated': '2022/11/15', 
			'first_name': first_name_entry.get(), 
			'last_name': last_name_entry.get(), 
			'business_name': business_name_entry.get(), 
			'business_address': business_address_entry.get(),
			'website': website_entry.get(),
			'phone': phone_entry.get(),
			'email': email_entry.get(),
			'status': 'gray'
		}
	)

	conn.commit()
	conn.close()
	
	first_name_entry.delete(0, END)
	last_name_entry.delete(0, END)
	business_name_entry.delete(0, END)
	business_address_entry.delete(0, END)
	website_entry.delete(0, END)
	phone_entry.delete(0, END)
	email_entry.delete(0, END)


def search():
	conn = sqlite3.connect('database.db')
	c = conn.cursor()

	# insert into
	c.execute('select oid, * from leads')
	rows = c.fetchall()
	# print(rows)

	# print_row = ''
	# for row in rows:
	# 	print_row += str(row) + '\n'
	
	# label = Label(root, text=print_row)
	# label.grid(row=0, column=2)

	conn.commit()
	conn.close()

	return rows


def delete():
	conn = sqlite3.connect('database.db')
	c = conn.cursor()

	id = delete_entry.get()

	c.execute(f'delete from leads where oid={id}')
	
	conn.commit()
	conn.close()


def demo_drop_table():
	conn = sqlite3.connect('database.db')
	c = conn.cursor()

	c.execute('DROP TABLE leads')

	conn.commit()
	conn.close()


demo_drop_table()
	



conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute('''
	create table if not exists leads (
		date_first_added text,
		date_last_updated text,
		first_name text,
		last_name text,
		business_name text,
		business_address text,
		website text,
		phone text,
		email text,
		status text
	)
''')

conn.commit()
conn.close()



root = Tk()
root.title("OZONOGROUP CRM")
root.iconbitmap('logo.ico')
root.geometry("1280x720")

# i = 0

# frame1 = LabelFrame(root, text='Lead Info', padx=5, pady=5)
# frame1.grid(row=i, column=0, padx=10, pady=10)


# date_first_added_label = Label(frame1, text=f'2022/09/11', width=12, anchor=E)
# date_first_added_label.grid(row=i, column=0)
# i += 1

# date_last_updated_label = Label(frame1, text=f'2022/11/15', width=12, anchor=E)
# date_last_updated_label.grid(row=i, column=0)
# i += 1

# first_name_label = Label(frame1, text=f'{lead_labels[0][1]}:', width=12, anchor=E)
# first_name_label.grid(row=i, column=0)
# first_name_entry = Entry(frame1, width=50)
# first_name_entry.grid(row=i, column=1)
# i += 1

# last_name_label = Label(frame1, text=f'{lead_labels[0][2]}:', width=12, anchor=E)
# last_name_label.grid(row=i, column=0)
# last_name_entry = Entry(frame1, width=50)
# last_name_entry.grid(row=i, column=1)
# i += 1

# business_name_label = Label(frame1, text=f'{lead_labels[0][0]}:', width=12, anchor=E)
# business_name_label.grid(row=i, column=0)
# business_name_entry = Entry(frame1, width=50)
# business_name_entry.grid(row=i, column=1)
# i += 1

# business_address_label = Label(frame1, text=f'Business Address', width=12, anchor=E)
# business_address_label.grid(row=i, column=0)
# business_address_entry = Entry(frame1, width=50)
# business_address_entry.grid(row=i, column=1)
# i += 1

# website_label = Label(frame1, text=f'{lead_labels[0][4]}:', width=12, anchor=E)
# website_label.grid(row=i, column=0)
# website_entry = Entry(frame1, width=50)
# website_entry.grid(row=i, column=1)
# i += 1

# phone_label = Label(frame1, text=f'{lead_labels[0][5]}:', width=12, anchor=E)
# phone_label.grid(row=i, column=0)
# phone_entry = Entry(frame1, width=50)
# phone_entry.grid(row=i, column=1)
# i += 1

# email_label = Label(frame1, text=f'{lead_labels[0][6]}:', width=12, anchor=E)
# email_label.grid(row=i, column=0)
# email_entry = Entry(frame1, width=50)
# email_entry.grid(row=i, column=1)
# i += 1

# img1 = ImageTk.PhotoImage(Image.open('logo.png'))
# image_label = Label(image=img1)
# image_label.grid(row=i, column=0)
# i += 1

# button = Button(root, text='Save', width=60, command=lambda: save())
# button.grid(row=i, column=0, columnspan=2)
# i += 1

# submit_button = Button(root, text='Submit', width=60, command=lambda: submit())
# submit_button.grid(row=i, column=0, columnspan=2)
# i += 1

# search_button = Button(root, text='Search', width=60, command=lambda: search())
# search_button.grid(row=i, column=0, columnspan=2)
# i += 1

frame_left = LabelFrame(root, text='Frame Left', width=120)
frame_left.pack(side=LEFT, fill=Y)
frame_center = LabelFrame(root, text='Frame Center')
frame_center.pack(side=LEFT, fill=BOTH, expand=True)

i = 0

business_name_label = Label(frame_left, text='Business Name', width=12)
business_name_label.grid(row=i, column=0)
business_name_entry = Entry(frame_left, width=30)
business_name_entry.grid(row=i, column=1)
i += 1

first_name_label = Label(frame_left, text='First Name', width=12)
first_name_label.grid(row=i, column=0)
first_name_entry = Entry(frame_left, width=30)
first_name_entry.grid(row=i, column=1)
i += 1

list_button = Button(frame_left, text='Get', command=lambda: get_list_item())
list_button.grid(row=i, column=0)
i += 1


# leads = [
# 	['1', 'Leen', 'Randell'],
# 	['2', 'Rain', 'Willbert'],
# 	['3', 'Noah', 'BlahBlah'],
# ]



def add_lead(line):
	conn = sqlite3.connect('database.db')
	c = conn.cursor()

	# # insert into
	# c.execute('insert into leads values (:date_first_added, :date_last_updated, :first_name, :last_name, :business_name, :business_address, :website, :phone, :email, :status)',
	# 	{
	# 		'date_first_added': '2022/09/11', 
	# 		'date_last_updated': '2022/11/15', 
	# 		'first_name': first_name_entry.get(), 
	# 		'last_name': last_name_entry.get(), 
	# 		'business_name': business_name_entry.get(), 
	# 		'business_address': business_address_entry.get(),
	# 		'website': website_entry.get(),
	# 		'phone': phone_entry.get(),
	# 		'email': email_entry.get(),
	# 		'status': 'gray'
	# 	}
	# )

	c.execute('insert into leads values (:date_first_added, :date_last_updated, :first_name, :last_name, :business_name, :business_address, :website, :phone, :email, :status)',
		{
			'date_first_added': '2022/09/11', 
			'date_last_updated': '2022/11/15', 
			'first_name': '', 
			'last_name': '', 
			'business_name': line[0], 
			'business_address': line[0],
			'website': '',
			'phone': '',
			'email': '',
			'status': 'gray'
		}
	)

	conn.commit()
	conn.close()
	

import csv
def get_list_item():
  
	# Parsed the specifications to the
	# Text widget using .configure( ) method.

	with open("salumifici_treviso.csv", "r") as f:
		reader = csv.reader(f, delimiter="\\")
		for i, line in enumerate(reader):
			print(line)
			add_lead(line)
	# print(listbox.curselection())

	leads = search()
	for lead in leads:
		print(lead)

	listbox.delete(0, END)
	s = f"{'ID' : <8}{'Date 1' : <16}{'Date 2' : <16}{'First Name' : <16}"
	print(s)
	listbox.insert(i, s)
	for i, lead in enumerate(leads):
		s = f"	{lead[0] : <8}\
				{lead[1] : <16}\
				{lead[2] : <16}\
				{lead[3] : <16}\
				{lead[4] : <16}\
				{lead[5] : <64}\
				{lead[6] : <16}\
				"
		print(s)
		listbox.insert(i+1, s)


listbox = Listbox(frame_center)

Font_tuple = (".fonts/FiraMono-Regular.ttf", 12, "bold")
listbox.configure(font = Font_tuple)

listbox.pack(fill=X) 

# list_button = Button(root, text='Get', width=60, command=lambda: get_list_item())
# list_button.pack()


# def open():
# 	second_window = Toplevel()

# 	new_business_name_label = Label(second_window, text='Second window')
# 	new_business_name_label.grid(row=0, column=0)
# 	new_business_name_entry = Entry(second_window, width=30)
# 	new_business_name_entry.grid(row=0, column=1, padx=20)


# BUTTON
# button_window = Button(root, text='Open', width=60, command=lambda: open())
# button_window.grid(row=i, column=0, columnspan=2)
# i += 1


# delete_label = Label(frame1, text=f'Delete id: ', width=12, anchor=E)
# delete_label.grid(row=i, column=0)
# delete_entry = Entry(frame1, width=50)
# delete_entry.grid(row=i, column=1)
# i += 1

# delete_button = Button(root, text='Delete', width=60, command=lambda: delete())
# delete_button.grid(row=i, column=0, columnspan=2)
# i += 1

# status_label = Label(root, text='status ok', bd=1, relief=SUNKEN, anchor=E)
# status_label.grid(row=i, column=0, columnspan=2, sticky=W+E)
# i += 1

root.mainloop()
