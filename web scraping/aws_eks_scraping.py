import requests
from bs4 import BeautifulSoup
import csv
'''
This script scrapes the AWS EKS documentation to extract configuration snippets.


'''
# Base URL for the EKS documentation
BASE_URL = "https://docs.aws.amazon.com/eks/"

def crawl_eks_docs(start_url, output_file):
    visited_links = set()
    to_visit = [start_url]
    extracted_data = []
    print("start_url is ", start_url)

    while to_visit:
        current_url = to_visit.pop(0)
        if current_url in visited_links:
            continue
        
        visited_links.add(current_url)
        print(f"Visiting: {current_url}")
        
        response = requests.get(current_url)
        if response.status_code != 200:
            print(f"Failed to fetch: {current_url}")
            continue
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the main content of the page
        main_content = soup.find('div', id='main')  # Adjust based on AWS site structure
        if main_content:
            # Extract headings and associated configurations
            for section in main_content.find_all(['h2', 'h3']):  # Change tags as needed
                problem = section.text.strip()
                config = None

                # Find configuration snippets (e.g., code blocks)
                code_block = section.find_next('code')
                if code_block:
                    config = code_block.text.strip()

                if config:
                    extracted_data.append({
                        "Link": current_url,
                        "Problem": problem,
                        "Config": config
                    })
        # Add internal links to the to_visit list
        for link in main_content.find_all('a', href=True):
            print("this link is",link)
            href = link['href']
            if href.startswith('/') and BASE_URL + href not in visited_links:
                to_visit.append(BASE_URL + href)
            elif href.startswith('http') and href not in visited_links:
                to_visit.append(href)

    # Save the extracted data to a CSV file
    save_to_csv(extracted_data, output_file)


def save_to_csv(data, output_file):
    keys = ["Link", "Problem", "Config"]
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    start_url = BASE_URL
    output_file = "eks_configurations.csv"
    crawl_eks_docs(start_url, output_file)
    print(f"Data saved to {output_file}")
