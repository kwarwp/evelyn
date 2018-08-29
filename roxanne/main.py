# evelyn.roxanne.main.py
LUGARES = dict(
PEDRAS1 = "Introducao_a_Computacao/Untitled_20180828_102220.jpg",
PEDRAS2 = "Introducao_a_Computacao/Untitled_20180828_105412.jpg",
PEDRAS3 = "Introducao_a_Computacao/Untitled_20180828_105419.jpg",
PEDRAS4 = "Introducao_a_Computacao/Untitled_20180828_105624.jpg",
TEMPLOTRAS2 = "Introducao_a_Computacao/Untitled_20180828_110148.jpg",
TEMPLOTRAS3 = "Introducao_a_Computacao/Untitled_20180828_110145.jpg"
)
PERSONAGENS = dict(
CARTASENTRAESAI = "Introducao_a_Computacao/Untitled_20180828_105727.jpg",
CARTASTRAS = "Introducao_a_Computacao/Untitled_20180828_105833-2.jpg",
ARTEFATOS1 = "Introducao_a_Computacao/Untitled_20180828_105529.jpg",
ARTEFATOS2 = "Introducao_a_Computacao/Untitled_20180828_105528.jpg",
MOSTROS1 = "Introducao_a_Computacao/Untitled_20180828_105623.jpg",
MOSTROS = "Introducao_a_Computacao/Untitled_20180828_105627.jpg"
)
TEMPLOTRAS1 = "Introducao_a_Computacao/Untitled_20180828_110147.jpg",
ACTIVE = "http://activufrj.nce.ufrj.br/studio/"
POS = "?disp=inline&size=G"
from _spy.vitollino.main import Cena, Elemento, STYLE
STYLE["width"] = 800
class Cubo:
    def __init__(self, faces=PERSONAGENS, onde=LUGARES):
        self.perf = list(faces.values())
        self.per = Elemento(ACTIVE+self.perf[0]+POS, style=dict(left=100, top=100, width=300, height="300px"))
        self.lugf = list(onde.values())
        self.lug = Elemento(ACTIVE+self.lugf[0]+POS, style=dict(left=400, top=100, width=300, height="300px"))
        self.cena = Cena(TEMPLOTRAS1)
        self.lug.entra(self.cena)
        self.per.entra(self.cena)
        
    def shuffle_face(*_):
        faces = self.perf
        shuffle(faces)
        self.per.img.src = faces[0]
