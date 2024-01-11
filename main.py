from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("The US States Game")
turtle = Turtle()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()


guess_state = []
while len(guess_state) < 50:
    answer_state = screen.textinput(title=f"{len(guess_state)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    # exit the game
    if answer_state == "Exit":
        # solution 1 : save the states have not guessed in state_to_learn.csv
        missing_state = [state for state in all_states if state not in guess_state]
        # solution 2 :
        # missing_state = []
        # for state in all_states:
        #     if state not in guess_state:
        #         missing_state.append(state)
        frame = pandas.DataFrame(missing_state)
        frame.to_csv("state_to_learn.csv")
        break
    # if answer_state is one of the state in the all state of 50_states.csv
    if answer_state in all_states:
        guess_state.append(answer_state)
        # create a turtle to write down the state's name
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)



