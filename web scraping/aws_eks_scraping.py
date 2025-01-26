import requests
from bs4 import BeautifulSoup
import csv

# Base URL for the EKS documentation
BASE_URL = "https://docs.aws.amazon.com/eks/latest/userguide/"

def crawl_eks_docs(start_url, output_file):
    visited_links = set()
    to_visit = [start_url]
    extracted_data = []

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
        main_content = soup.find('main')  # Adjust based on AWS site structure
        if not main_content:
            continue

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
            href = link['href']
            if href.startswith('/eks') and BASE_URL + href not in visited_links:
                to_visit.append(BASE_URL + href)

    # Save the extracted data to a CSV file
    save_to_csv(extracted_data, output_file)


def save_to_csv(data, output_file):
    keys = ["Link", "Problem", "Config"]
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    start_url = BASE_URL + "quickstart.html"
    output_file = "eks_configurations.csv"
    crawl_eks_docs(start_url, output_file)
    print(f"Data saved to {output_file}")
