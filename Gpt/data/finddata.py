import openai
openai.api_key = "sk-vd2r2GG6tVkv9i2T43A5D1E8AfA141E8B22aB45d5a75Ab8b"
content = openai.File.download("file-EwBgHNI7Oz1gdMJyczTpkIi7")
print(content)