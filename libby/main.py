# evelyn.libby.main.py
from _spy.vitollino.main import Cena, Texto, Elemento, STYLE
from _spy.vitollino.main import INVENTARIO as inv
STYLE["width"]=400

TARZAN = "https://img00.deviantart.net/4962/i/2017/235/5/2/disney_poster___tarzan_by_shade_silverwing-dbl0y6s.png"
CASA = "https://3.bp.blogspot.com/-kycDY3DU1uM/V97QiIwu7BI/AAAAAAAABkE/76x3WukbcpsinxLa7Lrd-vkW5Xxrw8LVgCLcB/s1600/Casa.png"
CASAPORDENTRO = "https://thumbs.dreamstime.com/b/desenhos-animados-da-sala-34028210.jpg"
PESQUISADORES = "https://thumbs.dreamstime.com/z/grupo-dos-desenhos-animados-dos-car%C3%A1teres-dos-cientistas-42704789.jpg"
BARBIE = "http://2.bp.blogspot.com/_bxIEyRir30g/SdgNUixRJmI/AAAAAAAAAYU/bFu6rtPwx0g/s1600-h/tarzan-84-1.png"
FLORESTA = "https://4.bp.blogspot.com/-DUzzlN6dknE/Vi5_j9WAaFI/AAAAAAABPtA/5rgbiLpv2ac/s1600/mariavento1.png"

def criarcenas():
    casa = Cena(img=CASA)
    casapordentro = Cena(img = CASAPORDENTRO)
    casa.direita = casapordentro
    
    tarzan = Elemento(img=TARZAN, tit="Tarzan", style=dict(left="100px", top="100px", width="130px", height="220px"))
    tarzan.entra(casapordentro)
    etarzan = Texto (casapordentro, "Onde estou? Essa não é minha casa!")
    tarzan.vai = etarzan.vai
    
    
    
    casa.vai()
    
criarcenas()