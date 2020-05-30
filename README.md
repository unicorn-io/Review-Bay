<p align="center"><img src="https://github.com/unicorn-io/Review-Bay/blob/master/static/images/ReviewBay.png" width = 40%</p>

### Making an Sentiment-Analyzer for SIH-2020

Organization :ISRO (Indian Space Research and Developement Organization)
SIH is an university level hackathon organised by Govt. of India. Our team choose this problem statement,as we felt that  this problem statement has a huge relevance as major websites and businness do not use an automated sentiment analyzer which is now the defunct thing.
 
### Problem Statement : 
[Problem Statement](https://www.sih.gov.in/sih2020PS/MTE=/U29mdHdhcmU=/SW5kaWFuIFNwYWNlIFJlc2VhcmNoIE9yZ2FuaXNhdGlvbiAoSVNSTyk=/QWxs)

### Output Expected : 
1. Classification of individual comments/reviews.
2. Determining overall rating based on individual comments /reviews

### The dataset used for this purpose is :
[Dataset]( http://jmcauley.ucsd.edu/data/amazon/)


#### The authors for this project are :

1. DhruvRaipure
2. unicorn-io
3. smritisingh26
4. ShamanthNyk
5. nimesh
6. sagnik-chatterjee

#### Contributions are welcome , please refer to contributing.md for contributing to this project.  

#### Running the web-app
* Clone the repository
* To run the app make sure the requirements are installed.
```
pip install -r requirements.txt
```
We will be relocating to the directory and exporting the flask app.
```
cd ../
export FLASK_APP=Review-Bay  # GNU/LINUX
set FLASK_APP=Review-Bay # Windows
```
Now that we are set for development uses or contributions we might suggest to run the app in development environment.
```
set FLASK_ENV=development # Windows
export FLASK_ENV=development # GNU/LINUX
```
Finally we are all set to run this
```
flask run
```
The application can be accessed on your local host server.
