import turtle, pandas
from turtle import Turtle, Screen

screen = Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_state = []
# COUNT = 0

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50, states are correct", prompt="What is another "
                                                                                                 "state's name ?").title()
    # print(answer_state)

    data = pandas.read_csv("50_states.csv")
    states_list = data.state.to_list()

    # check if answer is there on the states list
    if answer_state == "Exit":
        missing_states = []
        for state in states_list:
            if state not in guessed_state:
                missing_states.append(state)
        # print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States to Learn.csv")
        break
    if answer_state in states_list:
        guessed_state.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data['state'] == answer_state]
        # if right , place the state to x,y coordinates
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)  # t.write(state_data.state.item())
        # COUNT += 1

