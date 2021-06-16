from browser import document, html, window
import random
import javascript
from snake_logic import display_game



Vue = window.Vue

def data(*args):
    return {
        'greeting': 'Ready Player Python'
    }

def handle_click(event):
    print("clicked!")
    javascript.this().greeting = "change to this greeting"

def show_names(event):
    pass

def start_game(event):
    display_game()

methods = {
    "handle_click": handle_click,
    "show_names": show_names,
    "start_game": start_game
}

template = """
   <button @click="start_game">TEST</button>
"""


# Put it all together
app = Vue.createApp(
    {
        "template": template,
        "data": data,
        "methods": methods
    }
)

# Mount it to #app
app.mount("#app")

