from tkinter import *
from PIL import Image, ImageTk
import random

userscore = 0
pcscore = 0
games_played = 0  # Total number of games played

# Declare uninitialized variables
L1 = None
pcchose = None


### Functions of the game
def enter(event):
    rock.config(bg='black', fg='white')


def enter1(event):
    paper.config(bg='black', fg='white')


def enter2(event):
    scissor.config(bg='black', fg='white')


def leave(event):
    rock.config(bg='white', fg='black')


def leave1(event):
    paper.config(bg='white', fg='black')


def leave2(event):
    scissor.config(bg='white', fg='black')


def entergame(event):
    maingame()


# Maingame Function will open a new GUI window and provide a platform to play RPS
def maingame():
    global userscore, pcscore, games_played, L1, pcchose
    global nameinp, rock, paper, scissor
    global stats_label, winrate_label

    root.geometry('650x450')
    name.destroy()
    f1.destroy()
    inpname.destroy()
    sub.destroy()

    # Function to update score and statistics
    def update_stats():
        # Calculate win rate
        if games_played > 0:
            user_winrate = round((userscore / games_played) * 100, 1)
            pc_winrate = round((pcscore / games_played) * 100, 1)
        else:
            user_winrate = pc_winrate = 0.0

        # Update statistics labels
        stats_label.config(text=f"Games Played: {games_played}")
        winrate_label.config(text=f"Winrate - {nameinp.get()}: {user_winrate}%, PC: {pc_winrate}%")

    # Display game title
    head = Label(root, text='Rock Paper Scissor', font='arial 35 bold', bg='black', fg='white')
    head.grid(columnspan=2, row=0, ipadx=70, padx=33, pady=10)

    # Display win rate and total games played
    stats_label = Label(root, text="Games Played: 0", font='Rockwell 13 bold', bg='#FFD700', fg='black')
    stats_label.grid(row=1, column=0, columnspan=2, pady=5)

    winrate_label = Label(root, text="Winrate - You: 0.0%, PC: 0.0%", font='Rockwell 13 bold', bg='#FFD700', fg='black')
    winrate_label.grid(row=2, column=0, columnspan=2, pady=5)

    # Display user and PC scores
    L2 = Label(root, text=f"{nameinp.get()} Score: {userscore}", bg='#4834DF', fg='#ffffff', borderwidth=5,
               relief=RAISED, font='Rockwell 13 bold', padx=4, pady=2)
    L2.grid(row=3, column=0, pady=15)
    L3 = Label(root, text=f"PC Score: {pcscore}", bg='#4834DF', fg='white', borderwidth=5, relief=RAISED,
               font='Rockwell 13 bold', padx=4, pady=2)
    L3.grid(row=3, column=1, pady=15)

    # Function to handle click events
    def click(event):
        global userscore, pcscore, games_played, L1, pcchose

        # Remove previous result
        if L1:
            L1.grid_forget()
        if pcchose:
            pcchose.destroy()

        val = event.widget.cget('text')  # User's choice

        # PC's choice
        l1 = ['Rock', 'Paper', 'Scissor']
        pc_opt = random.choice(l1)

        # Display PC's choice
        pcchose = Label(root, text=f'PC Opted: {pc_opt}', font='lucida 15 bold', bg='black', fg='red')
        pcchose.grid(row=5, column=1, pady=15)

        # Game logic
        if val == 'Rock' and pc_opt == 'Paper':
            L1 = Label(root, text='PC Won', font='lucida 15 bold', bg='black', fg='gold')
            L1.grid(row=6, column=1, pady=15)
            pcscore += 1
        elif val == 'Rock' and pc_opt == 'Scissor':
            L1 = Label(root, text=f'{nameinp.get()} Won', font='lucida 15 bold', bg='black', fg='gold')
            L1.grid(row=6, column=1, pady=15)
            userscore += 1
        elif val == 'Paper' and pc_opt == 'Scissor':
            L1 = Label(root, text='PC Won', font='lucida 15 bold', bg='black', fg='gold')
            L1.grid(row=6, column=1, pady=15)
            pcscore += 1
        elif val == 'Paper' and pc_opt == 'Rock':
            L1 = Label(root, text=f'{nameinp.get()} Won', font='lucida 15 bold', bg='black', fg='gold')
            L1.grid(row=6, column=1, pady=15)
            userscore += 1
        elif val == 'Scissor' and pc_opt == 'Rock':
            L1 = Label(root, text='PC Won', font='lucida 15 bold', bg='black', fg='gold')
            L1.grid(row=6, column=1, pady=15)
            pcscore += 1
        elif val == 'Scissor' and pc_opt == 'Paper':
            L1 = Label(root, text=f'{nameinp.get()} Won', font='lucida 15 bold', bg='black', fg='gold')
            L1.grid(row=6, column=1, pady=15)
            userscore += 1
        elif val == pc_opt:
            L1 = Label(root, text=f"It's A Tie", font='lucida 15 bold', bg='black', fg='gold')
            L1.grid(row=6, column=1, pady=15)

        # Increment total games played
        games_played += 1

        # Update scores and statistics
        L2.config(text=f"{nameinp.get()} Score: {userscore}")
        L3.config(text=f"PC Score: {pcscore}")
        update_stats()

    # Player 1 buttons
    rock = Button(root, text='Rock', font='comicsansms 14 bold', height=1, width=7)
    rock.grid(row=4, column=0, pady=15)
    rock.bind('<Enter>', enter)
    rock.bind('<Leave>', leave)
    rock.bind('<Button-1>', click)

    paper = Button(root, text='Paper', font='comicsansms 14 bold', height=1, width=7)
    paper.grid(row=5, column=0)
    paper.bind('<Enter>', enter1)
    paper.bind('<Leave>', leave1)
    paper.bind('<Button-1>', click)

    scissor = Button(root, text='Scissor', font='comicsansms 14 bold', height=1, width=7)
    scissor.grid(row=6, column=0, pady=15)
    scissor.bind('<Enter>', enter2)
    scissor.bind('<Leave>', leave2)
    scissor.bind('<Button-1>', click)

    # Close button
    btnclose = Button(root, text="Close Game", command=root.destroy, bg='green', font='arial 10 bold')
    btnclose.grid(row=7, column=0, columnspan=2, pady=20)


''' GUI Program Starting '''
root = Tk()
root.title('Rock Paper Scissor')
root.geometry('650x450')
root.maxsize(650, 450)
root.minsize(650, 450)

# Initial image and frame
f1 = Frame(root)
img = Image.open('rps.png')
img = img.resize((650, 450), Image.Resampling.LANCZOS)
pic = ImageTk.PhotoImage(img)
Lab = Label(f1, image=pic)
Lab.pack()
f1.pack()

# Initial screen widgets
name = Label(root, text='Enter Your Name :', font='arial 15 bold')
name.place(x=262, y=20)

nameinp = StringVar()
inpname = Entry(root, textvar=nameinp, font='arial 10 bold')
inpname.bind('<Return>', entergame)
inpname.place(x=275, y=60)

sub = Button(root, text="Let's Play", font='arial 15 bold', bg='white', fg='black', command=maingame)
sub.place(x=290, y=88)

root.mainloop()