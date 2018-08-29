
{'date': 'Wed Aug 29 2018 11:01:47.116 GMt-0300 (Hora oficial do Brasil) -X- SuPyGirls -X-',
'error': '''
 module <string> line 17
  tarzan = Elemento(img=TARZAN, tit="Tarzan", style=dict(left="100px", top="160px, width="60px", height="200px"))
                                                                                           ^
SyntaxError: invalid syntax
'''},
{'date': 'Wed Aug 29 2018 11:20:46.615 GMt-0300 (Hora oficial do Brasil) -X- SuPyGirls -X-',
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
  module <module> line 4
    STYLE ["width=500"]
KeyError: width=500
'''},