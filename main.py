import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import json
import charts as charts


st.set_page_config(page_icon='', layout='wide')

st.header('India EV Market (2001 - 2024)')
st.write("The purpose of the Indian EV Market Dashboard is to provide a comprehensive, interactive visualization of the electric vehicle landscape in India. By analyzing key metrics and trends within the EV market, this dashboard offers insights into EV adoption rates, market share, regional distributions, vehicle types, and growth patterns over time. This tool aims to support data-driven decision-making for stakeholders such as policymakers, industry analysts, and businesses, helping them understand market dynamics and identify emerging opportunities in India’s rapidly evolving EV sector.")

df = pd.read_csv('EV Maker by Place.csv')
df_ev_sales = pd.read_csv('ev_sales_by_makers_and_cat_15-24.csv')

# Sidebar for filters
st.sidebar.header("Filters")

# Filter by vehicle category with "Select All" option
categories = ["Select All"] + df_ev_sales['Cat'].unique().tolist()
selected_categories = st.sidebar.multiselect("Select Vehicle Category", categories, default=["Select All"])

# Filter data by selected categories
if "Select All" in selected_categories:
    filtered_data = df_ev_sales  # Select all categories
else:
    filtered_data = df_ev_sales[df_ev_sales['Cat'].isin(selected_categories)]

# Get unique vehicle makers for the selected categories
vehicle_makers = filtered_data['Maker'].unique().tolist()

# Multiselect for Vehicle Makers with "Select All" functionality
vehicle_maker_selection = st.sidebar.multiselect(
    "Pick Vehicle Maker", 
    options=["Select All"] + vehicle_makers, 
    default=["Select All"]
)

# Implement "Select All" functionality for vehicle makers
if "Select All" in vehicle_maker_selection:
    selected_makers = vehicle_makers  # Select all makers
else:
    selected_makers = vehicle_maker_selection  # Select specific makers

# Filter data based on selected makers
filtered_data = filtered_data[filtered_data['Maker'].isin(selected_makers)]

# Optional checkbox to show or hide the filtered data table
show_data = st.sidebar.checkbox("Show Sales Data for Selected Makers", value=False)

if show_data:
    st.write(f"### {', '.join(selected_categories)} Sales Data for Selected Makers")
    st.dataframe(filtered_data)


charts.plot_ev_makers_by_state(df)

charts.plot_ev_makers_by_city(df)



df_ev_growth = df_ev_sales[['2015','2016','2017','2018','2019','2020','2021','2022','2023','2024']]

charts.plot_ev_sales_growth(df_ev_sales)

year = st.selectbox(label='Select Year of Sales', options=['2015','2016','2017','2018','2019','2020','2021','2022','2023','2024'], placeholder='Choose an year')

if year:
    filtered_df = df_ev_sales[['Maker' , year]]
    filtered_df = filtered_df.groupby('Maker')[year].sum().to_frame('Total Sales').sort_values(by='Total Sales', ascending=False).reset_index()
    chart = alt.Chart(filtered_df.head(20)).mark_bar(color='#880808').encode(
    x=alt.X('Maker', sort=None),  # Keeps the sorted order
    y='Total Sales'
    ).properties(
    title=f'Top 20 EV Manufacturer (Sales) for {year}',
    padding={'left': 10, 'right': 10, 'top': 10, 'bottom': 10}
    )
    st.altair_chart(chart, use_container_width=True)

df_charging_station = pd.read_csv('OperationalPC.csv')
with open('Indian_States.json','r') as f:
    geojson_data = json.load(f)
# Inspect the GeoJSON data to find the key for state names
st.write(geojson_data['features'][0]['properties'])

fig = px.choropleth(
    df_charging_station,
    locations='State',  # Column in df representing states
    locationmode='geojson-id',  # Use 'geojson-id' for locationmode
    color='No. of Operational PCS',  # Column in df for color scale
    hover_name='State',  # Display state name on hover
    geojson=geojson_data,  # GeoJSON data for the map
    labels={'No. of Operational PCS': 'Operational PCS'},  # Label for the color legend
    title="Distribution of Charging Stations Across States in India"
)

fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

st.plotly_chart(fig)

st.dataframe(df_vehicle_class.dtypes)


