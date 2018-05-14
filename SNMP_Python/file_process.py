xml = open("xml_1.1","r")
ProcessedValue = 0
NotYetProcessed = ""
#line = xml.readline()
for  line in xml:
	value = line[0]+line[1]+line[2]+line[3]+line[4]
	#if line[0] == 'c' and line[1] == 'l' and line[2] == 'a' and line[3] == 's' and line[4] == 's':
	#print(line[10]+line[11]+line[12]+line[13]+line[14]+line[15])	
	if value == "class":
		
		RawValue = line[10]+line[11]+line[12]+line[13]+line[14]+line[15]+line[16]
		
		for char in RawValue:
			if char == " ":
				continue
			elif char != " ":
				NotYetProcessed = NotYetProcessed + char
				#print(NotYetProcessed)
		ProcessedValue = int(ProcessedValue)+int(NotYetProcessed)
		NotYetProcessed = ""
	
	
print(ProcessedValue)
		
		 		
		
	
		


