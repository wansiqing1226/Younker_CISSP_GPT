from bs4 import BeautifulSoup
import json

def extract_data(html_file):
    with open(html_file, 'r') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    data = []

    panel_items = soup.find_all('li', class_='panel')
    for item in panel_items:
        domain_name = item.find('span', class_='hide-sm').text.strip().replace('Domain ', '')

        domain_items = item.find_all('div', class_='domainListItem')
        for domain_item in domain_items:
            prompt = domain_name
            completion = domain_item.find('h3').text.strip()

            data.append({
                'prompt': prompt,
                'completion': completion
            })

    return data

def generate_jsonl(data, output_file):
    with open(output_file, 'w') as file:
        for item in data:
            json.dump(item, file, ensure_ascii=False)
            file.write('\n')

html_file = 'web_source_code.html'
jsonl_file = '1st_layer.jsonl'

extracted_data = extract_data(html_file)
generate_jsonl(extracted_data, jsonl_file)
