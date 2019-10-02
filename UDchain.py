a = input()
udpair = ""
define = ""
linenumber = 0
str_arr = a.split(' ')
c=0
string_def=""
#for c in range (a.__len__()):str_arr = a.split(';')
print(str_arr)
i=1
u=0
defline=0
strlength = str_arr.__len__()
for i in range  (strlength):
    k =1
    if(str_arr[i] == "="):
        define = str_arr[i-1]
        udpair = udpair +"[["+ define + ","
        string_def = string_def + define
        udpair = udpair + str(linenumber)+ "]"
        defline = linenumber
        u=u+1

        counter_line = 0
        for k in range(strlength):
            if str_arr[k] == ';': counter_line = counter_line + 1
            if (str_arr[k] == define):
                if (str_arr[k + 1] == "="):
                    k = k + 1
                elif k>=2:
                    #udpair = udpair - define
                    udpair = udpair + "**["+str_arr[k]+","+ str(defline) +"]"
                    udpair = udpair + "["+define+","+str(counter_line)+"]]"
                else:
                    udpair = udpair + "[" + str_arr[k] + ","
                    udpair = udpair  + str(counter_line) + "]]"


    if (str_arr[i]== ';'): linenumber = linenumber+1
#udpair = udpair + "*"
check = 0
i = 0
counter=0
for check in range (udpair.__len__()):
    i = check
    for i in range (udpair.__len__()):
        #if(udpair[i-1]!="*"):
           if(udpair[check]==udpair[i]):
            counter=counter+1
           else : counter=0
          # if counter==2: udpair[check]=""
print(udpair)
#print(string_def)
