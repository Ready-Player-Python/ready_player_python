from browser import window
import javascript
# TEST

Vue = window.Vue

def data(*args):
    return {
        'greeting': 'Ready Player Python',
        'color': '#50b333',
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
<body class="backdrop-opacity-1=20 bg-gradient-to-r from-yellow-300 via-red-400 to-pink-400">

    <header class="bg-gradient-to-r from-yellow-300 via-red-400 to-pink-400">logo?</header>

    <h2 class="flex justify-center text-4xl m-8 ">{{ greeting }}</h2>

    <body>
        <div class="flex justify-center space-x-36 mx-8 text-2xl">

            <a href="https://www.google.com">Home</a>

            <a href="https://www.google.com">About the Developers</a>
        </div>
    </body>

    <div class="flex justify-center space-y-20 mt-24 text-3xl">THIS WILL BE PLAY BUTTON?</div>

    <div class="flex justify-center border-2 border-black mx-64 mt-24 mb-36 p-36">GAME SPACE</div>

   <footer>BYE</footer>



</body>
 
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

