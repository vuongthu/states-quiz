from turtle import Turtle, Screen
import pandas as pd

FONT = ("Arial", 7, "normal")
ALIGNMENT = "center"

screen = Screen()
screen.title("U.S. States Game")
screen.screensize(canvwidth=725, canvheight=491)

image = "blank_states_img.gif"
screen.addshape(image)

image_screen = Turtle()
text = Turtle()

image_screen.shape(image)

data = pd.read_csv("50_states.csv")

states_list = data.state.to_list()
x_list = data.x.to_list()
y_list = data.y.to_list()

correct_guesses = []

while True:
    user_guess = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                                  prompt="Name a state! Type exit if you give up.").title()

    if user_guess in states_list:
        position = states_list.index(user_guess)
        text.penup()
        text.hideturtle()
        text.goto(int(x_list[position]), int(y_list[position]))
        text.write(f"{states_list[position]}", align=ALIGNMENT, font=FONT)
        correct_guesses.append(user_guess)

    if len(correct_guesses) == 50 or user_guess == "Exit":
        missed_states = [state for state in states_list if state not in correct_guesses]
        break

# This will help us determine the location of where we click our mouse
# def get_mouse_click_coord(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coord)
#
# turtle.mainloop()

# screen.exitonclick()

# Now we can generate a new file called states_to_learn.csv
# See conditional above for List Comprehension edit

# missed_states = []
# for state in states_list:
#     if state not in correct_guesses:
#         missed_states.append(state)

# Uncomment below if you want to create a new CSV:

# states_dict = {
#     "Missed States": missed_states,
# }
#
# missed_states_data = pd.DataFrame(states_dict)
#
# missed_states_data.to_csv("states_to_learn.csv")
