import random

random_responses = ["정말 흥미롭네요, 더 자세히 말씀해주세요.",
                    "알겠습니다. 계속 말씀해주세요.",
                    "왜 그렇게 생각하세요?",
                    "최근 날씨가 참 특이하죠?",
                    "주제를 바꿔 볼까요?",
                    "어젯밤 경기 보셨나요?"]

print("안녕하세요, 저는 단순한 로봇인 마빈입니다.")
print("이 대화를 언제든지 '안녕'이라고 입력하면 종료할 수 있습니다.")
print("답변을 입력한 후에는 '엔터'를 누르세요.")
print("오늘 기분은 어떠세요?")

while True:
    user_input = input("> ")
    if user_input.lower() == "안녕":
        break
    else:
        response = random.choice(random_responses)
    print(response)

print("대화해 주셔서 감사합니다, 안녕히 가세요!")
