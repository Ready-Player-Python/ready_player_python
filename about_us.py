from browser import window, document
import javascript

Vue = window.Vue

fighters = ["Mason","Hunter","Klace","Brian"]
page_title = "Ready Player Python"
cta_button = "See It On Github"


def data(*args):
    return {
        'greeting': 'Choose a Fighter',
        'fighters': fighters,
        'page_title': page_title,
        'cta_button': cta_button
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
    <nav id="header" class="w-full z-30 top-0 text-white bg-black">
        <div class="w-full container mx-auto flex flex-wrap items-center justify-between mt-0 py-2">
            <div class="pl-4 flex items-center">
                <a class="toggleColour text-white no-underline hover:no-underline font-bold text-2xl lg:text-4xl" href="index.html">
                    {{ page_title }}
                </a>
            </div>
            <div class="block lg:hidden pr-4">
                <button id="nav-toggle" class="flex items-center p-1 text-pink-800 hover:text-gray-900 focus:outline-none focus:shadow-outline transform transition hover:scale-105 duration-300 ease-in-out">
                    <svg class="fill-current h-6 w-6" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                    <title>Menu</title>
                    <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z" />
                    </svg>
                </button>
            </div>
            <div class="w-full flex-grow lg:flex lg:items-center lg:w-auto hidden mt-2 lg:mt-0 bg-white lg:bg-transparent text-black p-4 lg:p-0 z-20" id="nav-content">
                <ul class="list-reset lg:flex justify-end flex-1 items-center">
                    <li class="mr-3">
                        <a class="inline-block py-2 px-4 text-white font-bold no-underline" href="about_us.html">About Us</a>
                    </li>
                </ul>
                <a
                    id="navAction"
                    class="mx-auto lg:mx-0 hover:underline bg-white text-gray-800 font-bold rounded-full mt-4 lg:mt-0 py-4 px-8 shadow opacity-75 focus:outline-none focus:shadow-outline transform transition hover:scale-105 duration-300 ease-in-out"
                    href="https://github.com/Ready-Player-Python/ready_player_python"
                    target="_blank"
                >
                    {{ cta_button }}
                </a>
            </div>
        </div>
        <hr class="border-b border-gray-100 opacity-25 my-0 py-0" />
    </nav>

    <!-- Container -->
    <div class="pt-24 pb-24 backdrop-opacity-1=20 bg-gradient-to-r from-yellow-300 via-red-400 to-pink-400">
        <div class="container px-3 mx-auto flex flex-wrap flex-col md:flex-row items-center justify-center">
            <!-- Terminal Board -->
            <div class="bg-gray-600 flex flex-col w-full md:w-5/6 items-start text-center md:text-left h-80 p-5">
                <div class="w-full">

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
                                <div id="body-mason" style="display:none">
                                    <div class="css-typing">
                                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate ve</p>
                                        <div class="hiders">
                                            <p>&nbsp;</p>
                                            <p>&nbsp;</p>
                                            <p>&nbsp;</p>
                                            <p>&nbsp;</p>
                                            <p>&nbsp;</p>
                                            <p>&nbsp;</p>
                                            <p>&nbsp;</p>
                                            <p>&nbsp;</p>
                                        </div>
                                    </div>
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
                </div>
            </div>
        </div>
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
app.mount("#about")
