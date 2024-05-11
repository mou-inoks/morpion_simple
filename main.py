import tkinter


def print_winner():
    global win
    if win is False:
        win = True
        print("The player ", current_player, " has won the game")


def check_null():

    if win is False:
        print("Match null")



def switch_player():

    global current_player

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


def check_victory(clicked_row, clicked_col):
    #horrizontal
    count = 0
    for i in range(3):
        current_button = buttons[i][clicked_row]

        if current_button["text"] == current_player:
            count += 1

    if count == 3:
        print_winner()

#vertical
    count = 0
    for i in range(3):
        current_button = buttons[clicked_col][i]

        if current_button["text"] == current_player:
            count += 1

    if count == 3:
        print_winner()

#diagonale
    count = 0
    for i in range(3):
        current_button = buttons[i][i]

        if current_button["text"] == current_player:
            count += 1

    if count == 3:
        print_winner()

#diagonale inverse
    count = 0
    for i in range(3):
        current_button = buttons[2-i][i]

        if current_button["text"] == current_player:
            count += 1

    if count == 3:
        print_winner()

    if win is False:
        count = 0

        for col in range(3):
            for row in range(3):
                current_button = buttons[col][row]
                if current_button["text"] == "X" or current_button["text"] == "O":
                    count += 1
        if count == 9:
            print("Match null")


def place_symbol(row, col):
    print("click", row, col)

    clicked_button = buttons[col][row]
    if clicked_button["text"] == "":
        clicked_button.config(text=current_player)

    check_victory(row, col)
    switch_player()


def draw_grid():
    for col in range(3):
        buttons_in_cols = []
        for row in range(3):
            button = tkinter.Button(
                root,
                command=lambda r=row, c=col: place_symbol(r, c),
                font=("Arial", 100),
                width=3,
                height=2,
            )
            button.grid(row=row, column=col)
            buttons_in_cols.append(button)
        buttons.append(buttons_in_cols)


# stock
buttons = []
current_player = "X"
win = False

root = tkinter.Tk()

root.title("Morpion")
root.minsize(500,500)
draw_grid()
root.mainloop()