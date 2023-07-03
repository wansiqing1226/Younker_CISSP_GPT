import openai
openai.api_key = "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"
content = openai.File.download("file-EwBgHNI7Oz1gdMJyczTpkIi7")
print(content)