"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";",index_col=0)
    df = df.copy()

    df.dropna(inplace=True)
    
    df = df.apply(lambda x: x.astype(str))
    df = df.apply(lambda x: x.str.lower () if x.dtype=="objetc" else x)
    df = df.apply(lambda x: x.str.replace("$", "")) 
    df = df.apply(lambda x: x.str.replace(",", "")) 
    df = df.apply(lambda x: x.str.replace("-", " ") if x.dtype == "object" else x) 
    df = df.apply(lambda x: x.str.replace("_", " ") if x.dtype == "object" else x)  
    df = df.apply(lambda x: x.str.replace("  ", " " ) if x.dtype == "object" else x)

    df ['monto_del_credito'] = df['monto_del_credito'].astype(float)
    df ['fecha_de_beneficio'] = pd.tp_datetime(df['fecha_De_beneficio'], dayfirst=True, format = 'mixed')

    df.drop_duplicates(inplace=True)
    return df
