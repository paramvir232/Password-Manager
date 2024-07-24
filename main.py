from tkinter import *
from tkinter import messagebox
from widgets import Widgets
from random import choice, randint, shuffle
import pyperclip
import json


def key_check():
    key = int(widgets.entry_list[3].get())
    if 1111 < key < 9999:
        return True
    return False


# --------------------------- TEXT ENCRYPTOR -----------------------------------#
def encrypt(text, direction):
    """ Encrypts and Decrypts the given text and direection as 'encode'/'decode'"""
    key = int(widgets.entry_list[3].get())
    if key > lengthOfList:  # adjusting shift according to length of list
        key = key % lengthOfList

    encrypted_password = ""
    # encrypted_password = [letter for letter in text if letter not in finalList]
    for letter in text:
        if letter not in finalList:  #if input text letter's are not in our list
            encrypted_password += letter
            continue
        indexInlist = finalList.index(letter)
        if direction == "encode":
            shifted_index = indexInlist + key
            if shifted_index > (lengthOfList - 1):
                shifted_index -= lengthOfList  #loop back to list
        else:
            shifted_index = indexInlist - key
            if shifted_index < 0:
                shifted_index += lengthOfList  #loop back to list
        encrypted_password += finalList[shifted_index]

    return encrypted_password

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    """ Generates the Random Password """
    password_entry = widgets.entry_list[2]
    password_entry.delete(0, END)

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_number
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(END, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    """ Saves the Credentials to json file """
    website = widgets.entry_list[0].get()
    username = widgets.entry_list[1].get()
    password = widgets.entry_list[2].get()
    try:
        encoded_password = encrypt(password, 'encode')
    except ValueError:
        messagebox.showinfo(title='Error', message='Please Enter a Valid Encryption Key !')
        widgets.entry_list[3].delete(0, END)
        widgets.entry_list[3].insert(0, '0')

    else:
        if key_check():
            encrypted_username = encrypt(username, 'encode')
            detail_dict = {'username': encrypted_username, 'password': encoded_password}
            encypted_website = encrypt(website.lower(), 'encode')
            new_data = {encypted_website: detail_dict}
            new_entry_list = widgets.entry_list[4:]
            if len(website) == 0 or len(username) == 0 or len(password) == 0:
                messagebox.showinfo(title='Error', message='!! Please don\'t leave any feilds Empty !!')
            else:
                new_entries = []
                for index in range(0, len(new_entry_list), 2):
                    if len(new_entry_list[index].get()) == 0 or len(new_entry_list[index + 1].get()) == 0:
                        messagebox.showinfo(title='Error', message='Added Entry feilds are Empty !!')

                    else:
                        encrypted_feild = encrypt(new_entry_list[index + 1].get(), 'encode')
                        detail_dict.update({new_entry_list[index].get(): encrypted_feild})
                        new_entries.append(f'{new_entry_list[index].get().title()}: {new_entry_list[index + 1].get()}')

                new_entries_printable = '\n'.join(new_entries)
                is_ok = messagebox.askokcancel(title=f'Confirm Credentials for {website}',
                                               message=f'Do you confirm this credentials for website :{website} ?\n\n'
                                                       f'Username:  {username}\nPassword:  {password}\n{new_entries_printable}')
                if is_ok:
                    try:
                        with open("data.json", 'r') as file:
                            data = json.load(file)
                            if website in data:
                                want_update = messagebox.askyesnocancel(title='Already Exist',
                                                                        message=f'Data already Exists !!\nDo you want to update credentials for {website}?')
                                if want_update:
                                    data.update(new_data)
                            else:
                                data.update(new_data)
                    except:
                        with open("data.json", 'w') as file:
                            json.dump(new_data, file, indent=4)
                    else:
                        with open("data.json", 'w') as file:
                            json.dump(data, file, indent=4)
                    finally:
                        for enteries in widgets.entry_list[0::2]:
                            enteries.delete(0, END)

                        for entr_s in widgets.entry_list[4:]:
                            entr_s.destroy()

        else:
            messagebox.showinfo(title='Key Error',message='Please enter valid key of four digit (eg: 0000) !!')
# ---------------------------- ACCOUNT BLOCKING --------------------------

def account_block():
    """ Blocks the account after 5 wrong key guesses"""
    for entries in widgets.entry_list:
        entries.config(state="disabled")
    for buttons in widgets.button_list:
        buttons.config(state="disabled")
    messagebox.showinfo(title='Account Blocked', message=' You exceed max limit.\nYour account is BLOCKED')

# ---------------------------- SEARCHING ---------------------------------#

def search_credentials():
    """ Search the credential for given website with correct key given"""
    global search_max_tries

    if search_max_tries == 0:
        account_block()
    elif search_max_tries == 2:
        messagebox.showinfo(title='Warning', message='You only have Two remaning guesses untill your account will be '
                                                     'BLOCKED')

    website = widgets.entry_list[0].get().lower()
    encpryted_website = encrypt(website, 'encode')
    decrypted_website = encrypt(website, 'decode')

    try:
        with open('data.json') as file:
            data = json.load(file)
        new_entries = [f'{key}:  {encrypt(value, 'decode')}' for key, value in data[encpryted_website].items()]
    except :
        messagebox.showinfo(title="Key Error", message=f"Key Entered is Wrong. No Data found .!!")
        search_max_tries -= 1
    else:
        printable_new_entries = '\n'.join(new_entries)
        saved_password = data[encpryted_website]['password']
        decoded_password = encrypt(saved_password, 'decode')
        if encpryted_website in data:
            pyperclip.copy(decoded_password)
            messagebox.showinfo(title=f"{decrypted_website} Crendentials",
                                message=f'{printable_new_entries}')

        else:
            messagebox.showinfo(title='Error', message=f'No Details for {website} Found !')


# ---------------------------- ADD ENTRY ------------------------------- #
def add_new_entry():
    """ Add new entry mechanism"""
    global row_num
    if row_num < 11:
        widgets.add_entry(width=15, column=0, row=row_num)
        widgets.add_entry(width=34, column=1, row=row_num)
        row_num += 1
    else:
        messagebox.showinfo(title=" Max Add Entry Limit Reached",
                            message='You can\'t add more Entries !!\nMAX LIMIT REACHED')


# ---------------------------- UI SETUP ------------------------------- #

# Setting up the window
FONT = ('Arial', 15)
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
widgets = Widgets()
website_entry = Widgets()
window.resizable(False, False)

# For Random password generation
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
           'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '/', '\\', '<', '>', '@', '{', '}', '|', '~']
finalList = letters + symbols + numbers
lengthOfList = len(finalList)

# Image
pass_image = PhotoImage(file='logo.png')
widgets.add_image(img=pass_image, canvas_height=200, canvas_width=200, column=1, row=0)

# Website
widgets.add_label(text='Website:', font=FONT, column=0, row=1)
widgets.add_entry(width=34, column=1, row=1, focus=True)

# Email/Username
widgets.add_label(text='Email/Username:', font=FONT, column=0, row=2)
widgets.add_entry(width=50, column=1, row=2, columnspan=2, insert='paramvirgrewal232@gmail.com', )

# Password
widgets.add_label(text='Password:', font=FONT, column=0, row=3)
widgets.add_entry(width=34, column=1, row=3)
widgets.add_buttons(text="Generate Password", width=14, column=2, row=3, command=generate_password)

# Save button
row_num = 6
widgets.add_buttons(text="Save", width=41, column=1, row=row_num + 5, columnspan=2, command=save)

# Search button
search_max_tries = 5
widgets.add_buttons(text="Search", width=14, column=2, row=1, command=search_credentials)

# Encryption key
widgets.add_label(text='Encyption Key:', font=FONT, column=0, row=4)
widgets.add_entry(width=34, column=1, row=4, insert='0000')

# Add Entry button
widgets.add_buttons(text="Add Entry", width=14, column=0, row=row_num + 5, command=add_new_entry)

window.mainloop()
