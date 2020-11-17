# Welcome to the test results of Stock Prediction

Hi! We are group 12 and we are testing a [system that predicts stock prices](https://github.com/lokesh45/StockPrediction). 
This is a repository made as part of the curriculum at NC State for the course CSC 510 Software Engineering.

## Description of the source repository
 The source repository `https://github.com/lokesh45/StockPrediction` is an attempt to predict the uncertain nature of the stock market.
 
 Over here, we find a flask app, where the web application can be started. A detailed explanation of the application, model, schema and the setup instructions can be found on the [repository](https://github.com/lokesh45/StockPrediction).



## Method: Test Plan

1. Get around 8 to 10 participants to test three websites: [Wallet Investor](https://walletinvestor.com/), [AIStockFinder](https://www.aistockfinder.com/) and [the app we are testing](https://radiant-falls-10905.herokuapp.com).
2. Assign keys to each user.
3. Record the data generated from the participant. Each participant will perform following activities:

    1. Analyse the project based on Ease of use, Accuracy, Cost, Range of choice.

    2. Compare current project with other real-life market solutions available online (for this project, they are Wallet Investor, AIStockFinder)

    3. Report bugs(if found)

    4. Review the project on scale 1(Low) to 5(High).
4. Utilize the data and analyse the feedback received from each participant. They will be stored using this [google form](https://docs.google.com/forms/d/e/1FAIpQLSfrOcLyx1ZxUexelyc2YJZB9imcJUHoP9oH8zVcHtOkJD-VYQ/viewform).
5. Generate aggregated rating for the entire project based on Ease of use, Accuracy, Cost, Range of choice.

## How to setup: from cloning to deploying on Heroku

1. Clone the [repository we are testing](https://github.com/lokesh45/StockPrediction). You can do this by typing `git clone https://github.com/lokesh45/StockPrediction`.

2. Change the file `Dockerfile` by replacing the last line from `CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]` to `CMD flask run --host 0.0.0.0 --port ${PORT}`.

3. Make an account on [Heroku](https://signup.heroku.com/login).

4. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).

5. Go back the folder where the `StockPrediction` you cloned is located and open a terminal inside it.

>Optional: Install the [docker cli](https://docs.docker.com/get-docker/). Type `docker ps -a`. A list of images will show up.

6. Type `heroku login` in the terminal and it will open a browser for you to login.

7. After logging in, type `heroku create`, followed by `heroku container:push web`. This will take few minutes.

8. For releasing it to the web, type: `heroku container:release web`.

9. Now to open the site you just pushed type `heroku open`.
## Materials

Below are the tools used to perform anonymous experiments

- Deployed application: [App](https://radiant-falls-10905.herokuapp.com/)
- Platform used to deploy App: Heroku
- Project 3 GitHub Repository: [GitHub](https://github.com/lokesh45/StockPrediction)
- For collecting responses: [Google form](https://docs.google.com/forms/d/e/1FAIpQLSfrOcLyx1ZxUexelyc2YJZB9imcJUHoP9oH8zVcHtOkJD-VYQ/viewform?usp=sf_link)
- Metrics used: [Test plan sheet](https://docs.google.com/spreadsheets/d/1rQDUvgM1uNTLeklLOQzoprsNrLaTmgU-nL8uw30S_xw/edit?usp=sharing)
- Tool used to setup meeting: [Zoom](https://zoom.us/)
- Code for plotting graphs: [Script](https://github.com/ssp4all/SE/tree/main/scriptsForAnalysis)



## Observations


### How people tested the sites
We told the participants to find stocks on each website and look at their prediction. Meetings were conducted via Zoom, timings of which were decided via communications on Slack or WhatsApp.

They were also told to stay at any website for any amount time, till they feel they were comfortable with the website. Only after that were they advised to fill up the google form. The participants were encouraged to talk about what they are feeling.

We found most of them took around 5 to 10 minutes for the first website and then the time it took for them to test other websites decreased in a linear fashion.

In total there were 9 participants, and we have responses from 8 of them. One of them exercised their Right to Refuse. 

Below you can find the responses of the 8 participants.
### We asked about their familarity of the stock markets.
| ![Figure 1](https://github.com/ssp4all/stock-prediction-evaluation/blob/main/images/1.PNG) | 
|:--:| 
| *Figure 1* |

## Analysis



### Analyzing the Recommendation Ratings.
After using all 3 platforms for predicting stock trends, we asked the users how likely are they to recommend each of the apps. This metric helps us understand the overall perception of the user. Following are the results:

| ![Figure 2](https://github.com/ssp4all/stock-prediction-evaluation/blob/main/images/Ai_Stock_finder.png) | 
|:--:| 
| *Figure 2* |

| ![Figure 3](https://github.com/ssp4all/stock-prediction-evaluation/blob/main/images/Wallet_investor.png) | 
|:--:| 
| *Figure 3* |

| ![Figure 4](https://github.com/ssp4all/stock-prediction-evaluation/blob/main/images/Stock_prediction.png) | 
|:--:| 
| *Figure 4* |

| ![Figure 5](https://github.com/ssp4all/stock-prediction-evaluation/blob/main/images/avg_score.png) | 
|:--:| 
| *Figure 5* |


## Conclusion

TODO

## Threats to validity

- ##### Error from the participants
    One of the crucial feedback that we wanted was the ranking of the matrics concerning its weightage. We stated in the survey form to choose the option of how users feel about this metric while performing experiments. But some participants ranked all of them with the same number. This can significantly hurt the mean of feedback we received. This changes the overall ranking than what we got previously. Anyways, we can not get a significant result from only 5 rankings and all the means are very close to each other. Future studies on this subject need to take into consideration that users can make errors and to "beta" test their forms before sending out to the participants, so they can find areas that people might misunderstand.

- ##### Fedback from the user
    We could have asked the user who experimented on how we could improve the feedback process or more in detail like what was the most difficult thing use faced or what did they like more.

- ##### Comparision
    To compare the product we have developed we decided to go with two popular websites available in the market which are Wallet Investor, AIStockFinder. As there was no in-depth research behind both options hence, there may be changes the better comparable product might be available in the market.
        
- ##### Bias
    There are chances that for some users, the "Ease of use" starts from a medium, I mean the user has a mindset of giving the lowest value of medium and highest being high. So, for such a kind of user, we should have a normalized rating for each user.
