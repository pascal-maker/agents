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

        # 🔍 DEBUG: Print full API response to your console
        print("🔵 Full Langflow Response:", response)

        # ✅ Check if the response contains 'outputs'
        if "outputs" in response and isinstance(response["outputs"], list) and len(response["outputs"]) > 0:
            try:
                # Attempt to extract the text from the nested structure
                response_text = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
            except (KeyError, IndexError, TypeError):
                response_text = "⚠ Unexpected response format from Langflow."
        else:
            response_text = "⚠ No response received from Langflow."

        st.markdown(response_text)

if __name__ == "__main__":
    main()