from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
import random


class ActionClass():
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option(
            'excludeSwitches', ['enable-logging'])
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--mute-audio")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)

    def open_driver(self):
        self.driver.get('https://www.youtube.com')

    def close_driver(self):
        self.driver.close()

    def search_video(self, search_key):
        # Wait for the search input to be present and get the element
        search_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input#search')))

        # Clear value search input
        search_input.clear()

        # Add video key to search input
        sleep(random.randint(1, 2))
        search_input.send_keys(search_key)

        # Click search
        sleep(random.randint(1, 2))
        search_input.send_keys(Keys.ENTER)

    def chose_video(self, video_key):
        sleep(random.randint(2, 3))

        # Move to last video to load more videos
        last_video = self.wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, 'a[href][id="video-title"]')))[-1]
        self.actions.move_to_element(last_video).perform()

        sleep(random.randint(1, 2))

        # Find all videos that match the video key
        videos = self.driver.find_elements(
            By.CSS_SELECTOR, f'a[title*="{video_key}"][href*="shorts"]')

        if (len(videos) == 0):
            return False

        # Choose a random video from the list
        video_chosen = random.choice(videos)

        # Move to and click the chosen video
        self.actions.move_to_element(video_chosen).perform()
        sleep(random.randint(1, 2))
        video_chosen.click()

        return True

    def watch_video(self, min_time: int = 15, max_time: int = 20):
        sleep(random.randint(min_time, max_time))

    def watch_next_video(self):
        next_video_element = self.driver.find_element(
            By.CSS_SELECTOR, '#navigation-button-down button.yt-spec-button-shape-next')
        next_video_element.click()
        self.watch_video()

    def check_next_video_content(self, video_key):
        # Get current video
        current_video_element = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.ytd-shorts[is-active]')))

        next_video_id = int(current_video_element.get_attribute('id')) + 1

        # Get next video
        next_video_element = self.driver.find_element(
            By.CSS_SELECTOR, f'.ytd-shorts[id="{next_video_id}"]')

        # Get next video title
        try:
            next_video_element = self.driver.find_element(
                By.CSS_SELECTOR, f'.ytd-shorts[id="{next_video_id}"]')
            next_video_title = next_video_element.find_element(
                By.CSS_SELECTOR, 'h2.title.style-scope .style-scope').text
            return video_key in next_video_title
        except:
            return False

    def go_to_home_page(self):
        home_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a#logo')))
        self.actions.move_to_element(home_button).perform()
        sleep(random.randint(1, 2))
        home_button.click()
        sleep(random.randint(1, 2))
