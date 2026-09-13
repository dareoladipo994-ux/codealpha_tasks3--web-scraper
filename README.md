# Webpage Title Scraper (Task Automation)

## Overview
This Python script automates the process of extracting information from the web. It fetches a designated webpage, uses Regular Expressions (Regex) to locate the HTML `<title>` tag, and automatically saves the extracted title to a local text file. 

This project was built for **Task 3: Task Automation with Python Scripts** during the CodeAlpha Python Programming Internship.

## Features
* **HTTP Requests:** Utilizes the `requests` library to fetch the raw HTML content of a webpage.
* **Regex Parsing:** Uses Python's built-in `re` module to cleanly parse the webpage title without needing heavy external scraping libraries like BeautifulSoup.
* **File Handling:** Automatically generates a `scraped_title.txt` file and writes the extracted URL and title into it.

## Prerequisites
* Python 3.x installed on your machine.
* The `requests` library. Since it is not a built-in Python module, you will need to install it before running the script:

```bash
pip install requests
```

## How to Run
1. Clone this repository or download the Python script.
2. Open your terminal and navigate to the folder containing the script.
3. Run the application using the following command:
```bash
python web_scraper.py
```

4. Check your folder for a newly created file named `scraped_title.txt` to view your automated results!

## Acknowledgements
Developed as part of the Python Programming Internship at [CodeAlpha](https://www.codealpha.tech/).