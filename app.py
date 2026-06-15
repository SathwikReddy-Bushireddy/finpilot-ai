import streamlit as st
from graph.workflow import graph
from rag.pdf_loader import load_pdf
from rag.text_splitter import split_documents
from rag.vector_store import create_vector_store, save_vector_store
from rag.rag_chain import ask_pdf,generate_summary,financial_insight

# ==========================================================
# PAGE CONFIG
# ==========================================================
st.set_page_config(
    page_title="FinPilot AI",
    page_icon="📈",
    layout="wide",
)
tab1, tab2 = st.tabs([
    "📈 Financial Assistant",
    "📄 Financial PDF Analysis"
])

with tab1:
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
        padding-bottom: 0rem !important;
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
        .response-text {
        color: #222222;
        font-size: 0.95rem;
        line-height: 1.6;
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
    margin-top:20px;
    padding-top:10px;
    border-top:1px solid #E5D5C5;
    }
                
    /* Streamlit Tabs */

    button[data-baseweb="tab"] {
        color: #444444 !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
    }

    /* Active Tab */

    button[data-baseweb="tab"][aria-selected="true"] {
        color: #FF6B35 !important;
        font-weight: 700 !important;
    }

    /* Inactive Tab */

    button[data-baseweb="tab"][aria-selected="false"] {
        color: #555555 !important;
    }
                
    /* Streamlit Headers */
    h1, h2, h3, h4, h5, h6 {
        color: #222222 !important;
    }

    /* Streamlit labels */
    label,
    .stMarkdown,
    .stText
    {
        color: #222222;
    }

    /* File uploader label */
    [data-testid="stFileUploader"] label {
        color: #222222 !important;
        font-weight: 600 !important;
    }

    /* Text input label */
    [data-testid="stTextInput"] label {
        color: #222222 !important;
        font-weight: 600 !important;
    }

    /* Expander title */
    [data-testid="stExpander"] summary {
        color: #222222 !important;
        font-weight: 600 !important;
    }

    /* Expander content (source chunks) */
    [data-testid="stExpander"] p,
    [data-testid="stExpander"] div,
    [data-testid="stExpander"] span {
        color: #222222 !important;
    }

    /* Markdown output */
    .stMarkdown p {
        color: #222222 !important;
    }

    /* Uploaded PDF chunk text */
    .element-container {
        color: #222222 !important;
    }

    /* Streamlit buttons */
    .stButton button {
        color: white !important;
        background-color: #0B1220 !important;
        font-weight: 600 !important;
    }

    /* Any text inside buttons */
    .stButton button p,
    .stButton button span,
    .stButton button div {
        color: white !important;
    }     
        
    /* Welcome Card */
    .welcome-card {
        background: white;
        border: 2px solid #FFE5D0;
        border-radius: 15px;
        padding: 14px;
        text-align: center;
    }

    /* Title above dark box */
    .welcome-title {
        color: #222222 !important;
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 15px;
    }

    /* Dark description box */
    .welcome-description {
        background: #0B1220;
        color: white !important;
        border-radius: 12px;
        padding: 25px;
        line-height: 1.8;
        font-size: 0.95rem;
    }

    /* Force all text inside description to remain white */
    .welcome-description * {
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)
    # ==========================================================
    # SESSION STATE
    # ==========================================================

    if "messages" not in st.session_state:
        st.session_state.messages=[]

    if "history" not in st.session_state:
        st.session_state.history=[]
    
    if "pdf_messages" not in st.session_state:
        st.session_state.pdf_messages = []

    if "pdf_sources" not in st.session_state:
        st.session_state.pdf_sources = []

    if "vector_db" not in st.session_state:
        st.session_state.vector_db = None

    if "current_pdf" not in st.session_state:
        st.session_state.current_pdf = None

    if "pdf_summary" not in st.session_state:
        st.session_state.pdf_summary = None

    if "pdf_history" not in st.session_state:
        st.session_state.pdf_history = []

    if "vector_built_for" not in st.session_state:
        st.session_state.vector_built_for = None

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
            <div class="welcome-title">
                Welcome to FinPilot AI
            </div>
            <div class="welcome-description">
                Get real-time stock prices, cryptocurrency data,
                currency conversions, and financial news using
                intelligent LangGraph workflows.
            </div>
        </div>
        """,unsafe_allow_html=True)
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
                        <div style="
                            color:#222222;
                            background:white;
                            padding:12px;
                            border-radius:12px;
                            margin-top:8px;
                            border:1px solid #FFE5D0;
                            ">{message["content"]}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(message["content"])
            else:
                st.markdown(message["content"])

    if len(st.session_state.messages) > 0:

        col1, col2,col3 = st.columns([6,2,2])

        with col3:
            if st.button(
            "🗑 Clear Chat",
            use_container_width=True
        ):
                st.session_state.messages = []
                st.session_state.history = []
                st.rerun()
    # ==========================================================
    # CHAT INPUT
    # ==========================================================
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
    # st.markdown(
    #     """
    #     <style>
    #     div[data-testid="stTextInput"] > div {
    #         color: #222222;
    #         background-color: white;
    #         padding: 12px;
    #         border-radius: 12px;
    #         margin-top: 8px;
    #         border: 1px solid #FFE5D0;
    #     }
    #     /* Optional: Ensure the actual input field background matches */
    #     div[data-testid="stTextInput"] input {
    #         background-color: white;
    #         color: #222222;
    #     }
    #     </style>
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
    config1={'configurable':{'thread_id':'user_thread'}}
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
                        "query": query,
                        "history": st.session_state.history
                    }, config=config1
                )
                response = result["response"]
                route = result["route"]
                st.session_state.history=result.get("history",st.session_state.history)
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
                <div style="
                    color:#222222;
                    background:white;
                    padding:12px;
                    border-radius:12px;
                    margin-top:8px;
                    border:1px solid #FFE5D0;
                    ">{response}
                </div>
                """,
                unsafe_allow_html=True
                )
    st.markdown(
        """
        <style>
        div[data-testid="stExpander"] {
            color: #222222;
            background: white;
            padding: 12px;
            border-radius: 12px;
            margin-top: 8px;
            border: 1px solid #FFE5D0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    DEBUG = False
    if DEBUG:
        with st.expander("🧠 Debug Memory"):
            st.write(st.session_state.get("history", []))
    st.markdown(
        """
        <div class="finpilot-footer">
            FinPilot AI • LangGraph • Gemini
        </div>
        """,
        unsafe_allow_html=True
    )

with tab2:
    st.subheader("📄 Financial Report Analyzer")
    uploaded_file = st.file_uploader(
        "Upload Annual Report",
        type=["pdf"]
    )
    import os
    if uploaded_file:
        save_path = os.path.join(
            "uploads",
            uploaded_file.name
        )
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(
            f"Uploaded: {uploaded_file.name}"
        )
    if uploaded_file:
        docs = load_pdf(save_path)
        chunks = split_documents(docs)
        if st.session_state.current_pdf != uploaded_file.name:
            st.session_state.pdf_summary = generate_summary(chunks)
            st.session_state.current_pdf = uploaded_file.name
        summary = st.session_state.pdf_summary
        pages = len(docs)
        chunk_count = len(chunks)
        word_count = sum(
            len(doc.page_content.split())
            for doc in docs
        )
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Pages", pages)
        with c2:
            st.metric("Chunks", chunk_count)
        with c3:
            st.metric(
                "Words",
                f"{word_count:,}"
            )
        st.subheader("📄 Executive Summary")
        st.info(summary)
        st.subheader("📊 Financial Insights")
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            summary_btn = st.button("📊 Summary")
        with c2:
            risk_btn = st.button("⚠ Risk Analysis")
        with c3:
            growth_btn = st.button("📈 Growth")
        with c4:
            profit_btn = st.button("💰 Profitability")
        insight_result = None
        if summary_btn:
            insight_result = financial_insight("summary",st.session_state.pdf_history)
            answer = insight_result["answer"]
            st.session_state.pdf_messages.append({
            "question": "📊 Summary",
            "answer": answer
            })
            st.session_state.pdf_history.append(
                "User: Summary"
            )
            st.session_state.pdf_history.append(
                f"Assistant: {answer}"
            )
        if risk_btn:
            insight_result = financial_insight("risk",st.session_state.pdf_history)
            answer = insight_result["answer"]
            st.session_state.pdf_messages.append({
            "question": "⚠ Risk Analysis",
            "answer": answer
            })
            st.session_state.pdf_history.append(
                "User: Risk Analysis"
            )
            st.session_state.pdf_history.append(
                f"Assistant: {answer}"
            )
        if growth_btn:
            insight_result = financial_insight("growth",st.session_state.pdf_history)
            answer = insight_result["answer"]
            st.session_state.pdf_messages.append({
            "question": "📈 Growth Analysis",
            "answer": answer
            })
            st.session_state.pdf_history.append(
                "User: Growth Analysis"
            )
            st.session_state.pdf_history.append(
                f"Assistant: {answer}"
            )
        if profit_btn:
            insight_result = financial_insight("profitability",st.session_state.pdf_history)
            answer = insight_result["answer"]
            st.session_state.pdf_messages.append({
            "question": "💰 Profitability",
            "answer": answer
            })
            st.session_state.pdf_history.append(
                "User: Profitability"
            )
            st.session_state.pdf_history.append(
                f"Assistant: {answer}"
            )
        if insight_result:
            answer = insight_result["answer"]
            sources = insight_result["sources"]
            st.session_state.pdf_sources = sources
            st.success(answer)
        suggested_questions = [
            "Summarize revenue growth",
            "What are the risk factors?",
            "What are the major expenses?",
            "What is management outlook?"
        ]
        cols = st.columns(4)
        for col, q in zip(cols, suggested_questions):
            with col:
                if st.button(q):
                    result = ask_pdf(q,st.session_state.pdf_history)
                    answer = result["answer"]
                    sources = result["sources"]
                    st.session_state.pdf_sources = sources
                    st.session_state.pdf_messages.append({
                        "question": q,
                        "answer": answer
                        })
                    st.session_state.pdf_history.append(f"User: {q}")
                    st.session_state.pdf_history.append(f"Assistant: {answer}")
                    st.success(answer)
        
        # Automatically build vector store
        if st.session_state.vector_built_for != uploaded_file.name:
            with st.spinner("Building vector store..."):
                vector_db = create_vector_store(chunks)
                save_vector_store(vector_db)
                st.session_state.vector_db = vector_db
                st.session_state.vector_built_for = uploaded_file.name

            st.success("Knowledge base built and saved!")
        
        st.subheader("Preview")
        st.text_area(
            "First Page",
            docs[0].page_content[:2000],
            height=300
        )

    sources = []
    question = st.text_input(
    "Ask about the report"
    )
    ask_pdf_button = st.button(
    "Ask PDF"
    )
    if ask_pdf_button and question:
        result = ask_pdf(question,st.session_state.pdf_history)
        answer = result["answer"]
        st.session_state.pdf_history.append(f"User: {question}")
        st.session_state.pdf_history.append(f"Assistant: {answer}")
        sources = result["sources"]
        st.session_state.pdf_sources = sources
        st.success(answer)
        st.session_state.pdf_messages.append({
        "question": question,
        "answer": answer
        })
    for chat in st.session_state.pdf_messages:
        st.markdown(
            f"### 🙋 Question\n{chat['question']}"
            )
        st.markdown(
            f"### 🤖 Answer\n{chat['answer']}"
            )
        st.divider()
    with st.expander("📚 Source Chunks"):
        if st.session_state.pdf_sources:
            for i, doc in enumerate(st.session_state.pdf_sources):
                st.markdown(f"### Source {i+1}")
                st.write(doc.page_content[:1000])

    if st.button("🗑 Clear PDF Chat"):
        st.session_state.pdf_messages = []
        st.session_state.pdf_history = []
        st.session_state.pdf_sources = []
        st.session_state.pdf_summary = None
        st.session_state.current_pdf = None
        st.session_state.vector_built_for = None
        st.session_state.vector_db = None

        st.rerun()
