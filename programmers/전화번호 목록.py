def solution(phone_book):
    # 한 요소를 잡고 다른 요소와 비교하며 접두어 확인
    for s1 in phone_book:
        s1_len = len(s1)
        for s2 in phone_book:
            # 다른 요소와 비교할 때 길이가 기준 요소보다 작으면 패스
            s2_len = len(s2)
            if (s1_len >= s2_len):
                continue
            # 비교
            is_equal = True
            for i in range(s1_len):
                if (s1[i] != s2[i]):
                    is_equal = False
                    break
            # 같으면 바로 리턴
            if (is_equal):
                return False
    return True
