from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json,time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome()
print('█░░█ █▀▀ █░░ █░░ █▀▀█   █░░░█ █▀▀█ █▀▀█ █░░ █▀▀▄ █\n█▀▀█ █▀▀ █░░ █░░ █░░█   █▄█▄█ █░░█ █▄▄▀ █░░ █░░█ ▀\n▀░░▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀   ░▀░▀░ ▀▀▀▀ ▀░▀▀ ▀▀▀ ▀▀▀░ ▄')
print('테스트입니다!')

driver.get('https://hcs.eduro.go.kr/#/loginHome')
time.sleep(0.5) #페이지 로딩
print('- Page loaded.')
driver.find_element(By.XPATH, '//*[@id="btnConfirm2"]').click() #GO 버튼 클릭

time.sleep(0.5) #페이지 로딩
driver.find_element(By.XPATH, '//*[@id="schul_name_input"]').click() #검색 버튼 클릭

with open("User_Information.json", encoding='utf-8') as f: #User_Information.json에 있는 개인정보 가져오기
    data = json.load(f)
driver.find_element(By.XPATH, '//*[@id="sidolabel"]/option['+ data['city'] +']').click() #서울특별시 클릭
driver.find_element(By.XPATH, '//*[@id="crseScCode"]/option['+ data['school_level'] +']').click() #중학교 클릭
school = driver.find_element(By.XPATH, '//*[@id="orgname"]') #학교 검색창 찾기
school.send_keys(data['shool_name'] + Keys.ENTER) #학교 검색창에다.윤중중학교 타이핑하고 엔터
time.sleep(0.5) #학교들 조회중...
driver.find_element(By.XPATH, '//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li[1]/a').click() #첫번째 학교 클릭
driver.find_element(By.XPATH, '//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click() #학교 선택 버튼 클릭

time.sleep(0.2) #ㅈ같은 js 애니매이션 (사이트 어떤새끼가 만들었냐)
driver.find_element(By.ID, 'user_name_input').send_keys(data['name']) #성명창에다 이름 타이핑
driver.find_element(By.ID, 'birthday_input').send_keys(data['YYMMDD']) #생년월일창에다 출생 타이핑
driver.find_element(By.XPATH, '//*[@id="WriteInfoForm"]/table/tbody/tr[4]/td/div/button').click() #보안키패드 창 클릭

time.sleep(0.2) #ㅈ같은 애니매이션 만들지 마라(cpu가 아깝다)
jsonpass = data['password']
driver.find_element(By.CSS_SELECTOR, '[aria-label="' + jsonpass[0] + '"]').click() #첫번째 비밀번호 클릭
driver.find_element(By.CSS_SELECTOR, '[aria-label="' + jsonpass[1] + '"]').click() #두번째 비밀번호 클릭
driver.find_element(By.CSS_SELECTOR, '[aria-label="' + jsonpass[2] + '"]').click() #세번째 비밀번호 클릭
driver.find_element(By.CSS_SELECTOR, '[aria-label="' + jsonpass[3] + '"]').click() #네번째 비밀번호 클릭

time.sleep(0.2) #또또 ㅈ같은 애니매이션 만들지 말라고(cpu가 아깝다)
driver.find_element(By.XPATH, '//*[@id="btnConfirm"]').click() #로그인 완료 버튼 클릭
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="container"]/div/section[2]/div[2]/ul/li/a[1]').click()  #자가진단 설문조사 버튼 클릭
time.sleep(1.5)
driver.find_element(By.XPATH, '//*[@id="survey_q1a1"]').click() #자가진단중..
driver.find_element(By.XPATH, '//*[@id="survey_q2a3"]').click() #자가진단중....
driver.find_element(By.XPATH, '//*[@id="survey_q3a1"]').click() #자가진단중.......
driver.find_element(By.XPATH, '//*[@id="btnConfirm"]').click() #자가진단중!
print('- DONE.') #종료를 알리는 print MOON

time.sleep(4)

page_source = driver.page_source