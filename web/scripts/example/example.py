import advent_of_code_explainer as aoce
from pyscript import document

def do_a_thing(event):
    input_text = document.querySelector("#input_number")
    input_number = input_text.value
    output_div = document.querySelector("#output_number")
    # The current version this is just a placeholder function that adds 2.
    output_div.innerText = str(aoce.puzzles.year_2024.day_1.solve_one(int(input_number)))
