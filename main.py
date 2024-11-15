import streamlit as st
import json
import charts as charts
import preprocessor

st.set_page_config(page_icon='analysis.ico', page_title='Indian EV Market', layout='wide')

col13,col14 = st.columns([1,4])
with col13:
    st.image('Indian EV Market Logo.svg', width=220, use_container_width=False)    
with col14:
    st.title('Indian EV Market (2001 - 2024)')
    st.write("The purpose of the Indian EV Market Dashboard is to provide a comprehensive, interactive visualization of the electric vehicle landscape in India. By analyzing key metrics and trends within the EV market, this dashboard offers insights into EV adoption rates, market share, regional distributions, vehicle types, and growth patterns over time. This tool aims to support data-driven decision-making for stakeholders such as policymakers, industry analysts, and businesses, helping them understand market dynamics and identify emerging opportunities in India’s rapidly evolving EV sector.")



df = preprocessor.ev_maker()

df_ev_sales = preprocessor.ev_sales()

df_charging_station = preprocessor.charging_station()

india_states = json.load(open('Indian_States.geojson', 'r'))

df_ev_cat_date = preprocessor.ev_cat_date()
df_ev_reg = preprocessor.ev_reg()


# KPI Section
total_sales = df_ev_sales.loc[:, '2015':'2024'].sum().sum()
top_year = df_ev_sales.loc[:, '2015':'2024'].sum().idxmax()
top_maker = df_ev_sales.groupby('Maker').sum().loc[:, '2015':'2024'].sum(axis=1).idxmax()

st.subheader("Overall EV Market Analysis")
col1, col2, col3 = st.columns(3)
col1.metric("Total EV Units Sold", f"{total_sales}")
col2.metric("Top Sales Year", top_year)
col3.metric("Top Manufacturer", top_maker)

col4, col5 = st.columns(2)

# Chart 1: EV Makers by State
with col4:
    charts.plot_ev_makers_by_state(df)

# Chart 2: EV Makers by City
with col5:
    charts.plot_ev_makers_by_city(df)

col6, col7 = st.columns(2)

# Chart 3: EV Sales Growth
with col6:
    charts.plot_ev_sales_growth(df_ev_sales)

# Chart 4: Yearly Sales by Category
with col7:
    year_cols = [col for col in df_ev_sales.columns if col.isdigit()]
    charts.plot_yearly_sales_category(df_ev_sales, year_cols)



# Filter for specific year selection and display the top 20 chart

st.header('Manufacturer Market Share (Year-on-Year)')
col8,col9 = st.columns(2)

with col8:
    year = st.slider(
    label='Select Year of Sales',
    min_value=2015,
    max_value=2024,
    value=2024,  # Default value when the app loads
    step=1
)
    if year:
        year = str(year)
        top_maker_name = charts.plot_top_makers(df_ev_sales, [year],year)  # Capture the top manufacturer name
with col9:
    top_makers_data = df_ev_sales.groupby('Maker')[[year]].sum().reset_index()
    top_makers_data = df_ev_sales.sort_values(by=year, ascending=False).head(10)
    top_makers_list = top_makers_data['Maker'].tolist()

    selected_maker = st.selectbox(
"Select a Manufacturer",
options=top_makers_list,
index=0
)

    charts.plot_top_market_share(df_ev_sales, selected_maker,year)  # Use the captured name



top_reg_cat = df_ev_reg.loc[df_ev_reg['Total Registration'].idxmax()]
top_reg_cat = top_reg_cat['Vehicle Class']
bot_reg_cat = df_ev_reg.loc[df_ev_reg['Total Registration'].idxmin()]
bot_reg_cat = bot_reg_cat['Vehicle Class']

# Display KPIs
st.header("Growth of EV by Vehicle Class")
col10, col11 = st.columns(2)

with col10:
    st.metric(label="Most Favourite Vehicle Class", value=top_reg_cat)

with col11:
    st.metric(label=f"Least Favourite Vehicle Class", value=bot_reg_cat)
    

col20, col21 = st.columns(2)

with col20:
    charts.ev_cat_reg(df_ev_reg)

with col21:
    selected_cat = st.selectbox('Select a Vehicle Category', options=df_ev_cat_date.columns[1:-1], index=14)
    charts.ev_cat_growth(df_ev_cat_date,selected_cat)



state_id_map = {}
for feature in india_states['features']:
    feature['id'] = feature['properties']['state_code']
    state_id_map[feature['properties']['st_nm']] = feature['id']

df_charging_station['id'] = df_charging_station['State'].apply(lambda x: state_id_map[x])

# Compute KPIs
total_stations_india = df_charging_station['No. of Operational PCS'].sum()
top_state = df_charging_station.loc[df_charging_station['No. of Operational PCS'].idxmax()]
top_state_name = top_state['State']
top_state_stations = top_state['No. of Operational PCS']

# Display KPIs
st.header("Public Charging Station Infrastructure of India")
col10, col11, col12 = st.columns(3)

with col10:
    st.metric(label="State with most PCS", value=top_state_name)

with col11:
    st.metric(label=f"No. of PCS in {top_state_name}", value=top_state_stations)

with col12:
    st.metric(label="Total PCS in India", value=total_stations_india)

charts.india_map_plot(df_charging_station,india_states)



footer = """
<style>
a:link, a:visited {
    color: red;
    background-color: transparent;
    text-decoration: solid;
}

a:hover, a:active {
    color: blue;
    background-color: transparent;
    text-decoration: solid;
}

.footer {
    position: relative; /* Make footer relative to the content */
    bottom: 0;
    width: 100%;
    background-color: white;
    color: black;
    text-align: center;
    margin-top: 20px; /* Adds spacing before the footer */
    padding: 10px 0;  /* Adds padding inside the footer */
    border-top: 1px solid #ddd; /* Optional: Add a subtle top border */
}
</style>
<div class="footer">
    <p>☀️Developed by Team Solar Circuit_031☀️ </p>
    <p> 
        <a href="https://www.linkedin.com/in/hemalatha-kasthuri-714919338" target="_blank">Hemalatha</a>, 
        <a href="https://www.linkedin.com/in/dattasnehendu/" target="_blank">Snehendu</a>, 
        <a href="https://www.linkedin.com/in/nikhil-kumar-001a812b0/" target="_blank">Nikhil</a>, & 
        <a href="https://www.linkedin.com/in/ishita-agarwal-b06889268" target="_blank">Ishita</a>
    </p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)