
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