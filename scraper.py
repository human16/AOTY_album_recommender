from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def find_user_ratings(user_name):
    driver = webdriver.Chrome()
    driver.get(f"https://www.albumoftheyear.org/user/{user_name}/ratings/")
    ratings = driver.find_element(By.ID, "albumOutput")
    collecting_ratings = []
    for rating in ratings.find_elements(By.CLASS_NAME, "albumBlock"):
        collecting_ratings.append((rating.find_element(By.TAG_NAME, "a").get_attribute("href"), rating.text.split("\n")))

    print(collecting_ratings)



#used to test the functions found in this file.
if __name__ == "__main__":
    user_name = input("Enter your AOTY username: ")
    
    find_user_ratings(user_name)
