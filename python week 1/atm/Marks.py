English = int(input("Enter English maarks:"))
Maths = int(input("Enter Maths marks:"))
Science = int(input("Enter Science marks:"))
Tamil = int(input("Enter Tamil marks:"))
Social = int(input("Enter Social marks:"))
total = English + Maths + Science + Tamil + Social
average = total / 5
print("Marks in English:", English)
if English < 35:
    print("grade in english: U")
    elif English >= 35 and English < 50:
        print("grade in english: E")
    elif English >= 50 and English < 60:
        print("grade in english: C")
print("Marks in Maths:", Maths)
print("marks in Science:", Science)
print("Marks in Tamil:", Tamil)
print("Marks in Social:", Social)
print("Total marks:", total)
print("Average marks:", average)
print("Percentage marks:", (total / 500) * 100)
if average >= 480:
    print("Grade: S")
elif average >= 450:
        print("Grade: A")
elif average >= 400:
        print("Grade: B")
elif average >= 350:
        print("Grade: C")
elif average >= 250:
        print("Grade: E")
else:
        print("Grade: U")
