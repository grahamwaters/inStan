import selenium
import json
import time
import logging
import random
import csv

# Read config from config.json
with open("config/config.json") as config_file:
    config = json.load(config_file)

# Scrape popular accounts with #art and #painting hashtags
def scrape_accounts(driver):
    # Use Selenium to scrape Instagram website
    # step 1: navigate to Instagram website
    # step 2: enter #art and #painting hashtags
    # step 3: click search button
    # step 4: wait for search results to load
    # step 5: find the first account in the search results
    # step 6: click on the first account
    # step 7: wait for the account page to load
    # step 8: find the number of followers for the account
    # step 9: find the number of posts for the account
    # step 10: find the account's handle
    # step 11: log the account's handle, number of followers, and number of posts
    pass

# Login to Instagram account
def login(driver, username, password):
    # Use Selenium to login to Instagram account
    # step 1: navigate to Instagram login page
    driver.get("https://www.instagram.com/accounts/login/")
    # step 2: enter username
    # find username input field
    username_input = driver.find_element_by_name("username")
    # enter username
    username_input.send_keys(username)
    # step 3: enter password
    # find password input field
    password_input = driver.find_element_by_name("password")
    # enter password
    time.sleep(random.randint(1, 3))
    password_input.send_keys(password)
    # step 4: click login button
    # find login button
    login_button = driver.find_element_by_xpath("//button[@type='submit']")
    # click login button
    time.sleep(random.randint(1, 6))
    login_button.click()
    # step 5: wait for login to complete
    time.sleep(5)

def read_account_handles():
    handles = []
    with open('accounts_to_stan.csv', 'r') as csvfile:
        accounts_reader = csv.reader(csvfile, delimiter=',')
        for row in accounts_reader:
            handles.append(row[0])
    return handles


# Repost content from target account
def repost(handle, driver):
    """
    In this example, the repost() function takes in a single argument, the handle of the account that the user wants to repost content from. The function uses Selenium to navigate to the account's page, wait for the page to load, find the first post on the account's page, click on the first post, wait for the post to open, and find the repost button. Once the repost button is clicked, the function waits for the repost modal to open, finds the button to repost to the user's own profile, and clicks on it. Finally, the function waits for the repost to complete and logs the reposted content.
    """
    # Use Selenium to navigate to the account's page
    driver.get(f"https://www.instagram.com/{handle}/")

    # Wait for the page to load
    time.sleep(5)

    # Find the first post on the account's page
    first_post = driver.find_element_by_css_selector("div._9AhH0")

    # Click on the first post
    first_post.click()

    # Wait for the post to open
    time.sleep(5)

    # Find the repost button
    repost_button = driver.find_element_by_xpath("//span[text()='Share']")

    # Click on the repost button
    repost_button.click()

    # Wait for the repost modal to open
    time.sleep(5)

    # Find the repost to own profile button
    repost_to_own_profile_button = driver.find_element_by_xpath("//button[text()='Repost to Your Profile']")

    # Click on the repost to own profile button
    repost_to_own_profile_button.click()

    # Wait for the repost to complete
    time.sleep(5)

    # Log the reposted content
    logging.info(f"Reposted content from account: {handle}")


# Main function to run the bot
def main():
    driver = selenium.webdriver.Chrome(config["chromedriver_path"])
    login(driver, config["username"], config["password"])
    handles = read_account_handles()
    for handle in handles:
        print(f"Reposting content from account: {handle}")
        repost(handle, driver)
    driver.close()


if __name__ == "__main__":
    main()
