
Subject = int(input("จำนวนวิชา : "))

i = 1
SumUnit = 0
Total = 0

while i <= (Subject) :
    print("วิชาที่ "+str(i))
    Unit = int(input("หน่วยกิต:"))
    Grade = float(input("เกรด:"))
    SumGU = (Unit * Grade)
    i= i+1
    Total = Total+SumGU
    SumUnit = SumUnit+Unit
GPA = Total/SumUnit
print("เกรดรวมหน่วยกิต = "+ str(Total))
print("หน่วยกิตรวม = "+ str(SumUnit))
print ("GPA = "+ str(GPA))
