class School: 
    def init(self, name, kor, eng, mat, sci): 
        self.name = name self.kor = kor self.eng = eng self.mat = mat self.sci = sci

def get_name(self):
    return self.name

def get_tot(self):
    return self.tot

def get_ave(self):
    return self.ave

def get_grade(self):
    return self.grade

def calculate(self):
    self.tot = self.kor + self.eng + self.mat + self.sci
    self.ave = self.tot/4

def set_grade(self):
    if self.ave >= 90:
        self.grade = 'A'
    elif self.ave >= 85:
        self.grade = 'B+'
    elif self.ave >= 80:
        self.grade = 'B'
    elif self.ave >= 70:
        self.grade = 'C'
    elif self.ave >= 60:
        self.grade = 'D'
    else:
        self.grade = 'F'
name = input('이름:') 
kor = int(input('국어 점수:')) 
eng = int(input('영어 점수:')) 
mat = int(input('수학 점수:')) 
sci = int(input('과학 점수:'))

School1 = School(name, kor, eng, mat, sci)

School1.calculate() School1.set_grade()

print('이름:', School1.get_name()) 
print('합계:', School1.tot) 
print('평균:', School1.get_ave()) 
print('학점:', School1.get_grade())