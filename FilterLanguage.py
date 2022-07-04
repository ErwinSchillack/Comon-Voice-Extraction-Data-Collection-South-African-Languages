import sys
import os

header = "Language, Sentence Count, Location, Sentence"
Languages = ["isiZulu","isiXhosa","Afrikaans","English","Sesotho","Sesotho sa Leboa","Setswana","Xitsonga","SiSwati","Tshivenḓa","isiNdebele"]
Languages.remove(sys.argv[1])

for check in Languages:
    file = open("/home/erwin/Current/PythonCode/"+sys.argv[1]+"/ComparedOutput_secondary_"+sys.argv[1]+"_"+check+".txt","w")
    file = open("/home/erwin/Current/PythonCode/"+sys.argv[1]+"/ComparedOutput_secondary_"+sys.argv[1]+"_"+check+".txt","r+")
    if os.path.exists("/home/erwin/Current/PythonCode/"+sys.argv[1]+"/ComparedOutput_secondary_"+sys.argv[1]+"_"+check+".txt"):
        file.truncate(0)
        file.close()
    else:
        print("The file does not exist") 


lines = []
with open('/home/erwin/Current/cv-sentence-extractor/'+sys.argv[2]) as f:
    lines = f.read()
    lines = lines.split('\n')

Out = []
#print(lines)

keyword_file = open('/home/erwin/Current/PythonCode/'+sys.argv[3])

OutputFile = open("/home/erwin/Current/PythonCode/"+sys.argv[1]+"/ComparedOutput_primary_"+sys.argv[1]+".txt","w")
OutputFile.write(header + "\n"+"\n")
#OutputFile.close
result = keyword_file.read()
countList = 0
count = 0
a = 0

for line in result.split('\n'):
    
    if line == sys.argv[1]:
        count = count+1
        a = countList
        #Out = "{}: {} : {} : {}".format(sys.argv[1],count, a, lines[a])
        Out = "{}".format(lines[a])
        print(Out)
        OutputFile.write(str(Out)+"\n")
    else:
        for i in Languages:
            if line == i:
                OutputFile_second = open("/home/erwin/Current/PythonCode/"+sys.argv[1]+"/ComparedOutput_secondary_"+sys.argv[1]+"_"+i+".txt","a")
                Out = "{}".format(lines[countList])
                print(Out)
                OutputFile_second.write(str(Out)+"\n")
                break


    countList += 1
