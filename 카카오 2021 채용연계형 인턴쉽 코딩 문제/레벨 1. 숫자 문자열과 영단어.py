'''
숫자의 일부 자릿수가 영단어로 이루어진 문자열을 입력받아서
영단어로 된 숫자를 숫자로 바꾼 후 출력
'''
def solution(s) :
    answer = s
    dict_num = {}
    # 영단어 숫자 리스트
    list_str_num = ['zero', 'one', 'two', 'three', 'four',
                    'five', 'six', 'seven', 'eight', 'nine']
    # 딕셔너리 안에 key와 value로 넣음
    for i in range(10) :
        dict_num[i] = list_str_num[i]
    # 영단어로 문 숫자를 숫자로 변환
    for key, value in dict_num.items() :
        if value in answer :
            answer = answer.replace(value, str(key))
    return answer

'''
입력                출력
"one4seveneight"	1478
"23four5six7"	    234567
"2three45sixseven"	234567
"123"	            123
'''
s = 'one4seveneight'
answer = solution(s)
print(answer)