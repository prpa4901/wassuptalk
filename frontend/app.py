from huggingface_hub import InferenceClient
from constants import *
import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000/chat/"

if "history" not in st.session_state:
    st.session_state["history"] = []

if "client" not in st.session_state:
    st.session_state["client"] = None

if "selected_model" not in st.session_state:
    st.session_state["selected_model"] = "mistralai/Mistral-7B-v0.1"

if "token_validated" not in st.session_state:
    st.session_state["token_validated"] = False


# Mapping of model IDs to alt text
model_mapping = {
    MISTRAL_MODEL_NAME: "Mistral 7B",
    FALCON_MODEL_NAME: "Falcon",
    PHI2_MODEL_NAME: "Phi",
    "gpt2": "GPT-2"
}

# User and bot images
USER_IMAGE = "static/images/your-image.png"  # Replace with your image path
BOT_IMAGE = "static/images/bot-image.png"  # Replace with bot image path



if not st.session_state["token_validated"]:
    with st.container():
        st.write(
            """
            To use this chatbot, you'll need a Hugging Face API token. 
            - **Don't have a token yet?** [Create an accout and Generate one here](https://huggingface.co/settings/tokens).
            - Copy the token and paste it below.
            """
        )

        api_token = st.text_input("Enter your Hugging Face API token:", type="password")

        # Step 3: Token Validation
        if st.button("Validate Token"):
            if api_token:
                # headers = {"Authorization": f"Bearer {api_token}"}
                # test_response = requests.get("https://api-inference.huggingface.co/status", headers=headers)

                try:
                    client = InferenceClient(token=api_token)
                    selected_model = st.session_state["selected_model"]
                    is_valid = client.get_model_status("gpt2")  # Replace "gpt2" with any public model
                    if is_valid:
                        st.session_state["client"] = client
                        st.session_state["token_validated"] = True
                        st.success("Token validated successfully! You can now use the chatbot.")
                        st.rerun()
                    else:
                        st.error("Token seems valid, but the model is not ready for inference.")
                except Exception as e:
                    st.error(f"Invalid token. Please check and try again. (Error: {e})")
            else:
                st.warning("Please enter a token before validating.")

st.title("Wassup!")

if st.session_state["token_validated"]:
    col1, col2 = st.columns([4, 1])

    if st.session_state["client"] is not None and st.session_state["selected_model"]:
        with col1:
            user_input = st.text_input("You:", key="user_input")
        
            if st.button("Send"):
                if user_input:
                    # headers = {"Authorization": f"Bearer {api_token}"}
                    # response = requests.post(BACKEND_URL, headers=headers, json={"user_input": user_input})
                    client = st.session_state["client"]
                    selected_model = st.session_state["selected_model"]

                    response = client.text_generation(model=selected_model,
                                                      prompt=user_input,
                                                      max_new_tokens=120,
                                                      temperature=0.7,
                                                      top_k=50,
                                                      repetition_penalty=1.2,
                                                      top_p=0.9)
                    if response:
                        print(response)
                        data = response
                        print(data)
                        st.session_state["history"].append({"user_message": user_input, "bot_response": response})
                else:
                    st.warning("Please enter a message before sending.")

        with col2:
            st.selectbox(
                "Select a model:",
                list(model_mapping.values()),
                index=list(model_mapping.values()).index(model_mapping[st.session_state["selected_model"]]),
                key="model_selector"
            )
            # Update the selected model in session state
            st.session_state["selected_model"] = list(model_mapping.keys())[list(model_mapping.values()).index(st.session_state["model_selector"])]
        
        st.write("### Chat History")
        for message in st.session_state["history"]:
            with st.container():
                col1, col2, col3 = st.columns([4, 5, 1])
                with col1:
                    st.empty()  # Placeholder to align to the right
                with col2:
                    st.markdown(f"**You:** {message['user_message']}")
                with col3:  
                    st.image(USER_IMAGE, width=30)

            with st.container():
                col1, col2, col3 = st.columns([1, 8, 1])
                with col1:
                    st.image(BOT_IMAGE, width=30)  # Bot image
                with col2:
                    st.markdown(f"**Talky:** {message['bot_response']}")
                with col3:
                    st.empty()

            
            
    else:
        st.info("Please validate your token first to enable chatbot functionality.")