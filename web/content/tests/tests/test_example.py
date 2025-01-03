import asyncio
from base import upytest

import advent_of_code_explainer as aoce

from pyscript import document, web, when

async def test_example():
    input_container = document.querySelector("#input_number")
    input_container.value = "101"

    just_a_button = web.page.find("#do_a_thing_button")[0]
    call_flag = asyncio.Event()

    @when("click", just_a_button)
    def on_click(event):
        call_flag.set()
        input_text = document.querySelector("#input_number")
        input_number = input_text.value
        output_div = document.querySelector("#output_number")
        # The current version this is just a placeholder function that adds 2.
        output_div.innerText = str(aoce.puzzles.year_2024.day_1.solve_one(int(input_number)))

    # Now let's simulate a click on the button (using the low level JS API)
    # so we don't risk dom getting in the way
    just_a_button._dom_element.click()
    await call_flag.wait()

    output_container = document.querySelector("#output_number")
    assert output_container.innerHTML == "102", output_container.innerHTML
