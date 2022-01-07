import io
import os

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from chromedriver_py import binary_path

from wikipedia import get_revision_ids
from chunk_image import make_horizontal
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

if os.getenv('debug'):
    chrome_options = Options()
    chrome_options.headless = True

else:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")

if os.getenv('debug'):
    service_object = Service(binary_path)
    driver = webdriver.Chrome(service=service_object, options=chrome_options)
else:
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

original_size = driver.get_window_size()


def screenshot(driver: webdriver.Chrome) -> bytes:
    required_width, required_height = driver.execute_script(
        'return [document.body.parentNode.scrollWidth, document.body.parentNode.scrollHeight]')
    driver.set_window_size(required_width, required_height)
    shot = driver.find_element(By.TAG_NAME, 'body').screenshot_as_png
    im = make_horizontal(Image.open(io.BytesIO(shot)))
    bytes = io.BytesIO()
    im.save(bytes, format='PNG')
    driver.set_window_size(original_size['width'], original_size['height'])
    return bytes.getvalue()


def screenshots(title, revision_ids):
    snapshot_url = f'https://en.wikipedia.org/w/index.php?title={title}'
    #revision_ids, timestamps = get_revision_ids(title)
    for page_id in reversed(revision_ids):
        page_id_param = f'&oldid={page_id}'
        driver.get(snapshot_url + page_id_param)
        driver.find_element(By.TAG_NAME, 'body')
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + screenshot(driver) + b'\r\n\r\n')



