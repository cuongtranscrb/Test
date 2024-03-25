import os
import sys

def create_chrome_profile():
    """
    This function creates a new profile in the Chrome browser.

    Returns:
    str: The name of the newly created profile or None if an error occurred.
    """
    try:
        # Import the necessary libraries
        import selenium
        from selenium.webdriver.chrome.options import Options

        # Check if the Chrome browser is installed
        if selenium.webdriver.common.is_chromium_present():
            # Get the path to the Chrome driver executable
            chrome_driver_path = selenium.webdriver.chrome.service.Service().path

            # Set the path to the new user data directory
            new_profile_path = os.path.join(os.getenv('TEMP'), 'new_profile')

            # Create the new user data directory
            if not os.path.exists(new_profile_path):
                os.makedirs(new_profile_path)

            # Set the options for creating a new profile
            options = Options()
            options.add_argument("--user-data-dir=%s" % new_profile_path)

            # Create a new Chrome driver instance with the specified options
            driver = selenium.webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=options)

            # Get the name of the newly created profile
            profile_name = driver.capabilities['chrome']['userDataDir']

            # Close the Chrome driver
            driver.quit()

            # Return the name of the newly created profile
            return profile_name
        else:
            # Log an error message if the Chrome browser is not installed
            print('Error: The Chrome browser is not installed on this machine.')

    except Exception as e:
        # Log the error
        print(f'Error: {e}')

    # Return None if an error occurred
    return None
