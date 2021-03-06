#python 연습문제 3-1, 1~5번

#1. 1. A=[1, 11, 13, 14, 15, 16, 111, 0.7] 의 최댓값과 최솟값을 구하세요.

A=[1, 11, 13, 14, 15, 16, 111, 0.7]
print("최댓값: " +str(max(A))) # 리스안의 요소 중 최댓값을 구해주는 내장함수 max()를 사용
print("최솟값: " +str(min(A))) # 리스안의 요소 중 최솟값을 구해주는 내장함수 min()를 사용

#2. 13자리의 주민 등록번호를 입력 후 성별을 출력하세요.

id_num = input('주민등록번호 : ') #input을 통해 주민등록번호를 str로 받는다.
print(id_num[6]) #주민등록번호의 성별을 나타내는 요소 출력

if id_num[6] == '1' or id_num[6] == '3' : #성별을 나타내는 요소가 1 또는 3이면 남자 출력
    print('남자입니다.')
elif id_num[6] == '2' or id_num[6] == '4': #성별을 나타내는 요소가 2 또는 4이면 여자 출력
    print('여자입니다.')
#이 코드의 단점은 '-'을 포함하여 주민등록번호를 입력 할 시 성별을 나타내는 요소의 위치가 달라져 코드가 실행되지 않음
#해결책으로 index을 뒤에서부터(-1부터) 카운트하면 '-'가 있어도 구별 가능

#3. 임의의 체중과 신장을 입력한 후 비만도를 출력하는 함수를 작성하세요.
# 매개변수 2개(키와 몸무게)를 받아 비만도를 구하는 함수 작성
def obesity (weight, height):
    bmi = float(weight/(height**2)) #bmi 공식
    # if와 elif, else을 사용하여 조건 별로 출력을 다르게 함
    if bmi < 18.5: #bmi가 18.5보다 작으면 '마른체형'출력
        result = '마른체형'
    elif bmi < 25.0: #bmi가 18.5보다 작지 않고, 25.0보다 작으면 '표준' 출력
        result = '표준'
    elif bmi < 30.0: #bmi가 25.0보다 작지 않고, 30보다 작으면 '비만' 출력
        result = '비만'
    else: #bmi가 30.0하고 같거나 크면 '고도비만' 출력
        result = '고도 비만'
    return print('bmi : {:.2f}  result : {}'.format(bmi, result))

info_w = input('몸무게(kg)를 입력 하세요') # 몸무게 입력
info_h = input('키(m)를 입력 하세요')     # 키 입력

obesity(float(info_w),float(info_h)) #입력받은 키와 몸무게를 매개변수로 사용하여 비만도를 구한다.

#4. 파일 이름이 저장된 리스트에서 확장자가 .h나 .c인 파일을 화면에 출력하세요.

# .endswith(): ()안의 문자 또는 문자열이 해당 문자열 접미어로 포함되어 있으면 True을 출력하는 method
files = ["intra.h", "intra.c", "define.h", "run.py"] #여러 문자열을 요소로 갖는 list 생성
for x in files: #files의 요소를 x에 하나씩 대입하여 조건을 확인하는 for문
    if x.endswith(".py") or x.endswith(".h") : #해당 문자열 끝에 '.py' 또는 '.h' 가 있는 경우 출력
        print(x)

#5. 중첩 반복을 사용하여 신문을 배달하는 프로그램을 작성하세요. 단 미납금이 있는 호수에는 배달하지 마세요.

#for문을 두번 사용하는 중첩 반복문을 사용
#apart 는 전체 아파트 호수를 가지고 있는 list(각 층별로 list로 묶여 있으면 이를 다시 요소로 갖고 있다)
apart = [[101, 102, 103, 104], [201,202,203,204], [301,302,303,304], [401,402,403,404]]
unpaid = [101, 202, 302, 403] # 미납 호수를 가지고 있는 list

for i in apart : #층별로 묶여 있는 list 요소를 i에 대입
    for j in i: #해당 층의 호수를 j에 대임
        if j in unpaid : #만약 j가 upaid list에 들어 있는 요소 중 값이 같은 것이 있으면 미납이으므로 미납 출력
            print('{}호 : 미납'.format(j))            
        else: # 그렇지 않은 경우는 배달 출력
            print('{}호 : 배달'.format(j))

#해당 연습문제는 list의 요소가 listf로 이루어져 있어서 호수 하나 하나의 조건을 찾기 위해 for문을 두 번 사용하였다.