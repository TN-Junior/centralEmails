from pathlib import Path
import streamlit as st

PASTA_ATUAL = Path(__file__).parent
PASTA_TEMPLATES = PASTA_ATUAL / 'templates'
PASTA_LISTA_EMAILS = PASTA_ATUAL / 'lista_email'


if not 'pagina_central_email' in st.session_state:
  st.session_state.pagina_central_email = 'home'

def mudar_pagina(nome_pagina):
  st.session_state.pagina_central_email = nome_pagina

def home():
  st.markdown('# Central de Emails')

def pag_templates():
  st.markdown('# Templates')

  st.button('Adicionar Template', on_click=mudar_pagina, args=('adicionar_novo_template',))

def pag_adicionar_novo_template():
  nome_template = st.text_input('Nome do template:')
  texto_template = st.text_area('Escreva o texto do template', height=600)
  st.button('Salvar', on_click= salvar_template, args=(nome_template, texto_template))
  

def salvar_template(nome, texto):
  PASTA_TEMPLATES.mkdir(exist_ok=True)
  nome_arquivo = nome.replace(' ', '_').lower() + '.txt'
  with open(PASTA_TEMPLATES / nome_arquivo, 'w') as f:
    f.write(texto)
    mudar_pagina('templates')



def pag_lista_emails():
  st.markdown('# Lista Email')

  st.button('Adicionar Lista',on_click=mudar_pagina, args=('adicionar_nova_lista',))

def pag_adicionar_nova_lista():
  nome_lista = st.text_input('Nome da lista:')
  emails_lista = st.text_area('Escreva os emails separados por vírgula: ', height=600)
  st.button('Salvar', on_click= _salvar_lista, args=(nome_lista, emails_lista))

def _salvar_lista(nome, texto):
  PASTA_LISTA_EMAILS.mkdir(exist_ok=True)
  nome_arquivo = nome.replace(' ', '_').lower() + '.txt'
  with open(PASTA_LISTA_EMAILS / nome_arquivo, 'w') as f:
    f.write(texto)
    mudar_pagina('lista_emails')


def pag_configuracao():
  st.markdown('# Configurações')

def main():
  st.sidebar.button('Central de Emails', use_container_width=True, on_click=mudar_pagina, args=('home',))
  st.sidebar.button('Templates', use_container_width=True, on_click=mudar_pagina, args=('templates',))
  st.sidebar.button('Lista de Emails', use_container_width=True, on_click=mudar_pagina, args=('lista_emails',))
  st.sidebar.button('Configuração', use_container_width=True, on_click=mudar_pagina, args=('configuracao',))



if st.session_state.pagina_central_email == 'home':
  home()

elif st.session_state.pagina_central_email == 'templates':
  pag_templates()

elif st.session_state.pagina_central_email == 'adicionar_novo_template':
  pag_adicionar_novo_template()

elif st.session_state.pagina_central_email == 'lista_emails':
  pag_lista_emails()

elif st.session_state.pagina_central_email == 'adicionar_nova_lista':
  pag_adicionar_nova_lista()

elif st.session_state.pagina_central_email == 'configuracao':
  pag_configuracao()


main()