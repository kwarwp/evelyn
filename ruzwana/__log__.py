
{'date': 'Wed Aug 29 2018 11:02:00.378 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 22
  textocastelo = Texto (castelo, "Tarzan encontra jesuítas na floresta que tentam catequisá-lo. Devido a sua recusa, foi levado por eles à Europa para tentarem novamente. Dessa vez, imerso na cultura européia e hospedado em um castelo.
                                                                                                                                                                                                                                           ^
SyntaxError: EOL while scanning string literal
'''},
{'date': 'Wed Aug 29 2018 11:02:24.888 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 2
    from _spy.vitollino.main import cena, texto, Elemento 
ImportError: cannot import name 'cena'

ImportError
Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 264
    action()
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 2
    from _spy.vitollino.main import cena, texto, Elemento 
'''},
{'date': 'Wed Aug 29 2018 11:02:55.365 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 22
  textocastelo = Texto (castelo, "Tarzan encontra jesuitas na floresta que tentam catequisa-lo. Devido a sua recusa, foi levado por eles à Europa para tentarem novamente. Dessa vez, imerso na cultura europeia e hospedado em um castelo.
                                                                                                                                                                                                                                           ^
SyntaxError: EOL while scanning string literal
'''},
{'date': 'Wed Aug 29 2018 11:03:46.379 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 24
    criarcenas()
  module <module> line 23
    floresta.vai()
NameError: name 'floresta' is not defined
'''},