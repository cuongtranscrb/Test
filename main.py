def create_chrome_profile():
    """
    This function creates a new profile in the Chrome browser.

    Returns:
    str: The name of the newly created profile
    """
    try:
        # Import the necessary libraries
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options

        # Set the path to the Chrome driver executableT
        chrome_driver_path = 'chromedriver.exe'

        # Set the options for creating a new profile
        options = Options()
        options.add_argument("--user-data-dir=/path/to/new_profile")

        # Create a new Chrome driver instance with the specified options
        driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=options)

        # Get the name of the newly created profile
        profile_name = driver.capabilities['chrome']['userDataDir']

        # Close the Chrome driver
        driver.quit()

        # Return the name of the newly created profile
        return profile_name
    except Exception as e:
        # Log the error
        print(f"Error: {e}")
        return None