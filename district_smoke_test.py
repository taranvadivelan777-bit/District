from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def scroll_down(driver, times=1):
    for _ in range(times):
        driver.swipe(500, 1600, 500, 600, 800)
        time.sleep(2)


def open_search(wait):
    wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.ID, "com.application.zomato.district:id/edit_text")
        )
    ).click()
    time.sleep(2)


def type_search(wait, text):
    field = wait.until(
        EC.presence_of_element_located(
            (AppiumBy.CLASS_NAME, "android.widget.EditText")
        )
    )
    field.clear()
    field.send_keys(text)
    time.sleep(3)


def main():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.udid = "emulator-5554"
    options.no_reset = True
    options.new_command_timeout = 300

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    wait = WebDriverWait(driver, 30)

    try:
        driver.activate_app("com.application.zomato.district")
        time.sleep(4)

        # ================= RAJA SAAB =================
        open_search(wait)
        type_search(wait, "Raja Saab")
        driver.tap([(118, 567)])
        time.sleep(3)

        # scroll_down(driver, 2)

        wait.until(
            EC.presence_of_element_located(
                (AppiumBy.ID, "com.application.zomato.district:id/radio_button")
            )
        ).click()
        time.sleep(2)

        wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, "com.application.zomato.district:id/primary_button")
            )
        ).click()
        time.sleep(3)

        scroll_down(driver, 3)

        driver.back()
        time.sleep(2)
        driver.back()
        time.sleep(2)
    
        # ================= PARA SAKTHI =================
        open_search(wait)
        type_search(wait, "Para Sakthi")
        driver.tap([(118, 567)])
        time.sleep(3)

        scroll_down(driver, 2)

        driver.back()
        time.sleep(2)

        # ================= JANA NAYAGAN =================
        open_search(wait)
        type_search(wait, "Jana Nayagan")
        driver.tap([(118, 567)])
        time.sleep(3)

        scroll_down(driver, 1)

        driver.back()
        time.sleep(2)

        # ================= DINING =================
        driver.tap([(265, 382)])  # Dining tab bounds
        time.sleep(3)

        # ---------- NANDANA PALACE ----------
        open_search(wait)
        type_search(wait, "Nandana Palace")
        driver.tap([(118, 572)])
        time.sleep(3)

        scroll_down(driver, 2)

        driver.tap([(500, 1200)])  # Menu image
        time.sleep(2)

        for _ in range(5):
            driver.tap([(980, 1200)])
            time.sleep(2)

        driver.back()
        time.sleep(2)
        driver.back()
        time.sleep(2)

        # ---------- BARBEQUE NATION ----------
        open_search(wait)
        type_search(wait, "Barbeque Nation")
        driver.tap([(118, 572)])
        time.sleep(3)

        scroll_down(driver, 3)

        # Book a table (TextView – bounds)
        driver.tap([(540, 2266)])  # [43,2236][1037,2296]
        time.sleep(3)

        # Continue button
        try:
            wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.ID, "com.application.zomato.district:id/bottom_button")
                )
            ).click()
        except:
            driver.tap([(540, 2260)])  # bounds fallback

        time.sleep(3)

        # Back to Home
        driver.back()
        time.sleep(2)
        driver.back()
        time.sleep(2)
        driver.back()
        driver.back()

        print("✅COMPLETED SUCCESSFULLY")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
