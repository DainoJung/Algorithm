def goDownfloor(current, target):
    for floor in range(current, target - 1, -1):
        print(f'현재층은 {floor} 입니다')

def goUpfloor(current, target):
    for floor in range(current, target + 1):
        print(f'현재층은 {floor} 입니다')


currentFloor = 1
while True:
    targetFloor = int(input("가고 싶은 층을 입력하세요(운행정지는 -100을 입력): "))
    if targetFloor == -100:
        break
    else:
        if currentFloor < targetFloor:
            goUpfloor(currentFloor, targetFloor)
            currentFloor = targetFloor
            print(f'{targetFloor}에 도착했습니다.')
        elif currentFloor > targetFloor:
            goDownfloor(currentFloor, targetFloor)
            currentFloor = targetFloor
            print(f'{targetFloor}에 도착했습니다.')
        else:
            print('입력하신 층은 현재 층입니다.')