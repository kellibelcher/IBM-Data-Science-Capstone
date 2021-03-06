![commits](https://img.shields.io/github/last-commit/kellibelcher/IBM-Data-Science-Capstone?label=Last%20Commit%20) 
![files](https://img.shields.io/badge/Files-9-9489e8)
![size](https://img.shields.io/github/repo-size/kellibelcher/IBM-Data-Science-Capstone?label=Repo%20Size%20)
<h1 align="center">
  SpaceX Rocket Landing Predictive Analysis :rocket:
</h1> 

<p align="center">
  <img src="https://img.shields.io/badge/Python-3670A0?&logo=python&logoColor=ffffff" /> 
  <img src="https://img.shields.io/badge/NumPy-%23013243.svg?&logo=numpy&logoColor=white"/> 
  <img src="https://img.shields.io/badge/pandas-%23130754.svg?logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/scikit--learn-%23F89939.svg?&logo=scikit-learn&logoColor=white"/>
  <img src="https://img.shields.io/badge/Plotly-%233F4F75.svg?&logo=plotly&logoColor=white"/>
  <img src="https://img.shields.io/badge/Jupyter-%23F37725.svg?&logo=jupyter&logoColor=white"/>
</p> 

## Background 🌎
SpaceX is a leading designer and manufacturer of advanced rockets and spacecraft. The company advertises Falcon 9 rocket launches on its website at a cost of $62 million, while other providers cost upwards of $165 million each. Much of the savings is because SpaceX can reuse the first stage of the launch. However, sometimes the first stage does not land and cannot be recovered. Therefore, if we can determine whether the first stage will land successfully, we can better estimate the cost of a launch.

In this project, I'll collect and process raw data from a variety of sources, explore the data using different visual analytics tools, and build a predictive model to determine whether the first stage of the SpaceX Falcon 9 rocket will land successfully to help competitors make more informed bids.


## Table of Contents :ringed_planet:
### [Data Collection](https://github.com/kellibelcher/IBM-Data-Science-Capstone/blob/master/Week%201%20Lab:%20Spacex%20Data%20Collection.ipynb) and [Webscraping](https://github.com/kellibelcher/IBM-Data-Science-Capstone-2/blob/master/Week%201%20Lab:%20Webscraping.ipynb)
- Collected launch data using the SpaceX REST API.
- Scraped additional data from the web using Python's `BeautifulSoup` package.

### [Data Wrangling](https://github.com/kellibelcher/IBM-Data-Science-Capstone/blob/master/Lab%202:%20Data%20Wrangling.ipynb) 
- Preprocessed and cleaned the data set to begin data exploration.

### [Exploratory Data Analysis with SQL](https://github.com/kellibelcher/IBM-Data-Science-Capstone/blob/master/Lab%203:%20SQL%20EDA.ipynb) 
- Queried IBM's DB2 cloud database using `sqlalchemy` to explore, summarize, and gain insights from the data.

### [Data Visualization EDA](https://github.com/kellibelcher/IBM-Data-Science-Capstone/blob/master/Lab%204:%20EDA%20Data%20viz.ipynb) 
- Explored the relationships between different sets of features in the data set and identified important variables in predicting rocket launch successes.

### [Geospatial Analysis using Folium](https://github.com/kellibelcher/IBM-Data-Science-Capstone/blob/master/Lab%205:%20Mapping%20launch%20site%20locations.ipynb) 
- Created interactive leaflet maps using `folium` and analyzed existing launch site locations to identify geographical trends in the data.

### [Launch Success Rate Dashboard](http://spacexdashappkellibelcher.pythonanywhere.com/) 
- Developed an interactive Plotly Dash app to analyze success rates based on launch site location and payload weight.

### [Predictive Modeling](https://www.kaggle.com/kellibelcher/spacex-rocket-landing-predictive-analysis) 
- Fit several classification models, including a Support Vector Machine, Logistic Regression, Decision Tree, and K-Nearest Neighbors model.
- Tuned model parameters using cross-validation and predicted whether the first stage of a rocket launch will land successfully with an Area Under the Curve of 0.958.

</br>

<p align="center">
  <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/api/Images/landing_1.gif" />
  <img src="https://media.designrush.com/inspiration_images/134929/conversions/_1512513081_152_ibm-mobile.jpg"/>
</p>


