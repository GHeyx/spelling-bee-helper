# This is a web-version of the spelling bee helper built using Flet 
import flet as ft

def main(page: ft.Page):
    # Title of page in center
    page.title = "Spelling Bee Helper"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.window_center()
    page.window_width = 700
    page.window_height = 900
    page.padding = 50
    
    gray = "#C8C8C6"
    ready_to_submit_color = "#8d7709"
    
    
    def submit_click(e):
        entry1_value = user_input_letters.value.lower()
        answers = find_words(entry1_value)
        t.value = (f"Here's what I found, " + str(len(answers)) + " words: ")
        
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
            submit_button.text = "Submit"
            submit_button.color = "BLACK"
            t.value = ("Ready to Submit!")
        else:
            submit_button.disabled = True
            submit_button.bgcolor = gray
            submit_button.text = " "
        page.update()
    
    def reset_click(e):
        user_input_letters.value = ""
        t.value = ("")
        submit_button.disabled = True
        submit_button.bgcolor = "#C8C8C6"
        submit_button.text = " "
        answers_list_view.controls.clear()
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
    user_input_letters = ft.TextField(label="Begin Here", hint_text="Enter 7 letters beginning with the center letter", icon=ft.icons.EMOJI_EMOTIONS, capitalization=ft.TextCapitalization.CHARACTERS ,width=1000, on_change=text_changed, on_submit=submit_click, max_length=7)
    
    # List of words that contain the given letters to be displayed
    answers_list_view = ft.ListView(width=1000, height=800,expand=True)
    
    
    
    

    # Button to submit user input
    submit_button = ft.FloatingActionButton(text=" ", width=100,bgcolor=gray, height=50, disabled=True, on_click=submit_click,icon=ft.icons.UPCOMING)
    # Button to reset user input and the list of words
    reset_button = ft.FloatingActionButton(text="Reset", width=100, bgcolor="BLUE",height=50, on_click=reset_click, icon=ft.icons.RESTORE)

    # Container of buttons to be displayed at the bottom of the page
    bottom_buttons = ft.Row(controls =
        [reset_button,submit_button], alignment=ft.MainAxisAlignment.SPACE_EVENLY)

    
    t = ft.Text()

    
    page.add(user_input_letters, t, answers_list_view, bottom_buttons)

# Run the app in a web browser by adding the following line:
# ft.app(target=main, view=ft.WEB_BROWSER)
ft.app(target=main)