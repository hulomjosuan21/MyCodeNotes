import streamlit as st
import mycodes

st.set_page_config("My Code Notes", layout='centered', initial_sidebar_state='auto')
def main():
    
    page = st.sidebar.selectbox("Choose a page",["Java","Cmd commands","JDBC","Sumo Robot Code","Java Syntax"])
    
    if page == "Java":
        for k, v in mycodes.javaCodes.items(): 
            st.subheader(k)
            st.code(v, language='java')
            st.markdown("---")
    elif page == "Cmd commands":
        for k, v in mycodes.cmdCommands.items(): 
            st.subheader(k)
            st.code(v, language='cmd')
            st.markdown("---")
    elif page == "JDBC":
        for k, v in mycodes.jdbcCodes.items(): 
            st.subheader(k)
            st.code(v, language='java')
            st.markdown("---")        
    elif page == "Sumo Robot Code":
        for k, v in mycodes.robotCode.items(): 
            st.subheader(k)
            st.code(v, language='c')
            st.markdown("---")
    elif page == "Java Syntax":
        for k, v in mycodes.javaSyntax.items(): 
            st.subheader(k)
            st.code(v, language='java')
            st.markdown("---")
    st.write("Copyright © 2024 Josuan. All rights reserved.")

if __name__ == '__main__':
    main()
