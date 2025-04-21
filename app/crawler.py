from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback

def crawl_blog(cafe_name: str):
    print(f"[크롤링 시작] 카페 이름: {cafe_name}")

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    query = f"{cafe_name} 후기"
    driver.get(f"https://search.naver.com/search.naver?query={query}")

    try:
        # 블로그 탭 클릭
        blog_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "블로그"))
        )
        blog_tab.click()

        # 첫 번째 블로그 글 클릭
        blog_links = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.api_txt_lines.total_tit'))
        )
        if blog_links:
            print(f"[링크 클릭] {blog_links[0].text}")
            blog_links[0].click()
            driver.switch_to.window(driver.window_handles[-1])

            # 블로그 본문 긁기
            content = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div.se-main-container'))
            )
            print(f"\n📄 본문 내용 일부:\n{content.text[:300]}...\n")
        else:
            print("❌ 블로그 글 없음")
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        traceback.print_exc() 
    finally:
        driver.quit()
