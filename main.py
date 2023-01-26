import tkinter as tk
from tkinter import messagebox
import customtkinter

customtkinter.set_appearance_mode('light')  
customtkinter.set_default_color_theme('blue')

root = customtkinter.CTk()
root.geometry('500x600')
root.title('Spelling Bee Helper')
root.bind('<Return>', lambda event: submit())


def find_words(letters):
    words = []

    with open('robust.txt') as file:
        text = file.read()
    
    words_in_text = text.split()

    letters_set = set(letters)

    first_letter = letters[0]

    for word in words_in_text:
    # check if the word is long enough and contains only the given letters
        if (set(word).issubset(letters_set) and first_letter in word):
            words.append(word)

    return words 

def disable_button():
   textbox.configure(state='disabled')
   checkbox.toggle()
   checkbox.configure(text='Letters Entered:'+ (entry1.get()).upper())
   entry1.delete(0, 'end')

def len_check():
    if len(entry1.get()) == 7:
        return True 
    else:
        return False
def alpha_check():
    if entry1.get().isalpha():
        return True
    else:
        return False
    
    # Clears the textbox
def delete():
   entry1.delete("0","end")
    
def submit():
    # get the letters from the entry box
    # Check if the letters are valid, and there are seven of them
    entry1_value = entry1.get()
    if len_check() == False:
        messagebox.showerror('Error', 'Please enter 7 letters')
        delete()
        return
    if alpha_check() == False:
        messagebox.showerror('Error', 'Please enter only letters')
        delete()
        return
    if len_check() and alpha_check():
        textbox.configure(state='normal')
        textbox.delete('1.0', 'end')
    words = find_words(entry1_value)
    for i in sorted(words, reverse=True):
        textbox.insert('1.0', i+'\n')
    disable_button()

    
    

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=60,fill='both',expand=True)

label = customtkinter.CTkLabel(master=frame, text='Spelling Bee Helper')
label.pack(pady=10, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text='Place Center Letter at Beginning', width=350, font=('Arial', 20))
entry1.pack(pady=10, padx=10)

button = customtkinter.CTkButton(master=frame, text='Submit', command=submit)
button.pack(pady=10, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text='test checkbox')
checkbox.pack(pady=10, padx=10)


textbox = customtkinter.CTkTextbox(master=frame)
textbox.pack(pady=5, padx=10)

root.mainloop()