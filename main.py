from AmazonBot import AmazonBot
import logging
import time

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

try:
    # Creating object for AmazonBot class and passing the JSON file parameter
    bot = AmazonBot(data_file='data.json')

    # Open Amazon website using selenium driver
    bot.open_amazon()

    # Wait for the website to load before login
    time.sleep(2)

    # Perform login
    bot.login()

    # Search and add multiple items to the cart
    for item in bot.items:
        bot.search_item(item)
        time.sleep(3)
        bot.select_item_add_to_cart()
        time.sleep(2)
        bot.driver.get("https://www.amazon.com/")  # Go back to the home page for the next search
        time.sleep(2)

    # Go to cart and checkout
    bot.go_to_cart()
    bot.check_out_items()
    bot.address_filling()
    bot.delete_cart_items()
    time.sleep(5)

    # Perform logout
    bot.logout()

except Exception as e:
    logging.error(f"An error occurred: {e}")
finally:
    # Close the browser
    if bot is not None:
        bot.close()
