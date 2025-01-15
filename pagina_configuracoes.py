import streamlit as st
from utilidades import *

def pag_configuracao():
  st.markdown('# Configurações')
  email = st.text_input('Digite seu email:')
  st.button('Salvar', key='salvar_email', 
                      on_click=_salvar_email,
                      args=(email, ))
  chave = st.text_input('Digite sua chave de email:')
  st.button('Salvar', key='salvar_chave',
                      on_click=_salvar_chave,
                      args=(chave, ))

def _salvar_email(email):
  PASTA_CONFIGURACOES.mkdir(exist_ok=True)
  with open(PASTA_CONFIGURACOES / 'email_usuario.txt', 'w') as f:
    f.write(email)


def _salvar_chave(chave):
  PASTA_CONFIGURACOES.mkdir(exist_ok=True)
  with open(PASTA_CONFIGURACOES / 'chave.txt', 'w') as f:
    f.write(chave)

def le_email_usuario():
  PASTA_CONFIGURACOES.mkdir(exist_ok=True)
  if (PASTA_CONFIGURACOES / 'email_usuario.txt').exists():
     with open(PASTA_CONFIGURACOES / 'email_usuario.txt', 'r') as f:
        return f.read()
  return ''

def le_chave_usuario():
  PASTA_CONFIGURACOES.mkdir(exist_ok=True)
  if (PASTA_CONFIGURACOES / 'chave.txt').exists():
     with open(PASTA_CONFIGURACOES / 'chave.txt', 'r') as f:
        return f.read()
  return ''