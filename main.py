import csv
import random
with open ("main.csv","r") as f:
    data=csv.reader(f)
    master=[]
    for num,listy in enumerate(data):
        if num==0:
            pass
        else:
            master.append(listy)
countries_list=[]
capitals_list=[]
probability_main=[]
for i in master:
    print(i)
    countries_list.append(i[0])
    capitals_list.append(i[1])
    probability_main.append(i[2])
with open("probable.csv","r") as prob:
    reader = csv.reader(prob)
    next(reader)
    prob_countries=[]
    prob_capitals=[]
    probability=[]
    for list in reader:
        prob_countries.append(list[0])
        prob_capitals.append(list[1])
        probability.append(list[2])
def main_file(main_choice):
    flag=True
    master_length=len(master)
    stopage=0
    while flag and stopage!=master_length:
        stopage+=1
        random_num=random.randrange(0,len(master))
        country=master[random_num][0]
        capital=master[random_num][1]
        print(f"Do you know the capital of {country}?\n1.Yes\n2.No")
        user=int(input("Enter choice:"))
        if user==1:
            user_capital=input("Enter the answer")
            if user_capital==capital:
                print("You were right")
                print("Play Again?\n1.Yes\n2.No")
                if int(input("Enter choice:"))==2:
                    flag=False
                else:
                    continue
            else:
                print("you were wrong")
                print("Play Again?\n1.Yes\n2.No")
                if int(input("Enter choice:"))==2:
                    flag=False
                else:
                    continue
    else:
        print("Exiting")
    #if stopage==master ask user for the probabler countries
def asking():
        asked_country=input("Enter the country name:")
        if asked_country not in countries_list:
            print("This was not in the country list")
            print("Do you know the capital of it?, 1 for yes 2 for no")
            if asked_country not in prob_countries:
                with open("probable.csv","+a",newline="\n") as prob:
                    writer=csv.writer(prob)
                    if int(input("Choice:"))==2:
                        writer.writerow([asked_country,"",0.1])
                    else:
                        told_capital=input("Enter capital:")
                        writer.writerow([asked_country,told_capital,0.25])
            else:
                prob_index=prob_countries.index(asked_country)
                prob_countries[prob_index]=asked_country
                if int(input("Choice:"))==1:
                    told_capital=input("Enter capital:")
                    if told_capital not in prob_capitals:
                        with open("probable.csv","+a",newline="\n") as prob:
                            writer=csv.writer(prob)
                            writer.writerow([asked_country,told_capital,0.25])
                    else:                     
                        prob_capitals[prob_index]=told_capital
                        probability[prob_index]=str(float(probability[prob_index])+0.25)
                        master=[]
                        for x in range(len(prob_countries)):
                            master.append([prob_countries[x],prob_capitals[x],probability[x]])
                        print(master)
                        with open("probable.csv","w",newline="\n") as prob:
                            writery=csv.writer(prob)
                            for list in master:
                                writery.writerow(list)
                
                
                
                '''for x in range(len(countries_list)):
                    master.append([countries_list[x],capitals_list[x],probability_main[x]])
                        told_capital=input("Enter capital:")
                        for list in master:
                            writery.writerow(list)'''
    
        else:
            index=countries_list.index(asked_country)
            surity=float(probability_main[index])*100
            print(f"The capital is {capitals_list[index]}, Surity:{surity}%")
def refresh():
        most_prob=0
        for target_prob in probability:
            target_prob=float(target_prob)
            if target_prob>most_prob:
                most_prob=target_prob
                target_prob=str(target_prob)
                index=probability.index(target_prob)
        if float(target_prob)>0.5:
            if prob_countries[index] not in countries_list:
                countries_list.append(prob_countries[index])
                capitals_list.append(prob_capitals[index])
                probability_main.append(most_prob)
            else:
                target_index=countries_list.index(prob_countries[index])
                countries_list[target_index]=prob_countries[index]
                capitals_list[target_index]=prob_capitals[index]
                probability_main[target_index]=probability[index]
            master=[]
            for x in range(len(countries_list)):
                master.append([countries_list[x],capitals_list[x],probability_main[x]])
            with open("main.csv","w",newline="") as f:
                writer=csv.writer(f)
                writer.writerow(["country","capital","probability"])
                for list in master:
                    writer.writerow(list)
                    print("new value added")
        else:
            print("no new value added")
asking()
refresh()
#country,capital,probability
#India,delhi,1.0
#germany,soltez,0.75
#current error some how whenever new value is added from probable file, one row from top gets removed, (can be issue because the cursor does next or skips the first line)
#also happened with main csv rows from mid got removed magically but not all and not everytime at  a certain time
