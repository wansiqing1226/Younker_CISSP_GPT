import openai
openai.api_key = "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"
openai.File.create(
  file=open("Execution1.json", "rb"),
  purpose='fine-tune'
)
i= openai.File.list()
print(i)