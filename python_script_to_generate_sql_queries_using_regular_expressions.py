import re


arrayoflocations=[] #not for colleges, but for front end
def addToList(self, str_to_add):
    if str_to_add not in self:
        self.append(str_to_add)
		
branches=['','Aeronotical','Automobile', 'Automobile', 'BioMedical', 'BioTechnology', 'Chemical', 'Civil', 'Computer', 'ElectricalAndElectronics', 'Electronics', 'ElectronicsAndCommunication', 'ElectronicsAndTelecommunication', 'Environmental', 'FoodProcessingTechnology', 'Industrial', 'Information technology', 'InstrumentationAndControl', 'Marine', 'Mechanical', 'Mechatronic', 'Metallurgy', 'Mining', 'PlasticTechnology', 'PowerElectronics', 'Production', 'RubberTechnology', 'TextileProduction', 'TextileTechnology', 'ComputerScienceAndEngineering', 'InformationAndCommunicationTechnology', 'ManufacturingEngineering', 'EnvironmentalScienceAndTechnology', 'Chemical Technology', ]		
# Apart from generating branches query and code for front end, we'll also use branches array to generate random branches for each college
f=open("table of colleges with other information.txt")
array=[]
array2=[]
array3=[]
array4=[]
collegeName=[]
collegeCode=[]
collegeFee=[]
collegeLoc=[]
strToSearch=""
pathFinder1=re.compile("\t\d{3,5}") #taking srno and collegecodes
pathFindercollegecode=re.compile("\d{3,5}") #taking college codes
pathFinder2=re.compile("\D+\,\s\w+")
pathFindercollegename=re.compile("\w+\D+")
pathFinder3=re.compile("\d+,\d+")
#no need for college fee path finder
pathFinder4=re.compile("\,\s\w+\D")
pathFindercollegeloc=re.compile("\w+") #taking college loc
for line in f:
	strToSearch=line
	findPat1=re.search(pathFinder1,strToSearch)
	findPat2=re.search(pathFinder2,strToSearch)
	findPat3=re.search(pathFinder3,strToSearch)
	findPat4=re.search(pathFinder4,strToSearch)
	array.append(findPat1)
	array2.append(findPat2)
	array3.append(findPat3)
	array4.append(findPat4)
	

	

#print(findPat2.group(0))
i=1
d=132
for element in array:
	if (i<d):
	
		#print(array[i].group(0))
		strToSearch=array[i].group(0)
		findPat1=re.search(pathFindercollegecode,strToSearch)
		collegeCode.append(findPat1);
		i+=1
	
i=0
for element in collegeCode: #for code . it starts from 0
	if (i<131):
		#print(collegeCode[i].group(0))
		i+=1

		
		
		
		
i=1		
for element in array2: 
	if (i<132):
	
		#print(array2[i].group(0))
		strToSearch=array2[i].group()
		findPat1=re.search(pathFindercollegename,strToSearch)
		collegeName.append(findPat1);
		i+=1
		
i=0
for element in collegeName: #for name . it starts from 0
	if (i<133):
		#print(collegeName[i].group())
		i+=1
		
		
		
i=1
d=132
for element in array3:
	if (i<d):
	
		#print(array3[i].group(0))
		collegeFee.append(array3[i].group(0));
		i+=1

i=0
for element in collegeFee: #for fee . it starts from 0 AND HAS NO GROUP
	if (i<133):
		#print(collegeFee[i])
		i+=1

		
		
i=1
d=132
for element in array4:
	if (i<d):
	
		#print(array4[i].group(0))
		strToSearch=array4[i].group()
		findPat1=re.search(pathFindercollegeloc,strToSearch)
		collegeLoc.append(findPat1);
		i+=1

i=0
for element in collegeLoc: #for loc . it starts from 0
	if (i<133):
		#print(collegeLoc[i].group())
		addToList(arrayoflocations,collegeLoc[i].group()) #this array has nothing to do with sql queries. This is for the locations file for the front end
		i+=1		
		
locations_file=open("locations.txt", "w");

for element in arrayoflocations:
	locations_file.write("<option value='"+element+"'>"+element+"</option>"+"\n")

locations_file.close() #locations file has been written now
	

print ("we will now create a file and write to it")
sql1=open("collegessql.txt", "w")
sql2=open("collegescoresql.txt", "w")
collegebranchessql=open("collegebranchessql.txt", "w")

import random
import string

def randomword(length): #random characters for generating college address
   return ''.join(random.choice(string.ascii_letters) for i in range(length))
   
i=0
index=1
while (i<131):
	#generating address
	numberoflettersinaddress=random.randint(50, 100)
	address=""
	address=randomword(numberoflettersinaddress)
		
	#generating pincode
	pincode=str(random.randint(111111,999999))
	
	#generating password
	password=str(random.randint(000000,999999))
	
	#generating contact
	contact=str(random.randint(00000000,99999999))
	
	#generating government/private
	government=str(0)
	if collegeName[i].group(0) == "DDIT GIA, Nadiad": 
		government=str(1)
	elif collegeName[i].group(0) == "BVM GIA, Vallabh":
		government=str(1)
	elif collegeName[i].group(0) == "GEC, Bharuch":
		government=str(1)
	elif collegeName[i].group(0) == "GEC, Bhavnagar":
		government=str(1)
	elif collegeName[i].group(0) == "GEC, Bhuj":
		government=str(1)
	elif collegeName[i].group(0) == "GEC, Dahod":
		government=str(1)
	elif collegeName[i].group(0) == "GEC, Gandhinagar":
		government=str(1)
	elif collegeName[i].group(0) == "GEC, Godhra":
		government=str(1)
	elif collegeName[i].group(0) == "GEC, Modasa":
		government=str(1)
	elif collegeName[i].group(0) == "GEC, Palanpur":
		government=str(1)
	elif collegeName[i].group(0) == "GEC, Patan":
		government=str(1)
	elif collegeName[i].group(0) == "GEC, Rajkot":
		government=str(1)
	elif collegeName[i].group(0) == "GEC, Surat":
		government=str(1)
	elif collegeName[i].group(0) == "GEC, Valsad":
		government=str(1)
	elif collegeName[i].group(0) == "L.D, Ahmedabad":
		government=str(1)
	elif collegeName[i].group(0) == "L.E, Morbi":
		government=str(1)
	elif collegeName[i].group(0) == "MSU, Vadodara":
		government=str(1)
	elif collegeName[i].group(0) == "Shantilal Shah, Bhavnagar":
		government=str(1)
	elif collegeName[i].group(0) == "VGEC, Ahmedabad":
		government=str(1)
	
	
	
	sql1.write("INSERT INTO `arleneupadatedmanas`.`colleges` (`college_id`, `name`, `address`, `pincode`, `email`, `password`, `contact`, `government`, `website`, `fees`, `city`) VALUES ("+collegeCode[i].group(0)+", '"+collegeName[i].group(0)+"', '"+address+"', "+pincode+", '"+collegeCode[i].group(0)+"@gtu.com""', '"+password+"', "+contact+", "+government+", '"+"http://"+collegeCode[i].group(0)+".com""', "+collegeFee[i]+", '"+collegeLoc[i].group(0)+"');\n")
	
	#generating random number for branches in this colleges
	numberofbranches=random.randint(3, 14)
	temparrayofbranchesforeachcollege=[]
	
	b=3
	while (b<=numberofbranches):
		
		#generating branch
		flag=0
		while(flag==0):
			randombranchnumber=random.randint(1,33)
			if branches[randombranchnumber] not in temparrayofbranchesforeachcollege:
				temparrayofbranchesforeachcollege.append(branches[randombranchnumber])
				flag=1
		
		#generating placement
		placement=str(random.randint(0,100))
		
		#generating infrastructure
		infrastructure=str(random.randint(0,4))
		
		#generating teachingquality
		teachingquality=str(random.randint(0,100))
		
		#generating resources
		resources=str(random.randint(1,5))
		
		sql2.write("INSERT INTO `arleneupadatedmanas`.`college_score` (`id`, `college_id`, `college_name`, `branch_id`, `branch_name`, `placement`, `infrastructure`, `teaching_quality`, `fees`, `location`) VALUES ("+str(index)+", "+collegeCode[i].group(0)+", '"+collegeName[i].group(0)+"', "+str(b)+", '"+branches[randombranchnumber]+"', "+placement+", "+infrastructure+", "+teachingquality+", "+collegeFee[i]+", '"+collegeLoc[i].group(0)+"');\n")
		collegebranchessql.write("INSERT INTO `arleneupadatedmanas`.`college_branches` (`college_id`, `branch_id`, `resources`) VALUES ("+collegeCode[i].group(0)+", "+str(b)+", "+resources+");\n");
		b+=1
		index+=1
	i+=1
sql2.close()
sql1.close()

#creating branches sql file
branchessql=open("branchessql.txt", "w")
i=1
while(i<=33):
	branchessql.write("INSERT INTO `arleneupadatedmanas`.`branches` (`branch_id`, `name`) VALUES ("+str(i)+", '"+branches[i]+"');\n")
	i+=1
		
branchessql.close()