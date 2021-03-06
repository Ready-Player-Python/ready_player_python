from browser import document, html, window
import random


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

ctx = None
canvas = None
game_loop = None


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
    ctx.fillRect(0, 0, canvas.width, canvas.height)
    ctx.fillStyle = "lime"
    for i in range(len(trail)):
        ctx.fillRect(trail[i][0] * gs, trail[i][1] * gs, gs - 2, gs - 2)
        if trail[i][0] == px and trail[i][1] == py:
            score = score if paused else 0
            tail = tail if paused else 5
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
        document["high-score"].innerHTML = "High Score: " + str(new_score)
        high_score = new_score


def key_push(evt):
    global xv, yv, pre_pause, paused
    key = evt.keyCode
    if key == 32 or key == 80:
        temp = [xv, yv]
        xv = pre_pause[0]
        yv = pre_pause[1]
        pre_pause = [*temp]
        paused = not paused
    elif key == 37 and paused == False or key == 65 and paused == False:
        xv = -1
        yv = 0
    elif key == 38 and paused == False or key == 87 and paused == False:
        xv = 0
        yv = -1
    elif key == 39 and paused == False or key == 68 and paused == False:
        xv = 1
        yv = 0
    elif key == 40 and paused == False or key == 83 and paused == False:
        xv = 0
        yv = 1
    else:
        pass


def show_instructions(evt):
    window.alert(
        "Use the arrow keys or a, w, s, d to move and press spacebar to pause the game."
    )


def display_game(refresh_rate):
    global canvas, ctx, game_loop
    instructions_btn = document["instructions-btn"]
    canvas = document["game-board"]
    ctx = canvas.getContext("2d")
    if game_loop:
        window.clearInterval(game_loop)
    else:
        document.addEventListener("keydown", key_push)
        instructions_btn.addEventListener("click", show_instructions)
    game_loop = window.setInterval(game, refresh_rate)


# def display_gamex():
#     global canvas, ctx
#     canvas = document["game-board"]
#     ctx = canvas.getContext("2d")
#     document.addEventListener("keydown", key_push)
#     game_loop = window.setInterval(game, 1000 / 10)
#     instructions_btn = document["instructions-btn"]
#     instructions_btn.addEventListener("click", show_instructions)
