# 데이터 수집(다양한 방법) -> 데이터 분석/처리(데이터 가공) -> 인공지능 모델 학습 -> 인공지능 모델 평가 -> 사용

# http hypertext transfer protocol 
# request 요청 - response 응답
# client 요청하는 자(웹브라우저: crom, edge) - server 정보 보여주는 자(서버) 
# html hypertext markup language 
# 웹사이트를 표현하기 위한 언어: 시각적으로 번역해준다고 할 수 있다. 
# <html></html> 태그와 태그 
# html 파싱 : 잘 읽고 분석하는 거. 필요한 것을 추출하는 것. 

# data crawling 데이터 크롤링 
# 파이썬으로 데이터를 받고 보내고 하겠다. 
# 외부라이브러리니까 터미널에서 받아오세요 pip install requests 
# import requests
# url = "https://www.naver.com/"
# response = requests.get(url) 
# html = response.text
# status = response.status_code # status code 

# print(status)
# print(html)

# http 상태 코드 
# 200 : OK
# 요청 성공 
# 302 : 리다이렉트 
# 다른 페이지로 바로 연결

# 클라이언트 리퀘스트에 오류가 있는 경우 
# 400 : 요청이 잘못됨 Bad Request
# 401 : Unauthorized 비인증됨
# 403 : Forbidden 접근 권한 없음 
# 404 : Not Found 요청받은 내용이 없음 (요청을 안한 게 아니라..) 주소 오류일 때가 가장 많음
# 405 : Method Not All 접근 방법이 잘못됨

# 500 : Internal Server Error 서버 에러. 개발을 잘못한 경우가 많음 
# 501 : Not Implemented
# 502 : Bad Gateway 잘못된 응답. 보통 서버 운영프로그램 문제 


# 파이썬으로 데이터 크롤링하기 : 웹이 아니라. 

# URL 구조
# 프로토콜: //호스트주소:포트번호/경로?쿼리
# ip 주소 : 숫자로 된, 인터넷에 연결된 특정 컴퓨터 서버를 가리킬 때 사용. domain: 별명.
# 포트번호: 서버가 말하길 서버에 문이 많은데 이 문으로만 주고 받을 거야. 
# ※ 주소창에서는 16진수로만 쓰기로 해서 글자가 깨진다. 
# 쿼리 : 경로와 다른 추가적인 데이터. 검색페이지 같은 거. 미리 만들어두기 어려운 페이지들.
# https://naver.com/경로?~~~~~~~~~ # 물음표 뒤에 쿼리이름=값&쿼리이름=값 이런 식으로 씀
# (query=치킨) 쿼리에 치킨을 집어 넣어서 검색을 요청한다. 


# import requests
# search_url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query="
# keyword = "맥주"
# url = search_url + keyword
# response = requests.get(url)
# # print(response.text)

# print(type(response.text)) # <class 'str'>

###################################################



# BeautifulSoup
# html 파싱(parsing)
# 터미널에서 받아오세용 pip install beautifulsoup4
# request에서 요청하고 불러오면 파싱한다. 
# html을 객체 구조화해서 사용 

# from bs4 import BeautifulSoup
# html 태그
# <태그이름 속성=속성값>내용</태그이름>
# <html><head></head><body></body></html>
# html.head
# html.body 
# 요렇게 사용할 수 있도록 만들어주는 

# html = "<html><body>Hello</body></html>" # html 문자열
# soup = BeautifulSoup(html, "html.parser") # 객체를 만드는 작업. "" 안의 내용은 어떤 식으로 파싱할 건지 정해주는 것.   

# # print(soup)
# # print(type(soup))
# print(soup.body.text) # 멤버접근 연산자 . 으로 구조 표현. 객체형태로 사용가능. 
# print(type(soup.body.text))

# print(type(response.text)) # <class 'str'>



# import requests
# from bs4 import BeautifulSoup

# search_url = "https://www.google.com/search?tbm=isch&q="
# keyword = "맥주"
# url = search_url + keyword
# response = requests.get(url)
# html = response.text
# soup = BeautifulSoup(html, "html.parser")

# # print(soup.body.div) # body 내용 호출됨
# # print(soup.find('div'))
# # print(soup.find_all('div')) # div를 리스트 형태로 가져온다.  
# # print(soup.find_all('div')[4]) # 4번째 div

# # images = soup.find_all('img', attrs={'class': ['_image', '_listimage']})
# # print(type(images))

# # # container = soup.find('div', attrs={'id': 'container'})

# imgs = soup.find_all('img') # 이미지 태그들 
# img = imgs[1] # 첫번째 이미지 태그 
# print(img['src']) # 주소만 쏙 빼옴 

# import os # 운영체제 작동하게
# folder_name = "imgs" # '이미지들' 이름 변수에 넣고 
# if not os.path.exists(folder_name): # 만약 폴더네임이라는 폴더가 존재하지 않는다면 
#     os.mkdir(folder_name) # 폴더네임이라는 폴더를 만들어라 

# for idx, img in enumerate(imgs[1:]): # 반복하면서 idx와 i에 인덱스 번호를 매기고 1부터 수를 올려라  
#     #enumerate [(0, 1번요소), (1, 2번 요소)]
#     print(idx, "번째 이미지 저장") # 위에서 받은 idx 수랑 "번째 이미지 저장"을 출력하라 
#     file_name = f"{keyword}_{idx}.gif" # file_name에 검색한 명칭과 인덱스번호(순서)와 .확장자를 붙인 문자열을 할당하라 
#     file_path = os.path.join(folder_name, file_name) # file_path에 folder_name과 file_name이 합쳐진 경로를 할당하라 
#     img_response = requests.get(img['src']) # 요청한 이미지를 찾아와라 
#     # print(img_data) # 이미지 데이터가 2진 컴퓨터 언어로 출력됨 
#     img_data = img_response.content # 요청한 이미지에 있는 내용을 img_data에 할당한다.  
#     with open(file_path, "wb") as f: # os를 통해서 file_path에 할당된 경로로, 2진수 형식의 파일을 아랫줄 내용으로 생성해서(써서) 저장하라. 
#         f.write(img_data) # 내용: 요청한 이미지 데이터
#     # with문을 쓸 수 있기 위해 변수들을 만들어 줌. 
# # # 저장 하기 


    # 쓸 것이다 == 저장한다. 


# container = soup.find_all('img', attrs={'class':['rg_i Q4LuWd']})
# print(container)

# 셀레니움(selenium)
# 나중에 찾아보세요. 


# # enumerate 번호 붙여주는 이터러블 돌려서 
# li1 = ["김연아", "류현진", "손흥민"]
# for name in enumerate(li1):
#     print(name)
"""
(0, '김연아')
(1, '류현진')
(2, '손흥민')
"""



# 네이버 과학 뉴스 크롤링
import requests # 정보 요청
import os
from bs4 import BeautifulSoup # 객체 형태로 파싱해줌 
folder_name = "네이버 과학 뉴스"
file_name = f"{folder_name} 문서.txt"
if not os.path.exists(folder_name): # 만약 폴더네임이라는 폴더가 존재하지 않는다면 
    os.mkdir(folder_name) 
file_path = os.path.join(folder_name, file_name) # file_path에 folder_name과 file_name이 합쳐진 경로를 할당하라 
url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
# headers={"User-Agent": "Mozilla/5.0"} 크롤링 방지 회피 
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
html = response.text
soup = BeautifulSoup(html, "html.parser") # 객체화 했다. 
div = soup.body.find('div', attrs={'class': 'list_body'})
headlines = div.find_all('a', attrs={'class': 'cluster_text_headline'})

for headline in headlines:
    cont_text = headline.text.strip()
# # 텍스트 파일 만들어서 저장하세요~
    with open(file_path, "a", encoding='utf-8') as f:
        f.write(f"[[[[[[[{cont_text}]]]]]]]")
        f.write("\n")
    article_response = requests.get(headline['href'])
    article_soup = BeautifulSoup(article_response.text, "html.parser")
    article = article_soup.find('div', attrs={"id": "dic_area"})
    for article1 in article:
        cont_cont = article1.text.strip()
        with open(file_path, "a", encoding='utf-8') as f:
            f.write(cont_cont)
            f.write("\n") 
            f.write("\n") 

# pip install requests
# pip install BeautifulSoup
# 공식문서 찾아보면 자료가 있다. 

# 다음주: 5월 1일 별일 없이 와라. 목요일까지 열심히 하세요.. 
# 월요일부터 다른 선생님 // 오신다. 꾸준히 복습할 것!!!!  계속 쓸 거니까 자동으로 복습될 거고
# 학원에서는 프로젝트를 완성하는 것까지 진행하는데. 
# 현업에서는 프로젝트 마무리 경험이 많지 않다. 좋은 경험이 될 것이다. 
#  