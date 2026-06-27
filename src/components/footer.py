import streamlit as st

def footer_home():
    st.markdown("""
    <div style="
        position: fixed;
        bottom: 200px;
        left: 50%;
        transform: translateX(-50%);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 16px;
        color: white;
        font-weight: 500;
        z-index: 9999;
    ">
        Created with <span style="color:red; margin:0 5px;">❤️</span> by <b style="margin-left:5px;">Ananya Sah</b>
    </div>
    """, unsafe_allow_html=True)