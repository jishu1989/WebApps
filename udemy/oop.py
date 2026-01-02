class Instructors:
    companyName = "BlueLime"
    
    def __init__(self,course,duration):
        self.course=course
        self.duration=duration
        
    def __str__(self):
        return f"Course: {self.course}, Duration: {self.duration}"
        
    def printinfo(self):
        print("My Company Name is:",Instructors.companyName)



elearning = Instructors("Python for beginners","2months") #object or instance of the class


bls = Instructors("Django for beginners","3months") #object or instance of the class

bls.course = "HTML"

print(bls)
print(elearning)

#elearning.printinfo()

#bls.printinfo()  

print(bls.course)    
print(elearning.course)   

#del bls.duration

#print(bls.course)

