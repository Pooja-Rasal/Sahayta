from kivy.app import App 
from kivy.uix.label import Label 
# from kivy.core.window._window_sdl2 import _WindowSDL2Storage

class FirstKivy(App):
   def build(self):
       return Label(text="Hello world")
   
app = FirstKivy()
app.run()
       
