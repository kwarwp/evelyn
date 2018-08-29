# evelyn.ruzwana.main.py
from _spy.vitollino.main import Elemento, Cena, Texto, STYLE
from _spy.vitollino.main import INVENTARIO as inv
STYLE["width"]=1150 
STYLE["height"]="600px" 

TARZAN = "https://vignette.wikia.nocookie.net/vsbattles/images/6/68/Tarzan.png/revision/latest?cb=20170117061234"
CINDERELA = "https://4.bp.blogspot.com/-c_4RlOC4vRk/WD8fPzbqbcI/AAAAAAAACA0/1ian8CfRW9o-HTtSpVWOU2AG1TmmkUY3QCLcB/s1600/Cinderella-Transparent-PNG.png"
ALICE = "https://3.bp.blogspot.com/-o7Y78sYGkjY/V6O1G7WysSI/AAAAAAAAMO8/IG0Q7cJKKcYA70fLNINSaLG02t9fQT52QCLcB/s1600/ALICE%2B%25283%2529.png"

CASTELO = "https://i.pinimg.com/originals/01/3a/9d/013a9d6ffc6bb0ed57c897df0475f8f1.gif"
CASINHA = "http://www.meriti.rj.gov.br/iptu2018/img/casinha.png"
PANTANO = "https://vignette.wikia.nocookie.net/clubpenguin/images/6/6a/Pantano_Pegajoso.PNG/revision/latest?cb=20140517014109&path-prefix=es"

def criarcenas():
    castelo = Cena(img=CASTELO)
    casinha = Cena(img=CASINHA)
    pantano = Cena(img=PANTANO)
    castelo.direita = casinha
    casinha.direita = pantano
    casinha.esquerda = castelo
    pantano.esquerda = casinha
    
    tarzan = Elemento(img=TARZAN, tit="Tarzan", style=dict(left="400px", top= "325px", width= "300px", height="300px"))
    tarzan.entra(castelo)
    etarzan = Texto (castelo, "Eu sou o tarzan!")
    tarzan.vai = etarzan.vai
    
    cinderela = Elemento(img=CINDERELA, tit="Cinderela", style=dict(left="800px", top= "225px", width= "300px", height="400px"))
    cinderela.entra(casinha)
    ecinderela = Texto (casinha, "Bom dia!")
    cinderela.vai = ecinderela.vai
    
    alice = Elemento(img=ALICE, tit="Tarzan", style=dict(left="800px", top= "320px", width= "300px", height="300px"))
    alice.entra(pantano)
    ealice = Texto (pantano, "Eu sou o tarzan!")
    alice.vai = ealice.vai
    
    castelo.vai()
    
    
criarcenas()
    
    
