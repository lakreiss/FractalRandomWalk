import tkinter as tk
from shape import Shape 

TK_SILENCE_DEPRECATION=1

SIZE, BORDER_SHRINK_FACTOR = 500, 10
WIDTH, HEIGHT = SIZE, SIZE

DEFAULT_NUMBER_OF_SIDES = 3
DEFAULT_WEIGHT_OF_CORNERS, DEFAULT_WEIGHT_OF_POINT = 1, 1
DEFAULT_NUMBER_OF_ITERATIONS = 10000
DEFAULT_ROTATION = {
    3: 30,
    4: 45,
    5: 54,
    6: 0,
    7: 13,
    8: 22,
    9: 30,
}

variables = [
    {"text": "Number of Sides", "value": DEFAULT_NUMBER_OF_SIDES, "stringvar": None},
    {"text": "Corner Weight", "value": DEFAULT_WEIGHT_OF_CORNERS, "stringvar": None},
    {"text": "Point Weight", "value": DEFAULT_WEIGHT_OF_POINT, "stringvar": None},
    {"text": "Number of Iterations", "value": DEFAULT_NUMBER_OF_ITERATIONS, "stringvar": None},
    {"text": "Rotation in Degrees", "value": DEFAULT_ROTATION[DEFAULT_NUMBER_OF_SIDES], "stringvar": None}
]

current_shape = None

def drawShape(canvas, number_of_sides, weight_of_corners, weight_of_point, number_of_iterations, rotation):
    global current_shape
    if current_shape and current_shape.number_of_sides != number_of_sides:
        current_shape = Shape(number_of_sides, WIDTH, HEIGHT, BORDER_SHRINK_FACTOR, getDefaultRotation(number_of_sides))
        variables[4]["value"] = getDefaultRotation(number_of_sides)
        variables[4]["stringvar"].set(getDefaultRotation(number_of_sides))
    else:
        current_shape = Shape(number_of_sides, WIDTH, HEIGHT, BORDER_SHRINK_FACTOR, rotation)
    current_shape.drawFractal(canvas, number_of_iterations, weight_of_corners, weight_of_point)

def clearCanvas(canvas):
    canvas.delete("all")

def createShape(event=None):
    clearCanvas(canvas)
    drawShape(canvas, int(variables[0]["stringvar"].get()), int(variables[1]["stringvar"].get()), int(variables[2]["stringvar"].get()), int(variables[3]["stringvar"].get()), int(variables[4]["stringvar"].get()))

def getDefaultRotation(number_of_sides):
    if number_of_sides > 9 or number_of_sides < 3:
        return 0
    else:
        return DEFAULT_ROTATION[number_of_sides]

root = tk.Tk()
root.title(string="Fractal Random Walk")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.grid(row=1, sticky=(tk.N, tk.W, tk.E, tk.S), columnspan=(len(variables) * 2))

for i, variable in enumerate(variables):
    tk.Label(root, text=variable["text"]).grid(column=(2 * i), row=0, columnspan=1)
    variable_entry = tk.Entry(root, width=int(WIDTH / (32 * len(variables))))
    variable_input = tk.StringVar(value=variable["value"])
    variable_entry["textvariable"] = variable_input
    variable_entry.grid(column=(1 + (2 * i)), row=0, columnspan=1)
    variable_entry.bind('<Key-Return>', createShape)
    variable["stringvar"] = variable_input

createShape()

root.mainloop()