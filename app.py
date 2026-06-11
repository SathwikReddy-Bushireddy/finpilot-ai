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
    padding: 10px;
    border-radius: 12px;
    text-align: center;
    font-weight: 600;
    border: 2px solid #FFE5D0;
    color: #222222;
    font-size: 0.9rem;
}

/* Welcome Card */
.welcome-card {
    background: white;
    border: 2px solid #FFE5D0;
    border-radius: 15px;
    padding: 14px;
    text-align: center;
    color: #333333;
    font-size: 0.92rem;
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

.error-badge {
    background-color: #FF4D4F;
    color: white;
    padding: 4px 10px;
    border-radius: 15px;
    font-size: 0.8rem;
    font-weight: 600;
    display: inline-block;
    margin-bottom: 8px;
}
            
/* Error Card */
.error-card {
    background: #FFF1F0;
    border: 2px solid #FFCCC7;
    color: #CF1322;
    padding: 12px;
    border-radius: 12px;
    font-size: 0.9rem;
    white-space: pre-wrap;
    line-height: 1.5;
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
# HOME SCREEN
# ==========================================================

if len(st.session_state.messages) == 0:
    # Tool Cards
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
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="welcome-card">
            <b>Welcome to FinPilot AI</b><br><br>

            Real-time stocks, crypto, and currency insights powered by LangGraph.
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
    """
    <h3 style="
        color:#222222;
        margin-bottom:15px;
        font-size:1.2rem;
        font-weight:600;
    ">
        Try Asking
    </h3>
    """,
    unsafe_allow_html=True
)
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button(
            "📊 Tesla stock price",
            use_container_width=True
        ):
            st.session_state.prefill_query = (
                "Tesla stock price"
            )
            st.rerun()
    with c2:
        if st.button(
            "₿ Bitcoin price",
            use_container_width=True
        ):
            st.session_state.prefill_query = (
                "Bitcoin price"
            )
            st.rerun()
    with c3:
        if st.button(
            "💱 Convert 100 USD to INR",
            use_container_width=True
        ):
            st.session_state.prefill_query = (
                "Convert 100 USD to INR"
            )
            st.rerun()

# ==========================================================
# CHAT HISTORY
# ==========================================================

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"] == "assistant":
            route = message.get("route")
            if route == "error":
                st.markdown(
                    f"""
                    <div class="error-card">
                    {message["content"]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            elif route:
                badge = {
                    "stock": "📊 Stock Tool",
                    "crypto": "₿ Crypto Tool",
                    "currency": "💱 Currency Tool"
                }.get(route, "🤖 FinPilot")
                st.markdown(
                    f"""
                    <div class="route-badge">
                    {badge}
                    </div>
                    {message["content"]}
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.markdown(message["content"])
        else:
            st.markdown(message["content"])

# ==========================================================
# CHAT INPUT
# ==========================================================
if len(st.session_state.messages) > 0:
    col1, col2 = st.columns([8, 1])
    with col2:
        if st.button(
            "🗑 Clear Chat",
            use_container_width=True
        ):
            st.session_state.messages = []
            st.rerun()
            
query = st.chat_input(
    "Ask a financial question..."
)

# Handle example button clicks
if "prefill_query" in st.session_state:
    query = st.session_state.prefill_query
    del st.session_state.prefill_query

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
            error_text = str(e)
            if "RESOURCE_EXHAUSTED" in error_text:
                response = """
🚫 Gemini API quota exceeded.

Please wait a minute and try again.

If the problem persists, check your Gemini API usage and billing.
"""
            else:
                response = error_text
            route = "error"

    # Tool Badge
    tool_map = {
        "stock": "📊 Stock Tool",
        "crypto": "₿ Crypto Tool",
        "currency": "💱 Currency Tool",
        "error": "⚠️ Error"
    }
    badge = tool_map.get(route, "🤖 FinPilot")
    badge_class = (
        "error-badge"
        if route == "error"
        else "route-badge"
    )
    if route == "error":
        final_response = f"""
    <div class="error-card">
        {response}
    </div>
    """
    else:
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
        "content": response,
        "route": route
    }
)
    # Display Assistant Response
    with st.chat_message("assistant"):
        if route == "error":
            st.markdown(
            f"""
            <div class="error-card">
            {response}
            </div>
            """,
            unsafe_allow_html=True
            )
        else:
            st.markdown(
            f"""
            <div class="route-badge">
            {badge}
            </div>
            {response}
            """,
            unsafe_allow_html=True
            )