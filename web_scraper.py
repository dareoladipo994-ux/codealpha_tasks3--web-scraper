import requests
import re

def scrape_title_and_save():
    url = "https://youtube.com"
    
    try:
        response = requests.get(url)
        response.raise_for_status() 
        html_content = response.text
        
        match = re.search(r'<title>(.*?)</title>', html_content, re.IGNORECASE)
        
        if match:
            title = match.group(1)
            print(f"Successfully scraped title: {title}")
            
            with open("scraped_title.txt", "w", encoding="utf-8") as file:
                file.write(f"URL: {url}\n")
                file.write(f"Page Title: {title}\n")
            print("Title saved to 'scraped_title.txt'.")
        else:
            print("No title tag could be found on this webpage.")
            
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while trying to fetch the webpage: {e}")

if __name__ == "__main__":
    scrape_title_and_save()