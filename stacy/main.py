# evelyn.stacy.main.py
from _spy.vitollino.main import Cena, Texto, Elemento
from _spy.vitollino.main import INVENTARIO as inv

ALICE ="http://vignette2.wikia.nocookie.net/disney/images/c/c8/Jane_clipart.png/revision/latest?cb=20140601220324"
TARZAN ="https://vignette.wikia.nocookie.net/p__/images/e/e2/Tarzan_Character.png/revision/latest?cb=20160309034227&path-prefix=protagonist"
FLORESTA ="https://4.bp.blogspot.com/-DUzzlN6dknE/Vi5_j9WAaFI/AAAAAAABPtA/5rgbiLpv2ac/s1600/mariavento1.png"
CASTELO ="http://www.fazarte.com.br/components/com_virtuemart/shop_image/product/Unic__rnio_4f48d8b8b7b1c.png"
ECASTELO ="http://www.fazarte.com.br/components/com_virtuemart/shop_image/product/Unic__rnio_4f48d8b8b7b1c.png"
ACASTELO ="http://www.fazarte.com.br/components/com_virtuemart/shop_image/product/Unic__rnio_4f48d8b8b7b1c.png"
BCASTELO ="http://www.fazarte.com.br/components/com_virtuemart/shop_image/product/Unic__rnio_4f48d8b8b7b1c.png"
PIANO ="https://illustorium.com/files/piano-music-notes.png"
BEIJO ="http://bp3.blogger.com/_A_cZ-NdBNt4/R4w0usTv5KI/AAAAAAAAAbI/tVUER5kJIO4/s1600/disney-clipart-tarzan18.gif"
FIM = "http://3.bp.blogspot.com/-zA1VKzme-9g/UZU6AxIeWQI/AAAAAAAAM_8/t7hzuQQkVhs/s1600/cora%C3%A7%C3%A3o+subindo.gif"

def criarcenas():
    floresta = Cena(img=FLORESTA)
    castelo = Cena(img=CASTELO)
    ecastelo = Cena(img=ECASTELO)
    acastelo = Cena(img=ACASTELO)
    bcastelo = Cena(img=BCASTELO)
    fim = Cena(img=FIM)    
    floresta.direita = castelo
    castelo.direita = ecastelo
    ecastelo.direita = acastelo
    acastelo.direita = bcastelo
    bcastelo.direita = fim
    
    alice = Elemento(img=ALICE, tit="Alice", style=dict(left="100px",top="160",width="60px",heigth="200px"))
    alice.entra(floresta)
    ealice = Texto(floresta, "Alice passeava pela floresta e, de repente,deparou-se com um lindo castelo.")
    alice.vai = ealice.vai
    
    alice = Elemento(img=ALICE, tit="Alice", style=dict(left="100px",top="160",width="60px",heigth="200px"))
    alice.entra(castelo)
    ealice = Texto(castelo, "Oh, que lindo! Quem será que mora aqui?")
    alice.vai = ealice.vai    
    
    piano = Elemento(img=PIANO, tit="Alice", style=dict(left="100px",top="160",width="190px",heigth="200px"))
    piano.entra(ecastelo)
    epiano = Texto(ecastelo, "O piano é mágico e toca uma linda valsa!")
    piano.vai = epiano.vai
    
    tarzan = Elemento(img=TARZAN, tit="Tarzan", style=dict(left="100px",top="160",width="60px",heigth="200px"))
    tarzan.entra(acastelo)
    etarzan = Texto(acastelo, "Surge um lindo príncipe que tira Alice para dançar...")
    tarzan.vai = etarzan.vai
    
    beijo = Elemento(img=BEIJO, tit="Beijo", style=dict(left="100px",top="160",width="190px",heigth="280px"))
    beijo.entra(bcastelo)
    ebeijo = Texto(bcastelo, "Os dois se apaixonam e...")
    beijo.vai = ebeijo.vai
    
    
    
    floresta.vai()
criarcenas()