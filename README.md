# Indian EV Market Dashboard 📊

## Introduction
The purpose of the Indian EV Market Dashboard is to provide a comprehensive, interactive visualization of the electric vehicle landscape in India. By analyzing key metrics and trends within the EV market, this dashboard offers insights into EV adoption rates, market share, regional distributions, vehicle types, and growth patterns over time. This tool aims to support data-driven decision-making for stakeholders such as policymakers, industry analysts, and businesses, helping them understand market dynamics and identify emerging opportunities in India’s rapidly evolving EV sector.

## Project Type
Data Analysis using Python Libraries

## Deplolyed App
Indian EV Market: https://indian-ev-market-dashboard.streamlit.app/

## Directory Structure
INDIAN-EV-MARKET-DASHBOARD
- ├─ assets/
- │  ├─ ├─ EV Maker by Place.csv/
- │  ├─ datasets/
- │  ├─ ├─ ev_cat_01-24.csv/
- │  ├─ ├─ ev_sales_by_makers_and_cat_15-24.csv/
- │  ├─ ├─ OperationalPC.csv/
- │  ├─ ├─ Vehicle Class - All.csv/
- ├─ images/
- │  ├─ analysis.ico/
- │  ├─ Indian EV Market Logo.svg/
- ├─ preprocessor.py/
- ├─ charts.py/
- ├─ main.py/
- ├─ Indian_States.geojson/
- ├─ requirements.txt/
- ├─ README.md/

## Video Walkthrough of the project
https://youtu.be/KmtujzDYeJM

## Video Walkthrough of the codebase
https://youtu.be/E963Q4vFQew

## Features
- Analysis of overall EV Market (2001-2024).
- KPIs of Overall EV Market.
- Top 10 Manufacturer Analysis and Market Share for each year.
- Growth of EV Market for each Vehicle Class.
- Operational Charging Station Analysis.
- Dynamic Map Representation of EV Adoption.

## Design decisions or assumptions
- Used Alatair Charts instead of Streamlit Charts for sorting data and applying custom color schemes.
- Used Plotly Express library for line plots instead of Streamlit Line plots for further customisation options.
- Used Mapbox library for a responsive and better looking map plot.
- Used third party Geojson data for accurate map plotting.
- Webapp divided into different segments for different analysis.
- Specific filters are segregated according to each section of analysis.
- Used a custom footer component available in Streamlit community, due to no footer component in streamlit documentation.

## Installation & Getting started
Detailed instructions on how to install:

- Setup a virtual environent
- Install the following libraries
- - pip install python
- - pip install pandas
- - pip install altair
- - pip install plotly
- - pip install streamlit

## Usage
How to use our project:
- Run a local Streamlit server
- - streamlit run main.py

## Technology Stack
- Python
- Pandas
- Altair
- Plotly.express
- Mapbox
- Streamlit