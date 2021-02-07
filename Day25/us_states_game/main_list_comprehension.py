import turtle
import pandas
from states import States

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = States()
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    print(answer_state)

    if data[data.state == answer_state.title()].empty:
        print("State doesnt exist")
        missing_states = [state for state in all_states if state not in guessed_states]
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        game_is_on = False
    else:
        print(data[data.state == answer_state.title()])
        df = data[data.state == answer_state.title()]
        print(int(df.x))
        print(int(df.y))
        states.create_state(answer_state, int(df.x), int(df.y))
        guessed_states.append(answer_state.title())


# Get co-ordinates of mouse click
def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()

# screen.exitonclick()
