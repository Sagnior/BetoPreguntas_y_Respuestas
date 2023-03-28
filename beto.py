# Importar
import streamlit as st
from string import hexdigits
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline  #importamos los módulos que usaremos
from textwrap import wrap # esto es para que nos muestre el texto en forma de párrafos de muchas lineas en vez de que muestre todo el texto en una sola linea y no pueda caber en la pantalla

the_model = 'mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es' #el link del modelo de huggingface que vamos a usar
tokenizer = AutoTokenizer.from_pretrained(the_model, do_lower_case=False) #separador y convertidor de palabras a números
model = AutoModelForQuestionAnswering.from_pretrained(the_model) #seleccionando el caso de uso a aplicar el modelo, en este caso es el QuestionAnswering
nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)

def pregunta_respuesta(model, contexto, nlp):
    
    col1,col2 = stcolumns(2)
    # Imprimir contexto
    col1.header("Contexto")
    col1.body(st.write(wrap(contexto)))
    #print('\n'.join())

    col1 = st.column(1)
    # Loop preguntas-respuestas:
    continuar = True
    while continuar:
        print('\nPregunta:')
        print('-----------------')
        pregunta = str(input())

        continuar = pregunta!=''

        if continuar:
            salida = nlp({'question':pregunta, 'context':contexto})
            
            col2.st.write(salida['answer'])


contexto = st.text_area("Dame un párrafo", height=275)


pregunta_respuesta(model, contexto, nlp)

