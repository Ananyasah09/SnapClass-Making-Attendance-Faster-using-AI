import streamlit as st

def footer_home():
    st.markdown("""
    <style>
    .custom-footer{
        position:fixed;
        left:0;
        bottom:0;
        width:100%;
        text-align:center;
        padding:12px;
        font-size:16px;
        font-weight:500;
        z-index:9999;
        color:white;
        background:transparent;
    }
    </style>

    <div class="custom-footer">
        Created with <span style="color:red;">❤️</span> by <b>Ananya Sah</b>
    </div>
    """, unsafe_allow_html=True)
def footer_dashboard():
    st.markdown("""
    <style>
    .custom-footer{
        position:fixed;
        left:0;
        bottom:0;
        width:100%;
        text-align:center;
        padding:12px;
        font-size:16px;
        font-weight:500;
        z-index:9999;
        color:black;
        background:transparent;
    }
    </style>

    <div class="custom-footer">
        Created with <span style="color:red;">❤️</span> by <b>Ananya Sah</b>
    </div>
    """, unsafe_allow_html=True)