total_dictionary = {}

while True:
    QUESTION = input("질문을 입력해주세요: ")
    if QUESTION == 'q' :
        break
    else:
        total_dictionary[QUESTION] = ""

for i in total_dictionary:
    print(i)
    answer = input("답변을 입력해주세요 : ")
    total_dictionary[i] = answer
print(total_dictionary)   