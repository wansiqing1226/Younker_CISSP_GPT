import jsonlines

def generate_jsonl(questions_file, answers_file, output_file):
    with open(questions_file, 'r') as questions_f, open(answers_file, 'r') as answers_f, \
            jsonlines.open(output_file, 'w') as jsonl_f:
        questions = questions_f.read().strip().split('\n\n')
        answers = answers_f.read().strip().split('\n\n')

        if len(questions) != len(answers):
            raise ValueError("Number of questions and answers do not match.")

        for question, answer in zip(questions, answers):
            question_lines = question.strip().split('\n')
            prompt = question_lines[0].split('. ', 1)[1]

            answer_lines = answer.strip().split('\n')
            completion = answer_lines[0].split('. ', 1)[1]

            json_obj = {"prompt": prompt, "completion": completion}
            jsonl_f.write(json_obj)

        print("JSONL file generated successfully.")


# 指定输入文件的路径
questions_file = "questions.txt"
answers_file = "answers.txt"
output_file = "file.jsonl"

# 生成JSONL文件
generate_jsonl(questions_file, answers_file, output_file)