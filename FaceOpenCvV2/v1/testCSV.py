
name =['duc','tan','tan','duc']

# with open('Attendance.csv','r+') as f:
#         myDataList=f.readlines()
        
#         nameList=[]
#         for line in myDataList:
#             entry = line.split(',')
#             nameList.append(entry[0])
#             print(nameList)
#             if name not in nameList:
#                 now = datetime.now()
#                 dtString= now.strftime('%H:%M:%S  %D')
#                 f.writelines(f'\n{name},{dtString}')


# with open('Attendance.csv','r+') as f:
#     for i,item in enumerate(name):
#         f.writelines(f'\n {i},{item}')

a={}
a['1']={'name':'duc','tuoi':22}
a['2']={'name':'g','tuoi':22}
a['3']={'name':'b','tuoi':22}
a['4']={'name':'c','tuoi':22}
print(a)