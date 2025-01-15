import streamlit as st
from utilidades import *


# ================ LISTAS DE EMAILS =================== 
def pag_lista_emails():
  st.markdown('# Lista Email')
  st.divider()
  for arquivo in PASTA_LISTA_EMAILS.glob('*.txt'):
    nome_arquivo = arquivo.stem.replace('_', ' ').upper()
    col1, col2, col3 = st.columns([0.6, 0.2, 0.2])
    col1.button(nome_arquivo, key=f'{nome_arquivo}',
                              use_container_width=True,
                              on_click=_usa_lista,
                              args=(nome_arquivo, ))
    col2.button('EDITAR', key=f'editar_{nome_arquivo}', 
                          use_container_width=True,
                          on_click=_editar_lista,
                          args=(nome_arquivo,))
    col3.button('REMOVER', key=f'remover_{nome_arquivo}',
                              use_container_width=True,
                              on_click=_remove_lista,
                              args=(nome_arquivo, ))
    
  st.divider()
  st.button('Adicionar Lista',on_click=mudar_pagina, args=('adicionar_nova_lista',))

def pag_adicionar_nova_lista(nome_lista='', emails_lista=''):
  nome_lista = st.text_input('Nome da lista:', value=nome_lista)
  emails_lista = st.text_area('Escreva os emails separados por vírgula:', value=emails_lista, height=600)
  st.button('Salvar', on_click= _salvar_lista, args=(nome_lista, emails_lista))

def _usa_lista(nome):
  nome_arquivo = nome.replace(' ', '_').lower() + '.txt'
  with open(PASTA_LISTA_EMAILS / nome_arquivo) as f:
    texto_arquivo = f.read()
  st.session_state.destinatarios_atual = texto_arquivo
  mudar_pagina('home')


def _salvar_lista(nome, texto):
  PASTA_LISTA_EMAILS.mkdir(exist_ok=True)
  nome_arquivo = nome.replace(' ', '_').lower() + '.txt'
  with open(PASTA_LISTA_EMAILS / nome_arquivo, 'w') as f:
    f.write(texto)
    mudar_pagina('lista_emails')

def _remove_lista(nome):
  nome_arquivo = nome.replace(' ', '_').lower() + '.txt'
  (PASTA_LISTA_EMAILS / nome_arquivo).unlink()


def _editar_lista(nome):
  nome_arquivo = nome.replace(' ', '_').lower() + '.txt'
  with open(PASTA_LISTA_EMAILS / nome_arquivo) as f:
    texto_arquivo = f.read()
  st.session_state.nome_lista_editar = nome
  st.session_state.texto_lista_editar = texto_arquivo
  mudar_pagina('editar_lista')
