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
- Count the number of houses that have more than or equal to 10 rooms and 7 full bathrooms  - Goutham
- Average Price per square foot-Kyle Thomspon
- Calculating average sales in a particular month.- Sumnima Rana
- Find the top 5 handles.- Pappu Sah
- For each tweet find Sentiment and then calculate total number of positive negative and neutral tweets-  Krishna Veni Karri


## Big Data Solutions

**Kyle:**
* Mapper Input: DC_Properties.csv
* Mapper Output/Reducer Input: Price/ Square Feet
* Reducer Output: Total Cost / Total Square Feet
* Language: Python
* Graph: Two bars to display ratio

**Sumnima:**
* Mapper Input: DC_Properties.csv
 ![alt text](https://github.com/Sumnimarana1/MapReduceProjectGroup4/blob/master/rana/images/mapper.png)
* Mapper Output/ Reducer Input:: MONTH / PRICE (price of most recent sales)
 ![alt text](https://github.com/Sumnimarana1/MapReduceProjectGroup4/blob/master/rana/images/MapperO.png)
* Reducer Output: Month, Average
 ![alt text](https://github.com/Sumnimarana1/MapReduceProjectGroup4/blob/master/rana/images/ReducerO.png)
* Language: Python
* Use: Bar Chart for 12 Months to show the Average sale

**Pappu:**
* Mapper Input: metootweets.csv
![alt text](https://github.com/Sumnimarana1/MapReduceProjectGroup4/blob/master/karri/images/mapper_input.PNG)
* Mapper Output/ Reducer Input:Twitter Handle , Followers

![alt text](https://github.com/Sumnimarana1/MapReduceProjectGroup4/blob/master/karri/images/sah_output.PNG)
* Reducer Output: Twitter Handle, count of Followers
* Language:Python
* Chart: Bar graph

**Krishna Veni:**
* Mapper Input: metootweets.csv
![alt text](https://github.com/Sumnimarana1/MapReduceProjectGroup4/blob/master/karri/images/mapper_input.PNG)
* Mapper Output/ Reducer Input: tweet id, Text
![alt text](https://github.com/Sumnimarana1/MapReduceProjectGroup4/blob/master/karri/images/Reducer_input.PNG)
* Reducer Output::  sentiment, count ({positive, count}, {negative, count}, {neutral, count})
* Language:  Python
* Chart: Pie chart

**Goutham Neravetla:**
* Mapper Input: DC_Properties.csv
![alt text](neravetla/images/neramapperinput.png)
* Mapper Output/Reducer Input: BATHRM and ROOMS <br />
![alt text](neravetla/images/nerareducerinput.png)
* Reducer Output- Number of houses that have more than or equal to certain number of houses and bathrooms
![alt text](neravetla/images/nerareduceroutput.png)
* Language: Python
* Chart: Bar Chart
