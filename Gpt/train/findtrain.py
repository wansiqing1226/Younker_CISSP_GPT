import openai
openai.api_key = "sk-vd2r2GG6tVkv9i2T43A5D1E8AfA141E8B22aB45d5a75Ab8b"

#list = openai.FineTune.retrieve(id="ft-f5o5MGYnZl7xvr5hUystNLuO")#100
list = openai.FineTune.retrieve(id="ft-f5o5MGYnZl7xvr5hUystNLuO")#失败
#list = openai.FineTune.list_events(id="ft-15kg0cRthx5Yw7FTng0qzk5D")#查找特定id模型状态50
#list = openai.FineTune.retrieve(id="ft-15kg0cRthx5Yw7FTng0qzk5D")#查找特定id微调数据
#list = openai.FineTune.list()#列出微调数据

print(list)
