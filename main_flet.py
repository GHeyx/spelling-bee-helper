# This is a web-version of the spelling bee helper built using Flet 
import this
import flet as ft

def main(page: ft.Page):
    page.title = "Spelling Bee Helper"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.window_center()
    page.window_width = 700
    page.window_height = 900
    page.padding = 50
    
    # Title of page in center
    def submit_click(e):
        t.value = ("You clicked the button!")
        page.update()
    
    # Submit Button clickable only when 7 characters are entered
    def text_changed(e):
        count = len(e.control.value)
        remaining = 7 - count
        t.value = (f"Letters Remaining:  {remaining} ")
        if count==7:
            submit_button.disabled = False
            submit_button.bgcolor = "BLUE"
            submit_button.text = "Submit"
            t.value = ("Ready to Submit!")
        else:
            submit_button.disabled = True
            submit_button.bgcolor = "WHITE"
            submit_button.text = " "
        page.update()
    
    # Automatically move to next text box when 1 character is entered
    def next_field(e):
        if len(e.control.value) == 1:
            e.control.next.focus()
        else:
            e.control.focus()
        
    # Text box for user input
    user_input_letters = ft.TextField(label="Begin Here", hint_text="Enter 7 letters beginning with the center letter", icon=ft.icons.EMOJI_EMOTIONS, capitalization=ft.TextCapitalization.CHARACTERS ,width=1000, on_change=text_changed, on_submit=submit_click, max_length=7)
    
    answers = ft.ListView(width=1000, height=800,expand=True)
    for i in range(50):
        answers.controls.append(ft.Text(f"Line {i}"))
    
    

    # Button to submit user input
    submit_button = ft.FloatingActionButton(text=" ", width=100, bgcolor="WHITE",height=50, disabled=True, on_click=submit_click)

    t = ft.Text()

    
    page.add(user_input_letters, submit_button,t, answers)

# Run the app in a web browser by adding the following line:
# ft.app(target=main, view=ft.WEB_BROWSER)
ft.app(target=main)