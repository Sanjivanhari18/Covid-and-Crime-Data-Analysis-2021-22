import tkinter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def enter():
    a=password.get()
    if str(a)=="root":
        window=tkinter.Tk()
        window.geometry("500x300")
        window.title("DATA ANALYSIS")
        lbl2=tkinter.Label(text=''''CHOOSE ANY ONE''')
        lbl2.pack()
        def covid():
            print("Accepted")
        covidb=tkinter.Button(window,text=''''COVID CASES''',command=covid).grid(row=2,column=1)    
        def crime():
            print("Accepted")
        crimeb=tkinter.Button(window,text=''''CRIME CASES''',command=crime).grid(row=2,column=5) 
        window.mainloop()
    else:
         print("Invalid Password")
mywindow=tkinter.Tk()
mywindow.geometry("500x300")
mywindow.title("DATA ANALYSIS")
lbl1=tkinter.Label(text="LOGIN ID")
lbl1.pack()
login=tkinter.Entry(width=20)
login.pack()
lbl2=tkinter.Label(text="PASSWORD")
lbl2.pack()
password=tkinter.Entry(width=20,show="*")
password.pack()
enterb=tkinter.Button(text="ENTER",command=enter)
enterb.pack()
mywindow.mainloop()
a=pd.read_csv("D:/Sanjivan/SHS11/SANJIVAN-MASTER/SANJIVAN CLASS 12/IP PROJECT/COVID csv.csv")
a.index=["Andaman and Nicobar Island","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chhattisgarh","Daman and Diu",
         "Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Ladakh","Lakshadweep",
         "Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim",
        "Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"]
b=pd.read_csv("D:/Sanjivan/SHS11/SANJIVAN-MASTER/SANJIVAN CLASS 12/IP PROJECT/COVID AGEWISE csv.csv")
b.index=["Andaman and Nicobar Island","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chhattisgarh","Daman and Diu",
         "Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Ladakh","Lakshadweep",
         "Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim",
        "Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"]
c=pd.read_csv("D:/Sanjivan/SHS11/SANJIVAN-MASTER/SANJIVAN CLASS 12/IP PROJECT/Vaccinecsv.csv")
c.index=["Andaman and Nicobar Island","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chhattisgarh","Daman and Diu",
         "Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Ladakh","Lakshadweep",
         "Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim",
        "Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"]         
d=pd.read_csv("D:/Sanjivan/SHS11/SANJIVAN-MASTER/SANJIVAN CLASS 12/IP PROJECT/POSITIVITY csv.csv")
d.index=["Andaman and Nicobar Island","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chhattisgarh","Daman and Diu",
         "Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Ladakh","Lakshadweep",
         "Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim",
        "Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"]
e=pd.read_csv("D:/Sanjivan/SHS11/SANJIVAN-MASTER/SANJIVAN CLASS 12/IP PROJECT/GDPcsv.csv")
e.index=["Andaman and Nicobar Island","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chhattisgarh","Daman and Diu",
         "Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Ladakh","Lakshadweep",
         "Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim",
        "Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"]
f=pd.read_csv("D:/Sanjivan/SHS11/SANJIVAN-MASTER/SANJIVAN CLASS 12/IP PROJECT/Helpnum csv.csv")
f.index=["Andaman and Nicobar Island","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chhattisgarh","Daman and Diu",
         "Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Ladakh","Lakshadweep",
         "Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim",
        "Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"]
print("TYPE 1 FOR VIEWING THE STATEWISE DATA FOR COVID-19\n" 
      "TYPE 2 FOR VIEWING THE AGEWISE DATA FOR COVID-19\n"
      "TYPE 3 FOR VIEWING THE STATEWISE VACCINATION STATUS\n"
      "TYPE 4 FOR VIEWING THE STATEWISE POSITIVITY RATE\n"
      "TYPE 5 FOR VIEWING THE IMPACT OF COVID-19 ON OUR ECONOMY(PER CAPITA INCOME)\n "
      "TYPE 6 FOR VIEWING THE STATEWISE HELPLINE NUMBER \n"
      "TYPE 7 FOR DONATION OF MONEY FOR COVID RELIEF FUND\n "
      "TYPE 8 FOR HEALTH RELATED ASSISTANCE FROM THE GOVT\n"
      "TYPE 9 FOR VIEWING THE TRAVEL GUIDELINES \n"
      "TYPE 10 FOR VIEWING THE STEP TO BE TAKEN FOR STOPPING THE SPREAD OF COVID-19\n"
      "TYPE 11 FOR VIEWING THE LOCKDOWN RESTRICTIONS\n"
      "TYPE 12 TO EXIT\n")
n=int(input("Enter a number by refering the above dataset index"))
if n==1:
    print(a)
    na=input("Would you like to visualize the data as a graph y/n")
    if na=='y':
        a.plot(kind='bar',title='COVID-19')
        plt.show()
        naa=input("Would you like to visualize more by selecting a few states y/n")
        if naa=='y':
            nbg=int(input("Enter the number of states for visualization"))
            y=[]
            for i in range(nbg):
                x=input("Enter the state name with the first letter in capital")
                y.append(x)
            print("The selected states are ",y)
            bg=a.loc[y]
            bg.plot(kind='bar',title='COVID-19 FOR SELECTED STATES')
            plt.show()
            ag=input("Would you like to view only a particular attribute y/n")
            if ag=='y':
                ga=input("Enter the attribute with the first letter in capital")
                gf=a.loc[y,ga]
                gf.plot(kind='bar',title='COVID-19 FOR A STATE')
                plt.show()
                n=int(input("Enter a number by refering the above dataset index"))
            else:
                n=int(input("Enter a number by refering the above dataset index"))
        else:
            n=int(input("Enter a number by refering the above dataset index"))
    else:
        n=int(input("Enter a number by refering the above dataset index"))
if n==2:
    print(b)
    ra=input("Would you like to visualize the data as a graph y/n")
    if ra=='y':
        b.plot(kind='bar',title='AGEWISE COVID CASES')
        plt.show()
        naa=input("Would you like to visualize more by selecting a few states by a bar graph y/n")
        nbb=input("Would you like to visualize  a  state's data  by a histogram y/n")
        if naa=='y':
            ng=int(input("Enter the number of states for visualization"))
            z=[]
            for j in range(ng):
                g=input("Enter the state name with the first letter in capital")
                z.append(g)
            ag=b.loc[z]
            ag.plot(kind='bar',title='AGEWISE CASES FOR SELECTED STATES')
            plt.show()
            dag=input("Would you like to view only a particular ages y/n")
            if dag=='y':
                dga=input("Enter the age group by the refering the data ")
                bf=a.loc[y,dga]
                bf.plot(kind='bar',title='AGEWISE CASES FOR SELECTED STATES AND SELECTED AGEGROUP')
                plt.show()
                n=int(input("Enter a number by refering the above dataset index"))
            else:
                n=int(input("Enter a number by refering the above dataset index"))
        
        else:
            n=int(input("Enter a number by refering the above dataset index"))
    else:
        n=int(input("Enter a number by refering the above dataset index"))
if n==3:
    print(c)
    xx=input("Would you like to visualize the data as a graph y/n")
    if xx=='y':
        c.plot(kind='bar',title='STATEWISE VACCINATION')
        plt.show()
        nat=input("Would you like to visualize more by selecting a few states y/n")
        if nat=='y':
            nk=int(input("Enter the number of states for visualization"))
            o=[]
            for k in range(nk):
                lk=input("Enter the state name with the first letter in capital")
                o.append(lk)
            tg=c.loc[o]
            tg.plot(kind='bar',title='VACCINATION STATUS FOR SELECTED STATES')
            plt.show()
            dag=input("Would you like to view only a particular dose or total y/n")
            if dag=='y':
                oa=input("Enter the attribue by the refering the data ")
                kf=c.loc[o,oa]
                kf.plot(kind='bar',x='State/UTs',title='VACCINATION STATUS FOR SELECTED STATES AND SELECTED AGEGROUP')
                plt.show()
                n=int(input("Enter a number by refering the above dataset index"))
            else:
                n=int(input("Enter a number by refering the above dataset index"))
        else:
            n=int(input("Enter a number by refering the above dataset index"))
    else:
        n=int(input("Enter a number by refering the above dataset index"))
if n==4:
    print(d)
    xo=input("Would you like to visualize the data as a graph y/n")
    if xo=='y':
        d.plot(kind='bar',title='STATEWISE POSITIVITY RATE')
        plt.show()
        nak=input("Would you like to visualize more by selecting a few states y/n")
        if nat=='y':
            nok=int(input("Enter the number of states for visualization"))
            q=[]
            for l in range(nok):
                lyk=input("Enter the state name with the first letter in capital")
                q.append(lyk)
            ig=d.loc[q]
            ig.plot(kind='bar',title='POSITIVITY RATE FOR SELECTED STATES')
            plt.show()
            n=int(input("Enter a number by refering the above dataset index"))
        else:
            n=int(input("Enter a number by refering the above dataset index"))
    else:
        n=int(input("Enter a number by refering the above dataset index"))
if n==5:
    print(e)
    xp=input("Would you like to visualize the data as a graph y/n")
    if xp=='y':
        e.plot(kind='bar',title='STATEWISE PER CAPITA INCOME')
        plt.show()
        nit=input("Would you like to visualize more by selecting a few states y/n")
        if nit=='y':
            nqk=int(input("Enter the number of states for visualization"))
            f=[]
            for k in range(nqk):
                jk=input("Enter the state name with the first letter in capital")
                f.append(jk)
            ty=e.loc[f]
            ty.plot(kind='bar',title='PER CAPITA INCOME FOR SELECTED STATES')
            plt.show()
            yyg=input("Would you like to view the per capita income for only a year y/n")
            if yyg=='y':
                ok=int(input("Enter the year"))
                kft=e.loc[f,ok]
                kft.plot(kind='bar',title='PER CAPITA FOR SELECTED STATES AND SELECTED YEAR')
                plt.show()
                n=int(input("Enter a number by refering the above dataset index"))
            else:
                n=int(input("Enter a number by refering the above dataset index"))
        else:
            n=int(input("Enter a number by refering the above dataset index"))
    else:
        n=int(input("Enter a number by refering the above dataset index"))
if n==6:
    print(f)
    ye=input("Would you like to view the helpline number of a state y/n")
    while ye=='y':
        tr=input("Enter the state name with the first letter in capital")
        print(f.loc[tr])
        ye=input("Would you like to view the helpline number of a state y/n")
    n=int(input("Enter a number by refering the above dataset index"))
if n==7:
    gy=input("Type y to proceed with the transaction")
    if gy=='y':
        aw=pd.DataFrame(columns=['NAME','PHONE NO','AMOUNT','CITY'])
        num=int(input("Enter your AADHAR number"))
        name=input("enter your name")
        pno=int(input("enter your phone number"))
        amt=int(input("enter the amount of money for donation"))
        ct=input("enter your city name")
        aw.loc[num]=[name,pno,amt,ct]
        print("Please wait for a few seconds....")
        print("Your Transaction has been made successfully")
        uy=input("Type y to view your details")
        if uy=='y':
            print(aw)
            uu=input("would you like to make any changes in the details")
            if uu=='y':
                ii=input("Type m to modify or Type anyother alphabet to kill the transaction")
                if ii=='m':
                    name1=input("enter your name")
                    pyo=int(input("enter your phone number"))
                    cty=input("enter your city name")
                    aw.loc[num]=[name1,pyo,amt,cty]
                    print("The change has been made")
                    print(aw)
                    n=int(input("Enter a number by refering the above dataset index"))
                else:
                    aw=aw.drop(num,axis='index')
                    print("Your money has been refunded")
                    print(aw)
                    n=int(input("Enter a number by refering the above dataset index"))
            else:
                n=int(input("Enter a number by refering the above dataset index"))
        else:
            n=int(input("Enter a number by refering the above dataset index"))
    else:
        n=int(input("Enter a number by refering the above dataset index"))
if n==8:
    gh=input("Type y to continue")
    if gh=='y':
        gt=input("Type c if you have been tested POSITIVE")
        if gt=='c':
            tt=pd.DataFrame(columns=['NAME','PHONE NO','ADDRESS','CITY'])
            num=int(input("Enter your AADHAR number"))
            name=input("enter your name")
            pno=int(input("enter your phone number"))
            add=int(input("enter your address"))
            ct=input("enter your city name")
            tt.loc[num]=[name,pno,add,ct]
            print("Your Details have been recorded and the officials will be at your house in a couple of days")
            io=input("Type y to view your details")
            if io=='y':
                print(tt)
                fg=input("Would you like to make any changes y/n")
                if fg=='y':
                    ii=input("Type m to modify or Type anyother alphabet to delete your data")
                    if ii=='m':
                        name1=input("enter your name")
                        pyo=int(input("enter your phone number"))
                        cty=input("enter your city name")
                        aw.loc[num]=[name1,pyo,amt,cty]
                        print("The change has been made")
                        print(tt)
                        n=int(input("Enter a number by refering the above dataset index"))
                    else:
                        tt=tt.drop(num,axis='index')
                        print("Your Details have been deleted")
                        print(tt)
                        n=int(input("Enter a number by refering the above dataset index"))
                else:
                    n=int(input("Enter a number by refering the above dataset index"))
            else:
                n=int(input("Enter a number by refering the above dataset index"))
        
        else:
            n=int(input("Enter a number by refering the above dataset index"))
    else:
        n=int(input("Enter a number by refering the above dataset index"))
if n==9:
    print(" General Advisory to all passengers"
          " People must follow required health protocols, as detailed below, whenever there is a need to travel:\n"
          "i. Passengers should self-monitor their health and travel only when they have no symptoms related to COVID-19.\n"
          "ii. All passengers shall follow COVID appropriate behavior at all times which includes use of mask/face cover,"
          "  hand hygiene and physical distancing of six feet (do gaj ki doori) as far as feasible.Masks/face covers must be"
          "  worn properly to cover nose and mouth. Touching the front portion of mask/face covers to be avoided.\n"
          "iii. Avoid spitting in public places during travel.\n"
          "iv. All passengers shall be advised to download Arogya Setu app on their mobile devices.\n"
          "v. If they develop fever during travel, they shall report to cabin crew/TTE/bus conductor as the case may be.\n"
          "vi. If they develop symptoms after reaching their final destination, they shall inform the District"
               "Surveillance Officer or the State/National Call Center (1075).")
    n=int(input("Enter a number by refering the above dataset index"))

if n==10:
    print("Wear a face mask in public indoor spaces.\n"
          "Maintain at least six feet of distance between yourself and others.\n"
          "Avoid large gatherings.\n"
           "Socialize indoors \n"
           "Get vaccinated and boosted as soon as you are eligible \n"
           "Avoid close contact with people who are sick. \n"
           "Minimize touching your eyes, nose, and mouth. \n"
           "Stay home when you are sick. \n"
           "Cover your cough or sneeze with a tissue, then throw the tissue in the trash \n"
           "Clean frequently touched objects and surfaces regularly. \n"
           "Wash your hands often with soap and water. ")
    n=int(input("Enter a number by refering the above dataset index"))

if n==11:
    print("* Vaccination centres will continue to operate in the lockdown period \n"
          "* Hotels and restaurants can function from 6 am to 10 am; 12 pm to 3 pm; 6 pm to 9 pm for takeaways only. \n"
          "* Tea shops (with take away service only) can operate till noon. \n"
          "* Food delivery aggregators like Swiggy and Zomato will be allowed to operate during the above hours \n"
          "* E-commerce companies are allowed to provide food, groceries, meat, provisions services \n"
          "* Amma canteens will be open \n"
          "* Flower and fruit pedestrian shops can operate till noon \n"
          "* Ration shops will operate from 8 am till noon \n"
          "* Hotels/lodges will be open only for customers who stay for financial/medical related works \n"
          "* A maximum of 50 members are allowed to participate in marriages and 20 members in funerals \n"
          "* Banks and other related services will operate with 50 per cent work force \n"
          "* Apart from necessary state departments, like Secretariat, Health, Revenue and"
          "disaster management, police, fire, prison, forests, local municipal administration, women and social welfare, others won’t function \n"
          "* Hospitals, labs and pharmacies, medical related shops, ambulance and hearse services will operate \n"
          "* Courier services will function \n"
          "* Lorries/tankers carrying fuel, oxygen, raw materials will be allowed to ply \n"
          "* Ongoing construction work will be allowed to carry on \n"
          "* Continuous processing industries and industries manufacturing essential commodities will continue to function \n"
          "* Petrol/diesel stations will operate as usual \n"
          "* All standalone groceries, fish and meat stalls will be allowed to operate till noon with 50 per cent customers \n")
    n=int(input("Enter a number by refering the above dataset index"))
    

if n==12:
    print("")
else:
    print("INVALID NUMBER")
    
    
    
        
        
        
    
    


    
    


                
    
                
        












                
