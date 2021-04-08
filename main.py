from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = r"C:\Users\Tweety\Desktop\Selenium\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url="https://www.linkedin.com/authwall?trk=gf&trkInfo=AQEbZk0DZoneGAAAAXiCf72oVBlE_NPYEMeg1J54-DUR-A7qDE8I_"
               "vS60RsX5U5K-saoSHUgRMediHFwxL_KKOvY2R6rF4tdjZKlMuR9EqL6EaN6bVmn8JPyV16H5yygFOm_r88=&originalReferer="
               "&sessionRedirect=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fsena-saltik-a3613820a%2F")

# login in your account
log_in = driver.find_element_by_xpath("/html/body/main/div/div/form[2]/section/p/a").click()
login_email = driver.find_element_by_id("login-email")
login_email.send_keys("ksenia790@mail.ru")

login_pass = driver.find_element_by_id("login-password")
login_pass.send_keys("hasbisait777")

login_submit = driver.find_element_by_id("login-submit").click()

# searching for job
time.sleep(5)
search = driver.find_element_by_xpath('//*[@id="ember18"]/input')
search.send_keys("python developer")
search.send_keys(Keys.ENTER)
time.sleep(10)
jobs_button = driver.find_element_by_css_selector("li.mr2 button").click()
time.sleep(10)
easy_apply_filter = driver.find_element_by_id("ember540").click()
time.sleep(5)
# applying for job
easy_apply = driver.find_element_by_css_selector("div.jobs-apply-button--top-card button").click()
phone_num = driver.find_element_by_id("urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2437929716,9,"
                                      "phoneNumber~nationalNumber)").send_keys("5538775561")
submit = driver.find_element_by_xpath('//*[@id="ember982"]/span').click()

driver.quit()
