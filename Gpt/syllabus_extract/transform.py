import jsonlines
from bs4 import BeautifulSoup

def convert_html_to_jsonl(html_file, output_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    domain_items = soup.find_all('div', class_='domainListItem')

    with jsonlines.open(output_file, 'w') as writer:
        for item in domain_items:
            domain_title = item.find_previous_sibling('h2').text.strip()
            domain_number = domain_title.split(':')[0].split()[1]

            item_title = item.find('h2').text.strip()
            item_content = item.find('div', class_='itemContent').text.strip()

            prompt = f"Domain {domain_number}:{domain_title}\n{item_title} {item_content}"
            completion = item_content.replace('\n', ' ')
            writer.write({"prompt": prompt, "completion": completion})

# Example usage
html_file = 'web_source_code.html'
output_file = 'test.jsonl'
convert_html_to_jsonl(html_file, output_file)