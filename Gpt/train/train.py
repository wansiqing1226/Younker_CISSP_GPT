import openai
openai.api_key = "sk-vd2r2GG6tVkv9i2T43A5D1E8AfA141E8B22aB45d5a75Ab8b"
#openai.FineTune.create(training_file="file-*",model = "ada",n_epochs = 100,batch_size = 100,learning_rate_multiplier = 0.1)

list = openai.FineTune.list()
print(list)

C:/Users/万/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/Scripts