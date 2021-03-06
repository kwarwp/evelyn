# evelyn.courtney# hedy.courtney.main.py
from _spy.vitollino.main import Cena, Texto, Elemento
from _spy.vitollino.main import Inventario as inv

TARZAN_NA_SELVA = "https://vignette.wikia.nocookie.net/vsdebating/images/6/68/Tarzan.png/revision/latest/scale-to-width-down/1000?cb=20170707201517"
TARZAN_EM_PE = "https://vignette.wikia.nocookie.net/disney/images/e/e2/Tarzan_Character.png/revision/latest?cb=20180126232838"
SELVA = "https://images.vexels.com/media/users/17482/121786/preview2/77d67f3e747a300e3d6ffc29b270badf-plantas-da-selva.png"
ALICE = "https://banner2.kisspng.com/20180327/jrw/kisspng-alice-liddell-alice-s-adventures-in-wonderland-the-alice-in-wonderland-5ab9ee8c3461e7.4784863815221346682146.jpg"
PANTANO = "https://vignette.wikia.nocookie.net/star-wars-the-force-unleashed/images/2/28/P%C3%A2ntanos_de_Dagobah.jpg/revision/latest?cb=20121220233139&path-prefix=pt-br"
MESA = "https://1.bp.blogspot.com/-8hu8fFASgiU/WT196QOBtdI/AAAAAAAAAaM/j5PPLpuWSj4_aMafNIj2t_8sMoyD7xh5ACLcB/s1600/primeiro_jantar_de%2B_dia_dos_namorados_meu_ape_34_mesa_posta.jpg"
CASTELO = "https://uploads.spiritfanfiction.com/fanfics/capitulos/201607/fanfiction-alice-no-pais-das-maravilhas-alice-in-wonderland-alice-no-mundo-quase-real-6006577-170720161600.png"

def criarcenas(): 
    selva = Cena(img=SELVA) 
    mesa = Cena(img=MESA)
    selva.direita = mesa
    mesa.esquerda = selva
    
    tarzan = Elemento(img=TARZAN_NA_SELVA, tit="Tarzan", style=dict(left="50px", top="40px", width="150px", heigth="150px"))
    tarzan.entra(selva)
    etarzan = Texto (selva, "Tarzan, que foi criado na selva, quando chega na idade adulta, por conhecer a selva muito bem e se achar o rei dela se perde na floresta.")
    tarzan.vai = etarzan.vai
    
    tarzan = Elemento(img=TARZAN_EM_PE, tit="Tarzan", style=dict(right="50px", top="50px", width="50px", heighth="50px"))
    alice = Elemento(img=ALICE, tit="Alice", style=dict(left="100px", top="100px", widht="100px", height="100px"))
    tarzan.entra(mesa)
    alice.entra(mesa)
    ealice = Texto (mesa, "Você veio do pântano?")
    etarzan = Texto (mesa, "Não, eu vim da selva. Me perdi tentando encontrar minha cinderela")
    alice.vai = ealice.vai
    tarzan.vai = etarzan.vai
    
    selva.vai()
criarcenas()    