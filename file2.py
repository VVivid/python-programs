S = str(input()).upper()
vowels = 'AEIOU'
kev_score = 0
stu_score = 0
for i in range(len(S)):
    if S[i] in vowels:
        kev_score += (len(S)-i)
    else:
        stu_score += (len(S)-i)
if kev_score > stu_score:
    print("Kevin", kev_score)
elif kev_score < stu_score:
    print("Stuart", stu_score)
else:
    print("Draw")

