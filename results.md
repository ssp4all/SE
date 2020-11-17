## Method: Test Plan

1. Get around 8 to 10 participants to test three websites: [Wallet Investor](https://walletinvestor.com/), [AIStockFinder](https://www.aistockfinder.com/) and [the app we are testing](https://radiant-falls-10905.herokuapp.com).
2. Assign keys to each user.
3. Record the data generated from the participant. Each participant will perform the following activities:

1. Analyse the project based on Ease of use, Accuracy, Cost, Range of choice.

2. Compare the current project with other real-life market solutions available online (for this project, they are Wallet Investor, AIStockFinder)

3. Report bugs(if found)

4. Review the project on a scale of 1(Low) to 5(High). 4. Utilize the data and analyze the feedback received from each participant. They will be stored using this [google form](https://docs.google.com/forms/d/e/1FAIpQLSfrOcLyx1ZxUexelyc2YJZB9imcJUHoP9oH8zVcHtOkJD-VYQ/viewform). 5. Generate an aggregated rating for the entire project based on Ease of use, Accuracy, Cost, Range of choice.

## How to setup: from cloning to deploying on Heroku

1. Clone the [repository we are testing](https://github.com/lokesh45/StockPrediction). You can do this by typing `git clone https://github.com/lokesh45/StockPrediction`.

2. Change the file `Dockerfile` by replacing the last line from `CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]` to `CMD flask run --host 0.0.0.0 --port ${PORT}`.

3. Make an account on [Heroku](https://signup.heroku.com/login).

4. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).

5. Go back to the folder where the `StockPrediction` you cloned is located and open a terminal inside it.

> Optional: Install the [docker cli](https://docs.docker.com/get-docker/). Type `docker ps -a`. A list of images will show up.

6. Type `heroku login` in the terminal and it will open a browser for you to log in.

7. After logging in, type `heroku create`, followed by `heroku container:push web`. This will take a few minutes.

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

We told the participants to find stocks on each website and look at their predictions. Meetings were conducted via Zoom, timings of which were decided via communications on Slack or WhatsApp.

They were also told to stay at any website for any amount of time, till they feel they were comfortable with the website. Only after that were they advised to fill up the google form. The participants were encouraged to talk about what they are feeling.

We found most of them took around 5 to 10 minutes for the first website and then the time it took for them to test other websites decreased in a linear fashion.

In total there were 9 participants, and we have responses from 8 of them. One of them exercised their Right to Refuse.

Below you can find the responses of the 8 participants.

### We asked about their familiarity with the stock markets

|            ![Figure 1](https://github.com/ssp4all/stock-prediction-evaluation/blob/main/images/1.PNG)             |
| :---------------------------------------------------------------------------------------------------------------: |
| _Figure 1: Indicates that the candidates were kinda aware of the stock market which makes evaluation much easier_ |

### These are the feelings about AI Stock finder

| ![Figure 2](https://github.com/ssp4all/stock-prediction-evaluation/blob/main/images/2.PNG) |
| :----------------------------------------------------------------------------------------: |
|        _Figure 2: Ease of use - AI Stock finder is more like a easy-medium to use_         |

| ![Figure 3](https://github.com/ssp4all/stock-prediction-evaluation/blob/main/images/3.PNG) |
| :----------------------------------------------------------------------------------------: |
|      _Figure 3: Accuracy - More than half of the testers found application accurate_       |

| ![Figure 4](https://github.com/ssp4all/stock-prediction-evaluation/blob/main/images/4.PNG) |
| :----------------------------------------------------------------------------------------: |
|       _Figure 4: Satisfaction - The users mostly saw stocks for popular companies _        |

| ![Figure 5](https://github.com/ssp4all/stock-prediction-evaluation/blob/main/images/5.PNG) |
| :----------------------------------------------------------------------------------------: |
|          _Figure 5: Recommendation - Users likely to recommend this application_           |

From the above graph, it can be seen that testers liked the AI Stock Finder application which has an average score of 3.5.

### These are the feelings about for Wallet Investor

| ![Figure 6](https://github.com/ssp4all/stock-prediction-evaluation/blob/main/images/6.PNG) |
| :----------------------------------------------------------------------------------------: |
|       _Figure 6: Ease of use - Wallet Investor seems like a moderate in ease of use_       |

| ![Figure 7](https://github.com/ssp4all/stock-prediction-evaluation/blob/main/images/7.PNG) |
| :----------------------------------------------------------------------------------------: |
|              _Figure 7: Accuracy - More sophisatication comes with accuracy_               |

| ![Figure 8](https://github.com/ssp4all/stock-prediction-evaluation/blob/main/images/8.PNG) |
| :----------------------------------------------------------------------------------------: |
|         _Figre 8: Satisfaction - Again testers went for popular company's stocks_          |

| ![Figure 9](https://github.com/ssp4all/stock-prediction-evaluation/blob/main/images/9.PNG) |
| :----------------------------------------------------------------------------------------: |
| _Figure 9: Recommendation - Users are less likely to recommend this app over AI Stock App_ |

Wallet Investor has an average score of 3.5.

From the above ratings of market solutions: **AI Stock Finder** and **Wallet Investor**, you can see that all ratings are in the range of 3-5 indicating no critical reviews. This is expected as these are market solutions specifically made to cater to the needs of the user.

### These are the feelings about for Stock Predictor

| ![Figure 10](https://github.com/ssp4all/stock-prediction-evaluation/blob/main/images/10.PNG) |
| :------------------------------------------------------------------------------------------: |
|    _Figure 10: Ease of use - More than half of tester feel this app has less ease of use_    |

| ![Figure 11](https://github.com/ssp4all/stock-prediction-evaluation/blob/main/images/11.PNG) |
| :------------------------------------------------------------------------------------------: |
|                          _Figure 11: Accuracy - Accurate enough..._                          |

| ![Figure 12](https://github.com/ssp4all/stock-prediction-evaluation/blob/main/images/12.PNG) |
| :------------------------------------------------------------------------------------------: |
|              _Figure 12: Satisfaction - Again testers chose popular companies_               |

|  ![Figure 13](https://github.com/ssp4all/stock-prediction-evaluation/blob/main/images/13.PNG)  |
| :--------------------------------------------------------------------------------------------: |
| _Figure 13: Recommendation - Less likely to get recommendation over existing stock predictors_ |

Stock predictor developed by received avg score of 3 and a median of 4 with one score of 1 and a total 4 scores of 4.

The ratings for Stock Predictor show mixed reviews. 3 ratings are in the range of 1-2, which comprises of 37.5% of the experiment reviewer pool while the rest 62.5% were inclined to use this application with a rating bracket of 4-5. This can partly be attributed to the ease of use of our platform. Users are less inclined to use a platform if they have difficulty navigating the platform intuitively. As we can see from the Ease of use Pie chart for Stock Predictor, only 37.5% found it easy to use while it 50% for AI Stock finder. This implies that we still have more scope in improving our platform's frontend and make it more user friendly.

## Analysis

### Correlation between parameters

Looking at the responses of the google form that were used during the experiment with lab rats, and performing some analysis, we were able to calculate the correlation between "How likely an app would be recommended to a friend ?" and 3 other parameters.

- Parameter 1: "Ease of Use"
- Parameter 2: "Do you think the stock data provided was accurate?"
- Parameter 3: "Were you satisfied with the range of stocks provided?"
- Result Parameter: "How likely are you to recommend this application to friends?"

According to the findings (as you can see in the table below):

| ![Figure 14](https://github.com/ssp4all/stock-prediction-evaluation/blob/main/images/14.PNG) |
| :------------------------------------------------------------------------------------------: |
|                      _Figure 14 : Correlation matrix for aiStockFinder_                      |

For aiStockFinder, we can see that there is a very low positive correlation between "Satisfaction" and "Recommending". So, we cannot give a statement without having enough data.

| ![Figure 15](https://github.com/ssp4all/stock-prediction-evaluation/blob/main/images/15.PNG) |
| :------------------------------------------------------------------------------------------: |
|                     _Figure 15 : Correlation matrix for walletInvestor_                      |

For walletInvestor, we can see that there is a significant correlation between "Ease of Use" and "Recommending". So, there is a good chance that a person recommends walletInvestor because they find it easy to use.

| ![Figure 16](https://github.com/ssp4all/stock-prediction-evaluation/blob/main/images/16.PNG) |
| :------------------------------------------------------------------------------------------: |
|                       _Figure 16 : Correlation matrix for StockGuide_                        |

In our case - StockGuide, we see a positive correlation between "Satisfaction" and "Recommending". We would obviously need more data to make a stronger statement.

Nevertheless, we would be able to assess the contributing factors towards the success of this application using this correlation study.

### Analyzing the Recommendation Ratings

After using all 3 platforms for predicting stock trends, we asked the users how likely are they to recommend each of the apps. This metric helps us understand the overall perception of the user. Following are the results:

| ![Figure 17](https://github.com/ssp4all/stock-prediction-evaluation/blob/main/images/avg_score_rating.png) |
| :--------------------------------------------------------------------------------------------------------: |
|                    _Figure 17: Comparison of an average rating between the 3 platforms_                    |

Seems like a tie between AI Stock finder and Wallet investor with an average score of 3.5 and Stock predictor has a score of 3.25.

Although our platform has mixed reviews, the average rating bar chart shown above tells otherwise. Our application only falls behind by a little in comparison with the market solutions.

### Analyzing if prior knowledge of stock market affected the ratings

If we look at [Figure 1](https://github.com/ssp4all/stock-prediction-evaluation/blob/main/results.md#we-asked-about-their-familiarity-with-the-stock-markets), we can see that no one had done stock trading before, but 75% of the people knew atleast something about the stock market before they were tested. 25% of the people were not familiar at all. We will now look at these two groups and see how they rated the different systems and if there was any difference.

   #### 1. AIStockFinder

| ![Figure 18](https://github.com/ssp4all/stock-prediction-evaluation/blob/main/images/18.png) |
| :------------------------------------------------------------------------------------------: |
|           _Figure 18: AIStockFinder Ratings of people familiar with stock market_            |

| ![Figure 19](https://github.com/ssp4all/stock-prediction-evaluation/blob/main/images/19.png) |
| :------------------------------------------------------------------------------------------: |
|      _Figure 19: AIStockFinder Ratings of people not familiar with stock market at all_      |

   We see that people who actually are familiar with the stock market rate the product more highly than the others.

   Mean rating with people who are **familiar** with stock market: 3.833

   Mean rating with people who are **not familiar** with the stock market: 3

   #### 2. WalletInvestor

| ![Figure 20](https://github.com/ssp4all/stock-prediction-evaluation/blob/main/images/20.png) |
| :------------------------------------------------------------------------------------------: |
|           _Figure 20: WalletInvestor Ratings of people familiar with stock market_           |

| ![Figure 21](https://github.com/ssp4all/stock-prediction-evaluation/blob/main/images/21.png) |
| :------------------------------------------------------------------------------------------: |
|     _Figure 21: WalletInvestor Ratings of people not familiar with stock market at all_      |

   Again, we see that people who actually are familiar with the stock market rate the product more highly than the others.

   Mean rating with people who are **familiar** with stock market: 3.833

   Mean rating with people who are **not familiar** with the stock market: 3

   #### 3. StockGuide

| ![Figure 22](https://github.com/ssp4all/stock-prediction-evaluation/blob/main/images/22.png) |
| :------------------------------------------------------------------------------------------: |
|             _Figure 22: StockGuide Ratings of people familiar with stock market_             |

| ![Figure 23](https://github.com/ssp4all/stock-prediction-evaluation/blob/main/images/23.png) |
| :------------------------------------------------------------------------------------------: |
|       _Figure 23: StockGuide Ratings of people not familiar with stock market at all_        |

   Again, we see that people who actually are familiar with the stock market rate the product more highly than the others.

   Mean rating with people who are **familiar** with stock market: 3.833

   Mean rating with people who are **not familiar** with the stock market: 1.5

Here, in all of the 3 cases, we see that people who have some familiarity with the stock market have rated all the products more highly than people who do not. This is an interesting result, it shows that people rate higher when they are more familiar. Also, the more interesting result is that the mean rating for the "people who are familiar" is exactly the same across all the 3 systems, but the mean rating for "people who are not familiar" is not the same for the native solution (StockGuide) vs the market solutions. Infact, the mean of the native solution is _half_ the mean rating of the market solution, among the non-familiar group. This shows that such people looked more at the UI elements than they looked at the predictions that the native solution offered.

## Conclusion

The figures in the observation section for both market solutions confirm that most of the users were aware of the stock market but didn’t have in-depth knowledge and because of this, almost no one found the applications difficult to use. Given the small amount of time, we can’t actually trust the responses on systems accuracy but obviously a general idea of stocks and news gives a person confidence to judge a company’s stock. Since a lot of users found it easy to play around with different stocks, we can say that the system had a wide variety of features and covered a lot of grounds.

In the case of our system, the numbers and charts show that there is room for improvement in our system - StockGuide and especially if we also plan to target novice stock enthusiasts because we saw that such people were not willing to recommend our system. Even then, the effectiveness of the system has to commended as the people who are familiar with the stock market, rated the system as high as they rated the market solutions.

## Threats to validity

### Error from the participants

One of the crucial feedback that we wanted was the ranking of the matrics concerning its weightage. We stated in the survey form to choose the option of how users feel about this metric while performing experiments. But some participants ranked all of them with the same number. This can significantly hurt the mean of feedback we received. This changes the overall ranking than what we got previously. Anyways, we can not get a significant result from only 5 rankings and all the means are very close to each other. Future studies on this subject need to take into consideration that users can make errors and to "beta" test their forms before sending out to the participants, so they can find areas that people might misunderstand.

### Feedback from the user

We could have asked the user who experimented on how we could improve the feedback process or more in detail like what was the most difficult thing use faced or what did they like more.

### Comparision

To compare the product we have developed we decided to go with two popular websites available in the market which are Wallet Investor, AIStockFinder. As there was no in-depth research behind both options hence, there may be changes the better comparable product might be available in the market.



### Bias

There are chances that for some users, the "Ease of use" starts from a medium, I mean the user has a mindset of giving the lowest value of medium and highest being high. So, for such a kind of user, we should have a normalized rating for each user.



### The side information offered by the market solutions

As soon as you a market solution, it has a lot of information besides stock market, for example all the stocks that are in green or red today. This can be disturbing for the poeple who are overwhelmed by the "on the market" solution, or underwhelmed when they do not find the same information when they test our native solution. These elements are especially important for the users who are not familiar witht the stock market.

### Lack of information about the stock market

A question in our form about how people feel about the predictions, and obviously as no one can predict the future, such a question was not actually aimed at that. We wanted to know if people feel confident about using our product and that was the purpose of the question. But we saw interesting observations while testing. People used solid "bull" stocks like Amazon and Apple to gauge if the system was in fact predicting correctly. This showed that people who knew even a bit about the stock market were able to find some way to verify the predictions. On the other hand, a lack of such knowledge seriously impedes one's ability to answer our questions with a certainty that is useful to us. They may end up rating the UI and side-information more than they rate the accuracy of the predictions.
