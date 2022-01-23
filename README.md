![image](https://user-images.githubusercontent.com/73279545/150691742-7616fc46-fb5a-443a-ae53-cc27b7f433bb.png)

This data science project series walks through step by step process of how to build a real estate price prediction website. We will first build a model using sklearn and linear regression using banglore home prices dataset from kaggle.com. Second step would be to write a python flask server that uses the saved model to serve http requests. Third component is the website built in html, css and javascript that allows user to enter home square ft area, bedrooms etc and it will call python flask server to retrieve the predicted price. During model building we will cover almost all data science concepts such as data load and cleaning, outlier detection and removal, feature engineering, dimensionality reduction, gridsearchcv for hyperparameter tunning, k fold cross validation etc. Technology and tools wise this project covers :

1. Python
2. Numpy and Pandas for data cleaning
3. Matplotlib and seaborn for data visualization
4. Sklearn for model building
5. Jupter Notebook , Visual Studio code and Pycharm as IDE
6. Python flask for http server
7. Postman for API testing 
8. HTML/CSS/Javascript for UI

# Deploy this app to cloud (AWS EC2)
1. Create EC2 instance using amazon console, also in security group add a rule to allow HTTP incoming traffic
2. Now connect to your instance using a command like this,

```bash
ssh -i "house_price_prediction.pem" ubuntu@ec2-44-202-146-183.compute-1.amazonaws.com
```

3. Nginx setup
  1. Install nginx on EC2 instance using these commands,
