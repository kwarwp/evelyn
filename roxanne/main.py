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
ALICE = "https://i.imgur.com/wLTlDgD.png",
BARBIE = "https://i.imgur.com/a3oxZpW.png",
HOMEMARANHA = "https://i.imgur.com/q4YqcdK.png",
MESTRE = "https://i.imgur.com/wbOu85i.png",
CINDERELA = "https://i.imgur.com/8YSQS00.png",
MOSTROS = "Introducao_a_Computacao/Untitled_20180828_105627.jpg"
)
TEMPLOTRAS1 = "Introducao_a_Computacao/Untitled_20180828_110147.jpg",
ACTIVE = "http://activufrj.nce.ufrj.br/studio/"
POS = "?disp=inline&size=G"
from _spy.vitollino.main import Cena, Elemento, STYLE
from random import shuffle
from browser import timer


STYLE["width"] = 800
class Cubo:
    def __init__(self, faces=PERSONAGENS, onde=LUGARES):
        self.perf = list(faces.values())
        self.per = Elemento(ACTIVE+self.perf[0]+POS, style=dict(left=100, top=100, width=300, height="300px"))
        self.lugf = list(onde.values())
        self.lug = Elemento(ACTIVE+self.lugf[0]+POS, style=dict(left=600, top=100, width=300, height="300px"))
        self.cena = Cena(TEMPLOTRAS1)
        self.lug.entra(self.cena)
        self.per.entra(self.cena)
        self.lug.vai = self.shuffle_place
        self.per.vai = self.shuffle_face
        self.lug_time = self.per_time = 10
        self.cena.vai()

    def shuffle_face(self, *_):
        faces = self.perf
        shuffle(faces)
        self.per.img.src = ACTIVE+faces[0]+POS
        if self.per_time < 500:
            self.per_time *= 1.2
            timer.set_timeout(self.shuffle_face, self.per_time)
        else:
            self.per_time = 10
    def shuffle_place (self, *_):
        places= self.lugf
        shuffle (places)
        self.lug.img.src = ACTIVE+places[0]+POS
        if self.lug_time < 500:
            self.lug_time *= 1.2
            timer.set_timeout(self.shuffle_place, self.lug_time)
        else:
            self.lug_time = 10
Cubo ()