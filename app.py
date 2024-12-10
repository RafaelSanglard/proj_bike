import pandas as pd
import streamlit as st

import src.answers as asw
from src.extraction import load_data

st.set_page_config(layout="wide")


def create_dataframe_section(df):
    st.title("Database - Descrição")

    col_1, col_2 = st.columns(2)

    col_1.header("Database")
    col_1.dataframe(df, height=530)

    col_2.header("Data Description")

    data_description = """
                        | Coluna | Descrição |
                        | :----- | --------: |
                        | ID | Identificador da linha/registro |
                        | name | Fabricante e Modelo da Moto |
                        | selling_price | Preço de Venda |
                        | year | Ano de Fabricação da Moto |
                        | seller_type | Tipo de Vendedor - Se é vendedor pessoal ou revendedor |
                        | owner | Se é primeiro, segundo, terceiro ou quarto dono da moto |
                        | km_driven | Quantidade de Quilometros percorrido pela moto |
                        | ex_showroom_price | Preço da motocicleta sem as taxas de seguro e registro |
                        | age | Quantidade de anos em que a moto está em uso |
                        | km_class | Classificação das motos conforme a quilometragem percorrida |
                        | km_per_year | Quantidade de Quilometros percorridos a cada ano |
                        | km_per_month | Quantidade de Quilometros percorridos por mês |
                        | company | Fabricanete da Motocicleta |
    """

    col_2.markdown(data_description)


def create_answers_section(df):
    st.title("Main Questions Answers")
    st.title("Principais Perguntas Respondidas")

    st.header("Primeira Rodada")
    st.subheader(
        "Quantas bicicletas estão sendo vendidas por seus proprietários e quantas bicicletas estão sendo vendidas por distribuidores?"
    )
    asw.rd1_question_9(df)

    st.subheader("Quantas bicicletas sendo vendidas são de um único proprietário?")
    asw.rd1_question_13(df)

    st.subheader(
        "Bicicletas com alta quilometragem são mais caras do que bicicletas com menor quilometragem?"
    )
    asw.rd1_question_14(df)

    st.subheader(
        "As bicicletas de um único proprietário são mais caras, em média, do que as outras bicicletas?"
    )
    asw.rd2_question_1(df)

    st.subheader(
        "As bicicletas que têm mais proprietários também são as bicicletas com mais quilômetros rodados, em média?"
    )
    asw.rd2_question_2(df)

    st.subheader("Qual empresa tem mais bicicletas registradas?")
    asw.rd2_question_7(df)

    st.subheader("Qual empresa tem as bicicletas mais caras, em média?")
    asw.rd3_question_2(df)

    st.subheader(
        "A empresa que tem as bicicletas mais caras registradas também é a empresa com mais bicicletas registradas?"
    )
    asw.rd3_question_5(df)

    st.subheader("Quais bicicletas são boas para comprar?")
    asw.rd3_question_7(df)



def create_main_layout():
    df = load_data()

    create_dataframe_section(df)

    create_answers_section(df)


if __name__ == "__main__":
    create_main_layout()
