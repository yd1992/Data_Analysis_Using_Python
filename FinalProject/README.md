#Data Analysis Using Python - Video Games Sales Datasets Analysis
  
##Introduction: 

  With gradually popularity of video games within all over ther world for so many years, there are more and more video games genres has been developed by different publishers on different platforms. In this data analysis project, I collect the data of all video games sales data on different platforms of different publishers in different districts of the world within recent 30 years, then analyzing the analysis results, and then use those results to help customers to choose which genres of videos on which platforms produced by which publishers is the most fit for them, and also help publishers to determine what kind of genres of videos on which platforms can have the most brightful future to be purchased by customers in the future.
  
  The Orginal Datasets: named "vgsales.csv" saved under folder "Datasets"
  
  ![alt tag](https://github.com/yd1992/Data_Analysis_Using_Python/blob/master/FinalProject/Readme%20Pic/Collect/Origin%20Datasets.png)

##Step1: Collecting the Data

  Run command line: python collect_data.py
 
  You will get all of the specific data, which are required for every data analysis task, and then they will be saved as the .csv file    into fold "Datasets"， and these saved data will be used for future analysis and prediction among five data analysis tasks
  
  I used two functions of panda read_csv() and to_csv()
  
  Example Source Code:
  
  ![alt tag](https://github.com/yd1992/Data_Analysis_Using_Python/blob/master/FinalProject/Readme%20Pic/Code/1.png)
  
  Saved .csv file: 

  Datasets_Analysis_1.csv: [Name, Platform, Year, Global_Sales]
  
  ![alt tag](https://github.com/yd1992/Data_Analysis_Using_Python/blob/master/FinalProject/Readme%20Pic/Collect/Collect1.png)

  Datasets_Analysis_2.csv: [Genre, NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales]
  
  ![alt tag](https://github.com/yd1992/Data_Analysis_Using_Python/blob/master/FinalProject/Readme%20Pic/Collect/Collect2.png)

  Datasets_Analysis_3.csv: [Year, Publisher, Global_Sales]
  
  ![alt tag](https://github.com/yd1992/Data_Analysis_Using_Python/blob/master/FinalProject/Readme%20Pic/Collect/Collect3.png)

  Datasets_Analysis_4.csv: [Platform, Genre, Global_Sales]
  
  ![alt tag](https://github.com/yd1992/Data_Analysis_Using_Python/blob/master/FinalProject/Readme%20Pic/Collect/Collect4.png)

  Datasets_Analysis_5.csv: [Year, NA_Sales, EU_Sales, JP_Sales, Other_Sales]
  
  ![alt tag](https://github.com/yd1992/Data_Analysis_Using_Python/blob/master/FinalProject/Readme%20Pic/Collect/Collect5.png)

##Step2: User Interface with Analysis

  ![alt tag](https://github.com/yd1992/Data_Analysis_Using_Python/blob/master/FinalProject/Readme%20Pic/Code/UI1.png)
  
  ![alt tag](https://github.com/yd1992/Data_Analysis_Using_Python/blob/master/FinalProject/Readme%20Pic/Code/UI2.png)

  In order to implement dynamic interaction with users, I implemented this user interface to return required analysis results based on users' input

  Run Command line: python User_Interface.py
  
  You will login to the User Interface. 
  You can choose different data analysis task by clicking the different radio buttons
  Then input required parameters based on reminder inside user interface. 
  Then click "Get Info" Button, you will get the result based on the user input and data analysis process.
  The Result will be presented through charts and tables.
  
  User Interface:
  
  ![alt tag](https://github.com/yd1992/Data_Analysis_Using_Python/blob/master/FinalProject/Readme%20Pic/Screen%20Shot%202016-12-10%20at%207.58.21%20PM.png)
  
##Step3_1: Data Analysis Task 1

  Run command line: python Data_Analysis_1.py [Platform Name: Wii]

  In this analysis, We will analyze the Global Sales based on different Platforms within all over the years, to show that the popularity of different platforms, and to help customers determine which platforms they should purchase to play video games
  
  ![alt tag](https://github.com/yd1992/Data_Analysis_Using_Python/blob/master/FinalProject/Readme%20Pic/Code/A1.png)
  
  ###User Interface Operation: 
  
  Run Command line: python User_Interface.py
  
  User can choose the first radio between 
  User can input Platform name, like Wii, into "Input1" box
  Then click button "Get Info"
  Then they will get the total Global Sales of this platform
  
  ###Analysis Result: 
  
  After analysis, the result file, named "Analysis1_User_Result.csv", will be saved under folder "Result", which save the total number of global sales of video games on the platform which is required by users
  
  ![alt tag](https://github.com/yd1992/Data_Analysis_Using_Python/blob/master/FinalProject/Readme%20Pic/ResultData/1_User.png)
  
  Also, we will save all the Total Global Sales based on all different platforms within all years in the dataset under the folder "Result", named file "Analysis1_Result.csv"
  
  ![alt tag](https://github.com/yd1992/Data_Analysis_Using_Python/blob/master/FinalProject/Readme%20Pic/ResultData/1.png)
  
  Except that, we will visualize the result with a cylindra chart, saved under the folder "Result", named file "Image_Analysis_1.png", which visualize the total number of global sales based on all differen platforms within all years in the dataset
  So we can easily find which platforms are more popular for customers who like video games within all other platforms based on video games sales data
  
  ![alt tag](https://github.com/yd1992/Data_Analysis_Using_Python/blob/master/FinalProject/Result/Image_Analysis_1.png)

##Step3_2: Data Analysis Task 2

  Run command line: python Data_Analysis_2.py [District:NA]

  In this analysis, we will analyze people' s Favorite Genre of Video Games based on different Districts, which can get the preferences to different genres of video games in different districts all over the world, and this can greatly help video game publishers determine to produce the genres of video games to different districts all over the world, and gain more benefits.
  
  ![alt tag](https://github.com/yd1992/Data_Analysis_Using_Python/blob/master/FinalProject/Readme%20Pic/Code/A2.png)

  ###User Interface Operation: 
  
  Run command line: python User_Interface.py

  User can choose the second radio button
  User can input District name into "Input1" box
  Then click button "Get Info"
  Then they will get the total Global Sales of this district based on different genres of video games
  
  ###Analysis Result:
  
  After analysis, the result file, named "Analysis2_User_Result.csv", will be saved under folder "Result", which will show the top three most sales video games of the required district input by users
  
  ![alt tag](https://github.com/yd1992/Data_Analysis_Using_Python/blob/master/FinalProject/Readme%20Pic/ResultData/2_User.png)
  
  Also, we will save all the Total Global Sales based on different districts and different genres of video games under the folder "Result", named file "Analysis2_Result.csv" and the data will be sorted by the descending order of global sales
  
  ![alt tag](https://github.com/yd1992/Data_Analysis_Using_Python/blob/master/FinalProject/Readme%20Pic/ResultData/2.png)
  
  Except that, we will visualize the result with a chart, saved under the folder "Result", named file "Image_Analysis_2.png"
  
  ![alt tag](https://github.com/yd1992/Data_Analysis_Using_Python/blob/master/FinalProject/Result/Image_Analysis_2.png)
  
##Step3_3: Data Analysis Task 3

  Run command line: python Data_Analysis_3.py [Publisher: Nintendo]

  We will analyze the relationship of the different Publishers within different years and the global sales of video games, which can help customers determine which publishers are more popular and can produce more high 
  
  ![alt tag](https://github.com/yd1992/Data_Analysis_Using_Python/blob/master/FinalProject/Readme%20Pic/Code/A3.png)

  ###User Interface Operation: 

  Run command line: python User_Interface.py

  User can choose the third radio button
  User can input Publisher name into "Input1" box
  Then click button "Get Info"
  Then they will get the total Global Sales of this  publisher within all years
  
  ###Analysis Result: 
  
  After this analysis, their result file, named "Analysis3_User_Result.csv", will be saved under folder "Result", which will save the total global sales of publishers which are require by users' input
  
  ![alt tag](https://github.com/yd1992/Data_Analysis_Using_Python/blob/master/FinalProject/Readme%20Pic/ResultData/3_User.png)
  
  Also, we will save all the Total Global Sales based on different publishers under the folder "Result", named file "Analysis3_Result.csv"
  
  ![alt tag](https://github.com/yd1992/Data_Analysis_Using_Python/blob/master/FinalProject/Readme%20Pic/ResultData/3.png)
  
  Except that, we will visualize the result with a pie chart, saved under the folder "Result", named file "Image_Analysis_3.png", which will show the percentage of the total globals sales of different publishers which are input by users
  
  ![alt tag](https://github.com/yd1992/Data_Analysis_Using_Python/blob/master/FinalProject/Result/Image_Analysis_3.png)
  
##Step3_4: Data Analysis Task 4

  Run command line: python Data_Analysis_4.py [Genre: Sports, Platform: Wii]

  We will analyze the effect of genres and platforms to total global sales, to see what kind of genres of video games on which platform are more popular, and then to help customer determine purchasing the video games based 
  
  ![alt tag](https://github.com/yd1992/Data_Analysis_Using_Python/blob/master/FinalProject/Readme%20Pic/Code/A4.png)

  ###User Interface Opeations:

  Run command line: python User_Interface.py

  User can choose the fourth radio button

  User can input Publisher name into "Input1" box and Genre name into "Input2" box
  
  Then click button "Get Info"
  
  Then they will get the total Global Sales of this platform and this genre
  
  ###Analysis Result: 
  
  The result file, named "Analysis4_User_Result.csv", will be saved under folder "Result", which will show the total sales based on genre and platform given by users
  
  ![alt tag](https://github.com/yd1992/Data_Analysis_Using_Python/blob/master/FinalProject/Readme%20Pic/ResultData/4_User.png)
  
  Also, we will save all the Total Global Sales based on different platforms and different genres under the folder "Result", named file "Analysis4_Result.csv", which will save all of the sales based on differen genres and platforms with descending order
  
  Except that, we will visualize the result with a chart, saved under the folder "Result", named file "Image_Analysis_4.png", which is a three dimensional chart, and reflect sales of video games based on genres and platforms, to help customers make decision
  
  ![alt tag](https://github.com/yd1992/Data_Analysis_Using_Python/blob/master/FinalProject/Result/Image_Analysis_4.png)

##Step3_5: Data Analysis Task 5

  Run command line: python Data_Analysis_5.py [District: NA]

  We will analyze the Total Global Sales based on Year and District, to see which year customer like playing video games mostly in different districts, and help publishers to determine future sales in video games in order to increase their benefits.

  ![alt tag](https://github.com/yd1992/Data_Analysis_Using_Python/blob/master/FinalProject/Readme%20Pic/Code/A5.png)

  ###User Interface Operation:

  Run command line: python User_Interface.py

  User can choose the fifth radio button
  
  User can input District name into "Input1" box
  
  Then click button "Get Info"
  
  Then they will get the total Global Sales of this District within all different years
  
  ###Analysis Result:
  
  The result file, named "Analysis5_User_Result.csv", will be saved under folder "Result", which will reflect all of the years global sales of video games in the region given by users
  
  ![alt tag](https://github.com/yd1992/Data_Analysis_Using_Python/blob/master/FinalProject/Readme%20Pic/ResultData/5_User.png)
  
  Also, we will save all the Total Global Sales based on different districts and different years under the folder "Result", named file "Analysis5_Result.csv", which 
  
  ![alt tag](https://github.com/yd1992/Data_Analysis_Using_Python/blob/master/FinalProject/Readme%20Pic/ResultData/5.png)
  
  Except that, we will visualize the result with a line chart, saved under the folder "Result", named file "Image_Analysis_5.png"， which will reflect the trends of global sales of video games in different districts within recent 30 years
  
  ![alt tag](https://github.com/yd1992/Data_Analysis_Using_Python/blob/master/FinalProject/Result/Image_Analysis_5.png)


