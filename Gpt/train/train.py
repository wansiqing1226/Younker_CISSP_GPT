import openai
openai.api_key = "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"
#openai.FineTune.create(training_file="file-*",model = "ada",n_epochs = 100,batch_size = 100,learning_rate_multiplier = 0.1)

list = openai.FineTune.list()
print(list)