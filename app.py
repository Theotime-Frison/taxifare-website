import streamlit as st
import datetime
import requests


'''
# TaxiFare Pricing
'''

#http://localhost:8000/predict?pickup_datetime=2014-07-06&19:18:00&pickup_longitude=-73.950655&pickup_latitude=40.783282&dropoff_longitude=-73.984365&dropoff_latitude=40.769802&passenger_count=2

date = st.date_input(
    "Pickup date",
    datetime.date(2024, 6, 1))
time = st.time_input('Pickup time', datetime.time(8, 45))

pick_datetime = datetime.datetime(date.year,date.month, date.day, time.hour, time.minute, time.second)

pick_lon = st.number_input('Pickup longitude', value=-73.950655)

pick_lat = st.number_input('Pickup latitude', value=40.783282)

drop_lon = st.number_input('Dropoff longitude', value=-73.984365)

drop_lat = st.number_input('Dropoff latitude', value=40.769802)

pass_count = st.number_input('Passenger count', value=1)


data = {
    'pickup_datetime':pick_datetime,
    'pickup_longitude':pick_lon,
    'pickup_latitude':pick_lat,
    'dropoff_longitude':drop_lon,
    'dropoff_latitude':drop_lat,
    'passenger_count':pass_count
}

url = 'https://taxifare.lewagon.ai/predict'


st.write('Your fare is :', round(requests.get(url, params=data).json()['fare'], 2),'$')
