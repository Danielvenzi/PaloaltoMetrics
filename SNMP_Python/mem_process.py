xml = open("mem.info_1.1","r")
ProcessedValue = 0
NotYetProcessed = ""
#line = xml.readline()
for  line in xml:

	value = line[0]+line[1]+line[2]+line[3]+line[4]+line[5]+line[6]+line[7]+line[8]+line[9]+line[10]+line[11]+line[12]+line[13]+line[14]+line[15]+line[16]+line[17]+line[18]+line[19]+line[20]+line[21]+line[22]+line[23]+line[24]+line[25]+line[26]+line[27]+line[28]+line[29]+line[30]+line[31]+line[32]+line[33]+line[34]+line[35]
        
	if value == "HOST-RESOURCES-MIB::hrStorageType.20":
		 print(line[50]+line[51]+line[52]+line[53]+line[54]+line[55]+line[56]+line[57])
