import re
import jsonlines

def extract_question_answer_pairs(questions_file, answers_file):
    pairs = []
    with open(questions_file, 'r') as q_file, open(answers_file, 'r') as a_file:
        questions_data = q_file.read().strip()
        answers_data = a_file.read().strip()

        question_pattern = r'(?<=\n\n)(.+?)(?=\n\n|\Z)'  # Matches the content between two consecutive empty lines
        answer_pattern = r'(?<=\n\n)(.+?)(?=\n\n|\Z)'  # Matches the content between two consecutive empty lines

        questions = re.findall(question_pattern, questions_data, re.DOTALL)
        answers = re.findall(answer_pattern, answers_data, re.DOTALL)

        if len(questions) != len(answers):
            raise ValueError("Number of questions and answers does not match.")

        for question, answer in zip(questions, answers):
            prompt = question.strip() + "\n"
            completion = answer.strip()
            pairs.append({'prompt': prompt, 'completion': completion})

    return pairs

def save_to_jsonl(data_list, output_path):
    with jsonlines.open(output_path, mode='w') as writer:
        for data in data_list:
            writer.write(data)

if __name__ == '__main__':
    questions_file = 'questions.txt'
    answers_file = 'answers.txt'
    output_jsonl_path = 'file.jsonl'

    try:
        pairs = extract_question_answer_pairs(questions_file, answers_file)
        if len(pairs) == 0:
            print("No question-answer pairs extracted.")
        else:
            save_to_jsonl(pairs, output_jsonl_path)
            print("JSONL file generated successfully.")

        # Print some extracted pairs for debugging
        for pair in pairs[:5]:
            print("Prompt:", pair['prompt'])
            print("Completion:", pair['completion'])
            print("---------------------------")

    except ValueError as ve:
        print("ValueError:", str(ve))
    except FileNotFoundError as fe:
        print("FileNotFoundError:", str(fe))
    except Exception as e:
        print("An error occurred:")
        print(str(e))
