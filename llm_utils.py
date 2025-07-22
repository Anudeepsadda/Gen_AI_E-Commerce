import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")  # replace with your key
model = genai.GenerativeModel("gemini-pro")

def get_sql_from_question(question: str) -> str:
    prompt = f"""
    Convert this question into SQL for a SQLite DB with:
    - Table 1: eligibility(item_id, eligibility_datetime_utc, eligibility, message)
    - Table 2: ad_sales(item_id, date, ad_sales, impressions, ad_spend, clicks, units_sold)
    - Table 3: total_sales(item_id, date, total_sales, total_units_ordered)

    Question: {question}
    SQL:
    """
    response = model.generate_content(prompt)
    return response.text.strip()
