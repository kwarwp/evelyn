# evelyn.danae.main.py
# ! /usr/bin/env python
# -*- coding: UTF8 -*-
# Este arquivo é parte do programa SuperPython
# Copyright 2013-2015 Carlo Oliveira <carlo@nce.ufrj.br>,
# `Labase <http://labase.selfip.org/>`__; `GPL <http://is.gd/3Udt>`__.
#
# SuperPython é um software livre; você pode redistribuí-lo e/ou
# modificá-lo dentro dos termos da Licença Pública Geral GNU como
# publicada pela Fundação do Software Livre (FSF); na versão 2 da
# Licença.
#
# Este programa é distribuído na esperança de que possa ser útil,
# mas SEM NENHUMA GARANTIA; sem uma garantia implícita de ADEQUAÇÃO
# a qualquer MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
# Licença Pública Geral GNU para maiores detalhes.
#
# Você deve ter recebido uma cópia da Licença Pública Geral GNU
# junto com este programa, se não, veja em <http://www.gnu.org/licenses/>

"""Módulo principal do Tesouro Inca.
.. moduleauthor:: Carlo Oliveira <carlo@nce.ufrj.br>
"""
from random import shuffle

from _spy.vitollino.main import Elemento, Cena

DESISTE = True
PERIGOS = "aranha mumia desabe fogo cobra".split()
ARTEFATOS = "estatua vaso colar broche adorno".split()
TESOUROS = "1 2 3 4 5 7 9 11 13".split()
JOGADORES = "Roxanne Stacy Libby Sara Kellee Courtney".split()
ACTIVE = "http://activufrj.nce.ufrj.br/studio/"
POS = "?disp=inline&size=G"
TEMPLOTRAS1 = ACTIVE + "Introducao_a_Computacao/Untitled_20180828_110147.jpg" + POS
IMGS = dict(
    PEDRAS1="Introducao_a_Computacao/Untitled_20180828_102220.jpg",
    PEDRAS2="Introducao_a_Computacao/Untitled_20180828_105412.jpg",
    PEDRAS3="Introducao_a_Computacao/Untitled_20180828_105419.jpg",
    PEDRAS4="Introducao_a_Computacao/Untitled_20180828_105624.jpg",
    TEMPLOTRAS1="Introducao_a_Computacao/Untitled_20180828_110147.jpg",
    TEMPLOTRAS2="Introducao_a_Computacao/Untitled_20180828_110148.jpg",
    TEMPLOTRAS3="Introducao_a_Computacao/Untitled_20180828_110145.jpg",
    CARTASENTRAESAI="Introducao_a_Computacao/Untitled_20180828_105727.jpg",
    CARTASENTRAESAITRAS="Introducao_a_Computacao/Untitled_20180828_105833-0.jpg",
    CARTASTRAS="Introducao_a_Computacao/Untitled_20180828_105833-2.jpg",
    ARTEFATOS1="Introducao_a_Computacao/Untitled_20180828_105529.jpg",
    ARTEFATOS2="Introducao_a_Computacao/Untitled_20180828_105528.jpg",
    MOSTROS1="Introducao_a_Computacao/Untitled_20180828_105623.jpg",
    MOSTROS="Introducao_a_Computacao/Untitled_20180828_105627.jpg"

)
IMGS = {key: ACTIVE + img + POS for key, img in IMGS.items()}
SPRITES = dict(
    aranha=(IMGS["PEDRAS1"], 0), mumia=(IMGS["PEDRAS1"], 0), desabe=(IMGS["PEDRAS1"], 0),
    fogo=(IMGS["PEDRAS1"], 0), cobra=(IMGS["PEDRAS1"], 0),
    estatua=(IMGS["PEDRAS1"], 0), vaso=(IMGS["PEDRAS1"], 0), colar=(IMGS["PEDRAS1"], 0),
    broche=(IMGS["PEDRAS1"], 0), adorno=(IMGS["PEDRAS1"], 0),
    t1=(IMGS["PEDRAS1"], 0), t2=(IMGS["PEDRAS1"], 0), t3=(IMGS["PEDRAS1"], 0), t4=(IMGS["PEDRAS1"], 0),
    t5=(IMGS["PEDRAS1"], 0), t7=(IMGS["PEDRAS1"], 0), t9=(IMGS["PEDRAS1"], 0), t11=(IMGS["PEDRAS1"], 0),
    t13=(IMGS["PEDRAS1"], 0),
)


class Sprite(Elemento):
    def __init__(self, img, tit="", index=0, w=100, h=100):
        super().__init__(img, tit=tit, style=dict(
            position="relative", width=w, height="{}px".format(h), overflow="hidden"))
        self.img.style.margin = "-{}px 0 0 0".format(index * w)


SPRITES = {key: Sprite(img, ind, tit=key) for key, (img, ind) in SPRITES.items()}


class Carta(object):
    PERIGO = []
    VALOR = 2

    def __init__(self, face):
        self.face = face
        self.valor = int(face) if face.isdigit() else 0
        self.elt = None

    def premia(self, jogadores):
        if len(jogadores) == 1:
            jogadores[0].recebe(10 // self.VALOR)
        return True

    def divide(self, jogadores, salas):
        for jogador in jogadores:
            jogador.recebe(self.valor // len(jogadores))
            self.valor %= len(jogadores)
        return True

    def entra(self, cena):
        cena.elt <= self.elt

    def __eq__(self, carta):
        return carta.face == self.face


class Perigo(Carta):
    def divide(self, jogadores, salas):
        _ = jogadores
        return self.face not in salas


class Artefato(Carta):
    def divide(self, jogadores, salas):
        return self.premia(jogadores)

    def premia(self, jogadores):
        if len(jogadores) == 1:
            jogadores[0].recebe(10 // self.VALOR)
        return True

    pass


class Tesouro(Carta):
    def premia(self, jogadores):
        for jogador in jogadores:
            jogador.recebe(self.valor // len(jogadores))
            self.valor %= len(jogadores)
        return True

    pass


class Baralho(object):
    def __init__(self):
        self.cartas = []
        self.monta_baralho()

    def embaralha(self, artefato):
        self.cartas.append(Artefato(face=artefato))
        shuffle(self.cartas)

    def descarta(self):
        return self.cartas.pop()

    def monta_baralho(self):
        self.cartas = []
        for perigo in PERIGOS:
            self.cartas.append(Perigo(face=perigo))
        for tesouro in TESOUROS:
            self.cartas.append(Tesouro(face=tesouro))

    def extend(self, salas):
        self.cartas.extend(salas)


class Jogador(object):
    def __init__(self, jogador, mesa):
        self.sprite = Sprite(IMGS["CARTASENTRAESAI"], 0, tit=jogador)
        self.sprite.entra(mesa.acampamento)
        self.jogador = "from {mod}.main import {mod}, self.jogada = {mod}".format(mod=jogador)
        self.jogada, self.joias, self.mesa = None, 0, mesa
        self.chance = shuffle(list(range(20)))

    pass

    def recebe(self, joias):
        self.joias += joias

    def joga(self):
        return self.chance.pop()

    def _joga(self):
        try:
            return self.jogada(self.mesa)
        except TypeError:
            exec(self.jogador)
            return self.jogada(self.mesa)


class Mesa(object):
    def __init__(self, jogadores):
        self.mesa = Cena(TEMPLOTRAS1)
        self.perigo = self.salas = []
        self.jogadores_ativos = self.jogadores = [Jogador(jogador, self) for jogador in jogadores]
        self.acampamento = Elemento("", style=dict(left=0, top=0))
        self.labirinto = Elemento("", style=dict(left=0, top=100))
        self.baralho = Baralho()
        # self.inicia()

    def inicia(self):
        for artefato in ARTEFATOS:
            self.rodada(artefato)

    def rodada(self, artefato):
        self.jogadores_ativos = self.jogadores[:]
        self.baralho.extend(self.salas)
        self.baralho.embaralha(artefato)
        self.perigo = self.salas = []
        while self.turno():
            pass
        self.salas = [carta for carta in self.salas if not isinstance(carta, Artefato)]

    def apresenta(self, carta):
        self.salas.append(carta)
        carta.entra(self.labirinto)

    def turno(self):
        carta_corrente = self.baralho.descarta()
        jogadores_saindo = []
        self.apresenta(carta_corrente)

        for jogador in self.jogadores_ativos:
            if jogador.joga() == DESISTE:
                self.jogadores_ativos.remove(jogador)
                jogadores_saindo.append(jogador)
            for carta in self.salas:
                carta.premia(jogador)
        return self.jogadores_ativos and carta_corrente.divide(jogadores_saindo, self.salas)


class Jogo:
    def __init__(self, jogadores=JOGADORES):
        self.mesa = Mesa(jogadores)

    def inicia(self):
        self.mesa.inicia()


if __name__ == '__main__':
    Jogo().inicia()
