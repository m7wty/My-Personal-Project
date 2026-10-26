name = input("what is student name?")
area = input("what is student area?")

with open ("student.csv","a") as file:
    file.write(f"{name}  {area}\n")

    print ("Saved successfully!")