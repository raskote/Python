print("ДА" if ((x:=int(input()))//1000 + x%10)==(x//100%10 - x//10%10) else "НЕТ")
