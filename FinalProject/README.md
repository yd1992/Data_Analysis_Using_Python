Data Analysis Using Python - Video Games Sales Datasets Analysis

Orginal Datasets: named "vgsales.csv" saved under folder "Datasets"

Step1: Collecting Data
#run command line: python collect_data.py
#You will get all of the specific data which are required for every data analysis task, and then save as csv file into fold Datasets
#Result files: 
#Datasets_Analysis_1.csv: [Name, Platform, Year, Global_Sales]
#Datasets_Analysis_2.csv: [Genre, NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales]
#Datasets_Analysis_3.csv: [Year, Publisher, Global_Sales]
#Datasets_Analysis_4.csv: [Platform, Genre, Global_Sales]
#Datasets_Analysis_5.csv: [Year, NA_Sales, EU_Sales, JP_Sales, Other_Sales]


Step2: Data Analysis Task 1
run command line: python Data_Analysis_1.py
We will analyze the total Global Sales based on different Platforms within all years, to help determine which platform has a good development future.
run command line: python User_Interface.py
User can input Platform name into "Input1" box, and then click button "Get Info", then they will get the total Global Sales of this platform, and their result file, named "Analysis1_User_Result.csv", will be saved under folder "Result"
Also, we will save all the Total Global Sales based on different platforms under the folder "Result", named file "Analysis1_Result.csv"
Except that, we will visualize the result with a cylindra chart, saved under the folder "Result", named file "Image_Analysis_1.png"

Step3: Data Analysis Task 2
run command line: python Data_Analysis_2.py
We will analyze people' s Favorite Genre of Video Games based on their Districts, to different district people have different preferences
run command line: python User_Interface.py
User can input District name into "Input1" box, and then click button "Get Info", then they will get the total Global Sales of this district based on different genres of video games, and their result file, named "Analysis2_User_Result.csv", will be saved under folder "Result"
Also, we will save all the Total Global Sales based on different districts and different genres of video games under the folder "Result", named file "Analysis2_Result.csv"
Except that, we will visualize the result with a chart, saved under the folder "Result", named file "Image_Analysis_2.png"

Step4: Data Analysis Task 3
run command line: python Data_Analysis_3.py
We will analyze the Total Global Sales based on Publishers in different years,to show which publishers is most popular in video games industry
run command line: python User_Interface.py
User can input Publisher name into "Input1" box, and then click button "Get Info", then they will get the total Global Sales of this publisher within all years, and their result file, named "Analysis3_User_Result.csv", will be saved under folder "Result"
Also, we will save all the Total Global Sales based on different publishers under the folder "Result", named file "Analysis3_Result.csv"
Except that, we will visualize the result with a pie chart, saved under the folder "Result", named file "Image_Analysis_3.png"

Step5: Data Analysis Task 4
run command line: python Data_Analysis_4.py
We will analyze the Total Global Sales based on Platform and Genre, to see which platform produce what kind of genres of video games, to help people determine purchasing.
run command line: python User_Interface.py
User can input Publisher name into "Input1" box and Genre name into "Input2" box, and then click button "Get Info", then they will get the total Global Sales of this platform and this genre, and their result file, named "Analysis4_User_Result.csv", will be saved under folder "Result"
Also, we will save all the Total Global Sales based on different platforms and different genres under the folder "Result", named file "Analysis4_Result.csv"
Except that, we will visualize the result with a chart, saved under the folder "Result", named file "Image_Analysis_4.png"

Step6: Data Analysis Task 4
run command line: python Data_Analysis_5.py
We will analyze the Total Global Sales based on Year and District, to see which year people like playing video games mostly, and help determine future sales in video games.
run command line: python User_Interface.py
User can input District name into "Input1" box and click button "Get Info", and then they will get the total Global Sales of this District within all different years, and their result file, named "Analysis5_User_Result.csv", will be saved under folder "Result"
Also, we will save all the Total Global Sales based on different districts and different years under the folder "Result", named file "Analysis5_Result.csv"
Except that, we will visualize the result with a line chart, saved under the folder "Result", named file "Image_Analysis_5.png"


