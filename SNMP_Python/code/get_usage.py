#                                        |
#Autor: Daniel Gomes Venzi Gonçalves     |
#E-mail: daniel@avantsec.com.br          |
#Empresa: AvantSec                       |
#----------------------------------------#

#Incluir um break no loop de verificação de status da interface

import os
import sys
import json

#argv[1] = Endereço IP do firewall
#argv[2] = Community name do firewall
#argv[3] = Credenciais do usuário para requisição via API

#-------------------------------------------------------------------------------------------------------------------------------

def file_process():

    #Colocar aqui dps
    xml = open("xml","r")
    ProcessedValue = 0
    NotYetProcessed = ""
    #line = xml.readline()
    for  line in xml:
        value = line[0]+line[1]+line[2]+line[3]+line[4]
	    	
        if value == "class":
		
            RawValue = line[10]+line[11]+line[12]+line[13]+line[14]+line[15]+line[16]
            for char in RawValue:
                if  char == " ":
                    continue
                elif char != " ":
                    NotYetProcessed = NotYetProcessed + char
                    #print(NotYetProcessed)
            ProcessedValue = int(ProcessedValue)+int(NotYetProcessed)
            NotYetProcessed = ""

#print(ProcessedValue)
    return ProcessedValue

#------------------------------------------------------------------------------------------------------------------------------

def mem_process():

    xml = open("mem.info","r")
    ProcessedValue = 0
    NotYetProcessed = ""
    #line = xml.readline()
    for  line in xml:

        value_1 = line[0]+line[1]+line[2]+line[3]+line[4]+line[5]+line[6]+line[7]+line[8]+line[9]+line[10]+line[11]+line[12]+line[13]+line[14]+line[15]+line[16]+line[17]+line[18]+line[19]+line[20]+line[21]+line[22]+line[23]+line[24]+line[25]+line[26]+line[27]+line[28]+line[29]+line[30]+line[31]+line[32]+line[33]+line[34]+line[35]
        value_2 = line[0]+line[1]+line[2]+line[3]+line[4]+line[5]+line[6]+line[7]+line[8]+line[9]+line[10]+line[11]+line[12]+line[13]+line[14]+line[15]+line[16]+line[17]+line[18]+line[19]+line[20]+line[21]+line[22]+line[23]+line[24]+line[25]+line[26]+line[27]+line[28]+line[29]+line[30]+line[31]+line[32]+line[33]+line[34]+line[35]+line[36]+line[37]

        if  value_1 == "HOST-RESOURCES-MIB::hrStorageType.20":
            return line[50]+line[51]+line[52]+line[53]+line[54]+line[55]+line[56]+line[57]
        elif value_2 == "HOST-RESOURCES-MIB::hrStorageUsed.1020":
            return line[50]+line[51]+line[52]+line[53]+line[54]+line[55]+line[56]+line[57]


#------------------------------------------------------------------------------------------------------------------------------

def intStatus():
    
    value = open("int","r")
    Bolean = 0
    for line in value:
        line = line.strip('\n')
        #print(line)
        if len(line) == 21:
            #print("Chegou 1")
            #print(len(line))
            if line[4]+line[5]+line[6]+line[7]+line[8]+line[9]+line[10]+line[11]+line[12]+line[13]+line[14]+line[15]+line[16]+line[17]+line[18]+line[19]+line[20] == "<state>up</state>":
                #print("Chegou 2")
                Bolean = 1
                break
        elif len(line) == 50:
            #print("Chegou 3")
            if line[2]+line[3]+line[4]+line[5]+line[6]+line[7]+line[8] == "<error>":
                #print("Chegou 4")
                Bolean = 2
                break
    return Bolean


#------------------------------------------------------------------------------------------------------------------------------
#Colocar o main aqui:

OID = ["1.3.6.1.2.1.25.3.3.1.2.1","1.3.6.1.2.1.25.3.3.1.2.2","1.3.6.1.2.1.25.2.3","1.3.6.1.4.1.25461.2.1.2.3.3.0"]
#result = []
snmp_values = []
for value in OID:

    if str(value) == "1.3.6.1.2.1.25.2.3":
        os.system("snmpwalk -v 2c -c {0} {1} {2} > mem.info".format(sys.argv[2],sys.argv[1],value))
        #os.system("echo {0} > mem.info".format(HOLDER))
        result = mem_process()
        result = result.strip('\n')
        snmp_values.append(result)
        #print(result)

    elif str(value) == "1.3.6.1.2.1.25.3.3.1.2.1":
    #else:    
        result = str(os.popen("snmpget -v 2c -c {0} {1} {2} | cut -c50-100".format(sys.argv[2],sys.argv[1],value)).read())
        #print(result, end='')
        result = result.strip('\n')
        snmp_values.append(result)
        #print(result)
    
    elif str(value) == "1.3.6.1.2.1.25.3.3.1.2.2":
        result = str(os.popen("snmpget -v 2c -c {0} {1} {2} | cut -c50-100".format(sys.argv[2],sys.argv[1],value)).read())
        #print(result, end='')
        result = result.strip('\n')
        snmp_values.append(result)
        #print(result)

    elif str(value) == "1.3.6.1.4.1.25461.2.1.2.3.3.0":
        result = str(os.popen("snmpget -v 2c -c {0} {1} {2} | cut -c54-100".format(sys.argv[2],sys.argv[1],value)).read())
        #print(result, end='')
        result = result.strip('\n')
        snmp_values.append(result)
        #print(result)
        
    with open("result", "a") as out:
        #os.system("echo '{0};' > result".format(result))
        out.write(result+';')

activeEth =[]
for iterator in range(1,301):

   os.system("curl -k -X GET 'https://{0}/api/?type=op&cmd=%3Cshow%3E%3Cinterface%3Eethernet1%2F{1}%3C%2Finterface%3E%3C%2Fshow%3E&key={2}' > int".format(sys.argv[1],iterator,sys.argv[3]))
   #os.system("echo {0} > int".format(query))
   control = intStatus()
   #print(control)

   if control == 1:
        str(iterator)
        activeEth.append(iterator)
   elif control == 2:
        break
   #print(activeEth)

activeEthThrough =[]
for iterator in activeEth:
    #print(iterator)
    os.system("curl -k -X GET 'https://{0}/api/?type=op&cmd=%3Cshow%3E%3Cqos%3E%3Cinterface%3E%3Centry%20name%3D%27ethernet1%2F{1}%27%3E%3Cthroughput%3E0%3C%2Fthroughput%3E%3C%2Fentry%3E%3C%2Finterface%3E%3C%2Fqos%3E%3C%2Fshow%3E&key={2}' > xml".format(sys.argv[1],iterator, sys.argv[3]))
    #os.system("echo {0} > xml".format(query))
    result = str(file_process())
    #print(result)
    activeEthThrough.append(result)
    
    with open("result", "a") as out:
        out.write(result+';')

with open("result","r") as final:

    for line in final:
        print(line)

os.system("rm -f result")

keys = ["CPU Usage Data","CPU Usage Management","Memory Used","Total Active Sessions"]
son = {}
i=0
while i <= len(snmp_values)-1:
    son[keys[i]] = snmp_values[i]
    i += 1
i=0
while i <= len(activeEth)-1:
    son["Ethernet 1/"+str(activeEth[i])] = activeEthThrough[i]
    i += 1

estructure = json.dumps(son, ensure_ascii=False)
print(estructure)
#-------------------------------------------------------------------------------------------------------------------------------