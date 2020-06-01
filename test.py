def comparegrade(Grade): #เปลี่ยนเกรดที่รับค่าเป็นstr ให้เป็น ตัวเลข เช่น A มีค่าเป็น 4
    if (Grade == "A") :
        return 4
    elif Grade == "B+" :
        return 3.5 
    elif Grade == "B" :
        return 3
    elif Grade == "C+" :
        return 2.5
    elif Grade == "C" :
        return 2
    elif Grade == "D+" :
        return 1.5
    elif Grade == "D" :
        return 1
    elif Grade == "F" :
        return 0
    else:
        return 0


Subject = int(input("จำนวนวิชา : "))

i = 1
SumUnit = 0
Total = 0

while i <= (Subject) :
    print("วิชาที่ "+str(i))
    Unit = int(input("หน่วยกิต:"))
    Grade = str(input("เกรด:"))
    SumGU = (Unit * comparegrade(Grade)) # เกรด * หน่วยกิต แล้วเอาทั้งหมดมาบวกกัน 
    i= i+1
    Total = Total+SumGU
    SumUnit = SumUnit+Unit #ผลรวมของ หน่วยกิตทุกวิชา เอาหน่วยกิตของทุกวิชามาบอกกัน 
GPA = Total/SumUnit 
print("เกรดรวมหน่วยกิต = "+ str(Total))
print("หน่วยกิตรวม = "+ str(SumUnit))
print ("GPA = "+ str(GPA))
