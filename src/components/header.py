import streamlit as st
def header_home():
    logo_url="https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(f"""
           <div style='display:flex;flex-direction:column;align-items:center;justify-content:center;margin-bottom:20px;'>
                <img src='{logo_url}' style='height:100px';/></div>
                <h1 style='text-align:center;color:#E0E3FF;'>SNAP</br>CLASS</h1>


   
""",unsafe_allow_html=True)
def header_dashboard():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
    <style>
    .snap-title {{
        font-family: 'Climate Crisis', sans-serif;
        font-size: 2rem;
        color: #5865F2;
        line-height: 0.8;
        margin:0;
    }}
    </style>

    <div style="display:flex;align-items:center;gap:10px;">
        <img src="{logo_url}" style="height:85px;">
        <div class="snap-title">
            SNAP<br>CLASS
        </div>
    </div>
    """, unsafe_allow_html=True)