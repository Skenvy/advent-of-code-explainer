from base import upytest

from pyscript import document, web, when

from scripts.example.example import do_a_thing

async def test_example():
    input_container = document.querySelector("#input_number")
    input_container.value = "101"

    just_a_button = web.page.find("#do_a_thing_button")[0]

    @when("click", just_a_button)
    def on_click(event):
        do_a_thing(event)

    just_a_button._dom_element.click()
    output_container = document.querySelector("#output_number")
    assert output_container.innerHTML == "102", output_container.innerHTML
