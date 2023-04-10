# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
print("Введите шестизначный номер билета")
numberTicket=int(input())
rightHalf=int(numberTicket%1000)
leftHalf=int(numberTicket//1000)
# print(rightHalf)
# print(leftHalf)
rightSum=0
leftSum=0
while rightHalf/10!=0:
    rightSum=rightSum+rightHalf%10
    rightHalf=rightHalf//10
while leftHalf/10!=0:
    leftSum=leftSum+leftHalf%10
    leftHalf=leftHalf//10
if leftSum==rightSum:print("Счастливый билет")
else:print ("Билет не является счастливым")