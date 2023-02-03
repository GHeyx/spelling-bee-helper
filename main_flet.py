# This is a web-version of the spelling bee helper built using Flet 
import flet as ft

# TODO: Add quit button
# TODO: Add panagram checker, and make the panagram in the list, if found, a bold typeface
# TODO: Add label below list view to source the dictionary
# TODO: Save the list of words to a file with date and time
# TODO: Save today's letters and words to a file with date and time to keep history
# TODO: Add project as a webpage to portfolio website

def main(page: ft.Page):
    # Title of page in center
    page.title = "Spelling Bee Helper"
    page.vertical_alignment = ft.MainAxisAlignment.SPACE_AROUND
    page.window_center()
    page.window_width = 700
    page.window_height = 1000
    page.padding = 50
    
    gray = "#C8C8C6"
    ready_to_submit_color = "#8d7709"
    
    
    def submit_click(e):
        entry1_value = user_input_letters.value.lower()
        answers = find_words(entry1_value)
        amount_of_words = (len(answers))
        if amount_of_words == 0:
            t.value = ("No words found.")
        else:
            t.value = (f"Here's what I found, " + str(amount_of_words) + " words: ")
        
        for i in sorted(answers):
            answers_list_view.controls.append(ft.Text(" " + i, size=20, style=ft.TextThemeStyle.LABEL_MEDIUM))
            page.update()
        
        
            
        page.update()
    
    # Submit Button clickable only when 7 characters are entered
    def text_changed(e):
        count = len(e.control.value)
        remaining = 7 - count
        t.value = (f"Letters Remaining:  {remaining} ")
        if count==7:
            submit_button.disabled = False
            submit_button.bgcolor = ready_to_submit_color
            t.value = ("Ready to Submit! Hit Enter or click the button.")
        else:
            submit_button.disabled = True
            submit_button.bgcolor = gray
        page.update()
    
    def reset_click(e):
        user_input_letters.value = ""
        t.value = ("")
        submit_button.disabled = True
        submit_button.bgcolor = "#C8C8C6"
        answers_list_view.controls.clear()
        user_input_letters.focus()
        page.update()
    
    # Find words in the dictionary that contain the given letters
    def find_words(word):
        words = []
        with open('robust.txt') as file:
            text = file.read()
        words_in_text = text.split()
        letters_set = set(word)

        first_letter = word[0]

        for word in words_in_text:
        # check if the word is long enough and contains only the given letters
            if (set(word).issubset(letters_set) and first_letter in word):
                words.append(word)
        return words
    
    # Automatically move to next text box when 1 character is entered, this is a future feature to mimic the behavior of a security code form that auto submits when all 7 boxes are filled
    def next_field(e):
        if len(e.control.value) == 1:
            e.control.next.focus()
        else:
            e.control.focus()
        
    # Text box for user input
    user_input_letters = ft.TextField(label="Begin Here", hint_text="Created by Ernest", icon=ft.icons.EMOJI_EMOTIONS, capitalization=ft.TextCapitalization.CHARACTERS,width=400, on_change=text_changed, on_submit=submit_click, max_length=7, content_padding=25, text_align=ft.TextAlign.CENTER)
    
    # Container type Row for text box
    e1 = ft.Row(controls=[user_input_letters], alignment=ft.MainAxisAlignment.CENTER, expand=0)
    
    
    # Instructions text
    c = ft.Column(controls=[
        ft.Text("Enter 7 letters beginning with the center letter.", text_align=ft.TextAlign.CENTER, size=16, style=ft.TextThemeStyle.LABEL_SMALL,color=gray)],horizontal_alignment=ft.CrossAxisAlignment.STRETCH,expand=0)
    # horizontal_alignment=ft.CrossAxisAlignment.END,
    # alignment=ft.MainAxisAlignment.END,

    
    
    # List of words that contain the given letters to be displayed
    answers_list_view = ft.ListView(width=400, height=400)
    # Container of type row for list of words
    alv_row = ft.Row(controls=[answers_list_view], alignment=ft.MainAxisAlignment.CENTER, expand=0)
    
    
    # Button to submit user input
    submit_button = ft.FloatingActionButton(text="Submit", width=150,expand=0, bgcolor=gray, height=50, disabled=True, on_click=submit_click,icon=ft.icons.UPCOMING)
    # Button to reset user input and the list of words
    reset_button = ft.FloatingActionButton(text="Reset", width=150,expand=0, bgcolor="BLUE",height=50, on_click=reset_click, icon=ft.icons.RESTORE)

    # Container of buttons to be displayed at the bottom of the page
    bottom_buttons = ft.Row(controls =
        [reset_button,submit_button], alignment=ft.MainAxisAlignment.CENTER, expand=0, spacing=20)

    # Text to be displayed above the list of words
    t = ft.Text(size=16, style=ft.TextThemeStyle.LABEL_MEDIUM,color=gray)
    t_row = ft.Row(controls=[t], alignment=ft.MainAxisAlignment.CENTER, expand=0)

    
    page.add(c, e1, t_row, alv_row, bottom_buttons)

# Run the app in a web browser by adding the following line:
# ft.app(target=main, view=ft.WEB_BROWSER)
ft.app(target=main)