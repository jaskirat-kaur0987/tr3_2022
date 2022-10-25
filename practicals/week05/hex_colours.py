COLOR_NAME_TO_COLOR_CODE = {
    "aliceblue":  "#f0f8ff",
    "apricot": "#fbceb1",
    "aqua": "#00ffff",
    "boysenberry": "#873260",
    "brunswick green": "#1b4d3e",
    "cadetblue": "#5f9ea0",
    "caribbean green": "#00cc99",
    "chartreuse1": "#7fff00",
    "cosmic cobalt": "#2e2d88",
    "darkseagreen2": "#b4eeb4",
}
color_name = input("Enter color name(hit enter to quit): ").lower()
while color_name != "":
    if color_name in COLOR_NAME_TO_COLOR_CODE:  # find key
        print(f"{color_name} is {COLOR_NAME_TO_COLOR_CODE[color_name]}")
    else:
        print("Invalid color name")
    color_name = input("Enter color name(hit enter to quit): ").lower()
print("Bye")


