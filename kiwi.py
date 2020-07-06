import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import random



class mygrid(GridLayout):
    def __init__(self,**kwargs):
        super(mygrid,self).__init__(**kwargs)
        self.cols=1

        self.new=GridLayout()
        self.new.cols = 2

        self.add_widget(Label(text="КАМЪК НОЖИЦА ХАРТИЯ"))

        self.new.add_widget(Label(text="НАПИШИ КАМЪК,НОЖИЦА ИЛИ ХАРТИЯ:"))
        self.name = TextInput(multiline=False)
        self.new.add_widget(self.name)

        self.new.add_widget(Label(text="ТВОИТЕ ТОЧКИ:"))
        self.lastname = TextInput(multiline=False)
        self.new.add_widget(self.lastname)

        self.new.add_widget(Label(text="ТОЧКИТЕ НА КОМПЮТЪРА:"))
        self.email = TextInput(multiline=False)
        self.new.add_widget(self.email)
        self.add_widget(self.new)

        self.submit=Button(text="ДАВАЙ",font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)



    def pressed(self, instance):
        rps=["камък","ножица","хартия"]
        pc_choice = random.choice(rps)
        p_choice = self.name.text
        self.p_points= 0
        self.pc_points=0




        if p_choice == "камък":
            if pc_choice == "ножица":
                self.name.text="победи ножица"
                self.p_points+=1
                self.lastname.text=str(self.p_points)
            if pc_choice == "хартия":
                self.name.text="загуби от хартия"
                self.pc_points+=1
                self.email.text = str(self.pc_points)
            if pc_choice == "камък": self.name.text="равенство"
        elif p_choice == "ножица":
            if pc_choice == "хартия":
             self.name.text="победи хартия"
             self.p_points += 1
             self.lastname.text = str(self.p_points)
            if pc_choice == "камък":
             self.name.text="загуби от камък"
             self.pc_points += 1
             self.lastname.text = str(self.pc_points)
            if pc_choice == "ножица": self.name.text="равенство"
        elif p_choice == "хартия":
            if pc_choice == "камък":
             self.name.text="победи камък"
             self.p_points += 1
             self.lastname.text = str(self.p_points)
            if pc_choice == "ножица":
             self.name.text="загуби от ножица"
             self.pc_points += 1
             self.email.text = str(self.pc_points)
            if pc_choice == "хария": self.name.text="равенство"
        else: self.name.text="можеш да избираш само между камък ножица или хария"



class myapp(App):
    def build(self):
        return mygrid()


if __name__=="__main__":
    myapp().run()