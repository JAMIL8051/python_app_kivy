from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class SayHello(App):
    def build(self):
        
        #returns a window object with all it's widgets
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

        # image widget
        self.window.add_widget(Image(source="background_image.jpg"))

        # label widget
        self.greeting = Label(
                        text= "What is your name?",
                        font_size= 28,
                        color= '#00FFCE'
                        )
        self.window.add_widget(self.greeting)

        # text input widget
        self.user = TextInput(
                    multiline= False,
                    padding_y= (20,20),
                    size_hint= (1, 0.5)
                    )

        self.window.add_widget(self.user)

        # button widget
        self.button = Button(
                      text= "GREET",
                      size_hint= (1,0.5),
                      bold= True,
                      background_color ='#00FFCE',
                      #remove darker overlay of background colour
                      # background_normal = ""
                      )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)
        self.close_button = Button(
                        text = "Close",
                        size_hint=(1, 0.5),
                        bold= True,
                        background_color = '#00FFCE'                        
        )
        self.close_button.bind(on_press=self.close_window)
        self.window.add_widget(self.close_button)
        
        return self.window

    def callback(self, instance):
        # change label text to "Hello + user name!"
        if self.user.text:
            self.greeting.text = "Hello" + self.user.text + "! and wishing you happy holidays!!"
        else:
            self.greeting.text = "Please enter a valid username or anything!!!!"
            
    def close_window():
        SayHello().stop()
        
        
if __name__ =='__main__':
    SayHello().run()