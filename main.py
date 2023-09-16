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
    countries_list.append(i[0])
    capitals_list.append(i[1])
    probability_main.append(i[2])
with open("probable.csv","r") as prob:
    reader = csv.reader(prob)
    prob_countries=[]
    prob_capitals=[]
    probability=[]
    for list in reader:
        prob_countries.append(list[0])
        prob_capitals.append(list[1])
        probability.append(list[2])
def main_file():
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
            user_capital=input("Enter the answer:")
            if user_capital.upper()==capital.upper():
                print("You were right")
                print("Play Again?\n1.Yes\n2.No")
                if int(input("Enter choice:"))==2:
                    exit()
                else:
                    continue
            else:
                print("You were wrong")
                print("Play Again?\n1.Yes\n2.No")
                if int(input("Enter choice:"))==2:
                    exit()
                else:
                    continue
    if stopage==len(master):
        print("Wow you were correct in most of them.. Do you want to check the probable files? \n1.Yes\n2.No")
        user_input=int(input("Enter:"))
        if user_input==1:
            most_probable=0
            for target_prob in probability:
                target_prob=float(target_prob)
                if target_prob>most_probable:
                    most_probable=target_prob
                    target_prob=str(target_prob)
                    index=probability.index(target_prob)
            print(f"Is the capital of {prob_countries[index]}, {prob_capitals[index]}?")
            print("1.Yes\n2.No")
            user_input=int(input("Enter:"))
            if user_input==1:
                probability[index] = str(float(probability[index]) + 0.25)
                refresh_prob()
            else:
                probability[index] = str(float(probability[index]) - 0.25)
                print("What is it?")
                given_capital=input("Enter capital:")
                probability.append("0.25")
                prob_countries.append(prob_countries[index])
                prob_capitals.append(given_capital)
                refresh_prob()
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
        if float(most_prob)>0.5:
            prob_countries[index]
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
                print("Refreshed,new value added to main")
        else:
            print("Refreshed")
def refresh_prob():
    with open('probable.csv','w',newline="")as filey:
        writer=csv.writer(filey)
        master=[]
        for i in range(len(prob_countries)):
            master.append([prob_countries[i],prob_capitals[i],probability[i]])
        for list in master:
            writer.writerow(list)
    print("probable refreshed!")
def precision():
    print("On making")
print('''      |-------------------------------|
      | 1. Play a Quizz               |
      | 2. Ask for a Capital          |
      | 3. Checl for Precission       |
      |-------------------------------|''')
try:
    user_main=int(input("Enter a choice:"))
    if user_main == 1:
        main_file()
    elif user_main==2:
        asking()
    elif user_main==3:
        precision()
except Exception as e:
    print("Error",e)
finally:
    refresh()
    
#country,capital,probability
#India,delhi,1.0
#germany,soltez,0.75
#current error some how whenever new value is added from probable file, one row from top gets removed, (can be issue because the cursor does next or skips the first line)
#also happened with main csv rows from mid got removed magically but not all and not everytime at  a certain time
