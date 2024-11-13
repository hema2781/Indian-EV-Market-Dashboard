import altair as alt
import streamlit as st
import pandas as pd

def plot_ev_makers_by_state(df):
    state_ev_maker = df.groupby('State')['EV Maker'].count().to_frame('Total Manufacturing Plants').sort_values(by='Total Manufacturing Plants', ascending=True).reset_index()
    chart = alt.Chart(state_ev_maker).mark_bar(color='#880808').encode(
        x=alt.X('State', sort=None),
        y='Total Manufacturing Plants'
    ).properties(
        title='Total Manufacturing Plants by State',
        padding={'left': 10, 'right': 10, 'top': 10, 'bottom': 10}
    )
    st.altair_chart(chart, use_container_width=True)

def plot_ev_makers_by_city(df):
    city_ev_maker = df.groupby('Place')['EV Maker'].count().to_frame('Total Manufacturing Plants').sort_values(by='Total Manufacturing Plants', ascending=True).reset_index()
    chart = alt.Chart(city_ev_maker).mark_bar(color='#880808').encode(
        x=alt.X('Place', sort=None),
        y='Total Manufacturing Plants'
    ).properties(
        title='Total Manufacturing Plants by City',
        padding={'left': 10, 'right': 10, 'top': 10, 'bottom': 10}
    )
    st.altair_chart(chart, use_container_width=True)

def plot_ev_sales_growth(df_ev_sales):
    df_ev_growth = df_ev_sales[['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']].sum().reset_index()
    df_ev_growth.columns = ['Year', 'Total EV Sales']
    st.line_chart(df_ev_growth.set_index('Year'), x_label='Years', y_label='Total EV Sales', color=['#880808'])
