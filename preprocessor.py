import pandas as pd
from datetime import datetime

def ev_maker():
    return pd.read_csv('EV Maker by Place.csv')


def ev_sales():
    return pd.read_csv('ev_sales_by_makers_and_cat_15-24.csv')

def charging_station():
    df_charging_station = pd.read_csv('OperationalPC.csv')
    df_charging_station['State']= df_charging_station['State'].astype('str')
    return df_charging_station

def ev_cat_date():
    df_ev_cat_date = pd.read_csv('ev_cat_01-24.csv')
    df_ev_cat_date=df_ev_cat_date.drop(0)
    df_ev_cat_date['Date'] = pd.to_datetime(df_ev_cat_date['Date'], format='mixed')
    df_ev_cat_date['Year'] = df_ev_cat_date['Date'].dt.year
    return df_ev_cat_date

def ev_reg():
    df_ev_reg = pd.read_csv('Vehicle Class - All.csv')
    df_ev_reg['Total Registration'] = df_ev_reg['Total Registration'].str.replace(',','')
    df_ev_reg['Total Registration'] = pd.to_numeric(df_ev_reg['Total Registration'])
    df_ev_reg = df_ev_reg.sort_values(by='Total Registration', ascending=False)
    return df_ev_reg