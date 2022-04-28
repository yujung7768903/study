def calculate_distance(hand_position, number_position):
    x_distance = hand_position[0] - number_position[0]
    if x_distance < 0:
        x_distance *= -1
    y_distance = hand_position[1] - number_position[1]
    if y_distance < 0:
        y_distance *= -1
    return x_distance + y_distance
    
def solution(numbers, hand):
    answer = ''
    left_position = [3, 0]
    right_position = [3, 2]
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            left_position = [(i // 3), 0]
            answer += 'L'
        elif i == 3 or i == 6 or i == 9:
            right_position = [(i // 3 - 1), 2]
            answer += 'R'
        else:
            if i == 0:
                number_position = [3, 1]
            else:
                number_position = [(i // 3), 1]
            # 왼손과 숫자와의 거리, 오른손과 숫자와의 거리 구하기
            distance_from_left = calculate_distance(left_position, number_position)
            distance_from_right = calculate_distance(right_position, number_position)
            # 거리가 같은 경우
            if distance_from_left == distance_from_right:
                if hand == 'left':
                    left_position = number_position
                    answer += 'L'
                else:
                    right_position = number_position
                    answer += 'R'
            elif distance_from_left < distance_from_right:
                left_position = number_position
                answer += 'L'
            else:
                right_position = number_position
                answer += 'R'
            
    return answer