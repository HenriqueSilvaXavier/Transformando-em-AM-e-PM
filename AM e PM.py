n=input("Digite o horário: ")
if int(n[0:2])<12:
	print(n, "A.M.")
n=n.split(":")
for k in range(0, len(n)):
	n[k]=int(n[k])
d=n[1]/60
n=n[0]+d
if n>=12:
	n=n-12
	d=n-int(n)
	n=n-d
	d=d*60
	n=int(n)
	d=int(d)
	print("{:02d}:{} P.M.".format(n, d))