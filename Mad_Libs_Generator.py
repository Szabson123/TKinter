from tkinter import *

root = Tk()
root.config(background='pink')
root.title('Libs Game')


def story1():
    
    newroot = Toplevel()
    newroot.config(background='yellow')
    
    def text(name, enter_a_game, eneter_a_city, player, drink, snack):
        return (f"One fine day, my friend {name} and I planned to engage in a {enter_a_game}\n "
                f"match in {eneter_a_city}. However, circumstances didn't allow us to participate.\n "
                f" Instead, we ended up attending the game and saw our most admired athlete, {player}, in action.\n "
                f"We sipped on {drink} and munched on some {snack}. It was truly an enjoyable experience!\n"
                f" We are eagerly anticipating another opportunity to go and relish the moment.")

    def close_window():
        newroot.destroy()

    def submit_story():
        story_text = text(name_input.get(), enter_a_game_input.get(),
                          enter_a_city_input.get(), player_input.get(),
                          drink_input.get(), snack_input.get())
        story_label.config(text=story_text)

        for widget in input_widgets:
            widget.destroy()
        submit.destroy()

        destroy_button = Button(newroot, text="End Story", command=close_window, background='blue')
        destroy_button.grid(row=1, column=0)
            
    title = Label(newroot, text='A Memorable Day', font=('Helvetica', 20))
    title.grid(row=0, column=0)
                
    name = Label(newroot, text='Name')
    name.grid(row=1, column=0)
    name_input = Entry(newroot)
    name_input.grid(row=1, column=1, pady=10)

    enter_a_game = Label(newroot, text='Game')
    enter_a_game.grid(row=2, column=0)
    enter_a_game_input = Entry(newroot)
    enter_a_game_input.grid(row=2, column=1, pady=10)
            
    enter_a_city = Label(newroot, text='City')
    enter_a_city.grid(row=3, column=0)
    enter_a_city_input = Entry(newroot)
    enter_a_city_input.grid(row=3, column=1, pady=10)

    player = Label(newroot, text='Player')
    player.grid(row=4, column=0)
    player_input = Entry(newroot)
    player_input.grid(row=4, column=1, pady=10)
            
    drink = Label(newroot, text='Drink')
    drink.grid(row=5, column=0)
    drink_input = Entry(newroot)
    drink_input.grid(row=5, column=1, pady=10)
            
    snack = Label(newroot, text='Snack')
    snack.grid(row=6, column=0)
    snack_input = Entry(newroot)
    snack_input.grid(row=6, column=1, pady=10)
            
    submit = Button(newroot, text='Submit', background='blue', command=submit_story)
    submit.grid(row=7, column=0, pady=15)

    story_label = Label(newroot, font=('Helvetica', 14), background='yellow')
    story_label.grid(row=8, column=0)

    input_widgets = [title, name, name_input, enter_a_game, enter_a_game_input, enter_a_city, enter_a_city_input,
                     player, player_input, drink, drink_input, snack, snack_input]


title = Label(root, text='Python Mad Libs Game', font=('Helvetica', 24))
title.grid(row=0, column=0)

button1 = Button(root, text='A memorable Game', background='blue', font=('Helvetica', 16), command=story1)
button1.grid(row=1, column=0, pady=100)

button2 = Button(root, text='Ambitions', font=('Helvetica', 16), background='blue')
button2.grid(row=2, column=0, pady=(0, 100))

root.mainloop()
