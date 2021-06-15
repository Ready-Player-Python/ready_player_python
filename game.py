from browser import document, html, window
import random
from index import canvas
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
    <button class="flex justify-center space-y-20 mt-24 text-3xl">THIS WILL BE PLAY BUTTON?</button>
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


# Start Game Code
# ===================================================

score = 0
high_score = 0

px = py = 10
gs = tc = 20
applex = appley = 15
xv = yv = 0
trail = []
tail = 5

pre_pause = [0, 0]
paused = False


def game():
    global px, py, tc, gs, applex, appley, trail, tail, score
    px += xv
    py += yv
    if px < 0:
        px = tc - 1
    if px > tc - 1:
        px = 0
    if py < 0:
        py = tc - 1
    if py > tc - 1:
        py = 0

    ctx.fillStyle = "black"
    ctx.fillRect(0, 0, canvas.width, canvas.heigth)
    ctx.fillStyle = "lime"
    for i in range(len(trail)):
        ctx.fillRect(trail[i][0] * gs, trail[i][1] * gs, gs - 2, gs - 2)
        if trail[i][0] == px and trail[i][1] == py:
            score = score if paused else 0
            score = tail if paused else 5
    trail.insert(0, [px, py])
    while len(trail) > tail:
        trail.pop()

    if applex == px and appley == py:
        tail += 1
        applex = int(random.random() * tc)
        appley = int(random.random() * tc)
        score += 1
    update_score(score)
    ctx.fillStyle = "red"
    ctx.fillRect(applex * gs, appley * gs, gs - 2, gs - 2)


def update_score(new_score):
    global high_score
    document["score"].innerHTML = "Score: " + str(new_score)
    if new_score > high_score:
        document["high_score"].innerHTML = "High Score: " + str(new_score)
        high_score = new_score


def key_push(evt):
    global xv, yv, pre_pause, paused
    key = evt.keyCode
    if key == 37 and not paused:
        xv = -1
        yv = 0
    elif key == 38 and not paused:
        xv = 0
        yv = -1
    elif key == 39 and not paused:
        xv = 1
        yv = 0
    elif key == 40 and not paused:
        xv = 0
        yv = 1
    elif key == 32:
        temp = [xv, yv]
        xv = pre_pause[0]
        yv = pre_pause[1]
        pre_pause = [*temp]
        paused = not paused


def show_instructions(evt):
    window.alert("Use the arrow keys to move and press spacebar to pause the game.")


canvas = document["game-board"]
ctx = canvas.getContext("2d")
document.addEventListener("keydown", key_push)
game_loop = window.setInterval(game, 1000 / 10)
instructions_btn = document["instructions-btn"]
instructions_btn.addEventListener("click", show_instructions)
