# Задача 2: Найдите сумму цифр трехзначного числа.
print("Введите трехзначное число")
tripleNumber=int(input())
sum=0
while tripleNumber/10!=0:
    sum=sum+tripleNumber%10
    tripleNumber=tripleNumber//10
print("Сумма цифр числа равна:",int(sum))


    