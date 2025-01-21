from taipy.gui import Markdown
from math import cos, exp

value = 10

def slider_moved(state):
    state.data = compute_data(state.value)

def compute_data(decay:int)->list:
    return [cos(i/6) * exp(-i*decay/600) for i in range(100)]

data = compute_data(value)

home_page = Markdown('pages/home/home.md')