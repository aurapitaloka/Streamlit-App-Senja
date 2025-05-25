import streamlit as st
from pymongo import MongoClient

MONGO_URI = st.secrets["MONGO_URI"]
client = MongoClient(MONGO_URI)
db = client["streamlit"] 

def get_collection(collection_name):
    return db[collection_name]
