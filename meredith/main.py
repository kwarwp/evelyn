# evelyn.meredith.main.py
from _spy.vitollino.main import Elemento, Cena, Texto
from _spy.vitollino.main import INVENTARIO as inv

BARBIE = "https://i.pinimg.com/originals/9d/85/6c/9d856c0168614e8d429ba0c6bb01d0f6.png"
ALICE = "https://3.bp.blogspot.com/-o7Y78sYGkjY/V6O1G7WysSI/AAAAAAAAMO8/IG0Q7cJKKcYA70fLNINSaLG02t9fQT52QCLcB/s1600/ALICE%2B%25283%2529.png"

FLORESTA = "https://3.bp.blogspot.com/-w42aVYJVVps/TicGHsUvjrI/AAAAAAAACxQ/KlDH3JScanE/s1600/pequeno-caminho-na-floresta-imagens-imagem-de-fundo-wallpaper-para-pc-computador-tela-gratis-ambiente-de-trabalho.jpg"
CASTELO = "https://img3.stockfresh.com/files/d/ddraw/m/85/4928415_stock-vector-mythological-landscape-with-medieval-castle.jpg"

def criarcenas():
    floresta = Cena(img=FLORESTA)
    castelo = Cena(img=CASTELO)
    floresta.direita = castelo
    
    alice = Elemento(img=ALICE, tit="Alice", style=dict(left="120px", top="110px", width="70px", height="190px")) 
    alice.entra(floresta)
    ealice = Texto (floresta, "Que floresta linda!")
    alice.vai = ealice.vai

    barbie = Elemento(img=BARBIE, tit="Barbie", style=dict(left="190px", top="50px", width="70px", height="160px"))
    barbie.entra(castelo)
    ebarbie= Texto (castelo, "Onde está o Ken?")
    barbie.vai = ebarbie.vai
    
    floresta.vai()
    
criarcenas()