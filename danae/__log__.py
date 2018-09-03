
{'date': 'Wed Aug 29 2018 09:33:29.797 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 128
    Jogo().inicia()
  module <module> line 107
    self.mesa = Mesa()
  module <module> line 92
    self.labirinto = Elemento()
TypeError: 'module' object is not callable
'''},
{'date': 'Thu Aug 30 2018 19:47:26.872 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 72
    SPRITES = {key: Sprite(*args) for key, *args in SPRITES.items()}
TypeError: __init__ missing 1 positional argument: 'img'
'''},
{'date': 'Thu Aug 30 2018 19:50:13.255 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 72
    SPRITES = {key: Sprite(img, ind) for key, (img, ind) in SPRITES.items()}
  module <module> line 67
    super().__init__(IMGS[img], tit=img, style=dict(
KeyError: http://activufrj.nce.ufrj.br/studio/Introducao_a_Computacao/Untitled_20180828_102220.jpg?disp=inline&size=G
'''},
{'date': 'Thu Aug 30 2018 19:51:34.634 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 72
    SPRITES = {key: Sprite(key, ind) for key, (img, ind) in SPRITES.items()}
  module <module> line 67
    super().__init__(IMGS[img], tit=img, style=dict(
KeyError: aranha
'''},
{'date': 'Thu Aug 30 2018 19:53:11.963 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 226
    Jogo().inicia()
  module <module> line 219
    self.mesa = Mesa(jogadores)
  module <module> line 180
    self.jogadores_ativos = self.jogadores = [Jogador(jogador, self) for jogador in jogadores]
TypeError: 'int' object is not iterable
'''},
{'date': 'Thu Aug 30 2018 19:54:08.17 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 226
    Jogo().inicia()
  module <module> line 219
    self.mesa = Mesa(jogadores)
  module <module> line 180
    self.jogadores_ativos = self.jogadores = [Jogador(jogador, self) for jogador in jogadores]
  module <module> line 155
    self.sprite = Sprite(mesa.acampamento, jogador)
AttributeError: 'Mesa' object has no attribute 'acampamento'
'''},
{'date': 'Thu Aug 30 2018 19:59:29.818 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 72
    SPRITES = {key: Sprite(img, ind, tit=key) for key, (img, ind) in SPRITES.items()}
TypeError: __init__() got multiple values for argument 'tit'
'''},
{'date': 'Thu Aug 30 2018 20:00:18.987 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 227
    Jogo().inicia()
  module <module> line 220
    self.mesa = Mesa(jogadores)
  module <module> line 181
    self.jogadores_ativos = self.jogadores = [Jogador(jogador, self) for jogador in jogadores]
  module <module> line 156
    self.sprite.entra(mesa.acampamento)
AttributeError: 'Mesa' object has no attribute 'acampamento'
'''},
{'date': 'Thu Aug 30 2018 20:01:59.134 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 229
    Jogo().inicia()
  module <module> line 222
    self.mesa = Mesa(jogadores)
  module <module> line 185
    self.jogadores_ativos = self.jogadores = [Jogador(jogador, self) for jogador in jogadores]
  module <module> line 156
    self.sprite.entra(mesa.acampamento)
  module _spy.vitollino.main line 456
    self.scorer.update(valor=cena.nome, move=self.xy,
AttributeError: 'Elemento' object has no attribute 'nome'
'''},
{'date': 'Thu Aug 30 2018 20:04:01.827 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 231
    Jogo().inicia()
  module <module> line 224
    self.mesa = Mesa(jogadores)
  module <module> line 187
    self.jogadores_ativos = self.jogadores = [Jogador(jogador, self) for jogador in jogadores]
  module <module> line 159
    self.chance = shuffle(list(range(20)))
TypeError: can't set attributes of built-in/extension type 'object'
'''},
{'date': 'Thu Aug 30 2018 20:05:36.278 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 232
    Jogo().inicia()
  module <module> line 228
    self.mesa.inicia()
  module <module> line 194
    self.rodada(artefato)
  module <module> line 201
    while self.turno():
  module <module> line 212
    self.apresenta(carta_corrente)
  module <module> line 207
    carta.entra(self.labirinto)
  module <module> line 96
    cena.elt <= self.elt
TypeError: can't add 'NoneType' object to DOMNode instance
'''},
{'date': 'Thu Aug 30 2018 20:07:00.153 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 232
    Jogo().inicia()
  module <module> line 225
    self.mesa = Mesa(jogadores)
  module <module> line 189
    self.baralho = Baralho()
  module <module> line 133
    self.monta_baralho()
  module <module> line 147
    self.cartas.append(Tesouro(face=tesouro))
  module <module> line 82
    self.elt = SPRITES[face]
KeyError: 1
'''},
{'date': 'Thu Aug 30 2018 20:08:15.182 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 232
    Jogo().inicia()
  module <module> line 228
    self.mesa.inicia()
  module <module> line 194
    self.rodada(artefato)
  module <module> line 201
    while self.turno():
  module <module> line 219
    carta.premia(jogador)
  module <module> line 122
    for jogador in jogadores:
TypeError: 'Jogador' object is not iterable
'''},
{'date': 'Thu Aug 30 2018 21:00:09.679 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 233
    Jogo().inicia()
  module <module> line 229
    self.mesa.inicia()
  module <module> line 195
    self.rodada(artefato)
  module <module> line 202
    while self.turno():
  module <module> line 220
    carta.premia(jogador)
  module <module> line 123
    for jogador in jogadores:
NameError: name 'jogadores' is not defined
'''},
{'date': 'Thu Aug 30 2018 21:01:40.108 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 231
    Jogo().inicia()
  module <module> line 227
    self.mesa.inicia()
  module <module> line 193
    self.rodada(artefato)
  module <module> line 200
    while self.turno():
  module <module> line 218
    carta.premia(jogador)
  module <module> line 122
    jogador.recebe(self.valor // len(jogadores))
NameError: name 'jogadores' is not defined
'''},
{'date': 'Thu Aug 30 2018 21:04:46.237 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 225
    Jogo().inicia()
  module <module> line 221
    self.mesa.inicia()
  module <module> line 187
    self.rodada(artefato)
  module <module> line 194
    while self.turno():
  module <module> line 212
    carta.premia(jogador, len(self.jogadores_ativos))
  module <module> line 116
    jogador.recebe(self.valorcota)
AttributeError: 'Tesouro' object has no attribute 'valorcota'
'''},
{'date': 'Thu Aug 30 2018 21:05:05.894 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 225
    Jogo().inicia()
  module <module> line 221
    self.mesa.inicia()
  module <module> line 187
    self.rodada(artefato)
  module <module> line 194
    while self.turno():
  module <module> line 203
    carta_corrente = self.baralho.descarta()
  module <module> line 133
    return self.cartas.pop()
IndexError: pop index out of range
'''},
{'date': 'Thu Aug 30 2018 21:19:19.363 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 227
    Jogo().inicia()
  module <module> line 223
    self.mesa.inicia()
  module <module> line 187
    self.rodada(artefato)
  module <module> line 194
    while self.turno():
  module <module> line 214
    carta.premia(jogador, len(self.jogadores_ativos))
  module <module> line 116
    jogador.recebe(self.valor // cota)
ZeroDivisionError: division by zero
'''},
{'date': 'Thu Aug 30 2018 21:22:25.67 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 227
    Jogo().inicia()
  module <module> line 223
    self.mesa.inicia()
  module <module> line 187
    self.rodada(artefato)
  module <module> line 194
    while self.turno():
  module <module> line 212
    if jogador.joga() == DESISTE:
  module <module> line 161
    return self.chance.pop()
IndexError: pop index out of range
'''},
{'date': 'Sat Sep 01 2018 12:22:34.46 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 232
    Jogo().inicia()
  module <module> line 224
    self.mesa = Mesa(jogadores)
  module <module> line 185
    self.baralho = Baralho()
  module <module> line 129
    self.monta_baralho()
  module <module> line 143
    self.cartas.append(Tesouro(face=tesouro))
  module <module> line 85
    self.elt = SPRITES[face if face.isalpha() else "t{}".format(face)]
KeyError: t14
'''},
{'date': 'Sat Sep 01 2018 12:23:56.435 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 62
  t13=(IMGS["PEDRAS3"], 2), t7=(IMGS["PEDRAS4"], 0), t9=(IMGS["PEDRAS4"], 1), t11=(IMGS["PEDRAS4"], 2),
                              ^
SyntaxError: keyword argument repeated
'''},
{'date': 'Sat Sep 01 2018 12:33:43.756 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 239
    Jogo().inicia()
  module <module> line 235
    self.mesa.inicia()
  module <module> line 193
    while self.baralho.carta:
AttributeError: 'Baralho' object has no attribute 'carta'
'''},
{'date': 'Sat Sep 01 2018 12:38:51.706 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 239
    Jogo().inicia()
  module <module> line 235
    self.mesa.inicia()
  module <module> line 193
    while self.baralho.carta:
AttributeError: 'Baralho' object has no attribute 'carta'
'''},
{'date': 'Sat Sep 01 2018 13:06:10.355 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 61
  t4=(IMGS["PEDRAS2"], 1), t3=(IMGS["PEDRAS2"], 2), t9=(IMGS["PEDRAS3"], 0), t11=(IMGS["PEDRAS3"], 1),
    ^
SyntaxError: keyword argument repeated
'''},
{'date': 'Sat Sep 01 2018 16:33:55.370 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 167
  self.sprite = self.sai
  ^
IndentationError: expected an indented block
'''},
{'date': 'Sat Sep 01 2018 18:28:25.38 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 270
    Jogo().inicia()
  module <module> line 263
    self.mesa = Mesa(jogadores)
  module <module> line 201
    self.mesa = Cenario(IMGS["TEMPLOTRAS3"], 0, 800)
  module <module> line 82
    super().__init__(img, style=dict(
  module _spy.vitollino.main line 771
    Cena.c(**kwargs)
  module _spy.vitollino.main line 814
    imagem, kwargs = (imagem, {}) if isinstance(imagem, str) \
KeyError: img
'''},
{'date': 'Sat Sep 01 2018 18:29:45.438 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 271
    Jogo().inicia()
  module <module> line 264
    self.mesa = Mesa(jogadores)
  module <module> line 202
    self.mesa = Cenario(IMGS["TEMPLOTRAS3"], 0, 800)
  module <module> line 83
    super().__init__(img, style=dict(
  module _spy.vitollino.main line 771
    Cena.c(**kwargs)
  module _spy.vitollino.main line 814
    imagem, kwargs = (imagem, {}) if isinstance(imagem, str) \
KeyError: img
'''},
{'date': 'Sat Sep 01 2018 18:31:03.49 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 271
    Jogo().inicia()
  module <module> line 264
    self.mesa = Mesa(jogadores)
  module <module> line 202
    self.mesa = Cenario(IMGS["TEMPLOTRAS3"], 0, 800)
  module <module> line 85
    self.etl.style.width = w
AttributeError: 'Cenario' object has no attribute 'etl'
'''},
{'date': 'Sat Sep 01 2018 18:32:49.517 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 270
    Jogo().inicia()
  module <module> line 263
    self.mesa = Mesa(jogadores)
  module <module> line 201
    self.mesa = Cenario(IMGS["TEMPLOTRAS3"], 0, 800)
  module <module> line 88
    self.img.style.marginLeft = "-{}px".format(index * w)
AttributeError: 'str' object has no attribute 'style'
'''},
{'date': 'Sat Sep 01 2018 19:10:59.548 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 277
    Jogo().inicia()
  module <module> line 270
    self.mesa = Mesa(jogadores)
  module <module> line 206
    self.jogadores_ativos = self.jogadores = [Jogador(jogador, self) for jogador in jogadores]
  module <module> line 169
    self.cena = mesa.acampamento
AttributeError: 'Mesa' object has no attribute 'acampamento'
'''},
{'date': 'Sat Sep 01 2018 20:10:43.108 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 31
    STYLE["width"] = 800
AttributeError: 'module' object has no attribute '__setitem__'
'''},
{'date': 'Sat Sep 01 2018 20:11:03.922 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 297
    Jogo().inicia()
  module <module> line 290
    self.mesa = Mesa(jogadores)
  module <module> line 225
    self.jogadores_ativos = self.jogadores = [Jogador(jogador, self) for jogador in jogadores]
  module <module> line 175
    self.mostrador = Codigo("0", "0", self.sprite)
  module _spy.vitollino.main line 503
    self.scorer = dict(ponto=1, valor=cena.nome, carta=img, casa=self.xy, move=None)
AttributeError: 'Sprite' object has no attribute 'nome'
'''},
{'date': 'Sat Sep 01 2018 20:11:33.348 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 297
    Jogo().inicia()
  module <module> line 290
    self.mesa = Mesa(jogadores)
  module <module> line 225
    self.jogadores_ativos = self.jogadores = [Jogador(jogador, self) for jogador in jogadores]
  module <module> line 175
    self.mostrador = Codigo("0", "0", self.sprite)
  module _spy.vitollino.main line 503
    self.scorer = dict(ponto=1, valor=cena.nome, carta=img, casa=self.xy, move=None)
AttributeError: 'Sprite' object has no attribute 'nome'
'''},
{'date': 'Sat Sep 01 2018 20:15:48.637 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 31
    STYLE["width"] = 800
AttributeError: 'module' object has no attribute '__setitem__'
'''},
{'date': 'Sat Sep 01 2018 20:16:17.621 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 298
    Jogo().inicia()
  module <module> line 291
    self.mesa = Mesa(jogadores)
  module <module> line 226
    self.jogadores_ativos = self.jogadores = [Jogador(jogador, self) for jogador in jogadores]
  module <module> line 176
    self.mostrador = Codigo("0", "0", self.sprite)
  module _spy.vitollino.main line 516
    _ = self.entra(cena) if cena and (cena != INVENTARIO) else None
  module _spy.vitollino.main line 459
    cena <= self
TypeError: '<=' not supported between instances of 'Sprite' and 'Codigo'
'''},
{'date': 'Sat Sep 01 2018 20:47:58.97 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 28
  from vitollino.main import Elemento, Cena, Codigo, Texto, , STYLE
                                                            ^
SyntaxError: trailing comma not allowed without surrounding parentheses
'''},
{'date': 'Sat Sep 01 2018 21:01:07.312 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 214
  self.mostrador.._code.html = "{}:{}".format(self.tesouro, self.joias)
                  ^
SyntaxError: invalid syntax
'''},
{'date': 'Sat Sep 01 2018 21:03:31.758 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
Exception: <TypeError: r.substring is not a function>
'''},
{'date': 'Sat Sep 01 2018 21:06:08.98 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
Exception: <TypeError: r.substring is not a function>
'''},
{'date': 'Sat Sep 01 2018 21:08:14.480 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
Exception: <TypeError: r.substring is not a function>
'''},
{'date': 'Sat Sep 01 2018 23:32:09.985 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 128
  self.divide_valor(, jogadores, sala)
                     ^
SyntaxError: invalid syntax
'''},
{'date': 'Sun Sep 02 2018 09:33:52.326 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 32
    STYLE["width"] = 800
AttributeError: 'module' object has no attribute '__setitem__'
'''},
{'date': 'Mon Sep 03 2018 17:51:17.50 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 129
  self.carta[imagem] = carta = Sprite(**SPRITES[imagem if imagem.isalpha() else "t{}".format(imagem)], tit=tit)
                                                                                                        ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Sep 03 2018 17:54:11.232 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 32
    STYLE["width"] = 800
AttributeError: 'module' object has no attribute '__setitem__'
'''},
{'date': 'Mon Sep 03 2018 18:00:12.61 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 129
  sprite = **SPRITES[imagem if imagem.isalpha() else "t{}".format(imagem)]
            ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Sep 03 2018 18:02:32.589 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 386
    Jogo().inicia()
  module <module> line 379
    self.mesa = Mesa(jogadores)
  module <module> line 303
    self.baralho = Baralho()
  module <module> line 230
    self.monta_baralho()
  module <module> line 243
    self.cartas.append(Perigo(face=perigo))
  module <module> line 147
    self.elt = GUI.carta(face)
TypeError: 'list' object is not callable
'''},
{'date': 'Mon Sep 03 2018 18:06:11.774 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 386
    Jogo().inicia()
  module <module> line 379
    self.mesa = Mesa(jogadores)
  module <module> line 303
    self.baralho = Baralho()
  module <module> line 230
    self.monta_baralho()
  module <module> line 243
    self.cartas.append(Perigo(face=perigo))
  module <module> line 147
    self.elt = GUI.carta(face)
  module <module> line 132
    self._carta[imagem] = carta = Sprite(**sprite)
IndexError: list assignment index out of range
'''},
{'date': 'Mon Sep 03 2018 18:45:23.325 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 397
    Jogo().inicia()
  module <module> line 390
    self.mesa = Mesa(jogadores)
  module <module> line 314
    self.baralho = Baralho()
  module <module> line 241
    self.monta_baralho()
  module <module> line 256
    self.cartas.append(Tesouro(face=tesouro))
  module <module> line 226
    self.elt.mostra(":{}:".format(self.valor))
  module <module> line 100
    self._mostrador.mostra(valor)
AttributeError: 'NoneType' object has no attribute 'mostra'
'''},