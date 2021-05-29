class student: 
    def init(self,name,kor): 
        self.name = name 
        self.kor = kor 
        self.mat = 90 
        self.eng = 80

def f_input(self):
    self.name = input('이름을 입력하시오:')
    self.kor = int(input('국어점수 :'))
    self.eng = int(input('영어점수 :'))
    self.mat = int(input('수학 점수 :'))

def f_proc(self):
    self.tot = self.kor + self.eng + self.mat
    self.ave = self.tot / 3
    
def f_print(self):
    print('이름 : ',self.name,'\n국어 점수:',self.kor,'\n영어 점수:',self.eng,'\n수학 점수',self.mat,)
st = student('홍길동', 50) 
kt = student('김길동', 90) 
#st.f_input() 
st.f_proc() 
st.f_print() 
kt.f_proc() 
kt.f_print()