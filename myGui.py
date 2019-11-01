from guizero import App, Text, TextBox, PushButton

app = App(title='Brodie Retallick', bg='blue ', width=1920, height=1080)
username = 'Michael'
password = 'Caleb'
def check_input():
    if un_box.value == username and pw_box.value == password:
        message = Text(app, text='Correct')
    else:
        message = Text(app, text='Incorrect!')
un_box = TextBox(app)
pw_box = TextBox(app)
submit = PushButton(app, text='Push if your TyLerR L0veridge', command=check_input)


# text1 = Text(app, text='Bruh backwards is Hurb "Hurbs and spices" lol.', size=35, font='TimesNewRomans')
# app.warn(title='Eben Eztebeth', text='Francios Faf De Klerk')
# app.yesno(title= "Second Row", text='Springboks')




app.display()
