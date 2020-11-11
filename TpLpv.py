#coding: utf-8

import wx
'''
Class JanelaExemplo, cria uma classe que extende a Classe wx.Fame da wxPython
esta janela
'''

class JanelaExemplo ( wx.Frame ):

	def __init__( self, parent ):

		'''
		cria uma janela 
		'''
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,442 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		'''
		seta o tamanho da janela
		'''
		self.SetSizeHints( 500, 400 )

		'''
		seta o titulo da janela
		'''
		self.SetTitle("Janela Apresentação TP")

		'''
		seta a renderização da tela no meio da janela
		'''
		self.Centre()

		'''
		Cria um wx.BoxSizer que é um elemento de layout um
		organizador de componentes na tela no qual os componetes
		sao adicionados verticalmente wx.VERTICAL.
		'''
		bs_OrganizacaoVertical = wx.BoxSizer( wx.VERTICAL )

		'''
		cria um componente wx.TextCtrl de apenas uma linha com uma string vazia wx.EmptyString
		e o adiciona no layout, a constante wx.TE_PROCESS_ENTER deve ser adicionada para a conexao
		com o evento wx.EVT_TEXT_ENTER
		'''
		self.txt_Exemplo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )

		'''
		O método Add () (herdado de wxSizer) anexa o componente
		à próxima linha / coluna do sizer.
		Parametros- componente, proporção, sinalizador, borda
		wx.All indica que a borda sera inserida nos 4 lados
		'''
		bs_OrganizacaoVertical.Add( self.txt_Exemplo, 0, wx.ALL, 5 )

		'''
		Relaciona a ação enter no campo de texto
		Vincula um evento a um manipulador de eventos(wx.TE_PROCESS_ENTER)
		O wx.EVT_TEXT_ENTER evento é acionado quando apertamos enter
		em um componente de texto.
		Especificamos o evento a ser acionado como segundo parametro.
		'''
		self.txt_Exemplo.Bind( wx.EVT_TEXT_ENTER, self.AcaoEnter)

		'''
		cria um componente wx.TextCtrl com uma string vazia wx.EmptyString
	    de multiplas linhas wx.TE_MULTILINE, quebra de linha adicionada
		automaticamente, para nao haver quebra adiconar wxTE_DONTWRAP.
		e o adiona no layout.
		'''
		self.txt_MultExemplo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,150 ), wx.TE_MULTILINE )
		bs_OrganizacaoVertical.Add( self.txt_MultExemplo, 0, wx.ALL, 5 )

		'''
		Cria um componente wx.StaticText um rotulo. 
		'''
		self.lbl_Exemplo = wx.StaticText( self, wx.ID_ANY, "Texto 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		'''
		Envolve um rotulo para que cada uma de suas linhas tenha no maximo
		um X pixels de largura, se a largura for negativa nenhum agupamento
		é feito deixando a linha livre
		'''
		self.lbl_Exemplo.Wrap( -1 )
		'''
		adiciona componente a organização vertical
		'''
		bs_OrganizacaoVertical.Add( self.lbl_Exemplo, 0, wx.ALL, 5 )

		'''
		Cria uma organização em forma de grade com 1 linha 2 colunas
		Ela se faz necessaria para que dois componentes possam dividir
		a mesma linha.
		'''
		gs_OrganizacaoGrid = wx.GridSizer( 1, 2, 0, 0 )

		'''
		Cria um componente wx.RadioButton e adiciona a organização de grade
		Um grupo de botões de opção é definido por ter o primeiro botão de opção do grupo contendo
		o wx.RB_GROUP estilo. Todos os outros botões de opção definidos após o primeiro botão
		opção com este sinalizador de estilo serão adicionados ao grupo de funções do primeiro
	    botão de opção.
		'''
		self.rb_Exemplo = wx.RadioButton( self, wx.ID_ANY, "Texto 1", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		gs_OrganizacaoGrid.Add( self.rb_Exemplo, 0, wx.ALL, 5 )
		'''
		Cria um componente wx.RadioButton e adiciona a organização de grade
		'''
		self.rb_Exemplo2 = wx.RadioButton( self, wx.ID_ANY, "Texto 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		gs_OrganizacaoGrid.Add( self.rb_Exemplo2, 0, wx.ALL, 5 )

		'''
		Vincula o wx.EVT_RADIOBUTTONevento ao manipulador de eventos
		no caso do rb_Exemplo rb1Marcado() e no rb_Exemplo2 rb2Marcad().
		'''
		self.rb_Exemplo.Bind( wx.EVT_RADIOBUTTON, self.rb1Marcado )
		self.rb_Exemplo2.Bind( wx.EVT_RADIOBUTTON, self.rb2Marcado )

		'''
		Adiciona os componetes wx.RadioButton a organização de grade
		para que fiquem lado a lado na janela
		'''
		bs_OrganizacaoVertical.Add( gs_OrganizacaoGrid, 0, wx.EXPAND, 5 )

		'''
		Cria um check box wx.CheckBox
		A wx.CheckBoxé um widget que possui dois estados: ligado e desligado.
		É uma caixa com uma etiqueta. O rótulo pode ser colocado à direita ou à esquerda da caixa.
		Se a wx.CheckBoxestiver marcado, ele é representado por uma marca em uma caixa.
		'''
		self.cb_Exemplo = wx.CheckBox( self, wx.ID_ANY, "Ativa Lista Suspensa", wx.DefaultPosition, wx.DefaultSize, 0 )
		bs_OrganizacaoVertical.Add( self.cb_Exemplo, 0, wx.ALL, 5 )
		'''
		Vincula owx.EVT_CHECKBOX evento ao manipulador de eventos AtivaLista().
		'''
		self.cb_Exemplo.Bind( wx.EVT_CHECKBOX, self.AtivaLista )

		'''
		Cria uma lista de itens a ser exibidos na lista supensa
		'''
		ls_ExemploChoices = [ "", "Python", "C++", "Ruby" ]
		'''
		Cria uma lista suspensa com o componente wx.Choice
		'''
		self.ls_Exemplo = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ls_ExemploChoices, 0 )
		'''
		Seleciona a opção 0 como opção inicial
		'''
		self.ls_Exemplo.SetSelection( 0 )
		'''
		Seta que o compontente esta indisponivel para utilização
		'''
		self.ls_Exemplo.Enable( False )
		'''
		O wx.EVT_CHOICE evento é acionado e quando escolhemos uma opcao no wx.Choice.
		O EscolhaLista() manipulador de eventos é chamado neste evento.
		'''
		self.ls_Exemplo.Bind( wx.EVT_CHOICE, self.EscolhaLista )
		'''
		Adiciona componete ao layout
		'''
		bs_OrganizacaoVertical.Add( self.ls_Exemplo, 0, wx.ALL, 5 )

		'''
		Cria um componente wx.StaticText um rotulo. Set wrap negativo para nao haver
		agrupamento por largura e adiciona rotulo ao layout
		'''
		self.lbl_Exemplo2 = wx.StaticText( self, wx.ID_ANY, "A liguagem escolhida foi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_Exemplo2.Wrap( -1 )
		bs_OrganizacaoVertical.Add( self.lbl_Exemplo2, 0, wx.ALL, 5 )


		'''
		Cria um Slider wx.Slider na orientação horizontal com limites de
		1 a 16 sendo escolhido como valor inicial 8.
		wx.Slider é um widget que possui um identificador simples.
		Contem uma alça pode ser puxada para frente e para trás. Assim podemos escolher um valor específico.
		'''
		self.sl_Exemplo = wx.Slider( self, wx.ID_ANY, 8, 1, 16, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		'''
		O wx.EVT_SCROLL evento é acionado e quando o valor no slider é alterado.
		O SliderActive() manipulador de eventos é chamado neste evento.
		'''
		self.sl_Exemplo.Bind( wx.EVT_SCROLL, self.SliderActive )
		bs_OrganizacaoVertical.Add( self.sl_Exemplo, 0, wx.ALL, 5 )

		'''
		cria um componente wx.button padrao com o texto do botao sendo 'sair'
		e o adiciona a janela
		'''
		self.bt_Exemplo = wx.Button( self, wx.ID_ANY, "Sair", wx.DefaultPosition)
		bs_OrganizacaoVertical.Add( self.bt_Exemplo, 0, wx.ALL, 5 )

		'''
		Cria um evento que fecha a tela
		Vincula um evento a um manipulador de eventos(botao)
		O wx.EVT_BUTTON evento é acionado quando clicamos no botão.
		Especificamos o evento a ser acionado como segundo parametro.
		'''
		self.bt_Exemplo.Bind (wx.EVT_BUTTON, self.FechaTela)

		'''
		Adiciona um layout a janela
		'''
		self.SetSizer( bs_OrganizacaoVertical )
		self.Layout()
		'''
		Abre a janela no meio da tela
		'''
		self.Centre( wx.BOTH )
		'''
		Exibe a janela
		'''
		self.Show()

	def FechaTela(self, e):
		self.Close()#Fecha a janela
	
	def AcaoEnter(self, e):
		sender = e.GetEventObject ()#atribui o objeto que chamou o evento a variavel sender
		self.textoSL=sender.GetValue()#metodo GetValue() pega o valor armazenado no objeto que chamou o evento
		self.textoMl="O Texto escrito na caixa de uma linha foi "+self.textoSL
		self.txt_MultExemplo.SetValue(self.textoMl)#o metodo SetValue() seta um valor para o objeto
	
	def rb1Marcado( self, e):
		sender = e.GetEventObject ()#atribui o objeto que chamou o evento a variavel sender
		self.lbl_Exemplo.SetLabel(sender.GetLabel())#metodo GetLabel() pega o rotulo do objeto, e SetLabel() seta um rotulo para o objeto

	def rb2Marcado( self, e):
		sender = e.GetEventObject ()#atribui o objeto que chamou o evento a variavel sender
		self.lbl_Exemplo.SetLabel(sender.GetLabel())#metodo GetLabel() pega o rotulo do objeto, e SetLabel() seta um rotulo para o objeto

	def AtivaLista( self, e):
		sender = e.GetEventObject ()#atribui o objeto que chamou o evento a variavel sender
		isChecked = sender.GetValue()#metodo GetValue() pega o valor armazenado no objeto
		if isChecked :
			self.ls_Exemplo.Enable(True)#Seta que o compontente esta disponivel para utilização
		else:
			self.ls_Exemplo.Enable(False)#Seta que o compontente esta indisponivel para utilização

	def EscolhaLista( self, e):
		sender = e.GetEventObject ()#atribui o objeto que chamou o evento a variavel sender
		'''
		O metodo GetString(int) retorna a string representada em uma determinada posição da lista
		o metodo GetCurrentSelection() retorna a posição de seleção da lista
		'''
		opc= sender.GetString(sender.GetCurrentSelection())
		self.lbl_Exemplo2.SetLabel("A liguagem escolhida foi "+opc)#seta um novo rotulo para o wx.StaticText

	def SliderActive( self, e):
		sender = e.GetEventObject()#atribui o objeto que chamou o evento a variavel sender
		tamanho = sender.GetValue()#metodo GetValue() pega o valor armazenado no objeto
		'''
		Metodo SetFont seta uma fonte para o rotulo exibido no wx.StaticText
		utiliza o valor escolhido no slider para setar o tamanho da fonte
		'''
		self.lbl_Exemplo2.SetFont( wx.Font( tamanho, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

def main():
	app = wx.App()#cria um app wx para execução
	JanelaExemplo(None)#cria uma janela que extende wx.Frame
	app.MainLoop()#inicia loop principal do aplicativo

main()#executa metodo main()