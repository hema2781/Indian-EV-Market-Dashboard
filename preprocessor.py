import pandas as pd
from datetime import datetime

#EV Maker, City & State Database
def ev_maker():
    return pd.read_csv('./assets/datasets/EV Maker by Place.csv')

#YOY EV sales by category Database
def ev_sales():
    return pd.read_csv('./assets/datasets/ev_sales_by_makers_and_cat_15-24.csv')

#Operational charging stations Database
def charging_station():
    df_charging_station = pd.read_csv('./assets/datasets/OperationalPC.csv')
    df_charging_station['State']= df_charging_station['State'].astype('str')
    return df_charging_station

#EV sales category by date
def ev_cat_date():
    df_ev_cat_date = pd.read_csv('./assets/datasets/ev_cat_01-24.csv')
    df_ev_cat_date=df_ev_cat_date.drop(0)
    df_ev_cat_date['Date'] = pd.to_datetime(df_ev_cat_date['Date'], format='mixed')
    df_ev_cat_date['Year'] = df_ev_cat_date['Date'].dt.year
    return df_ev_cat_date

#Total registered EVs
def ev_reg():
    df_ev_reg = pd.read_csv('./assets/datasets/Vehicle Class - All.csv')
    df_ev_reg['Total Registration'] = df_ev_reg['Total Registration'].str.replace(',','')
    df_ev_reg['Total Registration'] = pd.to_numeric(df_ev_reg['Total Registration'])
    df_ev_reg = df_ev_reg.sort_values(by='Total Registration', ascending=False)
    return df_ev_reg