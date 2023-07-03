import openai
openai.api_key = "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"

#openai.Model.delete('curie:ft-personal-2023-06-28-04-37-04')#删除模型
#openai.FineTune.cancel(id="ft-kqSJ4Ov5sn4CUOBKLThMyPNm")#取消微调
list = openai.FineTune.list()
print(list)
