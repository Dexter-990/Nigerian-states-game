import turtle
from turtle import Turtle, Screen
import pandas
image = "Nigeria-states-map (1).gif"
turtle.addshape(image)
turtle.shape(image)

screen = Screen()
screen.title("Nigerian states game")
screen.setup(800, 600)
states_list = ["Abia", "Adamawa", "Akwa Ibom", "Anambra", "Bauchi", "Bayelsa", "Benue", "Borno",
              "Cross River", "Delta", "Ebonyi", "Edo", "Ekiti", "Enugu", "Gombe", "Imo", "Jigawa", "Kaduna",
              "Kano", "Katsina", "Kebbi", "Kogi", "Kwara", "Lagos", "Nasarawa", "Niger", "Ogun", "Ondo", "Osun", "Oyo",
              "Plateau", "Rivers", "Sokoto", "Taraba", "Yobe", "Zamfara"]
states_x_cor = [-40, 165, -30, -70, 50, -120, 20, 200, -10, -120, -20, -110, -140, -50, 110, -65, 40, -20, 5, -40,
                -190, -70,
                -150, -210, -5, -140, -230, -150, -180, -230, 50, -70, -150, 100, 120, -100]

states_y_cor = [-150, 0, -190, -120, 70, -190, -80, 150, -150, -150, -120, -100, -50,
                -110, 50, -150, 150, 50, 120, 160, 130,
                -70, -10, -103, -20, 50, -80, -80, -60, -40, 10, -190, 190, -50, 150, 130]
Nigerian_states = {
    "state": states_list,
    "x": states_x_cor,
    "y": states_y_cor
}

data = pandas.DataFrame(Nigerian_states)
data.to_csv("36 states.csv")

tim = Turtle()
tim.hideturtle()
tim.penup()
states = data["state"].to_list()
guessed = []
while len(guessed) != 36:
    answer = screen.textinput(f"{len(guessed)}/50  36 states game", "Which state can you remember").title()
    if answer == "Exit":
        missing_s = [i for i in states if i not in guessed]
        missing_states = {
            "states": missing_s
        }
        miss = pandas.DataFrame(missing_states)
        miss.to_csv("missing_states.csv")
        print(f"You missed {len(states)}")
        mi = miss["states"]
        print(f"They're \n{mi}")
        break
    if answer in states:
        guessed.append(answer)
        row = data[data["state"] == answer]
        x = int(row.x)
        y = int(row.y)
        tim.goto(x, y)
        tim.write(answer, align="center")
