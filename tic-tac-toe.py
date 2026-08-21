mport tkinter as tk
from tkinter import messagebox 

def check_winner():
    global winner
    # Highlight winning combo
    for combo in [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] !="":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            messagebox.showinfo("TIC-TAC-TOE", f"Player {buttons[combo[0]]['text']} wins! ")
            winner = True
            ask_play_again()
            return
       
    # Check for Draw
    if all(button["text"] != "" for button in buttons) and not winner:
        messagebox.showboxinfo("TIC-TAC-TOE", "its a draw")
        winner = True
        ask_play_again()

def button_click(index):
    global winner
    if buttons[index]["text"] == "" and not winner:
       buttons[index]["text"] = current_player
       check_winner()
       if not winner:
        toggle_player()

def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player} 's turn ")

def restart_game():
        global winner, current_player
        for button in buttons:
            button.config(text="", bg="SystemButtonFace")
        winner = False
        current_player = "X"
        label.config(text=f"Player {current_player} 's turn ")
        
def ask_play_again():
    """ask player if they want to replay after win/draw"""
    again = messagebox.askyesno("Play again?", "Do you want to play again?")
    if again:
        restart_game()
    else:
        root.quit()

root = tk.Tk()
root.title("TIC-TAC-TOE")

buttons = [tk.Button(root , text ="", font=("normal",25), width=6,height=2,command=lambda i=i: button_click(i)) for i in range(9)]

for i, button in enumerate(buttons):
    button.grid(row=i //3, column=i%3)

current_player = "X"
winner = False

label = tk.Label(root,text=f"Player{current_player} 's turn", font=("normal",16))
label.grid(row=3, column=0, columnspan=3)

restart_btn = tk.Button(root, text="Restart Game", font=("normal",14), command=restart_game)
restart_btn.grid(row=3, column=2)

root.mainloop()