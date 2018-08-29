# evelyn.angie.main.py
from _spy.vitollino.main import Cena, Texto, Elemento
from _spy.vitollino.main import INVENTARIO as inv

ALICE = "http://images6.fanpop.com/image/photos/40400000/Alice-In-Wonderland-Png-rainbow-unicorn-40444811-307-500.png"
BARBIE = "https://images-na.ssl-images-amazon.com/images/I/91tfeZq8p6L._AC_UL320_SR222,320_.jpg"
FLORESTA = "http://4.bp.blogspot.com/-a8jf22vjtr8/TkPPLwQvpMI/AAAAAAAAAaY/W71RJTciQ00/s1600/floresta_fundo.jpg0"
CASTELO = "https://img.elo7.com.br/product/zoom/1E5C290/painel-de-festa-castelo-encantado-rosas-200x150-cm-khameo-decoracoes.jpg"
CENTRAL = "http://1.bp.blogspot.com/-rv7cx92E9fA/UbXRW7alqrI/AAAAAAAAAjY/uWd4UJfWIvw/s640/3.jpg"

def criarcenas():
    floresta = Cena(img=FLORESTA) 
    central = Cena(img=CENTRAL)
    floresta.direita = CENTRAL
    
    barbie = Elemento(img=barbie, tit="barbie", style=dict(left="100px", top="160px", width="60px", height="200 
    barbie.entra(floresta)
    ebarbie = Texto (floresta, "Que floresta assustadora minha gente")
    barbie.vai = ebarbie.vai
    
    castelo = Cena(img=CASTELO)
    central.direita = castelo
    
    Alice = Elemento(img=Alice, tit="BARBIE", style=dict(left="100px", top="160px", width="60px", height="200 
    alice.entra(castelo)
    ealice = Texto (castelo, "o que houve querida?")
    alice.vai = ealice.vai
    
    
    floresta.vai()
criarcenas()
    
    
