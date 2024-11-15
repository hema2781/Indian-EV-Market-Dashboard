import altair as alt
import streamlit as st
import pandas as pd
import plotly.express as px

def plot_ev_makers_by_state(df):
    state_ev_maker = df.groupby('State')['EV Maker'].count().to_frame('Total Manufacturing Plants').sort_values(by='Total Manufacturing Plants', ascending=False).reset_index()
    chart = alt.Chart(state_ev_maker).mark_bar().encode(
        x=alt.X('State', sort=None),
        y='Total Manufacturing Plants',
        color = alt.Color('Total Manufacturing Plants:Q',
                          scale=alt.Scale(scheme='reds'),
                                          legend=None)
    ).properties(
        title='Most Manufacturing Plants per State',
        padding={'left': 10, 'right': 10, 'top': 10, 'bottom': 10}
    )
    st.altair_chart(chart, use_container_width=True)

def plot_ev_makers_by_city(df):
    city_ev_maker = df.groupby('Place')['EV Maker'].count().to_frame('Total Manufacturing Plants').sort_values(by='Total Manufacturing Plants', ascending=False).reset_index()
    chart = alt.Chart(city_ev_maker.head(10)).mark_bar().encode(
        x=alt.X('Place', sort=None),
        y='Total Manufacturing Plants',
        color = alt.Color('Total Manufacturing Plants:Q',
                          scale=alt.Scale(scheme='reds'),
                                          legend=None)
    ).properties(
        title='Most Manufacturing Plants per City (Top 10)',
        padding={'left': 10, 'right': 10, 'top': 10, 'bottom': 10}
    )
    st.altair_chart(chart, use_container_width=True)

def plot_ev_sales_growth(df_ev_sales):
    # Prepare the data
    df_ev_growth = df_ev_sales[['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']].sum().reset_index()
    df_ev_growth.columns = ['Year', 'Total EV Sales']

    # Add a subheader in Streamlit
    st.subheader('All EV Sales YOY Growth')

    # Create the line chart
    fig = px.line(
        df_ev_growth,
        x='Year',
        y='Total EV Sales',
        labels={'Year': 'Years', 'Total EV Sales': 'Total EV Sales'}
    )
    # Customize the line's appearance
    fig.update_traces(
        line_color='#880808',  # Line color
        line_width=2,          # Set line width
        mode='lines+markers',  # Add markers at each data point
        marker=dict(size=8)    # Set marker size
    )

    # Display the Plotly chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)


def plot_yearly_sales_category(filtered_data, year_cols):
    yearly_sales_data = filtered_data.groupby('Cat')[year_cols].sum().reset_index()
    fig_yearly_sales = px.bar(yearly_sales_data.melt(id_vars='Cat', var_name='Year', value_name='Sales'),
                              x='Year', y='Sales', color='Cat')
    st.subheader("Yearly Sales by Category")
    st.plotly_chart(fig_yearly_sales)

def plot_top_makers(filtered_data, year_cols, year):
    # Prepare data for top manufacturers
    top_makers_data = filtered_data.groupby('Maker')[year_cols].sum().reset_index()
    top_makers_data['Total'] = top_makers_data[year_cols].sum(axis=1)
    top_makers_data = top_makers_data.sort_values('Total', ascending=False).head(10)
    
    # Capture the name of the top manufacturer
    top_maker_name = top_makers_data.iloc[0]['Maker']
    
    # Plot the bar chart with a gradient color
    fig_top_makers = px.bar(
        top_makers_data,
        x='Total',
        y='Maker',
        orientation='h',
        title=f"Top 10 Manufacturers in {year}",
        labels={'Total': 'Total Sales', 'Maker': 'Manufacturer'},
        color='Total',  # Use the 'Total' column for the gradient
        color_continuous_scale='Reds'  # Apply a red gradient
    )
    
    # Display the chart in Streamlit
    st.plotly_chart(fig_top_makers)
    
    return top_maker_name  # Return the top manufacturer's name



def plot_top_market_share(df_ev_sales, selected_maker,year):
    filtered_data = df_ev_sales[df_ev_sales['Maker'] == selected_maker]

    # Group by category and sum sales
    sales_by_category = filtered_data.groupby('Cat').sum().drop(columns=['Maker']).reset_index()

    # Bar plot for categories
    fig = px.bar(
        sales_by_category,
        x='Cat',
        y=year,
        title=f"Market Share of {selected_maker} in {year}",
        labels={'Cat': 'Vehicle Category', year: 'Sales'},
        color='Cat'
    )
    st.plotly_chart(fig)


def ev_cat_reg(df_ev_reg):
    chart = alt.Chart(df_ev_reg).mark_bar().encode(
    x=alt.X('Total Registration:Q', title='Total Registration'),
    y=alt.Y('Vehicle Class', sort=None, title='Vehicle Class'),
    color=alt.Color(
        'Total Registration:Q',
        scale=alt.Scale(scheme='reds'),
        legend=None
        )   
    ).properties(
    title='Total Registration of Each Category',
    padding={'left': 10, 'right': 10, 'top': 10, 'bottom': 10},
    height=475
    )
    st.altair_chart(chart, use_container_width=True)


def ev_cat_growth(df_ev_cat_date,selected_cat):
    filtered_df_cat = df_ev_cat_date.groupby('Year')[selected_cat].sum().to_frame('Total Registration').sort_values(by='Year', ascending = False).reset_index()
    chart = alt.Chart(filtered_df_cat).mark_bar().encode(
    x=alt.X('Year:N', title='Year'),
    y=alt.Y('Total Registration:Q', title='Total Registration'),
    color=alt.Color('Total Registration:Q', 
                    scale=alt.Scale(scheme='reds'), 
                    legend=None)  # Apply red gradient and hide legend
    ).properties(
    title=f"YOY Growth of {selected_cat}",
    width='container',  # Adjusts to container width
    height=400  # Optional: Set chart height
    )

    # Display the chart in Streamlit
    st.altair_chart(chart, use_container_width=True)



def india_map_plot(df_charging_station,india_states):
    fig = px.choropleth(df_charging_station, 
                    locations='id', 
                    geojson=india_states, 
                    color='No. of Operational PCS', 
                    hover_name=df_charging_station['State'],
                    hover_data=['No. of Operational PCS'])

    fig = px.choropleth_mapbox(df_charging_station, 
                    locations='id', 
                    geojson=india_states, 
                    color='No. of Operational PCS', 
                    hover_name=df_charging_station['State'],
                    hover_data={'id': False, 'No. of Operational PCS': True},
                    mapbox_style='carto-positron',
                    center={"lat": 20.5937, "lon": 78.9629},
                    zoom=3.5,
                    height=800,
                    color_continuous_scale=[

                        [0.0, "#FFEEEE"],   # Very light red (almost white)
                        [0.2, "#FF9999"],   # Light red
                        [0.4, "#FF5555"],   # Medium red
                        [0.6, "#FF0000"],   # Bright red
                        [0.8, "#B20000"],   # Dark red
                        [1.0, "#660000"]    # Very dark red
                        ]
                    )

    fig.update_geos(fitbounds='locations', visible=False)

    st.plotly_chart(fig)