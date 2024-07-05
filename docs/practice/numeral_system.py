# 2. 진수 변환기(십진수 > 2진수, 16진수 : 자동 변환 메서드 사용 금지 !!, 로직으로 구현해주세요)
number = int(input("진수 변환할 숫자를 입력하세요 "))
num = int(input("몇진수로 변환할까요? "))

def change(number, num):
  answer = []
  while number > 0:
      result = number % num
      answer.append(result)
      number = number // num
  return answer

a = change(number, num)
a.reverse()
print(a)