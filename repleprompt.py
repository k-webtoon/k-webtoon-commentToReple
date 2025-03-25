import google.generativeai as genai

# 본인의 API 키 입력
GOOGLE_API_KEY = ""  # ← 여기에 복붙

genai.configure(api_key=GOOGLE_API_KEY)

# 모델 초기화
model = genai.GenerativeModel("models/gemini-1.5-flash")

# 프롬프트 예시
prompt = """
너는 '전지적 독자 시점'의 김독자다.  
냉소적이고 이성적이며, 감정 표현에 인색하지만 사람을 누구보다 아낀다.  
한두 문장으로만 차갑고 날카롭게 대답하라.

사용자 댓글: "전독시 노잼이던데요? 김독자 너무 중2병 같음"  
답변:
"""

# 응답 생성
response = model.generate_content(prompt)

# 출력
print("응답:", response.text.strip())
