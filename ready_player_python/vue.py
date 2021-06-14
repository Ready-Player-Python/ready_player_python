
from browser import document, window

from javascript import this

Date = window.Date.new

Vue = window.Vue

app = Vue.new({
  'el': '#app',
  'data': {
    'message': 'Hello Brython Vue!'
  }
})

app2 = Vue.new({
  'el': '#app-2',
  'data': {
    'message': 'You loaded this page on ' + Date().toLocaleString()
  }
})

app4 = Vue.new({
  'el': '#app-4',
  'data': {
    'todos': [
      { 'text': 'Learn JavaScript' },
      { 'text': 'Learn Vue' },
      { 'text': 'Build something awesome' }
    ]
  }
})

def reverse_message(ev):
    this().message = ''.join(reversed(this().message))

app5 = Vue.new({
  'el': '#app-5',
  'data': {
    'message': 'Hello Vue.js!'
  },
  'methods': {
    'reverseMessage': reverse_message
  }
})

app6 = Vue.new({
  'el': '#app-6',
  'data': {
    'message': 'Hello Vue!'
  }
})

Vue.component('todo-item', {
  'props': ['todo'],
  'template': '<li>{{ todo.text }}</li>'
})

app7 = Vue.new({
  'el': '#app-7',
  'data': {
    'groceryList': [
      { 'id': 0, 'text': 'Vegetables' },
      { 'id': 1, 'text': 'Cheese' },
      { 'id': 2, 'text': 'Whatever else humans are supposed to eat' }
    ]
  }
})

def created():
    this().todos.push({"id":1, "text": "ADDED"})

Vue.new({
    "created": created,
    "el": "#pyapp1",
    "data": {
        "todos": [{"id":0, "text": "TODO"}],
    }
})

_id = 1
def add_item(*args):
    global _id
    _id += 1
    this().todos.push({"id": _id, "text": "ADDED"})

Vue.new({
    "methods": {
        "add_item": add_item
    },
    "el": "#pyapp2",
    "data": {
        "todos": [{"id":0, "text": "TODO"}],
    }
})

# issue 1185

class DictMore(dict):
    def __init__(self):
        self['count'] = 0

def produce_dict(*_):
    item = dict()
    item['count'] = 0
    return item

def produce_dict_more(*_):
    return DictMore()

Vue.component('button-counter', {
  'data': produce_dict,
  'template': '<button v-on:click="count++">You clicked me {{ count }} times.</button>',
})

Vue.component('button-counter-more', {
  'data': produce_dict_more,
  'template': '<button v-on:click="count++">You clicked me {{ count }} times.</button>',
})

Vue.new({"el": '#components-demo' })