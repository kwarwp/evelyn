# evelyn.ruzwana.main.py
from _spy.vitollino.main import Cena, Texto, Elemento
from _spy.viollino.main import INVENTARIO as inv

TARZAN = "https://vignette.wikia.nocookie.net/vsbattles/images/6/68/Tarzan.png/revision/latest?cb=20170117061234"
CASTELO = "http://cdn5.colorir.com/desenhos/color/201608/castelo-fantastico-edificios-castelos-1212559.jpg"
CINDERELA = "http://1.bp.blogspot.com/-2tR96Ygxq1w/UktUBEcmR4I/AAAAAAAAbd0/V2pztOVgW-Y/s1600/princesa-cinderela-desenho-colorido-disney-com-fundo-transparente-dibujos-ideia-criativa+(1).png"
CASINHA = "http://cdn5.colorir.com/desenhos/color/201605/casa-con-cuori-desenhos-dos-utentes-pintado-por-jejezinha-1203206.jpg"

ALICE = "https://icon2.kisspng.com/20180327/uue/kisspng-alice-liddell-alice-s-adventures-in-wonderland-the-alice-in-wonderland-5ab9ee8c10bb20.5426997015221346680685.jpg"
PANTANO = "http://2.bp.blogspot.com/_3WptCxQeZj8/TS6pqwa6MXI/AAAAAAAAA00/wr6duOxFZpc/s1600/p%25C3%25A2ntano.jpg"

def criarcenas():
    castelo = Cena(img=CASTELO)
    casinha = Cena(img=CASINHA)
    castelo.direita = casinha
    
    tarzan = Elemento(img=TARZAN, tit="Tarzan", style=dict(left="100px",top="160px" ,width="60px", height="200px"))
    tarzan.entra(castelo)
    etarzan = Texto (castelo, "Que lugar é esse?")
    textocastelo = Texto (castelo, "Tarzan encontra jesuitas na floresta que tentam catequisa-lo. Devido a sua recusa, foi levado por eles à Europa para tentarem novamente. Dessa vez, imerso na cultura europeia e hospedado em um castelo")
    tarzan.vai = etarzan.vai
    textocastelo.vai()
criarcenas() 
