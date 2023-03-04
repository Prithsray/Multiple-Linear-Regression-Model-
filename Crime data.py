import pandas as pd
import random
import math

dt = pd.read_csv(r"D:\COLLEGEMATERIALS\Project SR Sir\Vocabulary App\python project research paper\crime_data.csv")
# print(dt)

# DECLARATION OF LISTS !!!

state_list = dt["RacialMatchCommPol"].tolist()  # x2 list
#age_list_16to24 = dt["agePct16t24"].tolist()  # age list (x3)
crime_list = dt["ViolentCrimesPerPop"].tolist()  # education list (x7)
population_list = dt["population"].tolist()       # population list (x1)
drug_list = dt["NumKindsDrugsSeiz"].tolist()  # drug list (x4)
police_require_list = dt["LemasTotReqPerPop"].tolist()   # crime list
#income_list = dt["indianPerCap"].tolist()  # income list (x9)

#   AVERAGE FUNCTION

def average(list):
    return sum(list) / len(list)

#  AMOUNT OF DATA TAKEN

n_1_2 = int((1/2) * len(state_list))
n_2_3= int((2/3) * len(state_list))
n_4_5= int((4/5) * len(state_list))


#    DECLARATION OF NUMERATOR AND DENOMINATOR LIST FOR B 



b1_neu_list_1_2 = []
b1_deno_list_1_2 = []

b2_neu_list_1_2 = []
b2_deno_list_1_2 = []

b1_neu_list_2_3 = []
b1_deno_list_2_3 = []

b2_neu_list_2_3 = []
b2_deno_list_2_3 = []

b1_neu_list_4_5 = []
b1_deno_list_4_5 = []

b2_neu_list_4_5 = []
b2_deno_list_4_5 = []

#  AVERGAE LISTS .........

police_require_average = round(average(police_require_list), 2)
# print(police_require_average)
crime_average = round(average(crime_list), 2)
#crime_average_HS= round(average(crime_list_HS), 2)
population_average = round(average(population_list), 2)
# print(population_average)


# FUNCTIONS 

def refilling_drug():
    for i in range (0,len(drug_list)):
        if(drug_list[i]== 0):
                drug_list[i]=crime_average
            
                
def refilling_police():
    for i in range (0,len(police_require_list)):
        if(police_require_list[i]== 0):
                police_require_list[i]=police_require_average

def confusion_matrix(list_pred,list_given):
    tp=0
    tn=0
    fp=0
    fn=0
    x=min(list_given)
    #print(x)
    #y=max(police_require_list)
    for i in range(0,len(list_pred)):  # comparing calculated value with actual value
        if(abs(list_pred[i] - list_given[i]) <=(x+0.1)):
             tp=tp+1
        elif(abs(list_pred[i] - list_given[i]) <=0.2):
            tn=tn+1
        elif(abs(list_given[i] - list_pred[i]) <=0.3):
            fp=fp+1
        else:
            fn=fn+1
            

    Accuracy=(((tp+tn)/(tp+tn+fp+fn))*100)
    Sensitivity=(tp/(tp+fn)*100)
    Specificity=(tn/(tn+fp)*100)
    Precision=(tp/(tp+fp)*100)
    Recall=(tp/(tp+fn)*100)
    F1_Score=(2*Precision*Recall/(Recall+Precision))
    matrix_pack=[]
    #matrix_pack.append(tp)
    #matrix_pack.append(tn)
    #matrix_pack.append(fp)
    #matrix_pack.append(fn)
    matrix_pack.append(Accuracy) 
    matrix_pack.append(Sensitivity)
    matrix_pack.append(Specificity) 
    matrix_pack.append(Precision)
    matrix_pack.append(F1_Score)           
    return(matrix_pack)

def standard_deviation(list):
    mean=(sum(list)/len(list))
    mean_list=[]
    mean_list_square=[]
    for i in range(0,len(list)):
        mean_list.append(list[i]-mean)

    for i in range(0,len(mean_list)):
        mean_list_square.append(mean_list[i]*mean_list[i])
    
    sum_list=sum(mean_list_square)/len(mean_list_square)
    Standard_deviation=math.sqrt(sum_list)
    return(Standard_deviation)

def R_square(list_pred,list_giv):
    mean=(sum(list_giv)/len(list_giv))
    R_square_neu=[]
    R_square_deno=[]
    y_minus_ypred=[]
    y_minus_ypred_square=[]
    y_minus_yavg=[]
    y_minus_yavg_square=[]
    for i in range(0,len(list_pred)):
        y_minus_ypred.append(list_giv[i]-list_pred[i])
        y_minus_yavg.append(list_giv[i]-mean)

    for i in range(0,len(y_minus_ypred)):
        y_minus_ypred_square.append(y_minus_ypred[i]*y_minus_ypred[i])
    
    for i in range(0,len(y_minus_yavg)):
        y_minus_yavg_square.append(y_minus_yavg[i]*y_minus_yavg[i])

    R_square_neu.append(sum(y_minus_ypred_square))
    R_square_deno.append(sum(y_minus_yavg_square))

    a=(sum(R_square_neu)/sum(R_square_deno))
    R_square=1-a
    return(R_square)


sd_police_requirement=standard_deviation(police_require_list)
sd_population=standard_deviation(population_list)
sd_crime=standard_deviation(crime_list)
 

print("S.D OF POLICE REQUIREMENT LIST: ",sd_police_requirement)
print("MEAN OF POLICE REQUIREMENT LIST :",police_require_average)
print("S.D OF POPULATION LIST: ",sd_population)
print("MEAN OF POPULATION LIST :",population_average)
print("S.D OF CRIME LIST: ",sd_crime)
print("MEAN OF CRIME LIST :",crime_average)



# FUNCTION CALLING

refilling_drug()
refilling_police()


# NUMERATOR AND DENOMINATOR LIST APPENDMENTS 

for i in range(0, n_1_2):
    b1_neu_list_1_2.append(
        (population_list[i] - population_average) *
        (police_require_list[i] - police_require_average)
    )
    b1_deno_list_1_2.append(
        (population_list[i] - population_average)
        * (population_list[i] - population_average)
    )
    b2_neu_list_1_2.append(
        (crime_list[i]-crime_average)*(police_require_list[i]-police_require_average)
        )
    b2_deno_list_1_2.append(
        (crime_list[i]-crime_average)*(crime_list[i]-crime_average)
        )


for j in range(0, n_2_3):
    b1_neu_list_2_3.append(
        (population_list[j] - population_average) *
        (police_require_list[j] - police_require_average)
    )
    b1_deno_list_2_3.append(
        (population_list[j] - population_average)
        * (population_list[j] - population_average)
    )
    b2_neu_list_2_3.append(
        (crime_list[j]-crime_average)*(police_require_list[j]-police_require_average)
        )
    b2_deno_list_2_3.append(
        (crime_list[j]-crime_average)*(crime_list[j]-crime_average)
        )   

 
for s in range(0, n_4_5):
    b1_neu_list_4_5.append(
        (population_list[s] - population_average) *
        (police_require_list[s] - police_require_average)
    )
    b1_deno_list_4_5.append(
        (population_list[s] - population_average)
        * (population_list[s] - population_average)
    )
    b2_neu_list_4_5.append(
        (crime_list[s]-crime_average)*(police_require_list[s]-police_require_average)
        )
    b2_deno_list_4_5.append(
        (crime_list[s]-crime_average)*(crime_list[s]-crime_average)
        )
# CALCULAION OF B   

b1_1_2 = round(sum(b1_neu_list_1_2) / sum(b1_deno_list_1_2), 2)
b2_1_2 = round(sum(b2_neu_list_1_2) / sum(b2_deno_list_1_2), 2)

b1_2_3 = round(sum(b1_neu_list_2_3) / sum(b1_deno_list_2_3), 2)
b2_2_3 = round(sum(b2_neu_list_2_3) / sum(b2_deno_list_2_3), 2)

b1_4_5 = round(sum(b1_neu_list_4_5) / sum(b1_deno_list_4_5), 2)
b2_4_5 = round(sum(b2_neu_list_4_5) / sum(b2_deno_list_4_5), 2)


#   CALCULATION OF A

sum_y = sum(police_require_list)  # y
# print("The sum of crime list is: ",sum_y)

l = []
for i in range(0, len(population_list)):  # list (x1)^2
    l.append(population_list[i] * population_list[i])
    
# print(l)

sum_x1_2 = sum(l)  # sum  of x^2
# print("The sum of (state list)^2 is: ",sum_x1_2)

sum_x = sum(population_list)  # sum of x

xy_1_2 = []
xy_2_3=[]
xy_4_5=[]


for i in range(0, n_1_2):
    xy_1_2.append(population_list[i] * police_require_list[i])

for i in range(0, n_2_3):
    xy_2_3.append(population_list[i] * police_require_list[i])

for i in range(0, n_4_5):
    xy_4_5.append(population_list[i] * police_require_list[i]) 

xy_1_2_sum = sum(xy_1_2)  # x*y
xy_2_3_sum = sum(xy_2_3)  # x*y
xy_4_5_sum = sum(xy_4_5)  # x*y

a_1_2 = ((sum_y * sum_x1_2) - (sum_x * xy_1_2_sum)) / \
    ((n_1_2 * sum_x1_2) - (sum_x * sum_x))

a_2_3 = ((sum_y * sum_x1_2) - (sum_x * xy_2_3_sum)) / \
    ((n_2_3 * sum_x1_2) - (sum_x * sum_x))

a_4_5 = ((sum_y * sum_x1_2) - (sum_x * xy_4_5_sum)) / \
    ((n_4_5 * sum_x1_2) - (sum_x * sum_x))

#print(a)
#print(b1)
#print(b2)
#print(b3)
#print(b4)
#print(b5)
#print(b6)
#print(b7)
#print(b8)
#print(b9)

#y_store_0tolast = []  # creating a list to store the calculated l0 data

y_store=[]    #storing 1/2 data
q_store=[]    #storing 2/3 data
r_store=[]    #storing 4/5 data

# calculating value for the left out index.........

for i in range(n_1_2+1,len(population_list)):  
    y_store.append((a_1_2 + (b1_1_2 * population_list[i]) +(b2_1_2*crime_list[i])))
    
for j in range(n_2_3+1,len(population_list)):  
    q_store.append((a_2_3 + (b1_2_3 * population_list[j]) +(b2_2_3*crime_list[j])))
    
for s in range(n_4_5+1,len(population_list)):  
    r_store.append((a_4_5 + (b1_4_5 * population_list[s]) +(b2_4_5*crime_list[s])))


# comparing calculated value with actual value

#for i in range(0,len(y_store)):
     
    #print(y_store[i], "                 -                   ", police_require_list[i])
    #print("no. data ->",i)
    #print(len(y_store))

k = 0
for i in range(0,len(y_store)):  # comparing calculated value with actual value
    if (
        ((y_store[i] - police_require_list[i]) <=
         0.2) and ((y_store[i] - police_require_list[i]) >= 0.0)
    ) or (
        ((police_require_list[i] - y_store[i]) <=
         0.2) and ((police_require_list[i] - y_store[i]) >= 0.0)
    ):
        k += 1
        
g = 0
for j in range(0,len(q_store)):  # comparing calculated value with actual value
    if (
        ((q_store[j] - police_require_list[j]) <=
         0.2) and ((q_store[j] - police_require_list[j]) >= 0.0)
    ) or (
        ((police_require_list[j] - q_store[j]) <=
         0.2) and ((police_require_list[j] - q_store[j]) >= 0.0)
    ):
        g += 1
        
        
f = 0
for s in range(0,len(r_store)):  # comparing calculated value with actual value
    if (
        ((r_store[s] - police_require_list[s]) <=
         0.2) and ((r_store[s] - police_require_list[s]) >= 0.0)
    ) or (
        ((police_require_list[s] - r_store[s]) <=
         0.2) and ((police_require_list[s] - r_store[s]) >= 0.0)
    ):
        f += 1

print(" ")
print("DATA COMPARING ACCURACY-1/2-> ",round(((k / len(y_store)) * 100),2))
print(" ")
#print((k / len(y_store)) * 100)

print("DATA COMPARING ACCURACY-2/3-> ",round(((g / len(q_store)) * 100),2))
print(" ")
#print((k / len(q_store)) * 100)
print("DATA COMPARING ACCURACY-4/5-> ",round(((f / len(r_store)) * 100),2))
print(" ")
#print((k / len(r_store)) * 100)

#****************************************************************************************************************************************************
#                                      10 FOLD CROSS VALIDATION 
#****************************************************************************************************************************************************

# set declarations

s1=set() 
s2=set()
s3=set()
s4=set()
s5=set()
s6=set()
s7=set()
s8=set()
s9=set()
s10=set()     

s11=set()
s22=set()
s33=set()
s44=set()
s55=set()
s66=set()
s77=set()
s88=set()
s99=set()
s1010=set()

# 1. for population list


poplist1=[]
poplist2=[]
poplist3=[]
poplist4=[]
poplist5=[]
poplist6=[]
poplist7=[]
poplist8=[]
poplist9=[]
poplist10=[]

# 2.for crime list
 
crimelist1=[]
crimelist2=[]
crimelist3=[]
crimelist4=[]
crimelist5=[]
crimelist6=[]
crimelist7=[]
crimelist8=[]
crimelist9=[]
crimelist10=[]

# 3.police require list

policerequirelist1=[]
policerequirelist2=[]
policerequirelist3=[]
policerequirelist4=[]
policerequirelist5=[]
policerequirelist6=[]
policerequirelist7=[]
policerequirelist8=[]
policerequirelist9=[]
policerequirelist10=[]

#Dividing the list in 10parts and adding random datas to set

while(len(s1)<len(population_list)//10):
    s1.add(random.randint(0,len(population_list)-1))
while(len(s2)<len(population_list)//10):
    s2.add(random.randint(0,len(population_list)-1)) 
    s2=s2-s1  
while(len(s3)<len(population_list)//10):
    s3.add(random.randint(0,len(population_list)-1)) 
    s3=s3-s2-s1 
while(len(s4)<len(population_list)//10):
    s4.add(random.randint(0,len(population_list)-1)) 
    s4=s4-s3-s2-s1
while(len(s5)<len(population_list)//10):
    s5.add(random.randint(0,len(population_list)-1)) 
    s5=s5-s4-s3-s2-s1
while(len(s6)<len(population_list)//10):
    s6.add(random.randint(0,len(population_list)-1)) 
    s6=s6-s5-s4-s3-s2-s1
while(len(s7)<len(population_list)//10):
    s7.add(random.randint(0,len(population_list)-1)) 
    s7=s7-s6-s5-s4-s3-s2-s1
while(len(s8)<len(population_list)//10):
    s8.add(random.randint(0,len(population_list)-1)) 
    s8=s8-s7-s6-s5-s4-s3-s2-s1
while(len(s9)<len(population_list)//10):
    s9.add(random.randint(0,len(population_list)-1)) 
    s9=s9-s8-s7-s6-s5-s4-s3-s2-s1
while(len(s10)<len(population_list)//10):
    s10.add(random.randint(0,len(population_list)-1)) 
    s10=s10-s9-s8-s7-s6-s5-s4-s3-s2-s1
   
s11=s11.union(s2,s3,s4,s5,s6,s7,s8,s9,s10)   
s22=s22.union(s1,s3,s4,s5,s6,s7,s8,s9,s10)   
s33=s33.union(s2,s1,s4,s5,s6,s7,s8,s9,s10)   
s44=s44.union(s2,s3,s1,s5,s6,s7,s8,s9,s10)   
s55=s55.union(s2,s3,s4,s1,s6,s7,s8,s9,s10)   
s66=s66.union(s2,s3,s4,s5,s1,s7,s8,s9,s10)   
s77=s77.union(s2,s3,s4,s5,s6,s1,s8,s9,s10)   
s88=s88.union(s2,s3,s4,s5,s6,s7,s1,s9,s10)   
s99=s99.union(s2,s3,s4,s5,s6,s7,s8,s1,s10)   
s1010=s1010.union(s2,s3,s4,s5,s6,s7,s8,s9,s1)   

for i in s11:
    poplist1.append(population_list[i])
    crimelist1.append(crime_list[i])
    policerequirelist1.append(police_require_list[i])

for i in s22:
    poplist2.append(population_list[i])
    crimelist2.append(crime_list[i])
    policerequirelist2.append(police_require_list[i])
for i in s33:
    poplist3.append(population_list[i])
    crimelist3.append(crime_list[i])
    policerequirelist3.append(police_require_list[i])
for i in s44:
    poplist4.append(population_list[i])
    crimelist4.append(crime_list[i])
    policerequirelist4.append(police_require_list[i])
for i in s55:
    poplist5.append(population_list[i])
    crimelist5.append(crime_list[i])
    policerequirelist5.append(police_require_list[i])
for i in s66:
    poplist6.append(population_list[i])
    crimelist6.append(crime_list[i])
    policerequirelist6.append(police_require_list[i])
for i in s77:
    poplist7.append(population_list[i])
    crimelist7.append(crime_list[i])
    policerequirelist7.append(police_require_list[i])
for i in s88:
    poplist8.append(population_list[i])
    crimelist8.append(crime_list[i])
    policerequirelist8.append(police_require_list[i])
for i in s99:
    poplist9.append(population_list[i])
    crimelist9.append(crime_list[i])
    policerequirelist9.append(police_require_list[i])
for i in s1010:
    poplist10.append(population_list[i])
    crimelist10.append(crime_list[i])
    policerequirelist10.append(police_require_list[i])    

# average list and average
 
poplist_average=[]
crimelist_average=[]
policerequirelist_average=[]

poplist_average.append(average(poplist1))
poplist_average.append(average(poplist2))
poplist_average.append(average(poplist3))
poplist_average.append(average(poplist4))
poplist_average.append(average(poplist5))
poplist_average.append(average(poplist6))
poplist_average.append(average(poplist7))
poplist_average.append(average(poplist8))
poplist_average.append(average(poplist9))
poplist_average.append(average(poplist10))

crimelist_average.append(average(crimelist1))
crimelist_average.append(average(crimelist2))
crimelist_average.append(average(crimelist3))
crimelist_average.append(average(crimelist4))
crimelist_average.append(average(crimelist5))
crimelist_average.append(average(crimelist6))
crimelist_average.append(average(crimelist7))
crimelist_average.append(average(crimelist8))
crimelist_average.append(average(crimelist9))
crimelist_average.append(average(crimelist10))

policerequirelist_average.append(average(policerequirelist1))
policerequirelist_average.append(average(policerequirelist2))
policerequirelist_average.append(average(policerequirelist3))
policerequirelist_average.append(average(policerequirelist4))
policerequirelist_average.append(average(policerequirelist5))
policerequirelist_average.append(average(policerequirelist6))
policerequirelist_average.append(average(policerequirelist7))
policerequirelist_average.append(average(policerequirelist8))
policerequirelist_average.append(average(policerequirelist9))
policerequirelist_average.append(average(policerequirelist10))



# Test Case 1

b11_neu_list=[]
b11_deno_list=[]
b21_neu_list=[]
b21_deno_list=[]

for i in range(len(s11)):
    b11_neu_list.append((poplist1[i]-average(poplist_average))* (policerequirelist1[i]-average(policerequirelist_average)))
    b11_deno_list.append((poplist1[i]-average(poplist_average))*(poplist1[i]-average(poplist_average)))
    b21_neu_list.append((crimelist1[i]-average(crimelist_average))*(policerequirelist1[i]-average(policerequirelist_average)))
    b21_deno_list.append((crimelist1[i]-average(crimelist_average))*(crimelist1[i]-average(crimelist_average)))

b11=round(sum(b11_neu_list)/sum(b11_deno_list),2)
b21=round(sum(b21_neu_list)/sum(b21_deno_list),2)

l11 = []
for i in range(0, len(s11)):  # list (x1)^2
    l11.append(poplist1[i] * poplist1[i])
# print(l)

sum_x1_2_11 = sum(l11)  # sum  of x^2
# print("The sum of (state list)^2 is: ",sum_x1_2)

sum_x_11 = sum(population_list)  # sum of x
sum_y11 = sum(policerequirelist1)

xy11 = []
for i in range(0, len(s11)):
    xy11.append(poplist1[i] * policerequirelist1[i])


xy_sum11 = sum(xy11)  # x*y

a11 = ((sum_y11 * sum_x1_2_11) - (sum_x_11 * xy_sum11)) / \
    ((len(s11) * sum_x1_2_11) - (sum_x_11 * sum_x_11))

y_store_11=[] 
q_store_11=[]    #storing 2/3 data
r_store_11=[]    #storing 1/2 data

for i in range(len(s1)):  
    y_store_11.append((a11 + (b11 * poplist1[i]) +(b21*crimelist1[i])))
    
#for i in range(0,len(y_store_11)):  # comparing calculated value with actual value
    #print(y_store_11[i], "                 -                   ", policerequirelist1[i])
    #print(len(y_store))

k11 = 0

for i in range(0,len(y_store_11)):  # comparing calculated value with actual value
    if (
        ((y_store_11[i] - policerequirelist1[i]) <=
         0.2) and ((y_store_11[i] - policerequirelist1[i]) >= 0.0)
    ) or (
        ((policerequirelist1[i] - y_store_11[i]) <=
         0.2) and ((policerequirelist1[i] - y_store_11[i]) >= 0.0)
    ):
        k11 += 1
        
        
#print(" ")
#print((k11 / len(y_store_11)) * 100)
#print(" ")
Tc1_accuracy= confusion_matrix(y_store_11,policerequirelist1)
Tc1_Standard_Div=standard_deviation(y_store_11)
Tc1_R_square=R_square(y_store_11,policerequirelist1)
Tc1_mean_pred=average(y_store_11)
Tc1_mean_giv=average(policerequirelist1)


# Test Case 2

b12_neu_list=[]
b12_deno_list=[]
b22_neu_list=[]
b22_deno_list=[]

for i in range(len(s22)):
    b12_neu_list.append((poplist2[i]-average(poplist_average))* (policerequirelist2[i]-average(policerequirelist_average)))
    b12_deno_list.append((poplist2[i]-average(poplist_average))*(poplist2[i]-average(poplist_average)))
    b22_neu_list.append((crimelist2[i]-average(crimelist_average))*(policerequirelist2[i]-average(policerequirelist_average)))
    b22_deno_list.append((crimelist2[i]-average(crimelist_average))*(crimelist2[i]-average(crimelist_average)))

b12=round(sum(b12_neu_list)/sum(b12_deno_list),2)
b22=round(sum(b22_neu_list)/sum(b22_deno_list),2)

l22 = []
for i in range(0, len(s22)):  # list (x1)^2
    l22.append(poplist2[i] * poplist2[i])
# print(l)

sum_x1_2_22 = sum(l22)  # sum  of x^2
# print("The sum of (state list)^2 is: ",sum_x1_2)

sum_x_22 = sum(population_list)  # sum of x
sum_y22 = sum(policerequirelist2)

xy22 = []
for i in range(0, len(s22)):
    xy22.append(poplist2[i] * policerequirelist2[i])

xy_sum22 = sum(xy22)  # x*y

a22 = ((sum_y22 * sum_x1_2_22) - (sum_x_22 * xy_sum22)) / \
    ((len(s22) * sum_x1_2_22) - (sum_x_22 * sum_x_22))

y_store_22=[] 
q_store_22=[] 
r_store_22=[] 

for i in range(len(s2)):  
    y_store_22.append((a22 + (b12 * poplist2[i]) +(b22*crimelist2[i])))


#for i in range(0,len(y_store_22)):  # comparing calculated value with actual value

    #print(y_store_22[i], "                 -                   ", policerequirelist2[i])
    #print()
    #print(len(y_store))

k22 = 0
for i in range(0,len(y_store_22)):  # comparing calculated value with actual value
    if (
        ((y_store_22[i] - policerequirelist2[i]) <=
         0.2) and ((y_store_22[i] - policerequirelist2[i]) >= 0.0)
    ) or (
        ((policerequirelist2[i] - y_store_22[i]) <=
         0.2) and ((policerequirelist2[i] - y_store_22[i]) >= 0.0)
    ):
        k22 += 1
        
#print(" ")
#print((k22 / len(y_store_22)) * 100)
#print(" ")
Tc2_accuracy=confusion_matrix(y_store_22,policerequirelist2)
Tc2_Standard_Div=standard_deviation(y_store_22)
Tc2_R_square=R_square(y_store_22,policerequirelist2)
Tc2_mean_pred=average(y_store_22)
Tc2_mean_giv=average(policerequirelist2)


# Test Case 3

b13_neu_list=[]
b13_deno_list=[]
b23_neu_list=[]
b23_deno_list=[]

for i in range(len(s33)):
    b13_neu_list.append((poplist3[i]-average(poplist_average))* (policerequirelist3[i]-average(policerequirelist_average)))
    b13_deno_list.append((poplist3[i]-average(poplist_average))*(poplist3[i]-average(poplist_average)))
    b23_neu_list.append((crimelist3[i]-average(crimelist_average))*(policerequirelist3[i]-average(policerequirelist_average)))
    b23_deno_list.append((crimelist3[i]-average(crimelist_average))*(crimelist3[i]-average(crimelist_average)))

b13=round(sum(b13_neu_list)/sum(b13_deno_list),2)
b23=round(sum(b23_neu_list)/sum(b23_deno_list),2)

l33 = []
for i in range(0, len(s33)):  # list (x1)^2
    l33.append(poplist3[i] * poplist3[i])
# print(l)

sum_x1_2_33 = sum(l33)  # sum  of x^2
# print("The sum of (state list)^2 is: ",sum_x1_2)

sum_x_33 = sum(population_list)  # sum of x
sum_y33 = sum(policerequirelist3)

xy33 = []
for i in range(0, len(s33)):
    xy33.append(poplist3[i] * policerequirelist3[i])

xy_sum33 = sum(xy33)  # x*y

a33 = ((sum_y33 * sum_x1_2_33) - (sum_x_33 * xy_sum33)) / \
    ((len(s33) * sum_x1_2_33) - (sum_x_33 * sum_x_33))

y_store_33=[] 
q_store_33=[] 
r_store_33=[] 
for i in range(len(s3)):  
    y_store_33.append((a33 + (b13 * poplist3[i]) +(b23*crimelist3[i])))
    
#for i in range(0,len(y_store_33)):  # comparing calculated value with actual value

    #print(y_store_33[i], "                 -                   ", policerequirelist3[i])
    #print()
    #print(len(y_store))

k33 = 0
for i in range(0,len(y_store_33)):  # comparing calculated value with actual value
    if (
        ((y_store_33[i] - policerequirelist3[i]) <=
         0.2) and ((y_store_33[i] - policerequirelist3[i]) >= 0.0)
    ) or (
        ((policerequirelist3[i] - y_store_33[i]) <=
         0.2) and ((policerequirelist3[i] - y_store_33[i]) >= 0.0)
    ):
        k33 += 1
    

#print(" ")
#print((k33 / len(y_store_33)) * 100)
#print(" ")
Tc3_accuracy=confusion_matrix(y_store_33,policerequirelist3)
Tc3_Standard_Div=standard_deviation(y_store_33)
Tc3_R_square=R_square(y_store_33,policerequirelist3)
Tc3_mean_pred=average(y_store_33)
Tc3_mean_giv=average(policerequirelist3)


# Test Case 4

b14_neu_list=[]
b14_deno_list=[]
b24_neu_list=[]
b24_deno_list=[]

for i in range(len(s44)):
    b14_neu_list.append((poplist4[i]-average(poplist_average))* (policerequirelist4[i]-average(policerequirelist_average)))
    b14_deno_list.append((poplist4[i]-average(poplist_average))*(poplist4[i]-average(poplist_average)))
    b24_neu_list.append((crimelist4[i]-average(crimelist_average))*(policerequirelist4[i]-average(policerequirelist_average)))
    b24_deno_list.append((crimelist4[i]-average(crimelist_average))*(crimelist4[i]-average(crimelist_average)))

b14=round(sum(b14_neu_list)/sum(b14_deno_list),2)
b24=round(sum(b24_neu_list)/sum(b24_deno_list),2)

l44 = []
for i in range(0, len(s44)):  # list (x1)^2
    l44.append(poplist4[i] * poplist4[i])
# print(l)

sum_x1_2_44 = sum(l44)  # sum  of x^2
# print("The sum of (state list)^2 is: ",sum_x1_2)

sum_x_44 = sum(population_list)  # sum of x
sum_y44 = sum(policerequirelist4)

xy44 = []
for i in range(0, len(s44)):
    xy44.append(poplist4[i] * policerequirelist4[i])

xy_sum44 = sum(xy44)  # x*y

a44 = ((sum_y44 * sum_x1_2_44) - (sum_x_44 * xy_sum44)) / \
    ((len(s44) * sum_x1_2_44) - (sum_x_44 * sum_x_44))

y_store_44=[] 
q_store_44=[] 
r_store_44=[] 
for i in range(len(s4)):  
    y_store_44.append((a44 + (b14 * poplist4[i]) +(b24*crimelist4[i])))
    

#for i in range(0,len(y_store_44)):  # comparing calculated value with actual value

    #print(y_store_44[i], "                 -                   ", policerequirelist4[i])
    #print()
    #print(len(y_store))

k44 = 0
for i in range(0,len(y_store_44)):  # comparing calculated value with actual value
    if (
        ((y_store_44[i] - policerequirelist4[i]) <=
         0.2) and ((y_store_44[i] - policerequirelist4[i]) >= 0.0)
    ) or (
        ((policerequirelist4[i] - y_store_44[i]) <=
         0.2) and ((policerequirelist4[i] - y_store_44[i]) >= 0.0)
    ):
        k44 += 1
        
#print(" ")
#print((k44 / len(y_store_44)) * 100)
#print(" ")
Tc4_accuracy=confusion_matrix(y_store_44,policerequirelist4)
Tc4_Standard_Div=standard_deviation(y_store_44)
Tc4_R_square=R_square(y_store_44,policerequirelist4)
Tc4_mean_pred=average(y_store_44)
Tc4_mean_giv=average(policerequirelist4)


# Test Case 5

b15_neu_list=[]
b15_deno_list=[]
b25_neu_list=[]
b25_deno_list=[]

for i in range(len(s55)):
    b15_neu_list.append((poplist5[i]-average(poplist_average))* (policerequirelist5[i]-average(policerequirelist_average)))
    b15_deno_list.append((poplist5[i]-average(poplist_average))*(poplist5[i]-average(poplist_average)))
    b25_neu_list.append((crimelist5[i]-average(crimelist_average))*(policerequirelist5[i]-average(policerequirelist_average)))
    b25_deno_list.append((crimelist5[i]-average(crimelist_average))*(crimelist5[i]-average(crimelist_average)))

b15=round(sum(b15_neu_list)/sum(b15_deno_list),2)
b25=round(sum(b25_neu_list)/sum(b25_deno_list),2)

l55 = []
for i in range(0, len(s55)):  # list (x1)^2
    l55.append(poplist5[i] * poplist5[i])
# print(l)

sum_x1_2_55 = sum(l55)  # sum  of x^2
# print("The sum of (state list)^2 is: ",sum_x1_2)

sum_x_55 = sum(population_list)  # sum of x
sum_y55 = sum(policerequirelist5)

xy55 = []
for i in range(0, len(s55)):
    xy55.append(poplist5[i] * policerequirelist5[i])

xy_sum55 = sum(xy55)  # x*y

a55 = ((sum_y55 * sum_x1_2_55) - (sum_x_55 * xy_sum55)) / \
    ((len(s55) * sum_x1_2_55) - (sum_x_55 * sum_x_55))

y_store_55=[] 
q_store_55=[] 
r_store_55=[] 

for i in range(len(s5)):  
    y_store_55.append((a55 + (b15 * poplist5[i]) +(b25*crimelist5[i])))
    

#for i in range(0,len(y_store_55)):  # comparing calculated value with actual value

    #print(y_store_55[i], "                 -                   ", policerequirelist5[i])
    #print()
    #print(len(y_store))

k55 = 0
for i in range(0,len(y_store_55)):  # comparing calculated value with actual value
    if (
        ((y_store_55[i] - policerequirelist5[i]) <=
         0.2) and ((y_store_55[i] - policerequirelist5[i]) >= 0.0)
    ) or (
        ((policerequirelist5[i] - y_store_55[i]) <=
         0.2) and ((policerequirelist5[i] - y_store_55[i]) >= 0.0)
    ):
        k55 += 1
        
        
#print(" ")
#print((k55 / len(y_store_55)) * 100)
#print(" ")
Tc5_accuracy=confusion_matrix(y_store_55,policerequirelist5)
Tc5_Standard_Div=standard_deviation(y_store_55)
Tc5_R_square=R_square(y_store_55,policerequirelist5)
Tc5_mean_pred=average(y_store_55)
Tc5_mean_giv=average(policerequirelist5)


# Test Case 6

b16_neu_list=[]
b16_deno_list=[]
b26_neu_list=[]
b26_deno_list=[]

for i in range(len(s66)):
    b16_neu_list.append((poplist6[i]-average(poplist_average))* (policerequirelist6[i]-average(policerequirelist_average)))
    b16_deno_list.append((poplist6[i]-average(poplist_average))*(poplist6[i]-average(poplist_average)))
    b26_neu_list.append((crimelist6[i]-average(crimelist_average))*(policerequirelist6[i]-average(policerequirelist_average)))
    b26_deno_list.append((crimelist6[i]-average(crimelist_average))*(crimelist6[i]-average(crimelist_average)))

b16=round(sum(b16_neu_list)/sum(b16_deno_list),2)
b26=round(sum(b26_neu_list)/sum(b26_deno_list),2)

l66 = []
for i in range(0, len(s66)):  # list (x1)^2
    l66.append(poplist6[i] * poplist6[i])
# print(l)

sum_x1_2_66 = sum(l66)  # sum  of x^2
# print("The sum of (state list)^2 is: ",sum_x1_2)

sum_x_66 = sum(population_list)  # sum of x
sum_y66 = sum(policerequirelist6)

xy66 = []
for i in range(0, len(s66)):
    xy66.append(poplist6[i] * policerequirelist6[i])

xy_sum66 = sum(xy66)  # x*y

a66 = ((sum_y66 * sum_x1_2_66) - (sum_x_66 * xy_sum66)) / \
    ((len(s66) * sum_x1_2_66) - (sum_x_66 * sum_x_66))

y_store_66=[] 
q_store_66=[] 
r_store_66=[] 

for i in range(len(s6)):  
    y_store_66.append((a66 + (b16 * poplist6[i]) +(b26*crimelist6[i])))

#for i in range(0,len(y_store_66)):  # comparing calculated value with actual value

    #print(y_store_66[i], "                 -                   ", policerequirelist6[i])
    #print()
    #print(len(y_store))

k66 = 0
for i in range(0,len(y_store_66)):  # comparing calculated value with actual value
    if (
        ((y_store_66[i] - policerequirelist6[i]) <=
         0.2) and ((y_store_66[i] - policerequirelist6[i]) >= 0.0)
    ) or (
        ((policerequirelist6[i] - y_store_66[i]) <=
         0.2) and ((policerequirelist6[i] - y_store_66[i]) >= 0.0)
    ):
        k66 += 1
        

#print(" ")
#print((k66 / len(y_store_66)) * 100)
#print(" ")
Tc6_accuracy=confusion_matrix(y_store_66,policerequirelist6)
Tc6_Standard_Div=standard_deviation(y_store_66)
Tc6_R_square=R_square(y_store_66,policerequirelist6)
Tc6_mean_pred=average(y_store_66)
Tc6_mean_giv=average(policerequirelist6)


# Test Case 7

b17_neu_list=[]
b17_deno_list=[]
b27_neu_list=[]
b27_deno_list=[]

for i in range(len(s77)):
    b17_neu_list.append((poplist7[i]-average(poplist_average))* (policerequirelist7[i]-average(policerequirelist_average)))
    b17_deno_list.append((poplist7[i]-average(poplist_average))*(poplist7[i]-average(poplist_average)))
    b27_neu_list.append((crimelist7[i]-average(crimelist_average))*(policerequirelist7[i]-average(policerequirelist_average)))
    b27_deno_list.append((crimelist7[i]-average(crimelist_average))*(crimelist7[i]-average(crimelist_average)))

b17=round(sum(b17_neu_list)/sum(b17_deno_list),2)
b27=round(sum(b27_neu_list)/sum(b27_deno_list),2)

l77 = []
for i in range(0, len(s77)):  # list (x1)^2
    l77.append(poplist7[i] * poplist7[i])
# print(l)

sum_x1_2_77 = sum(l77)  # sum  of x^2
# print("The sum of (state list)^2 is: ",sum_x1_2)

sum_x_77 = sum(population_list)  # sum of x
sum_y77 = sum(policerequirelist7)

xy77 = []
for i in range(0, len(s77)):
    xy77.append(poplist7[i] * policerequirelist7[i])

xy_sum77 = sum(xy77)  # x*y

a77 = ((sum_y77 * sum_x1_2_77) - (sum_x_77 * xy_sum77)) / \
    ((len(s77) * sum_x1_2_77) - (sum_x_77 * sum_x_77))

y_store_77=[] 
q_store_77=[] 
r_store_77=[] 

for i in range(len(s7)):  
    y_store_77.append((a77 + (b17 * poplist7[i]) +(b27*crimelist7[i])))
    
#for i in range(0,len(y_store_77)):  # comparing calculated value with actual value

    #print(y_store_77[i], "                 -                   ", policerequirelist7[i])
    #print()
    #print(len(y_store))

k77 = 0
for i in range(0,len(y_store_77)):  # comparing calculated value with actual value
    if (
        ((y_store_77[i] - policerequirelist7[i]) <=
         0.2) and ((y_store_77[i] - policerequirelist7[i]) >= 0.0)
    ) or (
        ((policerequirelist7[i] - y_store_77[i]) <=
         0.2) and ((policerequirelist7[i] - y_store_77[i]) >= 0.0)
    ):
        k77 += 1
        

#print(" ")
#print((k77 / len(y_store_77)) * 100)
#print(" ")
Tc7_accuracy=confusion_matrix(y_store_77,policerequirelist7)
Tc7_Standard_Div=standard_deviation(y_store_77)
Tc7_R_square=R_square(y_store_77,policerequirelist7)
Tc7_mean_pred=average(y_store_77)
Tc7_mean_giv=average(policerequirelist7)

# Test Case 8

b18_neu_list=[]
b18_deno_list=[]
b28_neu_list=[]
b28_deno_list=[]

for i in range(len(s88)):
    b18_neu_list.append((poplist8[i]-average(poplist_average))* (policerequirelist8[i]-average(policerequirelist_average)))
    b18_deno_list.append((poplist8[i]-average(poplist_average))*(poplist8[i]-average(poplist_average)))
    b28_neu_list.append((crimelist8[i]-average(crimelist_average))*(policerequirelist8[i]-average(policerequirelist_average)))
    b28_deno_list.append((crimelist8[i]-average(crimelist_average))*(crimelist8[i]-average(crimelist_average)))

b18=round(sum(b18_neu_list)/sum(b18_deno_list),2)
b28=round(sum(b28_neu_list)/sum(b28_deno_list),2)

l88 = []
for i in range(0, len(s88)):  # list (x1)^2
    l88.append(poplist8[i] * poplist8[i])
# print(l)

sum_x1_2_88 = sum(l88)  # sum  of x^2
# print("The sum of (state list)^2 is: ",sum_x1_2)

sum_x_88 = sum(population_list)  # sum of x
sum_y88 = sum(policerequirelist8)

xy88 = []
for i in range(0, len(s88)):
    xy88.append(poplist8[i] * policerequirelist8[i])

xy_sum88 = sum(xy88)  # x*y

a88 = ((sum_y88 * sum_x1_2_88) - (sum_x_88 * xy_sum88)) / \
    ((len(s88) * sum_x1_2_88) - (sum_x_88 * sum_x_88))

y_store_88=[] 
q_store_88=[] 
r_store_88=[] 

for i in range(len(s8)):  
    y_store_88.append((a88 + (b18 * poplist8[i]) +(b28*crimelist8[i])))
    


#for i in range(0,len(y_store_88)):  # comparing calculated value with actual value

    #print(y_store_88[i], "                 -                   ", policerequirelist8[i])
    #print()
    #print(len(y_store))

k88 = 0
for i in range(0,len(y_store_88)):  # comparing calculated value with actual value
    if (
        ((y_store_88[i] - policerequirelist8[i]) <=
         0.2) and ((y_store_88[i] - policerequirelist8[i]) >= 0.0)
    ) or (
        ((policerequirelist8[i] - y_store_88[i]) <=
         0.2) and ((policerequirelist8[i] - y_store_88[i]) >= 0.0)
    ):
        k88 += 1
        
#print(" ")
#print((k88 / len(y_store_88)) * 100)
#print(" ")
Tc8_accuracy=confusion_matrix(y_store_88,policerequirelist8)
Tc8_Standard_Div=standard_deviation(y_store_88)
Tc8_R_square=R_square(y_store_88,policerequirelist8)
Tc8_mean_pred=average(y_store_88)
Tc8_mean_giv=average(policerequirelist8)


# Test Case 9

b19_neu_list=[]
b19_deno_list=[]
b29_neu_list=[]
b29_deno_list=[]

for i in range(len(s99)):
    b19_neu_list.append((poplist9[i]-average(poplist_average))* (policerequirelist9[i]-average(policerequirelist_average)))
    b19_deno_list.append((poplist9[i]-average(poplist_average))*(poplist9[i]-average(poplist_average)))
    b29_neu_list.append((crimelist9[i]-average(crimelist_average))*(policerequirelist9[i]-average(policerequirelist_average)))
    b29_deno_list.append((crimelist9[i]-average(crimelist_average))*(crimelist9[i]-average(crimelist_average)))

b19=round(sum(b19_neu_list)/sum(b19_deno_list),2)
b29=round(sum(b29_neu_list)/sum(b29_deno_list),2)

l99 = []
for i in range(0, len(s99)):  # list (x1)^2
    l99.append(poplist9[i] * poplist9[i])
# print(l)

sum_x1_2_99 = sum(l99)  # sum  of x^2
# print("The sum of (state list)^2 is: ",sum_x1_2)

sum_x_99 = sum(population_list)  # sum of x
sum_y99 = sum(policerequirelist9)

xy99 = []
for i in range(0, len(s99)):
    xy99.append(poplist9[i] * policerequirelist9[i])

xy_sum99 = sum(xy99)  # x*y

a99 = ((sum_y99 * sum_x1_2_99) - (sum_x_99 * xy_sum99)) / \
    ((len(s99) * sum_x1_2_99) - (sum_x_99 * sum_x_99))

y_store_99=[] 
q_store_99=[] 
r_store_99=[] 

for i in range(len(s9)):  
    y_store_99.append((a99 + (b19 * poplist9[i]) +(b29*crimelist9[i])))
    

#for i in range(0,len(y_store_99)):  # comparing calculated value with actual value

    #print(y_store_99[i], "                 -                   ", policerequirelist9[i])
    #print()
    #print(len(y_store))

k99 = 0
for i in range(0,len(y_store_99)):  # comparing calculated value with actual value
    if (
        ((y_store_99[i] - policerequirelist9[i]) <=
         0.2) and ((y_store_99[i] - policerequirelist9[i]) >= 0.0)
    ) or (
        ((policerequirelist9[i] - y_store_99[i]) <=
         0.2) and ((policerequirelist9[i] - y_store_99[i]) >= 0.0)
    ):
        k99 += 1
        
#print(" ")
#print((k99 / len(y_store_99)) * 100)
#print(" ")
Tc9_accuracy=confusion_matrix(y_store_99,policerequirelist9)
Tc9_Standard_Div=standard_deviation(y_store_99)
Tc9_R_square=R_square(y_store_99,policerequirelist9)
Tc9_mean_pred=average(y_store_99)
Tc9_mean_giv=average(policerequirelist9)



# Test Case 10

b110_neu_list=[]
b110_deno_list=[]
b210_neu_list=[]
b210_deno_list=[]

for i in range(len(s99)):
    b110_neu_list.append((poplist10[i]-average(poplist_average))* (policerequirelist10[i]-average(policerequirelist_average)))
    b110_deno_list.append((poplist10[i]-average(poplist_average))*(poplist10[i]-average(poplist_average)))
    b210_neu_list.append((crimelist10[i]-average(crimelist_average))*(policerequirelist10[i]-average(policerequirelist_average)))
    b210_deno_list.append((crimelist10[i]-average(crimelist_average))*(crimelist10[i]-average(crimelist_average)))

b110=round(sum(b110_neu_list)/sum(b110_deno_list),2)
b210=round(sum(b210_neu_list)/sum(b210_deno_list),2)

l1010 = []
for i in range(0, len(s1010)):  # list (x1)^2
    l1010.append(poplist10[i] * poplist10[i])
# print(l)

sum_x1_2_1010 = sum(l1010)  # sum  of x^2
# print("The sum of (state list)^2 is: ",sum_x1_2)

sum_x_1010 = sum(population_list)  # sum of x
sum_y1010 = sum(policerequirelist10)

xy1010 = []
for i in range(0, len(s1010)):
    xy1010.append(poplist10[i] * policerequirelist10[i])

xy_sum1010 = sum(xy1010)  # x*y

a1010 = ((sum_y1010 * sum_x1_2_1010) - (sum_x_1010 * xy_sum1010)) / \
    ((len(s1010) * sum_x1_2_1010) - (sum_x_1010 * sum_x_1010))

y_store_1010=[] 
q_store_1010=[] 
r_store_1010=[] 

for i in range(len(s10)):  
    y_store_1010.append((a1010 + (b110 * poplist10[i]) +(b210*crimelist10[i])))

#for i in range(0,len(y_store_1010)):  # comparing calculated value with actual value

    #print(y_store_1010[i], "                 -                   ", policerequirelist10[i])
    #print()
    #print(len(y_store))

k1010 = 0
for i in range(0,len(y_store_1010)):  # comparing calculated value with actual value
    if (
        ((y_store_1010[i] - policerequirelist10[i]) <=
         0.2) and ((y_store_1010[i] - policerequirelist10[i]) >= 0.0)
    ) or (
        ((policerequirelist10[i] - y_store_1010[i]) <=
         0.2) and ((policerequirelist10[i] - y_store_1010[i]) >= 0.0)
    ):
        k1010 += 1
        
        

Tc10_accuracy=confusion_matrix(y_store_1010,policerequirelist10)
Tc10_Standard_Div=standard_deviation(y_store_1010)
Tc10_R_square=R_square(y_store_1010,policerequirelist10)
Tc10_mean_pred=average(y_store_1010)
Tc10_mean_giv=average(policerequirelist10)

print("***************************************************************************************************************")
print("10 FOLD CROSS VALIDATION TEST CASES ACCURACY")
print(" ")

print("TEST CASES      Accuracy     Sensitivity     Specificity       Precision        F1 Score      Standard Deviation      R_Square      Mean of given data      Mean of predicted data")
print(" ")
print("TC-1->    ",Tc1_accuracy," ",Tc1_Standard_Div," ",Tc1_R_square," ",Tc1_mean_giv," ",Tc1_mean_pred)
print("TC-2->    ",Tc2_accuracy," ",Tc2_Standard_Div," ",Tc2_R_square," ",Tc2_mean_giv," ",Tc2_mean_pred)
print("TC-3->    ",Tc3_accuracy," ",Tc3_Standard_Div," ",Tc3_R_square," ",Tc3_mean_giv," ",Tc3_mean_pred)
print("TC-4->    ",Tc4_accuracy," ",Tc4_Standard_Div," ",Tc4_R_square," ",Tc4_mean_giv," ",Tc4_mean_pred)
print("TC-5->    ",Tc5_accuracy," ",Tc5_Standard_Div," ",Tc5_R_square," ",Tc5_mean_giv," ",Tc5_mean_pred)
print("TC-6->    ",Tc6_accuracy," ",Tc6_Standard_Div," ",Tc6_R_square," ",Tc6_mean_giv," ",Tc6_mean_pred)
print("TC-7->    ",Tc7_accuracy," ",Tc7_Standard_Div," ",Tc7_R_square," ",Tc7_mean_giv," ",Tc7_mean_pred)
print("TC-8->    ",Tc8_accuracy," ",Tc8_Standard_Div," ",Tc8_R_square," ",Tc8_mean_giv," ",Tc8_mean_pred)
print("TC-9->    ",Tc9_accuracy," ",Tc9_Standard_Div," ",Tc9_R_square," ",Tc9_mean_giv," ",Tc9_mean_pred)
print("TC-10->   ",Tc10_accuracy," ",Tc10_Standard_Div," ",Tc10_R_square," ",Tc10_mean_giv," ",Tc10_mean_pred)

print(" ")


#*************************************************************************************************************************************
#                                                   CONFUSION MATRIX   
#*************************************************************************************************************************************

tp_1_2=0
tn_1_2=0
fp_1_2=0
fn_1_2=0

tp_2_3=0
tn_2_3=0
fp_2_3=0
fn_2_3=0

tp_4_5=0
tn_4_5=0
fp_4_5=0
fn_4_5=0

x=min(police_require_list)

#print(x)
#y=max(police_require_list)


# CALCULATING TP,TN,FP,FN,R_SQAURE ,S.D FOR 1/2 DATA

for i in range(0,len(y_store)):  # comparing calculated value with actual value
        if(abs(y_store[i] - police_require_list[i]) <=(x+0.1)):
             tp_1_2=tp_1_2+1
        elif(abs(y_store[i] - police_require_list[i]) <=0.2):
            tn_1_2=tn_1_2+1
        elif(abs(y_store[i] - police_require_list[i]) <=0.3):
            fp_1_2=fp_1_2+1
        else:
            fn_1_2=fn_1_2+1

#CALCULATION TP,TN,FP,FN FOR 2/3 DATA  
          
            
for j in range(0,len(q_store)):  # comparing calculated value with actual value
        if(abs(q_store[j] - police_require_list[j]) <=(x+0.1)):
             tp_2_3=tp_2_3+1
        elif(abs(q_store[j] - police_require_list[j]) <=0.2):
            tn_2_3=tn_2_3+1
        elif(abs(q_store[j] - police_require_list[j]) <=0.3):
            fp_2_3=fp_2_3+1
        else:
            fn_2_3=fn_2_3+1                                


# CALCULATING TP,TN,FP,FN FOR 4/5 DATA



for s in range(0,len(r_store)):  # comparing calculated value with actual value
        if(abs(r_store[s] - police_require_list[s]) <=(x+0.1)):
             tp_4_5=tp_4_5+1
        elif(abs(r_store[s] - police_require_list[s]) <=0.2):
            tn_4_5=tn_4_5+1
        elif(abs(r_store[s] - police_require_list[s]) <=0.3):
            fp_4_5=fp_4_5+1
        else:
            fn_4_5=fn_4_5+1
#print(tp)
#print(tn)
#print(fp)
#print(fn)



#  MATRIX FOR 1/2 DATA


matrix_1_2=[]
count0=0
for i in range (2):
        a_1_2=[]
        b_1_2=[]
        for j in range(2):
            count0=count0+1
            if(count0==1):
                a_1_2.append(tp_1_2)
                a_1_2.append(fp_1_2)
            if(count0==2):
                b_1_2.append(tn_1_2)
                b_1_2.append(fn_1_2)  
        matrix_1_2.append(a_1_2)
        matrix_1_2.append(b_1_2)

print("***************************************************************************************************************")

print("CONFUSION MATRIX FOR 1/2 DATA")
print(" ")

for i in range(2):
    for l in range(2):
        print(matrix_1_2[i][l],end=" ")
    print("\n")

accuracy_1_2=round((((tp_1_2+tn_1_2)/(tp_1_2+tn_1_2+fp_1_2+fn_1_2))*100),2)
sensitivity_1_2=round((tp_1_2/(tp_1_2+fn_1_2)*100),2)
specificity_1_2=round((tn_1_2/(tn_1_2+fp_1_2)*100),2)
precision_1_2=(tp_1_2/(tp_1_2+fp_1_2)*100)
recall_1_2=(tp_1_2/(tp_1_2+fn_1_2)*100)
f1_Score_1_2=(2*precision_1_2*recall_1_2/(recall_1_2+precision_1_2))

print("ACCURACY FOR 1/2 DATA->",accuracy_1_2, end="    ")

print("SENSITIVITY FOR 1/2 DATA->",sensitivity_1_2, end="   ")

print("SPECIFICITY FOR 1/2 DATA->",specificity_1_2,end="   ")

print("PRECISION FOR 1/2 DATA->",precision_1_2,end="   ")

print("F1 SCORE FOR 1/2 DATA->",f1_Score_1_2)
print(" ")


#  MATRIX FOR 2/3 DATA


matrix_2_3=[]
count1=0
for i in range (2):
        a_2_3=[]
        b_2_3=[]
        for j in range(2):
            count1=count1+1
            if(count1==1):
                a_2_3.append(tp_2_3)
                a_2_3.append(fp_2_3)
            if(count1==2):
                b_2_3.append(tn_2_3)
                b_2_3.append(fn_2_3)  
        matrix_2_3.append(a_2_3)
        matrix_2_3.append(b_2_3)

print("***************************************************************************************************************")
print("CONFUSION MATRIX FOR 2/3 DATA")
print(" ")

for i in range(2):
    for l in range(2):
        print(matrix_2_3[i][l],end=" ")
    print("\n")

accuracy_2_3=round((((tp_2_3+tn_2_3)/(tp_2_3+tn_2_3+fp_2_3+fn_2_3))*100),2)
sensitivity_2_3=round((tp_2_3/(tp_2_3+fn_2_3)*100),2)
specificity_2_3=round((tn_2_3/(tn_2_3+fp_2_3)*100),2)
precision_2_3=(tp_2_3/(tp_2_3+fp_2_3)*100)
recall_2_3=(tp_2_3/(tp_2_3+fn_2_3)*100)
f1_Score_2_3=(2*precision_2_3*recall_2_3/(recall_2_3+precision_2_3))

print("ACCURACY FOR 2/3 DATA->",accuracy_2_3 ,end="   ")

print("SENSITIVITY FOR 2/3 DATA->",sensitivity_2_3 ,end="   ")

print("SPECIFICITY FOR 2/3 DATA->",specificity_2_3,end="   " )

print("PRECISION FOR 2/3 DATA->",precision_2_3,end="   ")

print("F1 SCORE FOR 2/3 DATA->",f1_Score_2_3)
print(" ")



#  MATRIX FOR 4/5 DATA



matrix_4_5=[]
count2=0
for i in range (2):
        a_4_5=[]
        b_4_5=[]
        for j in range(2):
            count2=count2+1
            if(count2==1):
                a_4_5.append(tp_4_5)
                a_1_2.append(fp_4_5)
            if(count2==2):
                b_4_5.append(tn_4_5)
                b_4_5.append(fn_4_5)  
        matrix_4_5.append(a_4_5)
        matrix_4_5.append(b_4_5)

print("***************************************************************************************************************")
print("CONFUSION MATRIX FOR 4/5 DATA")
print(" ")

for i in range(2):
    for l in range(1):
        print(matrix_4_5[i][l],end=" ")
    print("\n")

accuracy_4_5=round((((tp_4_5+tn_4_5)/(tp_4_5+tn_4_5+fp_4_5+fn_4_5))*100),2)
sensitivity_4_5=round((tp_4_5/(tp_4_5+fn_4_5)*100),2)
specificity_4_5=round((tn_4_5/(tn_4_5+fp_4_5)*100),2)
precision_4_5=(tp_4_5/(tp_4_5+fp_4_5)*100)
recall_4_5=(tp_4_5/(tp_4_5+fn_4_5)*100)
f1_Score_4_5=(2*precision_4_5*recall_4_5/(recall_4_5+precision_4_5))

print("ACCURACY FOR 4/5 DATA->",accuracy_4_5 ,end="   ")

print("SENSITIVITY FOR 4/5 DATA->",sensitivity_4_5 ,end="   ")

print("SPECIFICITY FOR 4/5 DATA->",specificity_4_5,end="    ")

print("PRECISION FOR 4/5 DATA->",precision_4_5,end="    ")

print("F1 SCORE FOR 4/5 DATA->",f1_Score_4_5)
print(" ")
