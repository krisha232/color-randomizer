from tkinter import *
import random
root=Tk()
root.title("Color Randomizer")
root.configure(bg="gold")
root.geometry("600x600")

color=Label(root,font=("Bahnschrift light",32),bg="gold")
color.place(relx=0.5,rely=0.3, anchor=CENTER)

score1=Label(root,text="Score: 0 ",font=("Bahnschrift light",12),bg="gold")
score1.place(relx=0.2,rely=0.1,anchor=E)

input_value=Entry(root)
input_value.place(relx=0.6,rely=0.5,anchor=E)
class game:
    def __init__(self):
        self.__score=0
    
    def __updateScore(self,input_value):
        if(input_value==self.color_list[self.random_color]):
            print(self.color_list[self.random_color])
            self.__score=self.__score+random.randint(0,10)
            score1["text"]="Score : "+str(self.__score)
    def get_user_value(self,input_value):
        self.__updateScore(input_value)
        
        
    def updateGame(self):
        self.list=["red","orange","green","blue","black","yellow","purple"]
        self.random_no=random.randint(0,6)
        self.color_list=["red","orange","green","blue","black","yellow","purple"]
        self.random_color=random.randint(0,6)
        color['text']=self.list[self.random_no]
        color['fg']=self.color_list[self.random_color]        
        

obj1=game()
def get_input():
    value=input_value.get()
    obj1.get_user_value(value)
    obj1.updateGame()
    input_value.delete(0,END)

btn=Button(root,text="START",bg="red3",fg="white",padx=10,pady=1,font=("Arial",
                                                                       15)
           ,relief=FLAT,command=obj1.updateGame)
btn.place(relx=0.75,rely=0.7,anchor=CENTER)

btn=Button(root,text="CHECK",bg="red3",fg="white",padx=10,pady=1,font=("Arial",
                                                                       15)
           ,relief=FLAT,command=get_input)
btn.place(relx=0.35,rely=0.7,anchor=CENTER)

root.mainloop()