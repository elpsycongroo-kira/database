f1 = open('file1.txt')
f2 = open('file2.txt')
f3 = open('file3.txt')
l1 = f1.readlines()
l2 = f2.readlines()
l3 = f3.readlines()
# direc = {'A' : 8,'B' : 8,'C' : 5,'D' : 10}
maxi = max(len(l1),len(l2))
maxi = max(maxi,len(l3))
# print maxi
for i in range(len(l1)):
	l1[i] = l1[i][:-1]
for i in range(len(l2)):
	l2[i] = l2[i][:-1]
for i in range(len(l3)):
	l3[i] = l3[i][:-1]
# j = 0
for p in range(maxi,0,-1):
	flag1=1
	flag2=1
	flag3=1
	uw = open(str(p)+'.txt_undo','w')
	rw = open(str(p)+'.txt_redo','w')
	old = 0
	i = 0
	direc = {'A' : 8,'B' : 8,'C' : 5,'D' : 10}
	while i<maxi:                                                             
		for j in range(3):
			i = old
			while i<=old+p-1 and i<maxi:                                       
				# print i,old
				if j%3 == 0 and i<len(l1):
					if i==0:
						uw.write("<START T1> A "+str(direc['A'])+" B "+str(direc['B'])+" C "+str(direc['C'])+" D "+str(direc['D'])+"\n")
						rw.write("<START T1> A "+str(direc['A'])+" B "+str(direc['B'])+" C "+str(direc['C'])+" D "+str(direc['D'])+"\n")
					if "READ" in l1[i]:
						temp = l1[i].split('READ')
						new = (temp[1].strip()).split(',')
						direc[new[1][:-1].strip()] = direc[new[0][1:].strip()]
						# print "read"
						# print direc
					elif "WRITE" in l1[i]:
						temp = l1[i].split('WRITE')
						# print temp
						new = (temp[1].strip()).split(',')
						new[0] = new[0].strip()
						new[0] = new[0][1:].strip()
						uw.write("<T1,"+new[0]+","+str(direc[new[0]])+"> A "+str(direc['A'])+" B "+str(direc['B'])+" C "+str(direc['C'])+" D "+str(direc['D'])+"\n")
						direc[new[0].strip()] = direc[new[1][:-1].strip()]
						# print direc
						rw.write("<T1,"+new[0]+","+str(direc[new[0]])+"> A "+str(direc['A'])+" B "+str(direc['B'])+" C "+str(direc['C'])+" D "+str(direc['D'])+"\n")
					elif "OUTPUT" in l1[i]:
						if flag1 ==1:
							uw.write("<COMMIT T1> A "+str(direc['A'])+" B "+str(direc['B'])+" C "+str(direc['C'])+" D "+str(direc['D'])+"\n")
							rw.write("<COMMIT T1> A "+str(direc['A'])+" B "+str(direc['B'])+" C "+str(direc['C'])+" D "+str(direc['D'])+"\n")
						# temp = l1[i].split('OUTPUT')
							flag1 = 0
						# print temp[1][:-1].strip()
					else:
						temp = l1[i].split('=')
						# print temp
						if "*" in temp[1]:
							new = temp[1].split('*')
							try:
								direc[temp[0].strip()] = direc[new[0].strip()]+direc[new[1].strip()]
							except:
								try:
								# print "hi"
								# print temp[0]
									direc[temp[0].strip()] = direc[new[0].strip()]*int(new[1].strip())
								except:
									direc[temp[0].strip()] = int(new[0].strip())*direc[new[1].strip()]
						if "-" in temp[1]:
							new = temp[1].split('-')
							try:
								direc[temp[0].strip()] = direc[new[0].strip()]+direc[new[1].strip()]
							except:
								try:
								# print "hi"
								# print temp[0]
									direc[temp[0].strip()] = direc[new[0].strip()]-int(new[1].strip())
								except:
									direc[temp[0].strip()] = int(new[0].strip())-direc[new[1].strip()]
						if "+" in temp[1]:
							new = temp[1].split('+')
							try:
								direc[temp[0].strip()] = direc[new[0].strip()]+direc[new[1].strip()]
							except:
								try:
								# print "hi"
								# print temp[0]
									direc[temp[0].strip()] = direc[new[0].strip()]+int(new[1].strip())
								except:
									direc[temp[0].strip()] = int(new[0].strip())+direc[new[1].strip()]
						if "/" in temp[1]:
							new = temp[1].split('/')
							try:
								direc[temp[0].strip()] = direc[new[0].strip()]+direc[new[1].strip()]
							except:
								try:
								# print "hi"
								# print temp[0]
									direc[temp[0].strip()] = direc[new[0].strip()]/int(new[1].strip())
								except:
									direc[temp[0].strip()] = int(new[0].strip())/direc[new[1].strip()]
						# print direc
				if j%3 == 1 and i<len(l2):
					# print i
					if i==0:
						uw.write("<START T2> A "+str(direc['A'])+" B "+str(direc['B'])+" C "+str(direc['C'])+" D "+str(direc['D'])+"\n")
						rw.write("<START T2> A "+str(direc['A'])+" B "+str(direc['B'])+" C "+str(direc['C'])+" D "+str(direc['D'])+"\n")
					if "READ" in l2[i]:
						temp = l2[i].split('READ')
						new = (temp[1].strip()).split(',')
						direc[new[1][:-1].strip()] = direc[new[0][1:].strip()]
					elif "WRITE" in l2[i]:
						temp = l2[i].split('WRITE')
						new = (temp[1].strip()).split(',')
						new[0] = new[0].strip()
						new[0] = new[0][1:].strip()
						uw.write("<T2,"+new[0]+","+str(direc[new[0]])+"> A "+str(direc['A'])+" B "+str(direc['B'])+" C "+str(direc['C'])+" D "+str(direc['D'])+"\n")
						direc[new[0].strip()] = direc[new[1][:-1].strip()]
						# print direc
						rw.write("<T2,"+new[0]+","+str(direc[new[0]])+"> A "+str(direc['A'])+" B "+str(direc['B'])+" C "+str(direc['C'])+" D "+str(direc['D'])+"\n")
					elif "OUTPUT" in l2[i]:
						if flag2 ==1:
						# temp = l1[i].split('OUTPUT(')
							uw.write("<COMMIT T2> A "+str(direc['A'])+" B "+str(direc['B'])+" C "+str(direc['C'])+" D "+str(direc['D'])+"\n")
							rw.write("<COMMIT T2> A "+str(direc['A'])+" B "+str(direc['B'])+" C "+str(direc['C'])+" D "+str(direc['D'])+"\n")
						# print temp[1][:-1].strip()
							flag2 = 0
					else:
						temp = l2[i].split('=')
						if "*" in temp[1]:
							new = temp[1].split('*')
							try:
								direc[temp[0].strip()] = direc[new[0].strip()]+direc[new[1].strip()]
							except:
								try:
								# print "hi"
								# print temp[0]
									direc[temp[0].strip()] = direc[new[0].strip()]*int(new[1].strip())
								except:
									direc[temp[0].strip()] = int(new[0].strip())*direc[new[1].strip()]
						if "-" in temp[1]:
							new = temp[1].split('-')
							try:
								direc[temp[0].strip()] = direc[new[0].strip()]-direc[new[1].strip()]
							except:
								try:
								# print "hi"
								# print temp[0]
									direc[temp[0].strip()] = direc[new[0].strip()]-int(new[1].strip())
								except:
									direc[temp[0].strip()] = int(new[0].strip())-direc[new[1].strip()]
						if "+" in temp[1]:
							new = temp[1].split('+')
							try:
								direc[temp[0].strip()] = direc[new[0].strip()]+direc[new[1].strip()]
							except:
								try:
								# print "hi"
								# print temp[0]
									direc[temp[0].strip()] = direc[new[0].strip()]+int(new[1].strip())
								except:
									direc[temp[0].strip()] = int(new[0].strip())+direc[new[1].strip()]
						if "/" in temp[1]:
							new = temp[1].split('/')
							try:
								direc[temp[0].strip()] = direc[new[0].strip()]+direc[new[1].strip()]
							except:
								try:
								# print "hi"
								# print temp[0]
									direc[temp[0].strip()] = direc[new[0].strip()]/int(new[1].strip())
								except:
									direc[temp[0].strip()] = int(new[0].strip())/direc[new[1].strip()]
				if j%3 == 2 and i<len(l3):
					if i==0:
						uw.write("<START T3> A "+str(direc['A'])+" B "+str(direc['B'])+" C "+str(direc['C'])+" D "+str(direc['D'])+"\n")
						rw.write("<START T3> A "+str(direc['A'])+" B "+str(direc['B'])+" C "+str(direc['C'])+" D "+str(direc['D'])+"\n")
					if "READ" in l3[i]:
						temp = l3[i].split('READ')
						new = (temp[1].strip()).split(',')
						direc[new[1][:-1].strip()] = direc[new[0][1:].strip()]
					elif "WRITE" in l3[i]:
						temp = l3[i].split('WRITE')
						new = (temp[1].strip()).split(',')
						new[0] = new[0].strip()
						new[0] = new[0][1:].strip()
						uw.write("<T3,"+new[0]+","+str(direc[new[0]])+"> A "+str(direc['A'])+" B "+str(direc['B'])+" C "+str(direc['C'])+" D "+str(direc['D'])+"\n")
						direc[new[0].strip()] = direc[new[1][:-1].strip()]
						rw.write("<T3,"+new[0]+","+str(direc[new[0]])+"> A "+str(direc['A'])+" B "+str(direc['B'])+" C "+str(direc['C'])+" D "+str(direc['D'])+"\n")
					elif "OUTPUT" in l3[i]:
						if flag3 ==1:
						# temp = l1[i].split('OUTPUT(')
							uw.write("<COMMIT T3> A "+str(direc['A'])+" B "+str(direc['B'])+" C "+str(direc['C'])+" D "+str(direc['D'])+"\n")
							rw.write("<COMMIT T3> A "+str(direc['A'])+" B "+str(direc['B'])+" C "+str(direc['C'])+" D "+str(direc['D'])+"\n")
						# print temp[1][:-1].strip()
							flag3 = 0
					else:
						temp = l3[i].split('=')
						if "*" in temp[1]:
							new = temp[1].split('*')
							try:
								direc[temp[0].strip()] = direc[new[0].strip()]+direc[new[1].strip()]
							except:
								try:
								# print "hi"
								# print temp[0]
									direc[temp[0].strip()] = direc[new[0].strip()]*int(new[1].strip())
								except:
									direc[temp[0].strip()] = int(new[0].strip())*direc[new[1].strip()]
						if "-" in temp[1]:
							new = temp[1].split('-')
							try:
								direc[temp[0].strip()] = direc[new[0].strip()]+direc[new[1].strip()]
							except:
								try:
								# print "hi"
								# print temp[0]
									direc[temp[0].strip()] = direc[new[0].strip()]-int(new[1].strip())
								except:
									direc[temp[0].strip()] = int(new[0].strip())-direc[new[1].strip()]
						if "+" in temp[1]:
							new = temp[1].split('+')
							try:
								direc[temp[0].strip()] = direc[new[0].strip()]+direc[new[1].strip()]
							except:
								try:
								# print "hi"
								# print temp[0]
									direc[temp[0].strip()] = direc[new[0].strip()]+int(new[1].strip())
								except:
									direc[temp[0].strip()] = int(new[0].strip())+direc[new[1].strip()]
						if "/" in temp[1]:
							new = temp[1].split('/')
							try:
								direc[temp[0].strip()] = direc[new[0].strip()]+direc[new[1].strip()]
							except:
								try:
								# print "hi"
								# print temp[0]
									direc[temp[0].strip()] = direc[new[0].strip()]/int(new[1].strip())
								except:
									direc[temp[0].strip()] = int(new[0].strip())/direc[new[1].strip()]
				i = i+1
		old = i
		
	if p == maxi:
		direc1 = direc
		
	if direc['A']==direc1['A'] and direc['B'] == direc1['B'] and direc['C'] == direc1['C'] and direc['D'] == direc1['D']:
		uw.write(str(p))
		rw.write(str(p))
		
	uw.close()
	rw.close()
