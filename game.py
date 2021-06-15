from browser import window, document
import javascript

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

methods = {
    "handle_click": handle_click,
    "show_names": show_names
}

template = """
    <h2 class="text-4xl">{{ greeting }}</h2>
    <div>
        <button @click="handle_click" type="button" class="bg-gray-800 inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-white hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-800 focus:ring-white">YO</button>
    </div>
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

