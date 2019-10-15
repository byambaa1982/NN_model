
#ANN MODEL FOR PREDICTION OF BUBBLE POINT PRESSURE OF CRUDE OILS

##1. Problem
Bubble point pressure is one of most important pressure, volume and temperature properties of crude oil and it plays an important role in reservoir and production engineering calculations. Rule-based and other traditional techniques are time-consuming, expensive and various other limitations.

##2. Solution
The project’s objective was to build an Artificial Neural Network (ANN) based model that determines bubble point pressure (Pb) and bubble point oil (Bob) of crude oil as a solution. 

##3. Data Collection and Cleaning
Data source and obtaining method:

 - Simulation Data.xlsx – downloaded in .csv format
 - Write any further detail of data cleaning if there is exists.

##4. Data Limitation: 

 - Write details of your dataset in bullet points.

##5.  Feature Selection
The target variables are bubble point pressure (Pb) and bubble point oil (Bob). For feature selection, I preferred to work on numerical-based features. I considered four features in order to determine bubble point pressure as follows:

 - GOR (Gas Oil Ratio)

 - Oil Gravity

 - Gas Gravity

 - Temperature

##6. Exploratory Data Analysis
Have a quick look at the joint distribution of a few pairs of columns from the training set.
Join Distribution ![Alt](/JoinDistribution.png "Join Distribution")


##7. Modeling
The data set was divided into training and test subsets--the training set was X%, and the test set was Y% of the total dataset, where the target are bubble point pressure (Pb) and bubble point oil (Bob).

Experimented vs Predicted for Pb ![Alt](/Pb.png "Experimented vs Predicted for Pb")

Experimented vs Predicted for Bob ![Alt](/Bob.png "Experimented vs Predicted for Bob")


##8. Conclusion

 - My dataset was in numerical form. I partitioned the dataset for training and testing purposes.
 - I selected four features i.e. Gas oil ratio (GOR), oil gravity, gas gravity and temperature for the determining of bubble point pressure (Pb) and bubble point oil (Bob).
 - My model was based on Artificial Neural Networks (ANN) while Mean Error Square (MEA) and R Square (RS) used as evaluation metrics.
 - Write accuracy and other important results if required.




