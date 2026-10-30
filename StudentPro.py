 
students = []

for i in range(5):
     name = input("Enter student  name : ")
     grade = int (input("Enter student grade : "))
     students.append({"name":name , "grade" : grade})


     for s in students:
        if s ["grade"] >= 90:
            letter  = "A" 
        elif s ["grade"] >= 80:
             letter = "B" 
        elif s ["grade"] >= 70:
            letter = "C"             
        elif s ["grade"] >= 60:
            letter = "D"
        else:
             letter = "F"

          
     print(f"Student {s['name']}, your {s['grade']} is {letter}")               