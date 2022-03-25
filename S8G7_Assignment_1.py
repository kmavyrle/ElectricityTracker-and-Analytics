# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 13:27:17 2022

@author: Kwan Yui Yang Mavyrle
"""
#Below are libraries that will be used
import os #Remind you where ur csv is saved
import datetime as dt #Record daily date
import time #Time import time.sleep(2) 
import csv


##### I. Preliminary Functions set up for different components of our program
def preliminary_info(electricity_rates):
    '''
    This function is meant to obtain user inputs with regards to their:
    1. Name
    2. Household Size
    3. Electricity supplier the user subscribes to
    The collated information will be saved on a csv document in the user's working directory
    '''
    print('We will be needing some preliminary information about your household and electricity supplier!\n')
    ###  USE A WHILE LOOP TO GET HOUSEHOLD SIZE AND ELECTRICITY PROVIDER. WHILE LOOP IS TO PREVENT WRONG ENTRY FROM PREVENTING SMOOTH
    time.sleep(1)
    while True:
        #Input user name
        name = input('Before we begin, what is your name?:')
        try:
            #input household size
            household_size = max(int(input('Next, please enter your household size:\n')),1)
            print('Thank you!\n')
            
            #input Electrical Supplier
            print ('''Below is the Electricity Supplier Menu!
    ------------------------------------------
    1. Geneco
    2. Keppel Electric
    3: Pacific Light
    4. Sembcorp Powerma
    5. Senoko       
    6. Tuas Power''')
            time.sleep(1)
            #Input the electrical supplier you use
            electricity_supplier = int(input('Please enter the number corresponding to the electricity supplier you use from the Electricity Supplier Menu above:\n'))
            electricty_rates[electricity_supplier]
            break #Break out of the loop if no errors
            
        except: #If error while loop will keep running
            print('Invalid input type. Please enter a valid integer between 1 to 6.')
    
    print(f'Thank you {name}! By using {electricty_rates[electricity_supplier][0]} as your electricity supplier, you will be charged at a rate of {electricty_rates[electricity_supplier][1]}.')
    ### Write to a csv file
    preliminary_inputs_csv = open('preliminary_inputs.csv','w')
    print(f'username,{name}',file =preliminary_inputs_csv )
    print(f'Electrical Supplier,{electricty_rates[electricity_supplier][0]}',file =preliminary_inputs_csv )
    print(f'Electricity Supplier Code,{electricity_supplier}',file = preliminary_inputs_csv)
    print(f'Electricity Rates (kWh),{electricty_rates[electricity_supplier][1]}',file =preliminary_inputs_csv)
    print(f'Household Size,{household_size}',file = preliminary_inputs_csv)
    preliminary_inputs_csv.close()
    
    #return the user's name, household size and electricity suppluer as inputs for later programs
    return name,household_size,electricity_supplier

def appliance_input_function():
    '''
    This function is to obtain the number of hours the user uses each common appliances
    1. For each appliance, there would be a KWh output which will be used to multiply by their electricity rates
    2. Daily electrical cost can then be estimated
    3. This function will call the global electrical_appliances dictionary to get the costs for each appliance
    4. The outputs (costs per appliance) will be saved in a csv which can be imported in future
    '''
    print('''Next, we will need an estimate of the average number of hours your household uses for a list of common electrical appliances.
You will only need to enter this once and it will be stored within our database!\n''')
    time.sleep(1)
    daily_cost = {} #Create empty dictionary to store number of KWh used per appliances
    

    #### Iterate through electical_appliances dictionary
    while True:
        for k,v in electrical_appliances.items():
            while True:
                try:
                    #Usage is capped at 24 hours per appliance
                    usage = min(float(input(f'Please enter the average number of hours you use the {k} in a day:')),24)
                    daily_cost[k] = usage * v
                    break
                except ValueError:
                    print('Please enter a valid number of hours. For example, if you use an appliance for 30 mins a day, please enter 0.5.')

        ### Confirmation input in case the user puts in the wrong inputs and wants to re-input
        confirmation = input('Would you like to confirm these inputs? [y/n]:').lower()
        while confirmation not in ['y','n']:
            confirmation = input('Would you like to confirm these inputs? [y/n]:\n').lower()
            if confirmation == 'y':
                print('Recording entries......\n')
                time.sleep(1.5)
                print('Thank you! Your entries have been recorded!')
                break
            elif confirmation =='n':
                print('Please re-enter daily usage')


            else:
                print('Please enter "y" or "n" only.')
        if confirmation == 'y':
            print('Recording entries......')
            print(f'Thanks {name}! Your entries have been recorded!')
            break
    #Rates charged calculation
    rate_charged = float(electricty_rates[electricity_supplier][1][1:7]) #Get the rates charged from the dictionary we created above
    fixed_cost = rate_charged * ((24 * 0.1)+(1*0.8)+(12*0.1)+(1*0.3)) #Fixed costs including fridge, cooking, residual lights etc
    fixed_cost = round(fixed_cost,2)
    daily_cost['Fixed Costs'] = fixed_cost #Store data into dictionary
    #Write the outputs to a csv file
    daily_cost_csv = open('daily_cost.csv','w')
    for appliance, cost in daily_cost.items():
        print(appliance,',',cost, file = daily_cost_csv)
    daily_cost_csv.close()    
    return daily_cost


def get_cumulative_cost(file_pointer,daily_elec_cost):
    '''
    This function will calculate the cumulative costs of the user
    1. The electricity report will be used for the computation
    2. Loop through each line in the csv
    3. Add on the value to the cumulative costs for each day
    '''
    count=0
    cumulative_cost = daily_elec_cost
    for line in file_pointer:
        count+=1
        if count >=13:
            cost = float(line.split(',')[1])
            cumulative_cost+=cost
    
    return cumulative_cost

def get_cumulative_points(file_pointer,points_acquired):
    '''
    This function will calculate the cumulative points acquired by the user
    '''
    count=0
    cumulative_points = int(points_acquired)
    numlist = []
    for line in file_pointer:
        count+=1
        if count >=13:
            points = (int(line.split(',')[3]))
            numlist.append(points)
    cumulative_points+=numlist[-1]
    return cumulative_points

#### The below functions are printouts for the user if they accumulate points by performing electricity saving tasks.
def print_thunder(points):
    
    print('⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡         Fantastic!')
    time.sleep(0.2)
    print('''            ------ 
  💧 💧     /    /  💧 💧 💧        You have''')
    time.sleep(0.5)
    print('''          /    / 
   💧    /    /       💧           accumulated''')
    time.sleep(0.5)
    print('''        /   /
       /  /                       a total of''')
    time.sleep(0.5)
    print(f'''      /   --------
     /-------    /   💧          {int(points)} points today!''')
    time.sleep(0.5)
    print('''            /   /
    💧     /   /   💧              Keep it up!!!''')
    time.sleep(0.5)
    print('''  💧      /   /
         /  /   💧     💧          🤪🤪🤪🤪''')
    time.sleep(0.5)
    print('''        / /
        --
⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡
    ''')
    
def print_no_pts():
    print('''
(*╯-╰)ノ  Sorry''')
    time.sleep(0.5)
    print('''
You did not accumulate any points today!''')
    time.sleep(0.5)
    print('''👎 👎 👎 ''')
    
def print_middle_pts(points):
    print('''( ◕◡◕)っ ♡''')
    time.sleep(0.5)
    print('Great job!!')
    time.sleep(0.5)
    print(f'''You have accumulated a total of {points} points today!!
Lets work towards accumulating 5 points in a day!''')
    
#Start    

print('Hello, thank you and welcome to MyElectricityTracker Program! \n')




##### II. Create a dictionary to store the rates for the respective electricity supplier
electricty_rates = {1:['Geneco', '$0.2510 per KWh'],
                 2:['Keppel Electric','$0.2580 per KWh'],
                 3:['Pacific Light','$0.2568 per KWh'],
                 4:['Sembcorp Power','$0.2710 per KWh'],
                 5:['Senoko','$0.2520 per KWh'],
                 6:['Tuas Power','$0.2711 per KWh']}

try:
    #### Try to reac the preliminary_inputs csv, if it fails that means the user is a first-time user
    with open('preliminary_inputs.csv','r') as file_pointer:
        prelim_data = file_pointer.readlines()
        name = prelim_data[0].split(",")[1]
        electricity_supplier = int(prelim_data[2].split(",")[1])
        household_size = int(prelim_data[4].split(",")[1])
        rate_charged = float(electricty_rates[electricity_supplier][1][1:7]) #Get the rates charged from the dictionary we created above
        
except:
    #### The first time user will input his preliminary information with the preliminary_info() function
    print('Looks like this is your first time using our program.\n')
    name,household_size,electricity_supplier = preliminary_info(electricty_rates)
    rate_charged = float(electricty_rates[electricity_supplier][1][1:7])
        

#Create dictionary for the kW usage for common appliances used in the project
electrical_appliances  = {'Air Conditioner':0.2,
                          'Shower Heater': 0.38,
                          'Fan':0.02,
                          'Lights':0.04,
                          'Laptop':0.06,
                          'TV': 0.06
                         }

while True:
    daily_usage_prompt = input('''Are there any changes to your daily electricity usage hours today compared to yesterday? [y/n] (if applicable):
    ''').lower()
    
    if daily_usage_prompt == 'n':
        try:
            daily_cost = {}
            with open('daily_cost.csv') as cost_file:
                csv_pointer = csv.reader(cost_file)
                for each in csv_pointer:
                    daily_cost[each[0].strip()] = round(float(each[1][1:]),2)
                break
        except:
            print('Looks like you do not have any past records...')
            daily_cost = appliance_input_function()
            break
    
    else:
        if daily_usage_prompt == 'y':
            daily_cost = appliance_input_function()
            break
        else:
            print('Please enter [y/n] only:')

print('Please wait while we retrieve your data......')
time.sleep(3)

#Fixed costs include Refrigerator costs, Cooking costs, Residual electricity costs (modem), washing machine
fixed_cost = rate_charged * ((24 * 0.1)+(1*0.8)+(12*0.1)+(1*0.3)) #Assume fixed costs from fridge? Some other appliances also on all day


#%% III. Reminder functionality to remind users to perform electricity saving tasks
###      1. Users have to input numbers based on which task they performed 
###      2. Outputs will be used to deduct electricity costs in our records
###      3. Points allocated based on tasks performed to recuce electricity

print('''
Here is a daily reminder for a list of tasks you can very easily do to save more electricity
---------------------------------------------------------------------
1. Use a fan instead of the air-conditioner
2. Take cold showers instead of warm showers
3. Use LED lights instead of incandescent lights
4. Turn off lights when not in use 
5. Use a microwave instead of oven
6. Turn on the energy saving function for your fridge
7. Turn off your routers overnight
''')
time.sleep(3)



cost_savings_calculator = {1: ['Air Conditioner',0.5*daily_cost['Air Conditioner']],
                           2: ['Shower Heater',daily_cost['Shower Heater']],
                           3: ['Lights',0.7* daily_cost['Lights']],
                           4: ['Lights',0.2* daily_cost['Lights']],
                           5: 0.1*0.8,
                           6: 3*0.1,
                           7: 12*0.01}

while True:
    cost_savings = 0
    try:
        save_prompt = input('''If you have done any of the above tasks, kindly input the corresponding numbers with a space in between.
If you did not perform any electricity savings task, please enter n:
''')
        
        if save_prompt == 'n':
            print('You did not do any electricity saving tasks today. Do try again tommorrow!')
            time.sleep(2)
            break
        savings = save_prompt.split(' ')
        
        for i in savings:
            i = int(i)
            app = cost_savings_calculator[i]
            if type(cost_savings_calculator[i]) == list:
                daily_cost[app[0]]-=app[1]
                cost_savings+=app[1]
            elif type(cost_savings_calculator[i])==float:
                
                fixed_cost -= app
                cost_savings+=app
        print('Calculating cost savings......')
        time.sleep(1.5)
        print(f'Well Done! Your costs savings for today is ${round(cost_savings,2)}\n')

        break
    except:
        print('Kindly enter the number corresponding to the cost saving activites separated by a space or n if you did not do any electricity saving tasks today')
        print('For example: 1 3 5 7')

### Point system
points_acquired= (cost_savings*10)//1
if points_acquired >= 5:
    print_thunder(points_acquired)
elif 1<=points_acquired<=4:
    print_middle_pts(points_acquired)
elif points_acquired == 0:
    print_no_pts()
print('\n')

time.sleep(3)

#%% IV. ELectricity Summary Report Function
###     1. Outputs will be saved to a csv daily to record their usage and points accumulated
###     2. Print out on the program itself to show the user its usage and costs
daily_elec_cost = sum(daily_cost.values())*household_size*rate_charged + fixed_cost-cost_savings
print(f'''Based on your input inclusive of fixed costs, your daily electricity expenses
would cost approximately ${round(daily_elec_cost,2)} and your monthly electricity expenses would cost approximately ${round(30 * daily_elec_cost,2)}\n''')
time.sleep(4)

#Get today's date
date=str(dt.datetime.now())[:10]

input('We will now print out your daily costs! Press Enter to continue:')

appliance_record = f'''Your Daily Appliance Usage for {date}:

1. Air-con => ${round(rate_charged * household_size * daily_cost["Air Conditioner"],2)}
2. Shower Heater => ${round(rate_charged *household_size *daily_cost["Shower Heater"],2)}
3. Fan => ${round(rate_charged *household_size *daily_cost["Fan"],2)}
4. Lights => ${round(rate_charged *household_size *daily_cost["Lights"],2)}
5. Laptop => ${round(rate_charged *household_size *daily_cost["Laptop"],2)}
6. TV => ${round(rate_charged *household_size *daily_cost["TV"],2)}
7. Fixed Costs -> ${round(fixed_cost,2)}
----------------------------------------
Daily ELectrical Bill Report'''




#Print out for visualisation
print(appliance_record)
header_date = 'Date'
header_cost = 'Cost($)'
header_cumul_cost = 'Cumulative($)'
header_cumul_points = 'Cumulative Points'
print('{:^12}|{:^15}|{:^16}|{:^24}'.format(header_date,header_cost,header_cumul_cost,header_cumul_points))


#%% Append daily electricity report data into an empty dict

try:
    ### Try to read the csv, if this lines of code fail, user does not have any prior csv reports
    datadict = {}
    temp_file = open('Electricity_Summary_Report.csv','r')
    cumulative_cost = get_cumulative_cost(temp_file,daily_elec_cost)
    temp_file.close()
    
    temp_file1 = open('Electricity_Summary_Report.csv','r')
    cumulative_points = int(get_cumulative_points(temp_file1, points_acquired))

    temp_file.close()
    
    temp_file = open('Electricity_Summary_Report.csv','r')
    count = 0
    for line in temp_file:
        count+=1
        if count >=13:
            linelist = line.split(',')
            datadict[linelist[0]]=linelist[1:]
    temp_file.close()


except:
    ### Write csv report file for user since he or she does not have a prior one
    temp_file = open('Electricity_Summary_Report.csv','w')
    cumulative_cost = daily_elec_cost
    cumulative_points = int((cost_savings*10)//1)
    print(appliance_record, file = temp_file)
    print('{:^12},{:^15},{:^16},{:^16}'.format(header_date,header_cost,header_cumul_cost,header_cumul_points),file = temp_file)
    temp_file.close()


data = {}
data[date] = ['{:^9.2f}'.format(daily_elec_cost),cumulative_cost,cumulative_points]

for i,v in data.items():
    print(i,' |','{:^13}'.format(v[0]),'|','{:^14.2f}'.format(float(v[1])),'|','{:^18}'.format(v[2]))
print('\n')

print('Saving your entries......\n')
time.sleep(2)
address = 'Electricity_Summary_Report.csv'
with open(address,'a') as file_pointer:  
    ### Append new day's records
    for key in data.keys(): 
        file_pointer.write(key)
        file_pointer.write(',')
        file_pointer.write(data[key][0])
        file_pointer.write(',')
        file_pointer.write(str(round(float(data[key][1]),2)))
        file_pointer.write(',')
        file_pointer.write(str(data[key][2])+'\n')
        
        
#Function to compare usage with national average
print('''Next, we will compare your electricity appliance usage with the national average. 
Fun fact! This is the average household electricity consumption by hours as well as the 
percentage breakdown for the respective appliances:
-------------------------------------------------------''')
time.sleep(3)
print('''                  
Air Conditioner:           8 hours per day at 24 %
Shower Heater:             1 hour per day at 11 %
Fans:                      8 hours per day at 4 %
Lights:                    6 hours per day at 6 %
TV:                        3 hours per day at 3%
Other Appliances:          12-24 hours per day at 49%
''')
national_average = {0:['Air Conditioner',24],
                   1:['Shower Heater',11],
                   2:['Fans',4],
                   3:['Lights',6],
                   4:['Laptop',3],
                   5:['TV',3],
                   6:['Others',49]}
advice_dict = {'Air Conditioner':'you can try to use the fan more often or if absolutely necessary to use the air conditioner, keep it at 25 degrees celsius',
              'Shower Heater': 'you can take quicker showers or cold showers more often',
              'Fans': 'you can open your windows in the day for more natural ventilation instead of turning on the fans',
              'Lights':'you can switch to LED lights which save about 70% of energy and turn off lights when not in use',
              'Laptop': 'you can turn off your laptop charger when fully charged. It helps to save electricity and residual energy',
              'TV':'you watch too much TV! Go outside and touch some grass',
              'Others':'other costs include: refrigerator, cooking You can switch to energy saving refrigerators, and remember to turn off appliances when you sleep'}
datalist = []
with open('daily_cost.csv','r') as file_pointer:
    data = file_pointer.readlines()
    for i in data:
        datalist.append(float(i.split(',')[1]))
total = sum(datalist)
breach_record = []
for i in range(len(datalist)):
    datalist[i] = round(100*datalist[i]/total,2)
    if datalist[i] > national_average[i][1]:
        
        breach_record.append(i)
for i in breach_record:
    print(f'Your {national_average[i][0]} usage exceeds the national average! To reduce electricity consumption for the {national_average[i][0]},{advice_dict[national_average[i][0]]}\n')
    time.sleep(3)

cwd = os.getcwd()
time.sleep(2)
print(f'''
Thank you for logging on the MyElectricityTracker Program and for your efforts to save electricity today!
You may find your recorded data in csv format in this directory {cwd}!
Goodbye!
''')
#%%




