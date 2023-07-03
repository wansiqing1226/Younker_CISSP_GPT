import  openai

openai.api_key = "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"
def fine_tuned(prompt):
    completion = openai.Completion.create(
        model = 'ada:ft-personal-2023-06-28-08-07-45',
        #model='ada:ft-personal-2023-06-28-08-07-45',
        prompt = prompt,
    max_tokens = 2000
    )
    print(completion.choices[0].text)
if __name__ == '__main__':
    while True:
        fine_tuned(input(">>"))