import streamlit as st
from utils.query_router import route_customer_query

def main():
    st.title("Luminus Energy Assistant")
    st.write("Ask your energy-related questions and get instant assistance!")

    message = st.text_area("Message", placeholder="Ask something...")

    if st.button("Run Flow"):
        if not message.strip():
            st.error("Please enter a message")
            return
        
        with st.spinner("Processing..."):
            response = route_customer_query(message)
        
        if "error" in response:
            st.error(response["error"])
        else:
            st.markdown(response["response"])

if __name__ == "__main__":
    main()
