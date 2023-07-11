import openai
openai.api_key = "sk-vd2r2GG6tVkv9i2T43A5D1E8AfA141E8B22aB45d5a75Ab8b"

#openai.Model.delete('curie:ft-personal-2023-06-28-04-37-04')#删除模型
#openai.FineTune.cancel(id="ft-kqSJ4Ov5sn4CUOBKLThMyPNm")#取消微调
list = openai.FineTune.list()
print(list)
