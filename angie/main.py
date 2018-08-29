# evelyn.angie.main.py
from _spy.vitollino.main import Cena, Texto, Elemento, STYLE
from _spy.vitollino.main import INVENTARIO as inv 
STYLE["width"]=800
STYLE ["height"]="600px"

BARBIE = "https://gallery.yopriceville.com/var/albums/Free-Clipart-Pictures/Cartoons-PNG/Barbie_PNG_Picture.png?m=1439866501"
FLORESTA = "https://www.blogodorium.com.br/wp-content/uploads/sonhar-com-floresta.jpg"
TARZAN = "https://vignette.wikia.nocookie.net/vsdebating/images/6/68/Tarzan.png/revision/latest?cb=20170707201517"
HOMEM_ARANHA = "https://vignette.wikia.nocookie.net/marvel/images/2/2e/Homem-aranha.png/revision/latest?cb=20141112195415&path-prefix=pt-br"
CINDERELA = "https://1.bp.blogspot.com/-V2tLZSbQiXk/WD8fBBsCwDI/AAAAAAAACAo/ik35d327hAAa6YfTwuN-tD2RozNXOgzpwCLcB/s1600/23.png"
CENTRAL_PARK = "http://visitarnovayork.com/wp-content/uploads/outono-em-Nova-York2.jpg"
ALICE = "https://i.pinimg.com/originals/73/3f/b0/733fb05bb25885546cec40e27e52bcea.jpg"
CASTELO = "https://img.elo7.com.br/product/original/1E64427/painel-sublimado-castelo-encantado-2-95x4-0-castelo-encantado.jpg"

def criarcenas():
    floresta = Cena(img=FLORESTA)
    central_park = Cena(img=CENTRAL_PARK)
    floresta.direita = central_park
    
    barbie = Elemento(img=BARBIE, tit="Barbie", style=dict(left="150px", top="300px", width="90px", height="300px"))
    barbie.entra(floresta) 
    ebarbie = Texto(floresta, "Que horror, essa floresta se mexendo e zumbindo!")
    barbie.vai = ebarbie.vai
    tarzan = Elemento(img=TARZAN, tit="Tarzan", style= dict(left="430px", top="50px", width="250px", height="300px"))
    tarzan.entra(floresta)
    ebarbie = Texto(floresta, "Socorro, você pode me ajudar? Estou com medo")
    
    floresta.vai()
    
    central_park = Cena(img=CENTRAL_PARK)
    
    homem_aranha = Elemento(img=HOMEM_ARANHA, tit="Homem-Aranha", style=dict(left="100px", top="200px", width="60px", height="200px"))
    homem_aranha.entra(central_park)
    cinderela = Elemento(img=CINDERELA, tit="Cinderela", style=dict(left="150px", top="160px", width="60px"))
    cinderela.entra(central_park)
    ehomem_aranha = Texto(central_park, "Ei, Cinderela, você ouviu este grito de socorro? Sabe o que está acontecendo?")
    ecinderela = Texto(central_park, "SIM, me ajude! É minha amiga Barbie, ela está perdida na parte assombrada.")

criarcenas()
    
    
    