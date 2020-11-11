# TPLPV
Repositório para apresentação do Trabalho da disciplina Linguagem de Programação Visual

Wx Python

  Wxpython é um kit de ferramentas Open Source que permite criação de interface gráfica de usuário com a linguagem python utilizando o Wxwidgets, que é escrita em C++.
	Esse kit e ferramentas permite a programadores Python criarem em seus programas uma interface gráfica de usuário robusta, funcional de forma simples e fácil, implementado como um conjunto de módulos de extensão python que empacotam os componentes da Wxwidgets.
	WxPython é multiplataforma o que permite que o mesmo programa seja executado em várias plataformas sem a necessidade de alguma modificação, de acordo com o site da comunidade https://www.wxpython.org/, atualmente suportadada pelas plataformas, Microsoft Windows, Mac OS X e mac OS, e Linux ou sistemas semelhantes ao Unix  com bibliotecas GTK2 ou GTK3.
	WxPython Phoenix é o projeto de uma implementação totalmente nova do wxPython, a intenção é torná-la melhor, mais forte e mais rápida do que antes, a implementação está focada em desempenho, estabilidade e manutenção assim como remover alguns lixos acumulados ao longo dos anos, sendo assim intencionalmente wxPython Phoenix não é totalmente compativel com o wxPython Classic. O projeto está em andamento e para mais informações pode-se acessar o guia de migração https://docs.wxpython.org/MigrationGuide.html.
	Voltando ao wxPython clássico ele é tão simples quanto a linguagem python, comandos simples, fáceis de entender e de escrever, abaixo um exemplo de HelloWorld.
Importa o pacote wxPython.
import wx

#Cria um objeto de aplicativo.

app = wx.App()

#Cria um quadro.

frm = wx.Frame(None, title="Olá, mundo" )

#Mostrar.

frm.Show()

#Inicia o loop de eventos.

app.MainLoop()

Desta forma simples já geramos nossa primeira GUI, porém como 5 linhas de código podem parecer muita coisa então vai o exemplo em 1 só linha:

import wx; a=wx.App(); wx.Frame(None, title="Hello World").Show(); a.MainLoop()

A portabilidade é a maior vantagem da wxPython qualquer aplicação tem uma aparência nativa da plataforma na qual está sendo utilizada, isto acontece com o acréscimo de uma camada extra entre a aplicação e o SÓ o que causa uma queda altíssima de desempenho. Abaixo as vantagens e desvantagens de se utilizar wxPython.
Vantagens:
Portabilidade: Aplicações escritas em wxPython rodam praticamente sem problemas em várias plataformas o que provavelmente está a deixando bem popular.
Componentes ricos - Nesse ponto a wxPython é imbatível, possuir todo tipo de componente, desde telas até caixas de texto que interpretam HTML e até mesmo a Scintilla que é uma biblioteca que fornece uma função de componente de edição de texto que utiliza recursos avançados de edição de código fonte.
Documentação: O wxPython vem com um demo da maioria dos seus widgets que serve como teste de exemplo de uso.
Disponibilidade: Existem diversos construtores GUI disponíveis apesar da maioria serem ferramentas comerciais
Desvantagens:
Desempenho: A performance não é ruim porém utiliza muita memória e o tempo de inicialização é alto.
Instabilidade: Mesmo em constante aprimoramento ainda possui problemas de estabilidade .
Aprendizado: Inicialmente muitas pessoas têm grandes dificuldades mas ao se acostumar percebe-se a facilidade de criar componentes.
Documentação: Apesar dos diversos exemplos de uso, nem todos os componentes são descritos completamente o que causa a dificuldade de alguns novos usuários.
Construtores: Possui muitos construtores livres, porém as melhores ferramentas são comerciais e os livres não possuem a mesma qualidade de ide.

Instalação
	A instalação é simples, no windows a instalação é simples possuindo o instalador no modo janela assim como os usuários do windows estão acostumados Utilizando o comando pip install -U wxPython, e no GNU/Linux - Debian ele pode ser instalado por meio do apt-get e também do pip, por meio de um comando como este a seguir: pip install -U \
    -f https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-16.04 \
    wxPython,dependendo da plataforma utilizada os passos são diferentes e não cabe aqui listar cada um deles, na pagina https://wiki.wxpython.org/How%20to%20install%20wxPython podemos encontrar maiores informações;
    
Componentes Básicos
Frame a linha abaixo cria uma janela wx.Frame
frm = wx.Frame(None, Title=”HelloWorld”)

Botão
wxButton é um botão é um controle que contém uma string de texto, pode ser colocado em quase qualquer janela, os parâmetros que pode fazer parte da criação de um botão são (1- janela pai do componente, 2- id do componente para futura identificação, 3- texto a ser apresentado, 4- Posição do componente, 5- tamanho do componente, 6- Estilo do componente):
Linha abaixo representa a criação de um frame e a inserção de um botao nesse frame.
bt_Exemplo = wx.Button(frm, 1, "Botão", wx.DefaultPosition, wx.DefaultSize, 0 )

Vincula um evento a um manipulador de eventos(botao). O wx.EVT_BUTTON evento é acionado quando clicamos no botão. Especificamos o evento a ser acionado como segundo parâmetro.
bt_Exemplo.Bind (wx.EVT_BUTTON, self.FechaTela)


Caixa para entrada de texto
	wx.TextCtrl é um controle de texto permite que o texto seja exibido e editado, pode ser apresentado em linha única ou múltiplas linhas. A linha a baixo cria um componente wx.TextCtrl de apenas uma linha com uma string vazia wx.EmptyString e o adiciona no layout, a constante wx.TE_PROCESS_ENTER deve ser adicionada para a conexão com o evento wx.EVT_TEXT_ENTER
txt_Exemplo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER ) 
Para criar uma entrada de texto de múltiplas linhas utilize a constante de estilo wx.TE_MULTILINE
txt_MultExemplo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,150 ), wx.TE_MULTILINE )
	
Para obter o valor escrito na entrada de texto usamos o método GetValue()
	esse método retorna uma string com o valor escrito na caixa de texto.
str = txt_Exemplo.GetValue()

	Evento Tecla Enter no input
	Cria um evento relacionado a ação enter no campo de texto Vincula um evento a um manipulador de eventos(wx.TE_PROCESS_ENTER) O wx.EVT_TEXT_ENTER evento é acionado quando apertamos enter em um componente de texto. Especificamos o evento a ser acionado como segundo parâmetro.
txt_Exemplo.Bind( wx.EVT_TEXT_ENTER, self.AcaoEnter)
		
Label de texto
wx.StaticLine este widget exibe uma linha simples na janela. Pode ser horizontal ou vertical. A linha abaixo cria um wx.StaticText para exibição de um rótulo na tela.
self.lbl_Exemplo = wx.StaticText( self, wx.ID_ANY, "Texto 1", wx.DefaultPosition, wx.DefaultSize, 0 )

Radio button
wx.RadioButton é um widget que permite ao usuário selecionar uma única escolha exclusiva de um grupo de opções. Um grupo de botões de opção é definido por ter o primeiro botão de opção do grupo contendo o wx.RB_GROUP estilo. Todos os outros botões de opção definidos após o primeiro botão de opção com este sinalizador de estilo serão adicionados ao grupo de funções do primeiro botão de opção. Declarar outro botão de opção com o wx.RB_GROUP sinalizador iniciará um novo grupo de botões de opção.
A linha abaixo cria um wx.RadioButton iniciando um grupo de botões de opção.
rb_Exemplo = wx.RadioButton( self, wx.ID_ANY, "Texto 1", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )

Para obter o rótulo do RadioButton utilizamos o metodo GetLabel()
str = rb_Exemplo.GetLabel()

Cria o evento e vincula o wx.EVT_RADIOBUTTON evento ao manipulador de eventos no caso rb1Marcado().
rb_Exemplo.Bind( wx.EVT_RADIOBUTTON, self.rb1Marcado)


CheckBox 
	A wx.CheckBox é um widget que possui dois estados: ligado e desligado. É uma caixa com uma etiqueta. O rótulo pode ser colocado à direita ou à esquerda da caixa. Se a wx.CheckBox estiver marcado, ele é representado por uma marca em uma caixa. A linha abaixo apresenta a criação de um wx.CheckBox
cb_Exemplo = wx.CheckBox( self, wx.ID_ANY, "Ativa Lista Suspensa", wx.DefaultPosition, wx.DefaultSize, 0 )

O método utilizado para saber se o CheckBox está ativo ou não é o GetValue() caso ativo retorna True senão retorna False
cb_Exemplo.GetValue()

Cria o evento e vincula owx.EVT_CHECKBOX evento ao manipulador de eventos AtivaLista().
cb_Exemplo.Bind( wx.EVT_CHECKBOX, self.AtivaLista )



Lista Suspensa
	O wx.Choice é uma combinação de um campo de texto de linha única, um botão com uma imagem de seta para baixo e uma caixa de listagem. Quando você pressiona o botão, uma caixa de listagem é exibida. Um usuário pode selecionar apenas uma opção da lista de strings. A linha a seguir apresenta a criação de um componente Choice
cb_Exemplo = wx.CheckBox( self, wx.ID_ANY, "Ativa Lista Suspensa", wx.DefaultPosition, wx.DefaultSize, 0 )

O metodo GetString(int) retorna a string representada em uma determinada posição da lista. O metodo GetCurrentSelection() retorna a posição de seleção da lista
str = cb_Exemplo.GetString(cb_Exemplo.GetCurrentSelection())

Vincula owx.EVT_CHECKBOX evento ao manipulador de eventos AtivaLista().
cb_Exemplo.Bind( wx.EVT_CHECKBOX, self.AtivaLista )


Slider
 	O wx.Slider contém uma alça pode ser puxada para frente e para trás. Assim podemos escolher um valor específico. A seguir linha de codigo com criação de um wx.Slider
sl_Exemplo = wx.Slider( self, wx.ID_ANY, 8, 1, 16, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )

O slider utiliza o método GetValue() para obter o valor selecionado no objeto.
sl_Exemplo.GetValue()

O wx.EVT_SCROLL evento é acionado e quando o valor no slider é alterado. O SliderActive() manipulador de eventos é chamado neste evento.
sl_Exemplo.Bind( wx.EVT_SCROLL, self.SliderActive )


No Exemplo de janela presente nos arquivos com componentes e eventos ativos podemos entender melhor o funcionamento de cada um deles. Na janela criada ao digitar um texto na caixa de texto de uma única linha e apertar ‘Enter’ o texto é exibido na caixa de múltiplas linhas, ao selecionar um dos componentes wx.RadioButton o rótulo do radiobutton é apresentado no componente wx.StaticText acima, ao selecionar a caixa de seleção o componente wx.Choice é liberado para uso, e ao clicar escolher um item na lista o texto escrito é adicionado ao rótulo do wx.STaticText abaixo da lista, ao deslizar o slider o tamanho da fonte do componente wx.StaticText acima do slider é alterado de acordo com o valor do slider e por fim ao clicar no botão a tela é fechada.
