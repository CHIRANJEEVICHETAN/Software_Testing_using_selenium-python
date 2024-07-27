from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import json
import time


class AmazonBot:

    def __init__(self, data_file):
        """
        Initialize the AmazonBot with credentials, item, and form details.
        """
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.load_data(data_file)

    def load_data(self, file_path):
        """
        Load data from a JSON file.
        """
        with open(file_path, 'r') as file:
            data = json.load(file)
            self.email = data['credentials']['email']
            self.password = data['credentials']['password']
            self.items = data['items']
            form = data['form']
            self.name = form['name']
            self.phone = form['phone']
            self.address = form['address']
            self.addresses = form['addresses']
            self.city = form['city']
            self.state = form['state']
            self.zip = form['zip']

    def open_amazon(self):
        """
        Open the Amazon website and prepare the browser.
        """
        try:
            self.driver.get("https://www.amazon.com/")
            self.driver.delete_all_cookies()
            self.driver.maximize_window()
        except Exception as e:
            print(f"Error opening Amazon: {e}")

    def login(self):
        """
        Perform the login action.
        """
        try:
            login_page = self.driver.find_element(
                By.XPATH,
                "/html/body/div[1]/header/div/div[1]/div[3]/div/a[2]/div/span")
            login_page.click()
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.NAME, "email")))
            login_email = self.driver.find_element(By.NAME, "email")
            login_email.send_keys(self.email)
            login_continue = self.driver.find_element(By.ID, "continue")
            login_continue.click()
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.NAME, "password")))
            login_password = self.driver.find_element(By.NAME, "password")
            login_password.send_keys(self.password)
            login_success = self.driver.find_element(By.ID, "signInSubmit")
            login_success.click()
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "nav-logo-sprites")))
        except Exception as e:
            print(f"Error during login: {e}")

    def logout(self):
        """
        Perform the logout action.
        """
        try:
            home = self.driver.find_element(By.ID, "nav-logo-sprites")
            home.click()
            hamBurger = self.driver.find_element(By.ID, "nav-hamburger-menu")
            hamBurger.click()
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "hmenu-content")))
            scroll_bar = self.driver.find_element(By.ID, "hmenu-content")
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight",
                scroll_bar)
            time.sleep(1)
            button = self.driver.find_element(
                By.XPATH, "/html/body/div[3]/div[2]/div/ul[1]/li[25]/a")
            button.click()
            time.sleep(3)
            self.driver.back()
            time.sleep(1)
            self.driver.refresh()
        except Exception as e:
            print(f"Error during logout: {e}")

    def search_item(self, item):
        """
        Search for the item specified.
        """
        try:
            search_box = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.ID, "twotabsearchtextbox")))
            search_box.send_keys(item)
            time.sleep(1)
            search_box.send_keys(Keys.ENTER)
        except Exception as e:
            print(f"Error searching for item: {e}")

    def select_item_add_to_cart(self):
        """
        Select the item from the search results and add it to the cart.
        """
        try:
            # Attempt to find the primary element
            select_item = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/span/div/div/div/div[1]/div/div[2]/div/span/a/div")
                )
            )
            select_item.click()
            print("Primary element clicked.")
            cart_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "add-to-cart-button"))
            )
            cart_button.click()
            print("Item added to cart.")
        except (TimeoutException, NoSuchElementException):
            print("Primary element not found, trying alternative element.")
            try:
                # Attempt to find the alternate element if the primary is not found
                alternate_item = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located(
                        (By.ID, "a-autoid-1-announce")
                    )
                )
                alternate_item.click()
                print("Alternate element clicked.")
            except (TimeoutException, NoSuchElementException):
                print("Alternate element also not found.")
                return  # Neither element was found, stopping further execution
            except Exception as e:
                print(f"Error with alternate item: {e}")
                return
        except Exception as e:
            print(f"Error opening the Product: {e}")

    def go_to_cart(self):
        """
        Navigate to the shopping cart.
        """
        try:
            cart_button = self.driver.find_element(By.ID, "nav-cart-count")
            cart_button.click()
            time.sleep(2)
        except Exception as e:
            print(f"Error going to cart: {e}")

    def check_out_items(self):
        """
        Proceed to checkout.
        """
        try:
            proceed_to_check_out = self.driver.find_element(
                By.NAME, "proceedToRetailCheckout")
            proceed_to_check_out.click()
            time.sleep(2)
        except Exception as e:
            print(f"Error checking out items: {e}")

    def address_filling(self):
        """
        Fill in the address form during checkout.
        """
        try:
            self._change_address()
            self._fill_address_form()
            self._save_address()
            self._skip_address_verification()
            self._continue_to_checkout()
            self._navigate_back()
        except Exception as e:
            print(f"Error filling address: {e}")

    def _change_address(self):
        change_Address_button = self.driver.find_element(
            By.ID, "addressChangeLinkId")
        change_Address_button.click()
        add_new_address_button = self.driver.find_element(
            By.ID, "add-new-address-popover-link")
        add_new_address_button.click()
        time.sleep(3)

    def _fill_address_form(self):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.XPATH,
                "/html/body/div[8]/div/div/div/div/form/div/div[7]/div/div[2]/span/span/span/span"
            )))
        dropdown.click()
        dropdown_item = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.ID,
                 "address-ui-widgets-countryCode-dropdown-nativeId_102")))
        dropdown_item.click()
        time.sleep(2)
        full_name = self.driver.find_element(
            By.NAME, "address-ui-widgets-enterAddressFullName")
        full_name.send_keys(self.name)
        time.sleep(3)
        phone_num = self.driver.find_element(
            By.NAME, "address-ui-widgets-enterAddressPhoneNumber")
        phone_num.send_keys(self.phone)
        time.sleep(3)
        address_1 = self.driver.find_element(
            By.ID, "address-ui-widgets-enterAddressLine1")
        address_1.send_keys(self.address)
        address_2 = self.driver.find_element(
            By.ID, "address-ui-widgets-enterAddressLine2")
        address_2.send_keys(self.addresses)
        city_name = self.driver.find_element(
            By.ID, "address-ui-widgets-enterAddressCity")
        city_name.send_keys(self.city)
        state_name = self.driver.find_element(
            By.ID, "address-ui-widgets-enterAddressStateOrRegion")
        state_name.send_keys(self.state)
        zip_code = self.driver.find_element(
            By.ID, "address-ui-widgets-enterAddressPostalCode")
        zip_code.send_keys(self.zip)

    def _save_address(self):
        use_this_address = self.driver.find_element(
            By.XPATH,
            "/html/body/div[8]/div/div/div/div/form/div/span[3]/span/span/input"
        )
        use_this_address.click()
        time.sleep(1)
        save_the_address = self.driver.find_element(
            By.NAME, "address-ui-widgets-saveOriginalOrSuggestedAddress")
        save_the_address.click()

    def _skip_address_verification(self):
        skip_address = self.driver.find_element(
            By.ID, "kyc_xborder_skip_section_label")
        skip_address.click()
        time.sleep(1)

    def _continue_to_checkout(self):
        continue_address = self.driver.find_element(
            By.XPATH,
            "/html/body/div[5]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[4]/div/div[3]/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/div/form/div/span/span/span/input"
        )
        continue_address.click()
        time.sleep(2)

    def _navigate_back(self):
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        time.sleep(1)
    
    def delete_cart_items(self):
        """
        Delete all items in the cart and redirect to the Amazon home page.
        """
        try:
            # Loop until no more items are found
            while True:
                # Find all delete buttons in the cart
                delete_buttons = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div[4]/div[4]/div/div[2]/div[1]/div/form/div[2]/div[3]/div[4]/div/div[3]/div[1]/span[2]/span/input")

                # Check if there are any delete buttons
                if not delete_buttons:
                    break

                # Click each delete button
                for button in delete_buttons:
                    button.click()
                    # Wait for a short period to ensure the item is deleted
                    time.sleep(2)

                # Refresh the page to update the cart
                self.driver.refresh()
                # Wait for the cart to update
                time.sleep(2)

            # Once all items are deleted, navigate to the Amazon home page
            self.driver.get("https://www.amazon.com/")
            time.sleep(2)

        except Exception as e:
            print(f"Error deleting items from cart: {e}")

    

    def close(self):
        """
        Close the browser and end the session.
        """
        self.driver.quit()
