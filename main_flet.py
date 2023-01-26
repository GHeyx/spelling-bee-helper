# This is a web-version of the spelling bee helper built using Flet 
import flet as ft

def main(page: ft.Page):
    page.title = "Spelling Bee Helper"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_center()
    page.window_width = 700
    page.window_height = 700
    
    # Title of page in center
    def submit_click(e):
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
        
    # Text box for user input
    user_input_letters = ft.TextField(label="Begin Here", hint_text="Enter 7 letters beginning with the center letter", icon=ft.icons.EMOJI_EMOTIONS, capitalization=ft.TextCapitalization.CHARACTERS ,width=1000, on_change=text_changed)


    # Button to submit user input
    submit_button = ft.FloatingActionButton(text=" ", width=100, bgcolor="WHITE",height=50, disabled=True, on_click=submit_click)

    t = ft.Text()

    
    page.add(user_input_letters, submit_button,t)

ft.app(target=main)