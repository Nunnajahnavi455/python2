#read data.txt and write into bengaluru.txt
fp1=open('data.txt','r')
data=fp1.read()
fp2=open('city.txt,'w)
fp2.write(data)  #file not available then it is going to create a new file.
open("city.txt",'a')
fp3=
