# selenium_self_check

# (아직 수동인) 자동 건강상태 자가진단
https://hcs.eduro.go.kr/#/loginHome << chrome driver (selenium) 이용해서 자동으로 자가진단 해줌

**[그냥 재미로 만든거고 아직 테스트입니다.]**

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

압축을 풀어주신 다음에 `install.bat` 를 실행해주세요 (selenium 모듈 다운받아줌)

무슨 패키지를 다운받는지 알고싶으면 `requirements.txt` 를 확인해주세요

![image](https://user-images.githubusercontent.com/61219866/189472465-6fda4147-e130-4d46-82dc-8e0d57cf4ce5.png) ![image](https://user-images.githubusercontent.com/61219866/189472862-04f6d8c3-bf78-40c8-9b2e-1b67075fcd6a.png)

패키지를 다 다운받고 창이 닫아지면 다운로드가 완료된거임

# 3. json 개인정보 설정방법

`User_Information.json`파일을 열어주세요 (메모장으로 열어도 상광 없음)

`"only_read~" :` 는 읽기 전용 (수정 X)

#
**지역 [city]**

밑에 있는 표에서 `다니고 있는 학교의 시/도` 를 찾은 다음에, 옆에 있는 숫자를 아래있는 사진처럼 수정해주세요

![image](https://user-images.githubusercontent.com/61219866/189497476-ce582a8a-7da2-4647-a27f-6c0b7f9ada3b.png)

^^^위 사진은 예로 인천광역시를 선택했을떄^^^

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
#
**학교 레벨 [school_level]**

밑에 있는 표를 보고 다니고 있는 `학교의 레벨or학교급` 을 찾아서, 옆에 있는 숫자를 입력해주세요

![image](https://user-images.githubusercontent.com/61219866/189497389-62b7df52-093a-4ffb-932f-4f4390f4cd58.png)

^^^위 사진은 예로 중학교를 선택했을떄^^^

- 유치원 = 2
- 초등학교 = 3
- 중학교 = 4
- 고등학교 = 5
- 특수학교 등 = 6
#

**학교 이름 [shool_name]**

학교 이름은 정확하게 써주세요 (비슷한 이름 때문에 다른 학교로 선택될수도 있음)

![image](https://user-images.githubusercontent.com/61219866/189514989-7407d646-c1fc-4ea6-a349-c12042f34379.png)

#
**이름 [name]**

니 이름

![image](https://user-images.githubusercontent.com/61219866/189515082-aa12171e-bb25-4333-8098-a9453d52fa83.png)
#
**생년월일 [YYMMDD]**

ex) 2008년 6월 14일 이면 >> `080614` 적어주세요

![image](https://user-images.githubusercontent.com/61219866/189515151-b4193e44-be34-4fe9-99c0-45010c65620b.png)
#

**로그인 비밀번호 [password]**

자가진단 로그인할때 항상 쓰는 비밀번호 적어주세요

![image](https://user-images.githubusercontent.com/61219866/189515401-4b93409e-0953-40a9-8322-39f6ed57526d.png)

![passss](https://user-images.githubusercontent.com/61219866/189305084-e970eb47-37f0-484f-91d4-e8d396d370f8.png)
#
EX)
![image](https://user-images.githubusercontent.com/61219866/189515564-c92817ed-d82d-4a50-9ec6-fd8638e5bb7a.png)

그리고 마지막으로 `Ctrl + S` 를 눌러서 저장해주시고 닫아주시면, 개인정보 설정은 끝

# 4. 실행 방법

`install.bat` `requirements.txt` `LICENSE` `README.md` 은 지우셔도 상관없음

![image](https://user-images.githubusercontent.com/61219866/189515493-fc89bfc7-340c-436a-ab5a-4cf5cdd42e25.png)

이제 `run_script` 를 실행해주시면...

![image](https://user-images.githubusercontent.com/61219866/189515655-01869002-8908-410a-8b6a-073e84a6831d.png)

콘솔창과 크롬창이 뜨면서 자동으로 자가진단을 해줌

![image](https://user-images.githubusercontent.com/61219866/189515943-ba31377e-6dff-47c7-8c0f-f6916adb9ccb.png)
#
**콘솔창에 이런거 뜨는게 정상임**
![just_know](https://user-images.githubusercontent.com/61219866/189515967-833fa28d-ab84-412a-bd8f-b89b759c591f.png)
![jobb](https://user-images.githubusercontent.com/61219866/189516052-d20482fb-9af9-486e-8ccb-62b016b9df27.png)

# 5. 오류 발생시
업데이트나 자가진단 설문조사 목록이 변경되거나 등등.....

걍 안된다면 `Issues` 에다가 올려주세요 (콘솔에 적혀있는 오류랑 어느 부분에서 막혔는지 알려주셈, 사진으로 주면 좋고)
![image](https://user-images.githubusercontent.com/61219866/189516155-87747470-9ef2-4b0c-add3-17c444a6056f.png)
