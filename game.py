from browser import window

Vue = window.Vue

def data(*args):
    return 


app = Vue.createApp(
    {
        "template": """
            <h2>Ready Player Python</h2>
            <div class="flex flex-col gap-8 w-1/2 mx-auto py-8">
                <button>YO</button>

            </div>
        """,
    }
)

vm = app.mount("#app")

