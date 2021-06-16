from browser import window, document
import javascript

Vue = window.Vue

fighters = ["Mason","Hunter","Klace","Brian"]


def data(*args):
    return {
        'greeting': 'Choose a Fighter',
        'fighters': fighters
    }

def handle_click(event):
    print("clicked!")
    javascript.this().greeting = "change to this greeting"

def handle_click_show_fighter_mason(event):
    document['body-mason'].style.display = "block"
    document['body-hunter'].style.display = "none"
    document['body-brian'].style.display = "none"
    document['body-klace'].style.display = "none"

def handle_click_show_fighter_hunter(event):
    document['body-hunter'].style.display = "block"
    document['body-mason'].style.display = "none"
    document['body-brian'].style.display = "none"
    document['body-klace'].style.display = "none"

def handle_click_show_fighter_brian(event):
    document['body-brian'].style.display = "block"
    document['body-mason'].style.display = "none"
    document['body-hunter'].style.display = "none"
    document['body-klace'].style.display = "none"

def handle_click_show_fighter_klace(event):
    document['body-klace'].style.display = "block"
    document['body-mason'].style.display = "none"
    document['body-hunter'].style.display = "none"
    document['body-brian'].style.display = "none"

methods = {
    "handle_click": handle_click,
    "handle_click_show_fighter_mason": handle_click_show_fighter_mason,
    "handle_click_show_fighter_hunter": handle_click_show_fighter_hunter,
    "handle_click_show_fighter_brian": handle_click_show_fighter_brian,
    "handle_click_show_fighter_klace": handle_click_show_fighter_klace,
}

template = """
    <section class="flex">
        <div class="mt-2 w-2/4">
            <h2 class="text-4xl mb-2">{{ greeting }}</h2>
            <div id="panel"></div>
            <button id="type" @click="handle_click_show_fighter_mason" type="button" class="bg-gray-800 inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-white hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-800 focus:ring-white mr-5">{{ fighters[0] }}</button>

            <button @click="handle_click_show_fighter_hunter" type="button" class="bg-gray-800 inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-white hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-800 focus:ring-white mr-5">{{ fighters[1] }}</button>

            <button @click="handle_click_show_fighter_klace" type="button" class="bg-gray-800 inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-white hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-800 focus:ring-white mr-5">{{ fighters[2] }}</button>

            <button @click="handle_click_show_fighter_brian" type="button" class="bg-gray-800 inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-white hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-800 focus:ring-white mr-5">{{ fighters[3] }}</button>
        </div>
        <div class="mt-2 mb-2 w-2/4">
            <div id="hello">
                <div id="body-mason" style="display:none" class="css-typing">
                    <p id="mason-body">{{ fighters[0] }} Aviles</p>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                </div>
                <div id="body-brian" style="display:none" class="css-typing">
                    <h2>{{ fighters[3] }}</h2>
                    <p>body brian</p>
                </div>
                <div id="body-hunter" style="display:none" class="css-typing">
                    <h2>{{ fighters[1] }}</h2>
                    <p>body hunter</p>
                </div>
                <div id="body-klace" style="display:none" class="css-typing">
                    <h2>{{ fighters[2] }}</h2>
                    <p>body klace</p>
                </div>
            </div>
        </div>
    </section>
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
app.mount("#about")
