

class SINHVIEN :
    def __init__(self,id,name,age,grade,credit) :
            self._id = id
            self._name = name 
            self._age = age
            self._grade = grade 
            self._credit = credit 
        


def sort(sv : SINHVIEN) :
    return sv._grade

class GET_INFORMATION :
    list_student = []

    def info_std(self) :
        try :
            n = int(input("Take the number of student: "))
        except :
            print("Error Input")
        for i in range(n) :
            try :
                id = int(input("Write the id of student: "))
                name = input("Write the name of student: ")
                age = int(input("Write the age of student: "))
                grade = float(input("Write the grade of student: "))
                credit = int(input("Total number of credit that student have took :"))
                sv = SINHVIEN(id,name,age,grade,credit)
                self.list_student.append(sv)
            except :
                print("Error Input")
        self.list_student.sort(reverse = True, key = sort ) 
        k = 0
        for s_v in self.list_student :
            print(f'{s_v._id} :{s_v._name}, age :{s_v._age},grade :{s_v._grade}, credit :{s_v._credit},result:{self.result(s_v)}, graduate : {self.graduate(s_v)}')
            if self.graduate(s_v) == True :
                k = k+1 
        print("Total number of graduated students is :", k)

    def graduate(self, sv : SINHVIEN) :
        return sv._grade >= 1.8
    
    def result(self, sv : SINHVIEN) :
        if sv._grade >=  3.8 and sv._grade <=  4 :
            return "A+"
        elif sv._grade <=  3.5 and sv._grade >=  3.3 :
            return "A"
        elif sv._grade >=  3 and sv._grade <=  3.2 :
            return "B+"
        elif sv._grade >=  2.6 and sv._grade <=  2.9 : 
            return "B"  
        elif sv._grade >=  1.8 and sv._grade <=  2.5 :
            return "C"
        elif sv._grade < 1.8 :
            return "D"

k = GET_INFORMATION()
k.info_std()