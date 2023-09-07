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
        st.error(f"Opps.. an error occurred.{e}")
        st.sidebar.write("\n\nIf you feel our site could't handle the link please help to log an issue on [issue](https://github.com/devilsaint99/Unshortener/issues) in our github.")


