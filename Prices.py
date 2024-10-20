from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.image import Image

class CalculatorLayout(BoxLayout):
    Window.size = (340,600)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10
 

        Window.clearcolor = (0.10,0.250,0.180,1) 
        


        self.text_label =Label(text='WHICH IS THE BEST PRICE?',font_size='24sp', padding=10, color=(1,1,1,1))
        self.text_labelP1 =Label(text='1ST PRODUCT',font_size='24sp',color=(0,110,0,1) )
        self.text_labelP2 =Label(text='2ND PRODUCT',font_size='24sp',color=(0,110,0,1))


       
        self.input_field = TextInput(
            multiline=False,
            font_size=30,
            size_hint_y=None,
            height=50,
            hint_text='Product Price'
        )
        self.input_field2 = TextInput(
            multiline=False, 
            font_size=30, 
            size_hint_y=None, 
            height=50, 
            hint_text='Product QTY'
            )
        
        self.img = Image(source='Castor.png',size_hint=(None,None), size=(400, 400))

        self.img_money = Image(source='money.png')
        self.img_scale = Image(source='scale.png')
        self.img_money2 = Image(source='money.png')
        self.img_scale2 = Image(source='scale.png')

        self.input_field3 = TextInput(
            multiline=False,
            font_size=30,
            size_hint_y=None,
            height=50,
            hint_text='Product Price'
        )
          
        self.input_field4 = TextInput(
            multiline=False,
            font_size=30,
            size_hint_y=None,
            height=50,
            hint_text='Product Qty'
        )
        
       
        self.calc_button = Button(
            text='Calculate',
            size_hint_y=None,
            height=50,
            background_color=(0.90,0,0,1)  
        )
        self.calc_button.bind(on_press=self.calculate)
        
       
        self.result_label = Label(
            text='',
            font_size=55,
            color=(1,1,1,1), 
            padding=30
        

        )

        self.result_calc = Label(
            text='',
            font_size=30,
            color= (10, 1, 1, 1)
        )
        self.result_calc2 = Label(
            text='',
            font_size=30, 
            color= (10, 1, 1, 1)
        )
       
        self.add_widget(self.text_label)
        self.add_widget(self.text_labelP1)
        self.add_widget(self.img_money)
        self.add_widget(self.img_scale)
        self.add_widget(self.input_field)
        self.add_widget(self.input_field2)
        self.add_widget(self.text_labelP2)
        self.add_widget(self.img_money2)
        self.add_widget(self.img_scale2)
        self.add_widget(self.input_field3)
        self.add_widget(self.input_field4)
        self.add_widget(self.calc_button)
        self.add_widget(self.result_label)
        self.add_widget(self.img)
        self.add_widget(self.result_calc)
        self.add_widget(self.result_calc2)
    
    def calculate(self, instance):
        try:
           
            value = int(self.input_field.text)/ int(self.input_field2.text)
            value2 = int(self.input_field3.text)/ int(self.input_field4.text)
            if value < value2:
                self.result_label.text = ('1st product is the winner')
                self.result_calc.text =(f'Product 1: {value}')
                self.result_calc2.text =(f'Product 2 : {value2}')
            else:
                self.result_label.text = '2nd product is the winner'
                self.result_calc.text =(f'Product 1: {value}')
                self.result_calc2.text =(f'Product 2 : {value2}')
        except ValueError:
            self.result_label.text = 'Please enter a valid value'

class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()


CalculatorApp().run()