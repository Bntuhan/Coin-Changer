import streamlit as st
import requests

response=requests.get('https://api.coinlore.net/api/tickers/')

veri=response.json()

coinlist=veri['data']

coinler={}

for coin in coinlist:
    coinler.update({coin['symbol']:float(coin['price_usd'])})

coinisimleri=list(coinler.keys())
coin1=st.sidebar.selectbox("Elinizdeki Coin",coinisimleri)
adet=st.sidebar.number_input("Elinizdeki Miktar")
coin2=st.sidebar.selectbox("Hedef Coin",coinisimleri)
coin1fiyat=coinler[coin1]
coin2fiyat=coinler[coin2]

sonuc=(coin1fiyat/coin2fiyat)*adet

st.write(adet,"adet",coin1,sonuc,"adet",coin2,"değerindedir.")



