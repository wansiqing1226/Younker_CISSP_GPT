import openai
openai.api_key = "sk-vd2r2GG6tVkv9i2T43A5D1E8AfA141E8B22aB45d5a75Ab8b"
openai.File.create(
  file=open("Execution1.json", "rb"),
  purpose='fine-tune'
)
i= openai.File.list()
print(i)