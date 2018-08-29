
{'date': 'Tue Aug 28 2018 23:38:33.324 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 20
  castelo = Cena(img=CASTELO)
  ^
IndentationError: expected an indented block
'''},
{'date': 'Tue Aug 28 2018 23:39:04.332 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <SyntaxError: Unexpected token {>
'''},
{'date': 'Wed Aug 29 2018 00:09:51.62 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 30
    criarcenas()
  module <module> line 21
    batman = elemento(img=BATMAN,tit="Flash",style=dict(left=100, top=160, width=60, height=200))
NameError: name 'elemento' is not defined
'''},