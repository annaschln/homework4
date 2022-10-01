from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import random
import string

def build_driver():
    # Set up the driver
    return webdriver.Chrome(ChromeDriverManager().install())


def check_exists_by_xpath(driver, xpath):
    try:
        x = driver.find_element(By.XPATH, xpath)
        if x.is_displayed():
            return 1
    except NoSuchElementException:
        return 0

def welcome_page(driver):
    # scroll down
    driver.execute_script("window.scrollTo(0, 200);")
    # driver.implicitly_wait(5)
    # Give input to the entry question - find the element by its id
    entry_question_id = 'id_entry_question'
    entry_question_input = 'Testing Input for Entry Question'
    driver.find_element(By.ID, entry_question_id).send_keys(entry_question_input)
    # eligible
    eligible = driver.find_elements(By.NAME, 'eligible_question')
    rand_selection1 = random.randint(0, len(eligible) - 1)
    # rand_selection = random.randint(0,1)
    eligible[rand_selection1].click()
    # age
    age = driver.find_elements(By.NAME, 'age_question')
    rand_selection2 = random.randint(0, len(age) - 1)
    # rand_selection = random.randint(0, 2)
    age[rand_selection2].click()
    # gender
    gender = driver.find_elements(By.NAME, 'gender')
    rand_selection3 = random.randint(0, len(gender) - 1)
    # rand_selection = random.randint(0, 3)
    gender[rand_selection3].click()
    # next button
    driver.find_element(By.XPATH, '//*[@id ="form"]/div/button').click()
    return rand_selection1, rand_selection2, rand_selection3


def demo_page(driver):
    # scroll down
    driver.execute_script("window.scrollTo(0, 200);")
    # xpath = "//*[@id='id_age_question']"
    # age = random.randint(1,30)
    # driver.find_element(By.XPATH, xpath).send_keys(str(age))
    # gender field
    # gender = driver.find_elements(By.NAME, 'gender')
    # rand_selection = random.randint(0, len(gender) - 1)
    # gender[rand_selection].click()
    # wait
    vote = driver.find_elements(By.NAME, 'eligibility')
    rand_selection = random.randint(0, len(vote) - 1)
    # rand_selection = random.randint(0, 1)
    vote[rand_selection].click()
    # favourite day
    day = driver.find_elements(By.NAME, 'day')
    rand_selection = random.randint(0, len(day) - 1)
    # rand_selection = random.randint(0, 7)
    day[rand_selection].click()

    # please elaborate
    elaborate_question_id = 'id_elaborate_question'
    elaborate_question_input = 'Testing Input for Elaborate Question'
    driver.find_element(By.ID, elaborate_question_id).send_keys(elaborate_question_input)

    # next
    driver.find_element(By.XPATH, '//*[@id ="form"]/div/button').click()

def onlyOneGroup(driver):
    # scroll down
    driver.execute_script("window.scrollTo(0, 500);")
    driver.set_page_load_timeout(5)
    # driver.implicitly_wait(5)
    # element = driver.find_element_by_xpath('//*[@id ="form"]/div/button')
    # driver.execute_script("return arguments[0].scrollIntoView(0, document.documentElement.scrollHeight-10);", element)
    # Find the element by its tag
    driver.find_element(By.TAG_NAME, 'button').click()

def Sunday_popout (driver):
    # two radio buttons
    yes = '//*[@id="merkelYes"]'
    no = '//*[@id="merkelNo"]'
    select = random.randint(0, 1)
    input_text = ''.join(random.choice(string.ascii_letters) for i in range(random.randint(1, 10)))
    if select == 0:
        driver.find_element(By.XPATH, yes).click()
        # are you sure
        driver.find_element(By.XPATH, '//*[@id="divYes"]/input').send_keys(input_text)
    else:
        driver.find_element(By.XPATH, no).click()
        # what do you have against sundays
        driver.find_element(By.XPATH, '//*[@id="divNo"]/input').send_keys(input_text)
    # next button
    driver.find_element(By.XPATH, '//*[@id = "form"]/div/button').click()


def end_of_survey(driver):
    # submit button
    driver.find_element(By.XPATH, '//*[@id = "form"]/div/button').click()


def run_bots(no_times, link):
    driver = build_driver()  # initialize the driver
    for i in range(no_times):  # go through the survey several times
        driver.get(link)  # open the browser to the url of your survey
        # check if one can do the survey(e.g. if quota is full start page is not shown
        if check_exists_by_xpath(driver, "//*[@id='id_entry_question']") == 1:
            x = welcome_page(driver) # check whether they are eligible
            if x == 0 and rand_selection2 == 3:  # then they are not eligible, otherwise no next page ... rand_selection1 != 2
                continue
        demo_page(driver) # demo-page(age, gender etc)
        if check_exists_by_xpath(driver, '// *[ @ id = "form"] / div / p[1] / b') == 1:
            continue
        # check if extra site is shown to you
        if check_exists_by_xpath(driver, '//*[@id="form"]/div/h1') == 1: #from h3
            onlyOneGroup(driver)
        Sunday_popout(driver)
        end_of_survey(driver)
    print("Success!")
# this is the session wide link
link = 'http://localhost:8000/join/dulapopi'
run_bots(no_times=10, link=link)
