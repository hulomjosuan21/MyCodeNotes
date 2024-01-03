import streamlit as st
from mycodes import codes

st.set_page_config("My Code Notes", layout='centered', initial_sidebar_state='auto')
def main():
    for k, v in codes.items(): 
        st.subheader(k)
        st.code(v, language='java')
        st.markdown("---")
    
    st.write("Copyright © 2024 Josuan. All rights reserved.")

if __name__ == '__main__':
    main()
