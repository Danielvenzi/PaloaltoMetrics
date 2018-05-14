import os
import sys

#files = os.system("ls")

#shout = os.system("echo Bananas de pijamas > file")

#print(sys.argv[1])

#parm = sys.argv[1]

#shout = os.system("echo {}".format(parm))

#OID = ["1.3.6.1.2.1.25.3.3.1.2.1", "1.3.6.1.2.1.25.3.3.1.2.2", "1.3.6.1.2.1.25.2.3"]

#print(OID[0])

#for value in OID:

#    with open("result","a") as out:
#        out.write(value+';')

#for value in range(0,300):

#    print(value)

#query = os.system("curl -k -X GET 'google.com'")
#print(query)

#def test1(value_1):
#    print("Value1")


#def test2(value_2):

#    Boolean = '0'
 #   for letter in value_2:
 ##           Boolean = '1'
  #      elif letter == 'h':
  #          break
   #     print(letter)
   # print(Boolean)

#test2("Python")
#test2("DA")

#result = os.system("curl -k -X GET 'google.com' > file_whatever")
#os.system("echo {} > file_whatever".format(result))
#os.system("")

#banana = open("file_whatever","w")
#banana.write(result)

#<dp>dp0</dp>

#os.system("echo 123 > firewall")

#with open("firewall","r") as one:
 #   value = one.readline()
#
#    print(value)

value = os.popen("ls -l").read()
#value = os.system("echo result")
print(value)