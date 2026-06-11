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
    transition: all 0.3s ease;
}
.tool-card:hover {
    transform: translateY(-3px);
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
            
.stock-badge {
    background: #E3F2FD;
    color: #1565C0;
    padding: 4px 10px;
    border-radius: 15px;
    font-size: 0.8rem;
    font-weight: 600;
    display: inline-block;
}

.crypto-badge {
    background: #FFF3E0;
    color: #E65100;
    padding: 4px 10px;
    border-radius: 15px;
    font-size: 0.8rem;
    font-weight: 600;
    display: inline-block;
}

.currency-badge {
    background: #E8F5E9;
    color: #2E7D32;
    padding: 4px 10px;
    border-radius: 15px;
    font-size: 0.8rem;
    font-weight: 600;
    display: inline-block;
}

.news-badge {
    background: #F3E5F5;
    color: #7B1FA2;
    padding: 4px 10px;
    border-radius: 15px;
    font-size: 0.8rem;
    font-weight: 600;
    display: inline-block;
}

/* Chat Messages */

[data-testid="stChatMessage"] {
    border-radius: 12px;
}

/* Custom Input Box */

.finpilot-input {
    background: white;
    padding: 15px;
    border-radius: 15px;
    border: 2px solid #FFE5D0;
    margin-top: 20px;
    margin-bottom: 20px;
}
/* Input Box */

.stTextInput input {
    background-color: #FFF8F0 !important;
    color: #222222 !important;
    border: 2px solid #FFE5D0 !important;
    border-radius: 12px !important;
    padding: 12px !important;
    font-size: 0.95rem !important;
}
.stButton button {
    border-radius: 10px;
    font-size: 0.9rem;
    padding: 0.4rem 0.8rem;
    font-weight: 600;
}

/* Footer */

.finpilot-footer {
    text-align:center;
    color:#555555;
    font-size:0.9rem;
    margin-top:80px;
    padding-top:20px;
    border-top:1px solid #E5D5C5;
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
    col1, col2, col3,col4 = st.columns(4)
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
    with col4:
        st.markdown(
        """
        <div class="tool-card">
            📰 News
        </div>
        """,
        unsafe_allow_html=True
        )
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
    """
    <div class="welcome-card">
        <b>Welcome to FinPilot AI</b><br><br>

        Get real-time stock prices, cryptocurrency data,
        currency conversions, and financial news using
        intelligent LangGraph workflows.
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
    c1, c2, c3, c4 = st.columns(4)
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
    with c4:
        if st.button(
            "📰 Latest Tesla news",
            use_container_width=True
        ):
            st.session_state.prefill_query = (
                "Latest Tesla news"
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
                    "currency": "💱 Currency Tool",
                    "news": "📰 News Tool"
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
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([7,1,2])
    with col3:
        if st.button(
            "🗑 Clear Chat",
            use_container_width=True
        ):
            st.session_state.messages = []
            st.rerun()
# ==========================================================
# CUSTOM INPUT
# ==========================================================

# st.markdown(
#     """
#     <div class="finpilot-input">
#     <b>Ask a Financial Question</b>
#     </div>
#     """,
#     unsafe_allow_html=True
# )

col1, col2 = st.columns([8,1])

with col1:
    query = st.text_input(
        "",
        placeholder="Ask about stocks, crypto, currency conversion, or financial news...",
        label_visibility="collapsed"
    )

with col2:
    send_clicked = st.button(
        "🚀 Ask",
        use_container_width=True
    )

# Handle example button clicks
if "prefill_query" in st.session_state:
    query = st.session_state.prefill_query
    send_clicked = True
    del st.session_state.prefill_query

# ==========================================================
# PROCESS QUERY
# ==========================================================

if send_clicked and query:
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
    badge_map = {
    "stock": (
        "📊 Stock Tool",
        "stock-badge"
    ),
    "crypto": (
        "₿ Crypto Tool",
        "crypto-badge"
    ),
    "currency": (
        "💱 Currency Tool",
        "currency-badge"
    ),
    "news": (
        "📰 News Tool",
        "news-badge"
    )
}
    badge, badge_class = badge_map.get(
    route,
    ("🤖 FinPilot", "route-badge")
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


st.markdown(
    """
    <div class="finpilot-footer">
        FinPilot AI • LangGraph • Gemini
    </div>
    """,
    unsafe_allow_html=True
)
