# evelyn.anastasia.main.py
from _spy.vitollino.main import Elemento, Cena, Texto

bgCena1 = "https://i1.wp.com/salmeninsurance.com/home/wp-content/uploads/2016/03/bg-grunge-1.jpg"
jimmyTex = "https://static1.squarespace.com/static/524750a6e4b0781833bea2e7/t/533c8507e4b02cbd82ce74ff/1396475144671/"
penseTex = "http://www.pngall.com/wp-content/uploads/2016/09/Thought-Bubble.png"

def Jogo():
    cena1 = Cena(img = bgCena1)
    jimmy = Elemento(img = jimmyTex, 
        style = dict(height = "150px", width = "300px", left = "0px", top = "150px"))
    jimmy.entra(cena1)
    jimmyPense1 = Elemento(img = penseTex, 
        style = dict(height = "110px", width = "100px", left = "20px", top = "50px"))
    jimmyPense1.entra(cena1)
    jimmyPense2 = Elemento(img = penseTex, 
        style = dict(height = "110px", width = "100px", left = "180px", top = "50px", transform = "scaleX(-1)"))
    jimmyPense2.entra(cena1)
    cena1.vai()
    
    s = jimmyPense1.img.style
    
    while (True):
        
    
    
Jogo()

