# Automation with Selenium for Amazon.com

This project is a Python-based automation script that uses Selenium to automate the process of logging into Amazon.com, searching for specified items, adding them to the cart, filling in address details, and finally, deleting all items from the cart. This is achieved by executing a series of steps defined in the `AmazonBot` class and controlled through the `main.py` script.

## File Structure

- `AmazonBot.py`: Contains the `AmazonBot` class that defines all the actions to be performed on Amazon.com.
- `main.py`: The main script that initializes the `AmazonBot` object and performs the automation sequence.
- `data.json`: A configuration file containing user credentials, items to search, and address details.
- `README.md`: This file, providing an overview and instructions for the project.

## Requirements

- Python 3.x
- Selenium
- Chrome WebDriver

## Setup and Installation

1. **Clone the repository**:

   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install the required Python packages**:

   ```sh
   pip install selenium
   ```

3. **Download Chrome WebDriver**:

   - Ensure you have the Chrome browser installed.
   - Download the corresponding Chrome WebDriver from [here](https://developer.chrome.com/docs/chromedriver/downloads#chromedriver_1140573590).
   - Extract the WebDriver executable and place it in the same directory as your scripts or add it to your system PATH.

4. **Update `data.json`**:
   - Ensure the `data.json` file contains the correct user credentials, items, and address details.

## Usage

1. **Run the main script**:

   ```sh
   python main.py
   ```

   The script will:

   - Open Amazon.com.
   - Log in with the provided credentials.
   - Search and add the specified items to the cart.
   - Fill in the address details during checkout.
   - Delete all items from the cart.
   - Log out from Amazon.com.

## Important Notes

- **Ensure your credentials in `data.json` are correct and updated**: The script requires valid Amazon.com login credentials to perform the actions.
- **Handle your credentials securely**: Be cautious with sensitive information. Avoid sharing your `data.json` file with others.
- **Browser and WebDriver compatibility**: The script uses Chrome WebDriver. Ensure your Chrome browser and WebDriver versions are compatible.

## Troubleshooting

- If the script fails or encounters an error, check the log messages for details.
- Ensure your network connection is stable.
- Make sure the elements the script is trying to interact with have not changed. Amazon frequently updates its website, which might require updates to the XPaths and element locators in the `AmazonBot` class.

## Contributing

Feel free to fork the repository and submit pull requests for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
