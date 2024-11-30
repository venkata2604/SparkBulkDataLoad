def is_valid_score(score):
    # Base case if score is zero, it's valid
    if score ==0:
        return True

    # if the score is negative its invalid
    if score <0:
        return False

    # Recursive check subtract possible scores (3, 7, 11) and check
    return is_valid_score(score-3) or is_valid_score(score-7) or is_valid_score(score-11)

def is_valid_score_2(score):
    # loop through combinations of 3, 7 & 11
    for i in range(score//3 +1):
        for j in range(score//7 +1):
            for k in range(score//1 +1):
                if 3*i+7 *j+11 *k == score:
                    return True
    return False

# function to check if both X and Y are valid
def is_valid_final_score(x, y):
    return is_valid_score(x) and is_valid_score(y)
def is_valid_final_score_2(x, y):
    return is_valid_score_2(x) and is_valid_score_2(y)

if __name__ =="__main__":
    n1,n2 = input("enter the values separated by commas").split(",")
    # print(is_valid_final_score(int(n1),int(n2)))
    print(is_valid_final_score_2(int(n1),int(n2)))
