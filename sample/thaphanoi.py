# Recursive Python function to solve the tower of hanoi

def TowerOfHanoi(n , dau, diemcuoi, trunggian):
	if n==1:
		print("Move disk 1 from source",dau,"to destination",diemcuoi)
		return
	TowerOfHanoi(n-1, dau, trunggian, diemcuoi)
	print("Move disk",n,"from source",dau,"to destination",diemcuoi)
	TowerOfHanoi(n-1, trunggian, diemcuoi, dau)
		
# Driver code
n = 4
TowerOfHanoi(n,'A','B','C')
# A, C, B are the name of rods

# Contributed By Dilip Jain

