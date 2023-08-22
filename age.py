ans = input('請問你是否有開過車?')
if ans !='有' and ans !='沒有':
	print('只能輸入有或是沒有')
	raise SystemExit
age = input('請問你的年紀?')
age = int(age)
if ans == '有'  :
	if age >= 18 :
		print('PASS')
	else:
		print('怪了你怎會開過車?')

elif ans == '沒有' :
    if age >= 18:
    	print('恭喜你可以去考駕照了')
    else :
    	print('你要滿18才可考駕照')
