# 打开文件并读取内容
with open('existing_words.txt', 'r', encoding='utf-8') as file:
    existing_words = file.readlines()

# 将内容按行拆分并存入一个集合中
existing_words_set = set(line.strip() for line in existing_words)

with open('new_words.txt', 'r', encoding='utf-8') as file:
    new_words = file.readlines()
new_words = [word.strip() for word in new_words]
new_words.reverse()

for word in new_words:
    if word not in existing_words_set:
        print(word)
