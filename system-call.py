'''Uma system call é o intermedio entre o usúario e o núcleo,
é ele que retora um programa precisa acessar funcionalidades que estão além do seu próprio escopo, 
ele faz uma chamada de sistema para o núcleo e ele executa a ação requisitada em seu nome. Exemplo:'''

import os

# Executa o comando "dir" no Windowns que serve para mostrar um conteúdo de uma pasta
os.system("dir")
