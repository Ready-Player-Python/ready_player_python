from browser import document, window
from javascript import this

app = Vue.new({
  'el': '#app',
  'data': {
    'message': 'Hello Vue!'
  }
})

# var app = new Vue({
#   el: '#app',
#   data: {
#     message: 'Hello Vue!'
#   }
# })