
{'date': 'Tue Aug 28 2018 15:23:56.518 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 15
  ARTEFATOS1 = "Introducao_a_Computacao/Untitled_20180828_105529.jpg
                                                                    ^
SyntaxError: EOL while scanning string literal
'''},
{'date': 'Tue Aug 28 2018 16:27:06.663 GMt-0300 (-03) -X- SuPyGirls -X-',
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
  module <module> line 28
    Tesouro ()
TypeError: Tesouro() missing 1 positional argument: inca
'''},