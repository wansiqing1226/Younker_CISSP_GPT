import openai
openai.api_key = "sk-vd2r2GG6tVkv9i2T43A5D1E8AfA141E8B22aB45d5a75Ab8b"
#openai.File.delete("file-xKNVI5aHwGFji3wLUIRm71gw")
#openai.File.delete("file-0OWwP7SxxkLgrdMOqQhedRci")

#openai.File.delete("file-FTUvhbRSjAqC1F1jD3cSq8Mu")
i= openai.File.list()
print(i)