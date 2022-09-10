# selenium_self_check

# (아직 수동인) 자동 건강상태 자가진단
https://hcs.eduro.go.kr/#/loginHome << chrome driver (selenium) 이용해서 자동으로 자가진단 해줌

[그냥 재미로 만든거고 아직 테스트입니다.]

(추후에 서버에 저장하고 특정 시간에 실행하거나, 앱으로 실행 가능하게 제작하겠습니다)

# 1. 파이썬(Python) 설치 방법 [필수]

https://www.python.org/downloads/release/python-3913/ << 여기서 자기 컴퓨터에 맞는걸로 깔아주세요 (3.9 ~ 버전 권장)

   `Windows installer (64-bit)` 추천

![pyinstall](https://user-images.githubusercontent.com/61219866/189373384-7a5984d4-371a-4c65-b613-31431451b953.png)



**`Add Python 3.9 to PATH` 체크해주세요, 필수입니다**

![python_install](https://user-images.githubusercontent.com/61219866/189372511-e5ce77e6-6c7e-4f0a-869a-3a6cf1809a54.png)


# 2. 소스 코드 다운로드, 세팅

`Code`를 클릭하신 다음에 `Download ZIP` 를 눌러주세요

![githubDOWN](https://user-images.githubusercontent.com/61219866/189377601-923f0c70-1fa8-4aff-ae50-d9bbb8a91a8b.png)

압축을 풀어주신 다음에 `install.bat` 를 실행해주세요 (파이썬 패키지를 다운받아줌)

무슨 패키지를 다운받는지 알고싶으면 `requirements.txt` 를 확인해주세요

![image](https://user-images.githubusercontent.com/61219866/189472465-6fda4147-e130-4d46-82dc-8e0d57cf4ce5.png) ![image](https://user-images.githubusercontent.com/61219866/189472862-04f6d8c3-bf78-40c8-9b2e-1b67075fcd6a.png)

패키지를 다 다운받고 창이 닫아지면(다운로드 완료된거임) `install.bat` `requirements.txt` `LICENSE` 은 지우셔도 상관없음

![image](https://user-images.githubusercontent.com/61219866/189483098-33ce31cd-a758-4681-b239-1856eb520a6c.png)

# json 개인정보 설정방법

`User_Information.json`파일을 열어주세요 (메모장으로 열어도 상광 없음)

![image](https://user-images.githubusercontent.com/61219866/189483568-f66a2937-60dc-4c21-ab67-b1594789adda.png)

![image](https://user-images.githubusercontent.com/61219866/189487715-049478f9-b74b-45f4-8598-70e70a4dd765.png)


**지역**
- 서울특별시 = 2
- 부산광역시 = 3
- 대구광역시 = 4
- 인천광역시 = 5
- 광주광역시 = 6
- 대전광역시 = 7
- 울산광역시 = 8
- 세종특별자치시 = 9
- 경기도 = 10
- 강원도 = 11
- 충청북도 = 12
- 충청남도 = 13
- 전라북도 = 14
- 전라남도 = 15
- 경상북도 = 16
- 경상남도 = 17
- 제주특별자치도 = 18

**학교 레벨**
- 유치원 = 2
- 초등학교 = 3
- 중학교 = 4
- 고등학교 = 5
- 특수학교 등 = 6

**학교 이름은 정확하게 써주세요** (다른 학교로 선택될수도 있음)

**자기 이름**

**생년월일 써주세요** ex) 2008년 6월 14일 이면 >> `080614` 적어주세요

![passss](https://user-images.githubusercontent.com/61219866/189305084-e970eb47-37f0-484f-91d4-e8d396d370f8.png)

**자가진단 로그인할때 항상 쓰는 비밀번호 입력**


