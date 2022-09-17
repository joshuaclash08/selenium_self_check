from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json,time
chrome_options = Options()
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get('https://hcs.eduro.go.kr/#/loginHome')
print('- Page loaded. \n- 테스트 전용')
wait = WebDriverWait(driver, 10) #10초 동안 기도하기
driver.find_element(By.XPATH, '//*[@id="btnConfirm2"]').click() #GO 버튼 클릭
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="schul_name_input"]'))) #학교 검색 clickable 될때까지 대기
driver.find_element(By.XPATH, '//*[@id="schul_name_input"]').click() #학교 검색 버튼 클릭
with open("User_Information.json", encoding='utf-8') as f: #User_Information.json에 있는 개인정보...
  data = json.load(f) #가지고 옴 ㅋ
driver.find_element(By.XPATH, '//*[@id="sidolabel"]/option['+ data['city'] +']').click() #서울특별시 클릭
driver.find_element(By.XPATH, '//*[@id="crseScCode"]/option['+ data['school_level'] +']').click() #중학교 클릭
school = driver.find_element(By.XPATH, '//*[@id="orgname"]') #학교 검색창 찾기
school.send_keys(data['shool_name'] + Keys.ENTER) #학교 검색창에다.윤중중학교 타이핑하고 엔터
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li[1]/a'))) #첫번쨰 학교 clickable 될때까지 대기
driver.find_element(By.XPATH, '//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li[1]/a').click() #첫번째 학교 클릭
driver.find_element(By.XPATH, '//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click() #학교 선택 버튼 클릭
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnConfirm"]'))) #로그인 완료 clickable 될때까지 대기
driver.find_element(By.ID, 'user_name_input').send_keys(data['name']) #성명창에다 이름 타이핑
driver.find_element(By.ID, 'birthday_input').send_keys(data['YYMMDD']) #생년월일창에다 출생 타이핑
driver.find_element(By.XPATH, '//*[@id="WriteInfoForm"]/table/tbody/tr[4]/td/div/button').click() #보안키패드 창 클릭
jsonpass = data['password']
driver.find_element(By.CSS_SELECTOR, '[aria-label="' + jsonpass[0] + '"]').click() #첫번째 비밀번호 클릭
driver.find_element(By.CSS_SELECTOR, '[aria-label="' + jsonpass[1] + '"]').click() #두번째 비밀번호 클릭
driver.find_element(By.CSS_SELECTOR, '[aria-label="' + jsonpass[2] + '"]').click() #세번째 비밀번호 클릭
driver.find_element(By.CSS_SELECTOR, '[aria-label="' + jsonpass[3] + '"]').click() #네번째 비밀번호 클릭
driver.find_element(By.XPATH, '//*[@id="btnConfirm"]').click() #로그인 완료 버튼 클릭
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div/section[2]/div[2]/ul/li/a[1]'))) #자가진단 설문조사 clickable 될때까지 대기
driver.find_element(By.XPATH, '//*[@id="container"]/div/section[2]/div[2]/ul/li/a[1]').click() #자가진단 설문조사 버튼 클릭
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnConfirm"]'))) #자가진단중(?) clickable 될때까지 대기
driver.find_element(By.XPATH, '//*[@id="survey_q1a1"]').click() #자가진단중..
driver.find_element(By.XPATH, '//*[@id="survey_q2a3"]').click() #자가진단중....
driver.find_element(By.XPATH, '//*[@id="survey_q3a1"]').click() #자가진단중.......
driver.find_element(By.XPATH, '//*[@id="btnConfirm"]').click() #자가진단중!
print('- DONE. \n- https://github.com/joshuaclash08') #종료를 알리는 print MOON
time.sleep(1)
driver.close()
