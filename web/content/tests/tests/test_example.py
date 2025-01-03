import asyncio
from base import upytest

from pyscript import document, web, when

async def test_example():
    input_container = web.page.find("#input_number")[0]
    input_container.innerHTML = "11"

    just_a_button = web.page.find("#do_a_thing_button")[0]
    call_flag = asyncio.Event()

    @when("click", just_a_button)
    def on_click(event):
        call_flag.set()

    # Now let's simulate a click on the button (using the low level JS API)
    # so we don't risk dom getting in the way
    just_a_button._dom_element.click()
    await call_flag.wait()

    output_container = web.page.find("#output_number")[0]
    assert output_container.innerHTML == "12", output_container.innerHTML
