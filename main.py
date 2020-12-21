import csv
import matplotlib.pyplot as plt
#you would add any other datasets to this list so the script can go through that data 
l=["1.csv"]
d={'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
for content in l:

    with open(content,'r',encoding="utf8") as f:
        csv_reader=csv.reader(f)
        #counting the first digit and appending it to the dictionary "d"
        #!!! in row.split(',')[x][0] .... replace the 3 with 0 for views, 1 for likes, 2 for dislikes and 3 for comments !!!
        for row in f:
            if row.split(',')[x][0] in d:
                d[row.split(',')[x][0]]+=1
            else:
                d[row.split(',')[x][0]]=1

#sum of all the occurances
sum=0
for i in d:
    sum=sum+int(d[i])
#new dictionary which holds the % of individual occurences   
d_new=dict()
for j in d:
    d_new[j]=(int(d[j])/sum)*100 
#shows the actual % values of the first digits.     
print(d_new)

#plotting the outcome
plt.bar(*zip(*d_new.items()))
plt.show() 
             
