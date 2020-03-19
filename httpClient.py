import kivy
kivy.require('1.0.5')

import sock
import time

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class WindowManager(ScreenManager):
    pass

class getHttp(Screen):
    host = ObjectProperty(None)
    port = ObjectProperty(None)
    files = ObjectProperty(None)

    def GET(self):

        try:
            if(self.host.text == ""):
                Info.header = "Host Invalido"
            elif(self.port.text == ""):
                Info.header = "Porta Invalido"
            else:
                Info.header = sock.getFile(self.host.text,self.port.text,self.files.text)
        except Exception as e:
           Info.header = "Ocorreu uma exceção:\nHost: "+self.host.text+"\nPorta: "+self.port.text + "\n\nErro: " + str(e)
    pass
        
class Info(Screen):
    header = ''
    response = ObjectProperty()
    
    def on_enter(self, *args):
        self.response.text = self.header

kv = Builder.load_file("mainWindow.kv")
sm = WindowManager()


sm.add_widget(getHttp())
sm.add_widget(Info())

sm.current = "request"        


class mainWindow(App):

    def build(self):
        return sm


if __name__ == '__main__':
    mainWindow().run()