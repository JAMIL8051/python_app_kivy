from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self):
        # Returns a window object with all its widgets
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # Load Bengali font
        self.bengali_font = "NotoSansBengali-VariableFont_wdth,wght.ttf"  # Replace with the path to your Bengali font

        # Image widget
        self.window.add_widget(Image(source="background_image.jpg"))

        # Label widget with Bengali font
        self.greeting = Label(
            text="আপনার নাম কি?",
            font_name=self.bengali_font,
            font_size=28,
            color='#00FFCE'
        )
        self.window.add_widget(self.greeting)

        # Text input widget
        self.user = TextInput(
            multiline=False,
            padding_y=(20, 20),
            size_hint=(1, 0.5)
        )

        self.window.add_widget(self.user)

        # Button widget
        self.button = Button(
            text="শুভেচ্ছা",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFCE',
        )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        # Close button widget
        self.close_button = Button(
            text="বন্ধ করুন",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFCE'
        )
        self.close_button.bind(on_press=self.close_window)
        self.window.add_widget(self.close_button)

        return self.window

    def callback(self, instance):
        # Change label text to "Hello + user name!"
        if self.user.text:
            self.greeting.text = "হ্যালো " + self.user.text + "! এবং আপনাকে শুভ অবধি জানাই!!"
        else:
            self.greeting.text = "দয়া করে একটি বৈধ ব্যবহারকারীর নাম অন্তর্ভুক্ত করুন!!!"

    def close_window(self, instance):
        self.stop()

if __name__ == '__main__':
    SayHello().run()
