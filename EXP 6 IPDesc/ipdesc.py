import operator
IPStr = input("Enter IP Address: ")
IPMask = input("Enter IP Mask: ")
IPDetails = []
SubnetIP = []

def bitWiseOperation(numerator,denominator,operation):
	finalIP = []
	for i in range(0,len(numerator)):
		finalIP.append(operation(denominator[i],numerator[i]))
	return finalIP
def findFirstLastIP(IPMask, SubnetIP):
	IPDetails[3] = bitWiseOperation(SubnetIP,[0,0,0,1],operator.or_)
	IPDetails[3] = ".".join(map(str, IPDetails[3]))
	result = bitWiseOperation(IPMask,[255,255,255,255],operator.xor)
	result2 = bitWiseOperation(result,[0,0,0,1],operator.xor)
	IPDetails[4] = bitWiseOperation(result2,SubnetIP,operator.or_)
	IPDetails[4] = ".".join(map(str, IPDetails[4]))

def findDetails(IPStr,IPMask):
	IP = list(map(int,IPStr.split(".")))
	IPMask = list(map(int,IPMask.split(".")))

	for i in range (0,6):
		IPDetails.append(None)

	if (IP[0] == 127):
		IPDetails[0] = "Loop Back Address"
	# Class A
	if (IP[0] >=1 and IP[0] <= 126):
		IPDetails[0] = 'A'
		IPDetails[1] = '255.0.0.0'
	# Class B 
	elif (IP[0] >= 128 and IP[0] <= 191): 
		IPDetails[0] = 'B'
		IPDetails[1] = '255.255.0.0'
	# Class C 
	elif (IP[0] >= 192 and IP[0] <= 223):
		IPDetails[0] = 'C' 
		IPDetails[1] = '255.255.255.0'
	# Class D 
	elif (IP[0] >= 224 and IP[0] <= 239):
		IPDetails[0] = 'D' 
		IPDetails[1] = '255.255.255.255'
	# Class E 
	else:
		IPDetails[0] = 'E'
	IPDetails[2] = bitWiseOperation(IP,IPMask, operator.and_)
	findFirstLastIP(IPMask,IPDetails[2])
	IPDetails[2] = ".".join(map(str, IPDetails[2]))

findDetails(IPStr,IPMask)

print("\nIP Class: {0} \nSubnet Mask: {1} \nSubnetID: {2} \nFirstIP: {3} \nLastIP: {4}"
.format(IPDetails[0],IPDetails[1],IPDetails[2],IPDetails[3],IPDetails[4]))
