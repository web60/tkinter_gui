#algorithm
#open fileone.txt 
#read line by line 
#for everyemail check if there is "one" and output it to a file called 'newfile.txt'


with open('fileone.txt','r',encoding='utf-8') as f:
    for line in f:
        currentLine=line
        email = currentLine.rsplit(':')[0]
        domain = email.split('@')[1]
        if(domain == "gmail.com"):
            newfile = open('newfile.txt','a',encoding='utf-8')
            newfile.write(email+'\n')
            newfile.close()
        