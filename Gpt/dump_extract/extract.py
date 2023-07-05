import re
import jsonlines

def generate_jsonl(questions_file, answers_file, output_file):
    with open(questions_file, 'r') as questions, open(answers_file, 'r') as answers, jsonlines.open(output_file, 'w') as jsonl_file:
        prompts = questions.read().split('\n\n')  # 按空行分割问题
        completions = answers.read().split('\n\n')  # 按空行分割答案

        for prompt, completion in zip(prompts, completions):
            prompt = remove_question_number(prompt)  # 删除问题中的题号
            completion = remove_question_number(completion)  # 删除答案中的题号
            json_obj = {"prompt": prompt, "completion": completion}
            jsonl_file.write(json_obj)

def remove_question_number(text):
    lines = text.strip().split('\n')
    new_lines = []
    for line in lines:
        # 使用正则表达式删除题号
        new_line = re.sub(r'^\d+\. ?', '', line)
        new_lines.append(new_line)
    return ' '.join(new_lines)

questions_file = "35-50Q.txt"
answers_file = "35-50A.txt"
output_file = "file.jsonl"

generate_jsonl(questions_file, answers_file, output_file)
