name = [] 
kor = [] 
eng = [] 
mat = [] 
sci = [] 
tot = [] 
ave = []

for i in range(3): n = input('이름대시오') k = int(input('국어성적')) e = int(input('영어성적')) m = int(input('수학성적')) s = int(input('과학성적'))

name.append(n)
kor.append(k)
eng.append(e)
mat.append(m)
sci.append(s)
for x in range(3): totlist = kor[x] + eng[x] + mat[x] + sci[x] avelist = totlist/4

tot.append(totlist)
ave.append(avelist)
for y in range(3): print('\n학생이름: ',name[y]) print('\n합산점수:',tot[y]) print('\n평균: ',ave[y])

all = sum(tot)/3 print('\n\n전체:',all)