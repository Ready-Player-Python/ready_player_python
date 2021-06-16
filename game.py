from browser import document, html, window
import random
import javascript
from snake_logic import display_game


Vue = window.Vue


def data(*args):
    return {"greeting": "Ready Player Python"}


def handle_click(event):
    print("clicked!")
    javascript.this().greeting = "change to this greeting"


def show_names(event):
    pass


def start_game_slow(event):
    display_game(1000 / 10)


def start_game_fast(event):
    display_game(500 / 10)


methods = {
    "handle_click": handle_click,
    "show_names": show_names,
    "start_game_slow": start_game_slow,
    "start_game_fast": start_game_fast,
}

template = """
    <button @click="start_game_slow">Slow Game</button>
    <button @click="start_game_fast">Fast Game</button>
"""


# Put it all together
app = Vue.createApp({"template": template, "data": data, "methods": methods})

# Mount it to #app
app.mount("#app")
