import requests
import json
import os

from dotenv import load_dotenv
load_dotenv()

# 1. Client ID와 Secret을 입력합니다.
CLIENT_ID=os.getenv("CLIENT_ID")
CLIENT_SECRET=os.getenv("CLIENT_SECRET")

client_id = CLIENT_ID
client_secret = CLIENT_SECRET

# 2. 조회 기간을 '과거'의 날짜로 올바르게 수정합니다.
# 예시: 2024년 1월 1일부터 2024년 11월 30일까지
startDate = "2025-01-01"
# 미래가 아닌 과거 또는 현재 날짜로 설정
endDate = "2025-12-03"
timeUnit = "month"

# 조회할 키워드 그룹은 그대로 유지합니다.
keyword_groups = [
    {'groupName': '비타민', 'keywords': ['비타민', '종합비타민', '비타민C']},
    {'groupName': '오메가3', 'keywords': ['오메가3', 'rTG오메가3']},
    {'groupName': '배즙', 'keywords': ['배즙', '아기배즙']}
]

# 3. API 요청 정보 (URL, 헤더, 바디)
api_url = "https://openapi.naver.com/v1/datalab/search"
headers = {
    'X-Naver-Client-Id': client_id,
    'X-Naver-Client-Secret': client_secret,
    'Content-Type': 'application/json'
}
body = {
    "startDate": startDate,
    "endDate": endDate,
    "timeUnit": timeUnit,
    "keywordGroups": keyword_groups,
}

# 4. API 요청 및 응답 받기
response = requests.post(api_url, headers=headers, data=json.dumps(body))

# 5. 결과 확인
if response.status_code == 200:
    response_data = response.json()
    print(json.dumps(response_data, indent=4, ensure_ascii=False))
else:
    print(f"Error Code: {response.status_code}")
    # 서버가 보내준 구체적인 오류 메시지를 확인하기 위해 response.text를 출력합니다.
    print(f"Error Message: {response.text}")