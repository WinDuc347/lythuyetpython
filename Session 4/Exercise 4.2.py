def average(s1, s2, s3, s4, s5):
    avg = (s1 + s2 + s3 + s4 + s5)/5
    return avg

def has_zero(s1, s2, s3, s4, s5):
    if s1 == 0 or s2 == 0 or s3 == 0 or s4 == 0 or s5 == 0:
        return True
    return False

def reward_class(avg, has_zero):
    if has_zero or avg < 12:
        print("No reward.")
    else:
        if avg >= 12 and avg < 16:
            print("Free coupons.")
        elif avg >= 16 and avg < 20:
            print("Free meal.")
        else:
            print("We will contact the exam ombuds, your grades are looking kinda sus.")
    

s1 = 20
s2 = 20
s3 = 20
s4 = 20
s5 = 20

average = average(s1, s2, s3, s4, s5)

has_zero = has_zero(s1, s2, s3, s4, s5)

reward_class(average, has_zero)
