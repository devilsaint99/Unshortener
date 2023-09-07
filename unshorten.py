import shortner as sh
import streamlit as st
st.title('URL Un-Shortener')
url = st.text_input("Enter URL: ")
if not url:
    pass  
else:
    try:
        shortIt = sh.UrlCheck(url)
        shortIt.hyper()
        st.write(f'Original URL: {shortIt.data}')
    except Exception as e:
        st.error("Opps.. an error occurred.\nIt is either due to\n1. Our site couldn't handle link.\n2. Link might be broken.")
        st.sidebar.write("\n\nIf you feel our site could't handle the link please help to log an issue on [issue](<link_of_issue>) in our github.")


