from utils.gemini import llm
from rag.retriever import get_relevant_chunks

def ask_pdf(question,history=None):
    docs = get_relevant_chunks(
        question
    )
    context = "\n\n".join(
        [
            doc.page_content
            for doc in docs
        ]
    )
    history_text = ""
    if history:
        history_text = "\n".join(history)

    prompt = f"""
        You are a financial analyst.
        Conversation History:{history_text}
        Context:{context}
        Current Question:
        {question}
        Use both conversation history and context.Answer accurately.
        """ 
    response = llm.invoke(prompt)

    return {
    "answer": response.content,
    "sources": docs
    }

def generate_summary(chunks):
    context = "\n".join(
        [
            chunk.page_content
            for chunk in chunks[:5]
        ]
    )
    prompt = f"""
You are a financial analyst.
Provide:
1. Company Overview
2. Revenue Highlights
3. Key Risks
4. Important Insights
Context:{context}
"""
    response = llm.invoke(prompt)

    return response.content

def financial_insight(prompt_type,history=None):
    prompt_map = {
        "summary": """
        Provide:
        1. Company Overview
        2. Revenue
        3. Risks
        4. Key Insights
        """,

        "risk": """Analyze major risks.
        Provide:
        1. Risk
        2. Impact
        3. Severity
        """,

        "growth": """Analyze growth trends.
        Include:
        1. Revenue Growth
        2. Expansion
        3. Future Outlook
        """,

        "profitability": """Analyze profitability.
        Include:
        1. Margins
        2. Net Income
        3. Cost Structure
        """
    }
    docs = get_relevant_chunks(
        prompt_type
    )
    context = "\n\n".join(
        [
            doc.page_content
            for doc in docs
        ]
    )
    history_text = ""
    if history:
        history_text = "\n".join(history)
    prompt = f"""
    You are a senior financial analyst.
    Conversation History:{history_text}    
    Context:{context}
    Task:{prompt_map[prompt_type]}
    Generate a professional analysis.
    """
    response = llm.invoke(prompt)
    return {
        "answer": response.content,
        "sources": docs
    }
