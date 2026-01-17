import tkinter as tk
import random

WIDTH=500
HEIGHT=500
speed=120
space_size=20 # block size
body_parts=3
food_color="red"
snake_color="green"
bg_color="black"

class Snake:
     def __init__(self):
          self.body_size=body_parts
          self.coordinates=[]  #this is snake body coordinates
          self.squares=[]

          for i in range(body_parts):
            self.coordinates.append([0,0])
          for x,y in self.coordinates :
               square=canvas.create_rectangle(
                   x, y, x+space_size, y+space_size, fill=snake_color,tag="snake"
               )

               self.squares.append(square)  

class Food:
    def __init__(self):
        x=random.randint(0, (WIDTH//space_size)-1)*space_size
        y=random.randint(0,(HEIGHT//space_size)-1)*space_size

        self.coordinates=[x,y] #this is food coordinates
        canvas.create_oval(
            x, y, x+space_size, y+space_size, fill=food_color,tag="food"
        )


def next_turn(snake,food):
    x,y=snake.coordinates[0]

    if direction =='up':
        y -= space_size
    elif direction == 'down':
        y += space_size
    elif direction == 'right':
        x += space_size
    elif direction == 'left':
        x -= space_size

    snake.coordinates.insert(0,[x,y])   

    square= canvas.create_rectangle(
        x, y, x+space_size, y+space_size,
        fill=snake_color
    )
    snake.squares.insert(0,square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score: {}".format(score))
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    #check collision
    if check_collision(snake):
        game_over()
    else:
        win.after(speed,next_turn,snake,food)

def change_direction(new_direction):
    global direction

    if new_direction == 'left' and  direction != 'right':
           direction= new_direction
    if new_direction == 'right' and  direction != 'left':
           direction= new_direction
    if new_direction == 'up' and  direction != 'down':
           direction= new_direction
    if new_direction == 'down' and  direction != 'up':
           direction= new_direction

def check_collision(snake):
    x,y =snake.coordinates[0]

    if x<0 or x>= WIDTH or y<0 or y>= HEIGHT:
         return True
    
    for body_part in snake.coordinates[1:]:
         if x==body_part[0] and y== body_part[1]:
              return True

    return False



def game_over():
    canvas.delete(tk.ALL)

    canvas.create_text(
        WIDTH / 2, HEIGHT / 2 - 40,
        font=("Arial", 30),
        text="GAME OVER",
        fill="red"
    )

    restart_btn = tk.Button(win,text="Restart",font=("Arial", 14),
                            bg="green",fg="white", command=restart_game)
    restart_btn.pack()



def restart_game():
    global snake, food, score, direction

    for widget in win.winfo_children():
        if isinstance(widget, tk.Button):
            widget.destroy()

    canvas.delete(tk.ALL)

    score = 0
    direction = "right"
    label.config(text="Score: 0")

    snake = Snake()
    food = Food()

    next_turn(snake, food)

    
win=tk.Tk()
win.title("Snake Game")
win.resizable(False,False)

score=0
direction ="right"

label=tk.Label(win,text="Score:0", font=("Arial",14))
label.pack()

canvas=tk.Canvas(win,bg=bg_color, height=HEIGHT,width=WIDTH)
canvas.pack()

win.update()
snake=Snake()
food=Food()

win.bind("<Left>", lambda e: change_direction("left"))
win.bind("<Right>", lambda e: change_direction("right"))
win.bind("<Up>", lambda e: change_direction("up"))
win.bind("<Down>", lambda e: change_direction("down"))

next_turn(snake, food)

win.mainloop()
