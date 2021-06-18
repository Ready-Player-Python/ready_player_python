from browser import document, html, window
import random
import javascript
from snake_logic import display_game


Vue = window.Vue


def data(*args):
    return {"greeting": "Ready Player Python"}


def handle_display_click(event):
    print("clicked!")
    if document['help-box'].style.display == "block":
        document['help-box'].style.display = "none"
    else:
        document['help-box'].style.display = "block"


def show_names(event):
    pass


def start_game_slow(event):
    display_game(1000 / 10)


def start_game_fast(event):
    display_game(500 / 10)


methods = {
    "handle_display_click": handle_display_click,
    "show_names": show_names,
    "start_game_slow": start_game_slow,
    "start_game_fast": start_game_fast,
}

template = """
    <button @click="start_game_slow" class="text-center block bg-blue-500 hover:bg-blue-400 text-white font-bold py-3 px-6 border-b-4 border-blue-700 hover:border-blue-500 rounded ring-transparent">Slow Game</button>
    <button @click="start_game_fast" class="text-center block bg-blue-500 hover:bg-blue-400 text-white font-bold py-3 px-6 border-b-4 border-blue-700 hover:border-blue-500 rounded ring-transparent">Fast Game</button>
    <div class="relative">
        <button @click="handle_display_click" id="instructions-btn" class="btn btn-info text-center block bg-blue-500 hover:bg-blue-400 text-white font-bold py-2 px-4 border-b-4 border-blue-700 hover:border-blue-500 rounded-3xl ring-offset-transparent	border-transparent">?</button>
        <div id="help-box" style="display:none" class="absolute w-72 bg-black text-white p-2 -right-20 top-20">
            <p>Instructions:</p>
            <p>Use W, A, S, D to move or Arrow keys</p>
            <p>Press spacebar to pause</p>
        </div>
    </div>
"""


# Put it all together
app = Vue.createApp({"template": template, "data": data, "methods": methods})

# Mount it to #app
app.mount("#app")
