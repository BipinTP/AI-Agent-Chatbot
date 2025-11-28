
import streamlit as st
import requests      # REQUIRED
import json          # REQUIRED

from config import FRONTEND_CONFIG
from session_manager import init_session_state
from ui_components import (
    display_header, 
    render_document_upload_section, 
    render_agent_settings_section, 
    display_chat_history, 
    display_trace_events
)
from backend_api import chat_with_backend_agent


def main():

    
    # Initialize session state variables
    init_session_state()

    fastapi_base_url = FRONTEND_CONFIG["FASTAPI_BASE_URL"]

    # Render UI sections
    display_header()
    render_document_upload_section(fastapi_base_url)
    render_agent_settings_section()

    st.header("Chat with the Agent")
    display_chat_history()

    # User input
    if prompt := st.chat_input("Your message"):

        # Store & show user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Assistant’s response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    agent_response, trace_events = chat_with_backend_agent(
                        fastapi_base_url,
                        st.session_state.session_id,
                        prompt,
                        st.session_state.web_search_enabled
                    )

                    st.markdown(agent_response)

                    st.session_state.messages.append(
                        {"role": "assistant", "content": agent_response}
                    )

                    display_trace_events(trace_events)

                except requests.exceptions.ConnectionError:
                    st.error("Backend unreachable. Start FastAPI first!")
                except requests.exceptions.RequestException as e:
                    st.error(f"Request error: {e}")
                except json.JSONDecodeError:
                    st.error("Backend returned invalid JSON.")
                except Exception as e:
                    st.error(f"Unexpected Error: {e}")


if __name__ == "__main__":
    main()
