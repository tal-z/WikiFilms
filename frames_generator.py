import io

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.chrome.options import Options
from chromedriver_py import binary_path

from wikipedia import get_revision_ids
from chunk_image import make_horizontal
from PIL import Image
options = Options()
options.headless = True


def screenshot(driver: webdriver.Chrome) -> bytes:
    original_size = driver.get_window_size()
    required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
    required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    driver.set_window_size(required_width, required_height)
    shot = driver.get_screenshot_as_png()
    im = make_horizontal(Image.open(io.BytesIO(shot)))
    bytes = io.BytesIO()
    im.save(bytes, format='PNG')
    driver.set_window_size(original_size['width'], original_size['height'])
    return bytes.getvalue()


def screenshots(title, options=options):
    service_object = Service(binary_path)
    driver = webdriver.Chrome(service=service_object, options=options)
    snapshot_url = f'https://en.wikipedia.org/w/index.php?title={title}'
    revision_ids, timestamps = get_revision_ids(title)
    for page_id in reversed(revision_ids):
        page_id_param = f'&oldid={page_id}'
        driver.get(snapshot_url + page_id_param)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + screenshot(driver) + b'\r\n\r\n')



