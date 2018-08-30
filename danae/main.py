# evelyn.danae.main.py
#! /usr/bin/env python
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

from view.kwarwp.kuarup import Elemento

DESISTE = True
PERIGOS = "aranha mumia desabe fogo cobra".split()
ARTEFATOS = "estatua vaso colar broche adorno".split()
TESOUROS = "1 2 3 4 5 7 9 11 13".split()
JOGADORES = "Roxanne Stacy Libby Sara Kellee Courtney".split()


class Carta(object):
    PERIGO = []
    VALOR = 2

    def __init__(self, face):
        self.face = face
        self.valor = int(face) if face.isdigit() else 0
        self.elt = None

    def entra(self, cena):
        cena.elt <= self.elt


class Perigo(Carta):
    def premia(self, jogadores):
        _ = jogadores
        return self.face not in self.PERIGO


class Artefato(Carta):
    def premia(self, jogadores):
        if len(jogadores) == 1:
            jogadores[0].recebe(10//self.VALOR)
        return True
    pass


class Tesouro(Carta):
    def premia(self, jogadores):
        for jogador in jogadores:
            jogador.recebe(self.valor//len(jogadodes))
            self.valor %= len(jogadores)
        return True
    pass


class Baralho(object):
    def __init__(self):
        self.cartas = []

    def embaralha(self):
        self.monta_baralho()
        shuffle(self.cartas)

    def descarta(self):
        return self.cartas.pop()

    def monta_baralho(self):
        self.cartas = []
        for perigo in PERIGOS:
            self.cartas.append(Perigo(face=perigo))
        for artefato in ARTEFATOS:
            self.cartas.append(Artefato(face=artefato))
        for tesouro in TESOUROS:
            self.cartas.append(Tesouro(face=tesouro))


class Mesa(object):
    def __init__(self):
        self.labirinto = Elemento()
        self.salas = []

    def inicia(self):
        self.salas = []

    def apresenta(self, carta):
        self.salas.append(carta)
        carta.entra(self.labirinto)


class Jogo:
    def __init__(self, jogadores=9):
        self.jogadores = jogadores
        self.jogadores_ativos = []
        self.mesa = Mesa()
        self.baralho = Baralho()

    def inicia(self):
        self.baralho.embaralha()
        Carta.PERIGO = []
        while self.rodada():
            pass

    def rodada(self):
        carta_corrente = self.baralho.descarta()
        jogadores_saindo = []
        self.mesa.apresenta(carta_corrente)
        for jogador in self.jogadores_ativos:
            if jogador.joga() == DESISTE:
                self.jogadores_ativos.remove(jogador)
                jogadores_saindo.append(jogador)
        return carta_corrente.premia(jogadores_saindo)


if __name__ == '__main__':
    Jogo().inicia()