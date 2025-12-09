#-*- coding: utf-8 -*-

# 필요한 라이브러리를 가져옵니다.
import os  # 운영체제와 상호작용하기 위한 모듈입니다. .env 파일에서 환경 변수를 불러올 때 사용됩니다.
import sys  # 파이썬 인터프리터와 상호작용하기 위한 모듈입니다. 여기서는 직접 사용되진 않지만, 일반적으로 포함될 수 있습니다.
import urllib.request  # URL을 열고 HTTP 요청을 보내기 위한 모듈입니다.
from dotenv import load_dotenv # .env 파일에서 환경 변수를 로드하기 위한 함수입니다.

# .env 파일을 찾아 환경 변수를 로드합니다.
# 이 기능을 통해 API 키와 같은 민감한 정보를 코드에 직접 작성하지 않고 안전하게 관리할 수 있습니다.
load_dotenv()

# 환경 변수에서 네이버 API 클라이언트 ID와 시크릿을 가져옵니다.
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# API 요청에 사용할 클라이언트 ID와 시크릿을 변수에 할당합니다.
client_id = CLIENT_ID
client_secret = CLIENT_SECRET

# 요청을 보낼 네이버 데이터랩 API의 URL 주소입니다.
url = "https://openapi.naver.com/v1/datalab/search";

# API에 전송할 요청 본문(body)을 JSON 형식의 문자열로 정의합니다.
# 이 예제에서는 2017년 1월 1일부터 2017년 4월 30일까지의 데이터를 월별 단위로 조회합니다.
# '한글' 그룹과 '영어' 그룹의 키워드에 대한 검색량을 PC에서, 특정 연령대(1, 2)의 여성(f)을 대상으로 조회합니다.
body = "{\"startDate\":\"2017-01-01\",\"endDate\":\"2017-04-30\",\"timeUnit\":\"month\",\"keywordGroups\":[{\"groupName\":\"한글\",\"keywords\":[\"한글\",\"korean\"]},{\"groupName\":\"영어\",\"keywords\":[\"영어\",\"english\"]}],\"device\":\"pc\",\"ages\":[\"1\",\"2\"],\"gender\":\"f\"}";

# URL 주소를 사용하여 요청 객체를 생성합니다.
request = urllib.request.Request(url)

# 요청 헤더에 네이버 API 인증 정보를 추가합니다.
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

# 요청 헤더에 콘텐츠 유형이 JSON임을 명시합니다.
request.add_header("Content-Type", "application/json")

# 생성된 요청 객체와 본문 데이터를 사용하여 API에 요청을 보내고 응답을 받습니다.
# 본문 데이터는 UTF-8 형식으로 인코딩하여 전송해야 합니다.
response = urllib.request.urlopen(request, data=body.encode("utf-8"))

# 응답의 HTTP 상태 코드를 가져옵니다.
rescode = response.getcode()

# 상태 코드가 200이면 (성공적인 요청)
if(rescode == 200):
    # 응답 본문을 읽어옵니다.
    response_body = response.read()
    # 응답 본문은 바이트(byte) 형태이므로, 사람이 읽을 수 있도록 UTF-8로 디코딩하여 출력합니다.
    print(response_body.decode('utf-8'))
# 상태 코드가 200이 아니면 (에러 발생)
else:
    # 에러 코드와 함께 메시지를 출력합니다.
    print("Error Code:" + rescode)
