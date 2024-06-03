from AmazonBot import *
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    # Creating object for AmazonBot class and passing file parameters
    bot = AmazonBot(credentials_file='credentials.txt', item_file='itemList.txt', form_file='form_items.txt')
    
    # Open Amazon website using selenium driver
    bot.open_amazon()
    
    # Wait for the website to load before login
    time.sleep(2)
    
    # 1st Login function called, from the AmazonBot class to perform login operation
    bot.login()
    
    bot.search_item()
    time.sleep(3)
    
    bot.select_item_add_to_cart()
    bot.go_to_cart()
    bot.check_out_items()
    bot.address_filling()
    time.sleep(5)
    
    # 1st Logout function is called
    bot.logout()
    
except Exception as e:
    logging.error(f"An error occurred: {e}")
finally:
    # Close the browser
    if bot is not None:
        bot.close()
