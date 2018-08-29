# evelyn.angie.main.py
from _spy.vitollino.main import Cena, Texto, Elemento
from _spy.vitollino.main import INVENTARIO as inv

BARBIE = "https://rihappy.vteximg.com.br/arquivos/ids/313399-400-400/DHM41-boneca-barbie-bailarina-loira-mattel-detalhe-1.jpg?v=636064205433430000"
FLORESTA = "http://www.litury.com/wp-content/uploads/2017/12/sombre-fond-d-ecran-hd.jpg"
TARZAN = "https://vignette.wikia.nocookie.net/vsdebating/images/6/68/Tarzan.png/revision/latest/scale-to-width-down/400?cb=20170707201517"
HOMEM_ARANHA = "https://www.impaktovisual.com.br/3383-large_default/display-homem-aranha.jpg"
CIDADE = "https://st2.depositphotos.com/4829791/7830/i/950/depositphotos_78304622-stock-photo-the-central-park.jpg"
CINDERELA = "https://1.bp.blogspot.com/-V2tLZSbQiXk/WD8fBBsCwDI/AAAAAAAACAo/ik35d327hAAa6YfTwuN-tD2RozNXOgzpwCLcB/s320/23.png"
ALICE = "https://www.disneyclips.com/imagesnewb/images/alice3.png"
CASTELO = "https://img.elo7.com.br/product/main/1AD83BA/painel-castelo-com-flores-x2-8m-painel-3d.jpg"
YODA = "https://2.bp.blogspot.com/-V8V5RPZUD1M/V1LnlY7xeOI/AAAAAAAAEu4/lKAEq2C0z5Y1NUmrGvSdspKHiz6RiM9gACLcB/s640/Yodauur.png"
def criarcenas():
    floresta = Cena(img=FLORESTA)
    cidade = Cena(img=CIDADE)
    floresta.direita = cidade
    
    
    barbie = Elemento(img=BARBIE,tit="Barbie", style=dict(left="100px", top="160px", width="60px", height="200px"))
    barbie.entra(floresta)
    ebarbie = Texto (floresta, "Que floresta feia")
    barbie.vai = ebarbie.vai
    
    castelo = Cena(img=CASTELO)
    cidade.direita = castelo
    
    tarzan = Elemento(img=TARZAN,tit="Tarzan", style=dict(left="100px", top="160px", width="60px", height="200px"))
    tarzan.entra(floresta)
    etarzan = Texto (floresta, "Olá!!!!")
    tarzan.vai = etarzan.vai
    
    homem_aranha = Elemento(img=HOMEM_ARANHA,tit="homem_aranha", style=dict(left="100px", top="160px", width="60px", height="200px"))
    homem_aranha.entra(cidade)
    ehomem_aranha = Texto (cidade, "o que que ta acontecendo aqui bb?")
    homem_aranha.vai = ehomem_aranha.vai
    
    cinderela = Elemento(img=CINDERELA,tit="cinderela", style=dict(left="100px", top="160px", width="60px", height="200px"))
    cinderela.entra(cidade)
    ecinderela = Texto (cidade, "A BARBIE SO FAZ BESTEIRINHAAAAA SOS")
    cinderela.vai = ecinderela.vai
    
    alice = Elemento(img=ALICE,tit="Alice", style=dict(left="100px", top="160px", width="60px", height="200px"))
    alice.entra(castelo)
    ealice = Texto (castelo, "Vou ter que interromper meu momento de descanso, triste")
    alice.vai = ealice.vai
    
    yoda = Elemento(img=YODA,tit="Yoda", style=dict(left="100px", top="160px", width="60px", height="200px"))
    yoda.entra(castelo)
    eyoda = Texto (castelo, "SEMPRE SOBRA PARA MIM!!!!")
    yoda.vai = eyoda.vai
    

    floresta.vai()
criarcenas()