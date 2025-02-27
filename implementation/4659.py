
moeum = ["a", "e", "i", "o", "u"]


def acceptable(str):
    print(f"<{str}> is acceptable.")


def not_acceptable(str):
    print(f"<{str}> is not acceptable.")

while True:
    str = input()
    if str == "end":
        exit()

    is_moeum_included = False

    length = len(str)
    if length == 1:
        if str[0] in moeum:
            acceptable(str)
        else:
            not_acceptable(str)
    else:
        if str[0] in moeum or str[1] in moeum:
            if str[0] == str[1] and str[0] not in ["e", "o"]:
                not_acceptable(str)
                continue
            is_moeum_included = True
        elif str[0] == str[1] and str[0] not in ["e", "o"]:
            not_acceptable(str)
            continue

        for i in range(length-1, 1, -1): # 뒤에서부터 비교
            if str[i] in moeum:
                is_moeum_included = True

                if str[i-1] in moeum and str[i-2] in moeum:
                    not_acceptable(str)
                    break
            elif str[i-1] not in moeum and str[i-2] not in moeum:
                not_acceptable(str)
                break

            if str[i] == str[i-1] and str[i] not in ["e", "o"]:
                not_acceptable(str)
                break
        else:
            if is_moeum_included:
                acceptable(str)
            else:
                not_acceptable(str)

