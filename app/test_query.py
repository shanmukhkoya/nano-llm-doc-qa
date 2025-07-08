from app.query_engine import answer_question

question = "Give me telephony integrations used in U-Assit and which document you referred?"
answer = answer_question(question)

print("🧠 Answer:")
print(answer)
