# download_rivian_reports.py

import requests
from bs4 import BeautifulSoup
import os

# URL of Rivian's investor page (example URL)
url = "https://rivian.com/investors"

def download_latest_report():
    # Fetch the page content
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find document links that contain "Shareholder_Letter" in the href attribute
    links = soup.find_all('a', href=True)
    for link in links:
        if 'Shareholder_Letter' in link['href']:  # Adjust as needed
            file_url = link['href']
            if not file_url.startswith("http"):  # Handle relative URLs
                file_url = f"https://rivian.com{file_url}"
            
            file_name = os.path.basename(file_url)
            print(f"Downloading {file_name} from {file_url}")
            
            # Download the file if not already downloaded
            if not os.path.exists(file_name):
                with requests.get(file_url, stream=True) as r:
                    with open(file_name, 'wb') as f:
                        f.write(r.content)
                print(f"Downloaded {file_name}")
            else:
                print(f"{file_name} already exists")

if __name__ == "__main__":
    download_latest_report()
