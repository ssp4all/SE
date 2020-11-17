# Welcome to the test results of Stock Prediction

Hi! We are group 12 and we are testing a [system that predicts stock prices](https://github.com/lokesh45/StockPrediction).

## Description of the source repository

TODO

## Method: Test Plan

- Go to [TestPlan](https://docs.google.com/spreadsheets/d/1rQDUvgM1uNTLeklLOQzoprsNrLaTmgU-nL8uw30S_xw/edit#gid=632817659) spreadsheet.
- Assign keys to each user.
- Record the data generated from the participant. Each participant will perform following activities.
- Analyse the project based on Ease of use, Accuracy, Cost, Range of choice.
- Compare current project with other tools available online (Wallet Investor, AIStockFinder)
- Report bugs(if found)
- Review the project on scale 1(Low) to 5(High).
- Utilize the data and analyse the feedback received from each participant.
- Generate aggregated rating for the entire project based on Ease of use, Accuracy, Cost, Range of choice.

## How to setup: from cloning to deploying on Heroku

1. Clone the [repository we are testing](https://github.com/lokesh45/StockPrediction).

You can do this by typing `git clone https://github.com/lokesh45/StockPrediction`.

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

TODO: links to scrips, repo, data and forms. Go in more depth about how we conducted our test meetings.

## Observations

TODO: Paste the screenshots and a brief factual introduction of the screenshot

## Analysis

IMPORTANT TODO

## Conclusion

TODO

## Threats to validity

TODO
