"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    import pandas as pd
    import os
    
    df = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";", index_col=0)

    df = df.dropna()
    df = df.drop_duplicates()

    df['sexo'] = df['sexo'].str.lower()
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower()
    df['idea_negocio'] = df['idea_negocio'].str.lower().map(lambda x: x.replace("_", " ").replace("-", " ").strip())
    df['barrio'] = df['barrio'].str.lower().map(lambda x: x.replace("_", " ").replace("-", " "))
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].map(lambda x: pd.to_datetime(x, format='%d/%m/%Y') if '/' in x[:3] else pd.to_datetime(x, format='%Y/%m/%d'))
    df['monto_del_credito'] = df['monto_del_credito'].map(lambda x: int(x.replace(".00", "").replace(",", "").replace(" ", "").replace("$", "")))
    df['línea_credito'] = df['línea_credito'].str.lower().map(lambda x: x.replace("_", " ").replace("-", " ").strip())
    
    df = df.drop_duplicates()

    if not os.path.exists("files/output"):
        os.makedirs("files/output")
    df.to_csv("files/output/solicitudes_de_credito.csv", sep=';', index=False)

    return

pregunta_01()

