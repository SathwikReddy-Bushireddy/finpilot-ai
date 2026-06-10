import streamlit as st
from graph.workflow import graph

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="FinPilot AI",
    page_icon="📈",
    layout="wide",
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

/* Background */

.stApp {
    background-color: #FDF6EC;
}

/* Hide Streamlit Branding */

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Main Container */

.block-container {
    padding-top: 0.5rem;
    max-width: 1100px;
}

/* Main Title */

.main-title {
    text-align: center;
    font-size: 2.3rem;
    font-weight: 800;
    color: #FF6B35;
    margin-top: 5px;
    margin-bottom: 0px;
}

/* Subtitle */

.subtitle {
    text-align: center;
    color: #555555;
    font-size: 0.95rem;
    margin-bottom: 20px;
}

/* Tool Cards */

.tool-card {
    background: #FFF8F0;
    padding: 12px;
    border-radius: 12px;
    text-align: center;
    font-weight: 600;
    border: 2px solid #FFE5D0;
    color: #222222;
    font-size: 0.95rem;
}

/* Welcome Card */

.welcome-card {
    background: white;
    border: 2px solid #FFE5D0;
    border-radius: 15px;
    padding: 10px;
    text-align: center;
    color: #333333;
    margin-bottom: 15px;
    font-size: 0.95rem;
}

/* Example Box */

.example-box {
    background: white;
    padding: 14px;
    border-radius: 15px;
    border: 2px solid #FFE5D0;
    margin-top: 10px;
    margin-bottom: 15px;
    color: #222222;
    line-height: 1.5;
    font-size: 0.92rem;
}

/* Route Badge */

.route-badge {
    background-color: #FFB703;
    color: black;
    padding: 4px 10px;
    border-radius: 15px;
    font-size: 0.8rem;
    font-weight: 600;
    display: inline-block;
    margin-bottom: 8px;
}

/* Chat Messages */

[data-testid="stChatMessage"] {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)
# ==========================================================
# SESSION STATE
# ==========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# ==========================================================
# HEADER
# ==========================================================

st.markdown(
    """
    <div class="main-title">
        📈 FinPilot AI
    </div>

    <div class="subtitle">
        AI-Powered Financial Assistant using LangGraph and Gemini
    </div>
    """,
    unsafe_allow_html=True
)

# ==========================================================
# TOOL SECTION
# ==========================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="tool-card">
            💱 Currency
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="tool-card">
            📊 Stocks
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="tool-card">
            ₿ Crypto
        </div>
        """,
        unsafe_allow_html=True
    )

# ==========================================================
# WELCOME CARD
# ==========================================================

st.markdown(
    """
    <div class="welcome-card">
        <b>Welcome to FinPilot AI</b><br><br>

        Real-time stocks, crypto, and currency insights powered by LangGraph.
    </div>
    """,
    unsafe_allow_html=True
)

# ==========================================================
# EXAMPLE QUERIES
# ==========================================================
st.markdown(
    """
    <div class="example-box">
        <b>Try Asking:</b><br><br>

        📊 Tesla stock price<br>
        ₿ Bitcoin price<br>
        💱 Convert 100 USD to INR
    </div>
    """,
    unsafe_allow_html=True
)

# ==========================================================
# CHAT HISTORY
# ==========================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ==========================================================
# CHAT INPUT
# ==========================================================

query = st.chat_input(
    "Ask a financial question..."
)

# ==========================================================
# PROCESS QUERY
# ==========================================================

if query:

    # Show User Message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    with st.chat_message("user"):
        st.markdown(query)

    # Generate Response

    with st.spinner("FinPilot is analyzing the market..."):

        try:

            result = graph.invoke(
                {
                    "query": query
                }
            )

            response = result["response"]
            route = result["route"]

        except Exception as e:

            response = f"Error: {str(e)}"
            route = "error"

    # Tool Badge

    tool_map = {
        "stock": "📊 Stock Tool",
        "crypto": "₿ Crypto Tool",
        "currency": "💱 Currency Tool",
        "error": "⚠️ Error"
    }

    badge = tool_map.get(route, "🤖 FinPilot")

    final_response = f"""
<div class="route-badge">
{badge}
</div>

{response}
"""

    # Save Assistant Response

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": final_response
        }
    )

    # Display Assistant Response

    with st.chat_message("assistant"):
        st.markdown(
            final_response,
            unsafe_allow_html=True
        )