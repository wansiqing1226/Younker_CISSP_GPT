import openai
openai.api_key = "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"
#openai.File.delete("file-xKNVI5aHwGFji3wLUIRm71gw")
#openai.File.delete("file-0OWwP7SxxkLgrdMOqQhedRci")

#openai.File.delete("file-FTUvhbRSjAqC1F1jD3cSq8Mu")
i= openai.File.list()
print(i)