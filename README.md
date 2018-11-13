# Data Processing
- Course: BigData
- Project number: 4
- Developer Pair 1- Kyle Thompson, Goutham Neravetla, Sumnima Rana
- Developer Pair 2- Krishna Veni Karri, Pappu Shah


## Links
- [Webpage](https://sumnimarana1.github.io/MapReduceProjectGroup4/ "MapReduce Project group 4")
- [Source](https://github.com/sumnimarana1/MapReduceProjectGroup4 "MapReduce Project group 4")

## Introduction

We are using two datasets in our project.
One is real estate data which is structured data and the other is unstructured data related to social movement metoo.

Dataset 1: WashingtonDC real estate dataset
Dataset 2: 300k #metoo tweets.



## Data Source
- [DC Residential Properties](https://www.kaggle.com/christophercorrea/dc-residential-properties "Website for dataset")
This datasets has analysis showing real property information, including most recent sales price as of July 2018, for properties located Washington, D.C.Data is in CSV format and has 49 columns. Some of the attributes are ID, BATHRMNumber of Full Bathrooms, HF_BATHRM(Number of Half Bathrooms), HEATHeating, ACCooling, NUM_UNITS, etc.

- [#metoo Dataset](https://data.world/rdeeds/350k-metoo-tweets)
This is a data set which has tweets related to social movement metoo from October 2017 to february 2018. Data is in CSV format and has 16 columns. Some of the attributes are tweet_id, tweet text, timestamp of the tweet, handle etc.



## The Challenge

**5 V’s for WashingtonDC Dataset**
- Volume- There are 159K rows and 49 Col and size is 52.81 MB
- Velocity- The last update for the Datasets was done 3 Months ago.
- Value- This datas can be used to predict the property for the future business and help buyers and seller and know if its reasonable for you or not. 
- Variety- Pretty structured with numerical and nominal(categorical)
- Veracity- Downloaded from Kaggle dataset which is trusted site for the dataset.

**5 V’s for datasets**
- Volume- The size of the 122.82 MB
- Velocity- Using the API’s we can retrieve approximately 4000 live stream tweets in 30 seconds. The dataset is last updated on February 2018
- Value- This dataset provide insight of impact of social media on society and the swing of the movement.
- Variety- This data is combination of text and numerical data
- Veracity- We downloaded it from DataWorld which is trusted site for the dataset and scrapped using twitter bot. So we think it is accurate.

## Big Data Questions
- Average number of full bathrooms - Goutham
- Average Price per square foot-Kyle Thomspon
- Calculating average sales in a particular month.- Sumnima Rana
- Find the top 5 handles.- Pappu Sah
- Sentiment of tweet (total  number of positive negative and neutral tweets)-  Krishna Veni Karri


## Big Data Solutions

**Kyle:**
* Mapper Input: DC_Properties.csv 
* Mapper Output/Reducer Input: Price/ Square Feet
* Reducer Output: Total Cost / Total Square Feet
* Language: Python 
* Graph: Two bars to display ratio 

**Sumnima:**
* Mapper Input: DC_Properties.csv 
* Mapper Output/ Reducer Input:: SALEDATE / PRICE (price of most recent sales)
* Reducer Output: Month, Average
* Language: Python
* Use: Bar Chart for 12 Months to show the Average sale

**Pappu:**
* Mapper Input: metootweets.csv 
* Mapper Output/ Reducer Input:Twitter Handle , Followers
* Reducer Output: Twitter Handle, count of Followers
* Language:Python
* Chart: Bar graph

**Krishna Veni:**
* Mapper Input: metootweets.csv 
* Mapper Output/ Reducer Input: tweet id, Text
* Reducer Output::  sentiment, count ({positive, count}, {negative, count}, {neutral, count})
* Language:  Python
* Chart: Pie chart

**Goutham Neravetla:**
* Mapper Input: DC_Properties.csv 
* Mapper Input/Reducer Input: ID and BATHRM
* Reducer Output- bathroom and Count
* Language: Python
* Chart: Bar Chart
