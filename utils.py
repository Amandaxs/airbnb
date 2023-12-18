"""Funções úteis para a análise dos dados do airbnb"""
import numpy as np
import pandas as pd
import plotnine as ptn
from plotnine import ggplot
from sklearn.metrics import mean_squared_error, r2_score,mean_absolute_error

def convert_latitude_ou_longitude(val:float,tipo:str) -> float:
    """_summary_

    Args:
        val (float): valor a ser convertido
        tipo (str): 'lat' para latitude, 'long' para longitude

    Raises:
        ValueError: Erro caso o tipo a ser convetido não seja 'lat' ou 'long'

    Returns:
        float: valor convertido
    """
    if tipo == 'lat':
        digitos = 2
    elif tipo == 'long':
        digitos = 3
    else:
        raise ValueError("O tipo especificado deve ser 'lat' ou 'long")
    sinal = 1 if val >=0 else -1
    int_val = int(abs(val))
    val_str = str(int_val)
    val_formatado = f"{val_str[:digitos]}.{val_str[digitos:]}"
    val_final = float(val_formatado) * sinal
    if tipo == 'lat' and not -90 <= val_final <= 90:
        return np.nan
    elif tipo == 'long' and not -180 <= val_final <= 180:
        return np.nan
    else:
        return val_final

def tabela_descritiva(var1:str,
                      var2:str,
                      df:pd.DataFrame,
                      precisao = 2,
                      drop_na = False,
                      mult = 1) -> pd.DataFrame :
    """_summary_

    Args:
        var1 (str): variável da qual queremos ver a distribuição
        var2 (str): variável de agrupamento
        df (pd.DataFrame): data rame onde as colunas estção contidas
        precisao (int, optional): numero de casas decimais. Defaults to 2.
        drop_na (bool, optional): Opção para desconsiderar dados faltantes. Defaults to False.
        mult (int, optional): Fator multiplicativo. Defaults to 1.

    Returns:
        pd.DataFrame: Tabela descritiva final
    """

    visu= pd.concat([round(df[var1].groupby(df[var2],dropna=drop_na).agg(['count'])),
    round(df[var1].groupby(df[var2],dropna=drop_na).agg(['count'])
    /df[var1].groupby(df[var2],dropna=drop_na).agg(['count']).sum()*100,2),
    round(df.groupby(var2,dropna=drop_na)[var1].mean()*mult,precisao),
    round(df.groupby(var2,dropna=drop_na)[var1].std()*mult,precisao),
    round(df.groupby(var2,dropna=drop_na)[var1].min()*mult,precisao),
    round(df.groupby(var2,dropna=drop_na)[var1].quantile(0.1)*mult,precisao),
    round(df.groupby(var2,dropna=drop_na)[var1].quantile(0.2)*mult,precisao),
    round(df.groupby(var2,dropna=drop_na)[var1].quantile(0.3)*mult,precisao),
    round(df.groupby(var2,dropna=drop_na)[var1].quantile(0.4)*mult,precisao),
    round(df.groupby(var2,dropna=drop_na)[var1].median()*mult,precisao),
    round(df.groupby(var2,dropna=drop_na)[var1].quantile(0.6)*mult,precisao),
    round(df.groupby(var2,dropna=drop_na)[var1].quantile(0.7)*mult,precisao),
    round(df.groupby(var2,dropna=drop_na)[var1].quantile(0.8)*mult,precisao),
    round(df.groupby(var2,dropna=drop_na)[var1].quantile(0.9)*mult,precisao),
    round(df.groupby(var2,dropna=drop_na)[var1].max()*mult,precisao)],
    axis=1, ignore_index = drop_na)
    columns = (['n', '%','Média','Desvio','Min',"10%","20%","30%",
                "40%",'Mediana',"60%","70%","80%","90%",'Max'])
    visu.columns = columns


    return visu

def boxplot_comparativo(df:pd.DataFrame,
                       valores: str,
                       categorias:str,
                       ylim: float = None,
                       rotation:float = 0)-> ptn.ggplot:
    """_summary_

    Args:
        df (pd.DataFrame): Data frame que contém os dados
        valores (str): Coluna do valor numérico
        categorias (str): Coluna do valor categórico
        ylim (float): limite para o valor y 

    Returns:
        ptn.ggplot: _description_
    """
    titulo = f"distribuição de: {valores} por {categorias}"
    if ylim:
        return (ggplot(df, ptn.aes(x = categorias, y = valores, fill= categorias))
        +ptn.geom_boxplot()
        + ptn.scale_fill_brewer(type="qual", palette="Set3")
        + ptn.coord_cartesian(ylim=(0,ylim))
        + ptn.labs(title = titulo)
        + ptn.theme_classic()
        + ptn.theme(legend_position='none',
                      axis_text_x=ptn.element_text(rotation= rotation, hjust= 1))
        )
    else:
        return (ggplot(df, ptn.aes(x = categorias, y = valores, fill= categorias))
        +ptn.geom_boxplot()
        + ptn.scale_fill_brewer(type="qual", palette="Set3")
        + ptn.labs(title = titulo)
        + ptn.theme_classic()
        + ptn.theme(legend_position='none',
                      axis_text_x=ptn.element_text(rotation= rotation, hjust= 1))
        )


def grafico_dispersao(df:pd.DataFrame,
                       valor1: str,
                       valor2:str)-> ptn.ggplot:
    """_summary_

    Args:
        df (pd.DataFrame): Data frame que contém os dados
        valor1 (str): eixo x do grafico
        valor2 (str): eixo y do grafico


    Returns:
        ptn.ggplot: diagrama de dispersãoe ntre os eixos x e y
    """
    titulo = f"distribuição de: {valor1} por {valor2}"

    return (ggplot(df, ptn.aes(x = valor1, y = valor2))
        +ptn.geom_point()
        + ptn.coord_cartesian(xlim=(0,2000))
        + ptn.theme_classic()
        +ptn.labs(title = titulo)
        )

def preenche_na(row: pd.Series, col: str, col_condition: str) -> float:
    """_summary_

    Args:
        row (pd.Series): _description_
        col (str): _description_
        col_condition (str): _description_

    Returns:
        float: _description_
    """
    if not pd.isna(row[col]):
        return row[col]
    if pd.isna(row[col]) and row[col_condition] == 'Shared room':
        return 2
    else:
        return 1


def registro_metricas(model_name: str,
                    df_init: pd.DataFrame,
                    y_test: pd.Series,
                    y_pred:pd.Series,
                    best_param:str) -> pd.DataFrame:
    """_summary_

    Args:
        model_name (str): Nome do modelo a ser registrado
        df_init (pd.DataFrame): Data frame com os modelos ja salvos
        y_test (pd.Series): Y teste
        y_pred (pd.Series): Y prdito
        best_param (str): Melhores paremetros encontrados no processo de treinamendo do modelo

    Returns:
        pd.DataFrame:  Novo data frame coma inclusão do novo modelo
    """
    df = df_init.copy()
    mse = mean_squared_error(y_test, y_pred)
    data = {
        'model': model_name,
        'params':best_param,
        'mse':mse,
        'rmse':np.sqrt(mse),
        'mae':mean_absolute_error(y_test, y_pred),
        'r2':r2_score(y_test, y_pred)
    }
    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    return df
