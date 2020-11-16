import pandas as pd
import matplotlib.pyplot as plt

def histogramForRecommendation(sheet, website, familarity):
    sheetNotFamiliar = sheet.loc[
        sheet["How familiar are you with the stock market?"] == familarity
    ]
    recommendStockGuide = sheetNotFamiliar[
        website + " How likely are you to recommend this application to friends?"
    ]
    recommendStockGuide.sort_values()
    meanRecommendStockGuide = recommendStockGuide.mean()
    sdRecommendStockGuide = recommendStockGuide.std()
    plt.hist(recommendStockGuide)
    plt.suptitle(
        "Website: "
        + website
        + "\n. People who said '"
        + familarity
        + "'.\nTotal responses = "
        + str(len(recommendStockGuide))
        + "."
    )
    plt.xticks([1, 2, 3, 4, 5])
    plt.yticks([x for x in range(11)])
    plt.show()
    return recommendStockGuide, meanRecommendStockGuide, sdRecommendStockGuide

columns = [
    "Timestamp",
    "Your key",
    "How familiar are you with the stock market?",
    "aiStockFinder Ease of Use",
    "aiStockFinder Do you think the stock data provided was accurate?",
    "aiStockFinder Were you statisfied with the range of stocks provided?",
    "aiStockFinder How likely are you to recommend this application to friends?",
    "walletInvestor Ease of Use",
    "walletInvestor Do you think the stock data provided was accurate?",
    "walletInvestor Were you statisfied with the range of stocks provided?",
    "walletInvestor How likely are you to recommend this application to friends?",
    "stockGuide Ease of Use",
    "stockGuide Do you think the stock data provided was accurate?",
    "stockGuide Were you statisfied with the range of stocks provided?",
    "stockGuide How likely are you to recommend this application to friends?",
]

sheet = pd.read_csv("sheet.csv", usecols=columns)

# histogram for stock guide who said "I am familiar but have never used stocktrading platforms"
website = "stockGuide"
familarity = "I am familiar but have never used stock trading platforms"
histogramForRecommendation(sheet, website, familarity)

# histogram for stock guide who said "Not familiar at all"
website = "stockGuide"
familarity = "Not familiar at all"
histogramForRecommendation(sheet, website, familarity)

# histogram for ai stock finder who said "I am familiar but have never used stock trading platforms"
website = "aiStockFinder"
familarity = "I am familiar but have never used stock trading platforms"
histogramForRecommendation(sheet, website, familarity)

# histogram for ai stock finder who said "Not familiar at all"
website = "aiStockFinder"
familarity = "Not familiar at all"
histogramForRecommendation(sheet, website, familarity)

# histogram for walletInvestor who said "I am familiar but have never used stock trading platforms"
website = "walletInvestor"
familarity = "I am familiar but have never used stock trading platforms"
histogramForRecommendation(sheet, website, familarity)

# histogram for walletInvestor who said "Not familiar at all"
website = "walletInvestor"
familarity = "Not familiar at all"
histogramForRecommendation(sheet, website, familarity)
