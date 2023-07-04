import json
from bs4 import BeautifulSoup

def convert_html_to_jsonl(html_file, jsonl_file):
    # 读取 HTML 文件
    with open(html_file, 'r') as f:
        html_content = f.read()

    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # 提取 prompt 和 completion
    prompt_completion_pairs = []
    h3_elements = soup.find_all('h3')
    for h3 in h3_elements:
        prompt = h3.text.strip()
        completion_items = []
        li_elements = h3.find_next('ul').find_all('li')
        for li in li_elements:
            completion_items.append(li.text.strip())
        completion = ', '.join(completion_items)
        prompt_completion_pairs.append({'prompt': prompt, 'completion': completion})

    # 将结果写入 JSONL 文件
    with open(jsonl_file, 'w') as f:
        for pair in prompt_completion_pairs:
            json_line = json.dumps(pair)
            f.write(json_line + '\n')

# 调用函数进行转换
convert_html_to_jsonl('web_source_code.html', '2nd_layer.jsonl')
