import streamlit as st
import mymodel as m

st.write("""
  # Simple Sales Model
  This is just a test for some of the amazing things done by stremlit.
  """)

st.write(m.run(window = 15))

window = st.slider("Forecast window (days)")
st.write(m.run(window = window))
