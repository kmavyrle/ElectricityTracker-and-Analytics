# ElectricityTracker-and-Analytics
Coursework: AB0403 Decision Making with Programming and Analytics

# Part 1: Electricity Tracker Program
## 1. Objective of the Project
Our group has decided to simulate an electricity consumption tracker program to address the topic on climate change. We have identified our target audience to be local households instead of commercial sectors and designed our program for general public use. More specifically, households that are willing to save electricity but find it inconvenient and lack the motivation to do so.

Upon identifying our target audience, we can then understand their needs and preferences for a program that allows them to track their carbon footprint. With that context in mind, the first need we have focused on would be to provide utility and value to our users, which is the most important function an application can provide for (Shaoolian, 2017). Secondly, we want to provide a differentiated and engaging user experience. The objective of our project would be to address the aforementioned needs through our program functionalities, with the end goal of encouraging electricity consumption awareness.

## 2. Project Functions
#### 2.1 Daily Electricity Consumption Report
We start off with a preliminary assessment where our program prompts users to key in the average number of hours their household uses for a list of electrical appliances (air conditioner, shower heater, fan, lights, laptop, TV), which will be stored in the database as a csv file. The aforementioned electrical appliances are selected as they are the main driver of electricity consumption in a household.

After receiving the preliminary data as well as incorporating the respective cost-savings (addressed later) for the user, a daily electricity consumption report is generated. This report lists the cost breakdown for each individual appliance before arriving at the total daily bill and the estimated monthly bill. Additionally, we also provide the historical daily reports of the user.

This functionality aims to provide utility and value-add to the users in the form of calculating and tracking daily household electricity consumption and converting it into a dollar amount, providing an estimate of their household electricity bill.

#### 2.2 Electricity & Cost Savings
After collecting the user's electricity usage data, a list of electricity-saving tasks are displayed for the user to complete. The list of tasks are curated based on the highest amount of cost savings that can be achieved for the respective appliances. By taking the initiative to provide the user with suggestive actions, they will be more motivated to implement them in their lifestyle.

Once the users have indicated their completion of the tasks, we will display the estimated amount of cost savings that they have achieved as well as the amount of points they’ve earned (explained subsequently). We hope to allow our users to visualize the tangible benefits of their electricity-saving actions to further incentivize this behavior.
 
#### 2.3 National Average Comparison
After gathering and compiling the user’s electricity consumption data, we introduced a form of benchmarking comparison function between the user’s data and the national average. The objective is to value-add to the existing insights provided to our users by allowing them to understand their relative consumption. Subsequently, we are able to identify the respective appliance(s) that is/are over-consuming.

Additionally, we also provide a percentage breakdown comparison between the national average and the user’s daily consumption report, in terms of each individual appliance. This provides a more detailed comparison coupled with a different perspective for the users to compare their electricity usage and helps the user to identify the appliances’ that are the main key drivers of their electricity consumption.

Once the preliminary assessment has been concluded, our program will provide further electricity savings tips that are specific to the appliances that our user is underperforming for, further individualizing the user experience.

#### 2.4 Gamification 
To further enhance the user experience through increased engagement, we included elements of gamification into our program through incorporating a point-based system and an individualized user interface.

Under the Electricity & Cost Savings feature, we converted the amount of savings into a point-based system through a fixed conversion rate of $0.10 = 1 point (arbitrary rate). Electricity saving tasks that allow users to save more electricity would correspondingly be allocated more points given the larger amount of cost savings. From this, users are able to achieve a total score of points earned based on the electricity saving tasks that they have completed for the day. To reward and motivate our users based on their daily performance, we have included certain printouts that would be displayed depending on their daily score. Additionally, users are able to track their score performance over a period of time through the daily electricity consumption report, which includes their historical daily scores. In the future implementation of our program, these points can be exchanged to tangible rewards, such as vouchers or coupons with our sponsored partners. This feature allows us to integrate a form of progression and sense of achievement in our users. 

Another subtlety that we have incorporated into our program would be to identify our users based on their names. Through this feature, we can individualize the user experience and assign an identity for our user.
 
## 3. User Manual 
#### 3.1 Introduction
1.	Dear user, we will provide you a walkthrough on how to go about using the MyElectricityTracker program in the following parts.
2.	This program will help you track your daily electricity usage, electricity costs and also encourage you to perform electricity saving tasks.
3.	This program is meant to be run everyday for you to key in your inputs for the usage of common electricity appliances, as well as whether you have performed any electricity saving activities during the day.
4.	There would be csv outputs saved for different stages of the program where we will save your data for future use so that you do not have to re-input your details (unless changes have been made).
5.	Note: Users should only run the program only once a day. Running the program more than once per day will result in extra data saved for the same day. Each user is supposed to have only 1 set of data per day.
3.2 Input of Preliminary Information
#### First-time Users:
1.	For first-time users running the program, you will need to key in some preliminary information about your profile, your household size and the electricity supplier your household subscribes to. This information would then be stored in a csv document on your computer.
 ![image](https://user-images.githubusercontent.com/85161103/160041022-913b2c19-8239-4830-acee-e2e82f3a1261.png)
 ![image](https://user-images.githubusercontent.com/85161103/160041027-4cc23eab-29af-48d7-a5d8-a989f11e30d5.png)

2.	After keying in your inputs, these inputs would be saved into a csv file named preliminary_info.csv in your designated working directory as shown below.
 ![image](https://user-images.githubusercontent.com/85161103/160041047-92660b10-43a6-47e2-b252-fb3f9c2d1476.png)

3.	The data presented in the csv can then be accessed via Microsoft Excel or any other csv reader.
 ![image](https://user-images.githubusercontent.com/85161103/160041058-98e3dbcd-e7e1-42f9-8f9f-0ae155f07dd9.png)

4.	A printout of your information will then be done as shown:
  ![image](https://user-images.githubusercontent.com/85161103/160041077-a9a3bf53-6557-43f2-a3df-c550ef2592a0.png)

For Repeated users:
1.	The program will automatically import your saved information from the csv document and run the program.
2.	Hence you would not need to re-input this information again.

#### 3.3 Input of Daily Electrical Appliance Usage
First-time users:
1.	You will need to key in the number of hours you spend using a list of common household electrical appliances. This value will be used to calculate your daily electrical costs.
2.	You will be prompted on whether there are any changes to your electrical bill compared to the previous day. However, since you are a first-time user, the program will prompt you for your inputs regardless of what you enter in the previous prompt.
 ![image](https://user-images.githubusercontent.com/85161103/160041115-0ecb8284-47a2-4298-8eca-1c4e90af45a0.png)
 
3.	The appliances include:
•	Air conditioner
•	Shower heater
•	Fan
•	Lights 
•	Laptop
•	Television
Other estimated fixed costs within the household will also be automatically added such as the refrigerator and other residual costs.
4.	If you key in a wrong data type into our program, it will re-run the particular component again for you to input. Also, if you would like to change your inputs if you made an error, a prompt will ask if you would like to confirm your inputs as shown:
   ![image](https://user-images.githubusercontent.com/85161103/160041134-4c75e913-9e6c-4336-9093-47d52251eab5.png)

If you enter ‘y’, this will confirm your inputs and the program will proceed to the next step. Inputting ‘n’ will re-run this step for you to input the hours used per appliance.
5.	Your inputs will then be saved into a csv file in your designated working directory so that you do not have to re-input them in future.
The numbers in the csv file represent your cost incurred per appliance used for the day.
6.	The csv will be saved with the name daily_cost.csv as shown:

  ![image](https://user-images.githubusercontent.com/85161103/160041149-22865a70-a6fd-46b7-a3d8-b32ce2750521.png)
  
  ![image](https://user-images.githubusercontent.com/85161103/160041155-a654b307-6f24-4b7b-997e-4c4c72cc271a.png)

 
Repeated Users:
1.	A prompt would ask if your electricity usage today has changed from the previous day.
2.	If there are any changes, input ‘y’ and you will get to re-input your inputs. The program will overwrite the current saved csv document with your new inputs.
  ![image](https://user-images.githubusercontent.com/85161103/160041166-9ca8ea9b-2a27-4740-b402-531a9b8fbb4c.png)

3.	Inputting ‘n’ will cause the program to use the data from the csv inputs from the previous day.

#### 3.4 Electricity-Saving Tasks and Reminder
1.	For this component, you will be provided with a curated list of electricity saving activities to do which will help you reduce your electricity costs.
2.	You will then need to key in the numbers corresponding to the tasks that you have done.
For example if you have done the first and third task, input the numbers 1 and 3 with a space in between as shown: 1 3
3.	If you have not done any tasks, you can input ‘n’
 ![image](https://user-images.githubusercontent.com/85161103/160041182-9bf9048c-f5cd-4ed3-9e2d-3bd3d183f6f0.png)

4.	The cost savings will be included in your daily electrical report in the form of reductions in your daily electricity costs. These will be reflected in your electricity cost report which will be covered later.

#### 3.5 (Gamification) Point System:
1.	Based on the electricity saving tasks that you have performed, points can be accumulated and recorded in the electricity cost report.
2.	Different printouts will be printed out based on the number of points you have accumulated within the day.
3.	The points accumulated will be equal to 1 point for every $0.10 of electricity cost saved.
An example of the printout is as shown:
 ![image](https://user-images.githubusercontent.com/85161103/160041196-206dc26d-5691-4ced-ab19-2336aff5d1e4.png)

4.	In future, when our program goes live, your accumulated points can be exchanged for attractive rewards!

#### 3.6 Generation of Electricity Cost Report
1.	After all your information has been recorded, the program will save all your data on a csv file called ‘Electricity_Summary_Report.csv’ as shown:

 ![image](https://user-images.githubusercontent.com/85161103/160041225-f5c768de-ccba-491f-951d-e933b2a7386d.png)

2.	This report will include a record of:
•	Electricity cost incurred each day
•	Cumulative costs incurred
•	Cumulative points acquired for performing electricity saving tasks
 
#### 3.7 National Average Comparison & Recommendations
1.	For this component, your usage of electricity appliances will be compared to the national average based on the percentage of total costs.
2.	For appliances which exceed the national average percentage use, targeted advice will be provided to you on how you can reduce consumption for the particular electrical appliance as shown:
 ![image](https://user-images.githubusercontent.com/85161103/160041243-ed509867-1f45-4662-8214-e0fea11fd77a.png)
 
 # Part 2: Analytics
 For performing analytics, we took a top down approach to investigate energy consumption trends globally, before zooming into Singapore.

