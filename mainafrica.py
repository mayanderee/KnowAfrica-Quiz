import turtle
import pandas

screen = turtle.Screen()
screen.title("AFRICAN COUNTRIES GAME")
image = "africa-vegetation.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("55_countries.csv")
all_countries = data.country.to_list()
guessed_countries = []

while len(guessed_countries) < 55:
    answer_country = screen.textinput(title=f"{len(guessed_countries)}/55 Countries Correct",
                                    prompt="What's another country's name?r").title()

    if answer_country == "Exit":
        missing_countries = []  # Create a new list to add countries not in guessed countries
        for country in all_countries:
            if country not in guessed_countries:
                missing_countries.append(country)
        new_data = pandas.DataFrame(missing_countries)
        new_data.to_csv("countries_to_learn.csv")  # Create a new file to add countries not guessed
        break
    if answer_country in all_countries:
        guessed_countries.append(answer_country)  # guessed successful country is added on the map
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        country_data = data[data.country == answer_country]
        t.goto(int(country_data.x), int(country_data.y))
        # t.write(state_data.state.item())
        t.write(answer_country)
    # create a turtle to write the name of the country at country's x and y coordinates


def get_mouse_click_oor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_oor)

turtle.mainloop()
