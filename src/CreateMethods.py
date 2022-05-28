from YahooFinanceClass import *
from YahooFinanceMethods import *
from HelperFunctions import *
import time

def createDataDF_AllTickers_AllData():
    wait = getWaitTime()
    
    tickers    = scrapeAllASXTickers()
    numTickers = len(tickers)

    passedTickers = []
    failedTickers = []

    count      = 1
    numSuccess = 0
    numFail    = 0

    begin = time.time()

    for ticker in tickers:
        try:
            passedTickers.append(allData(ticker))
            print(f'Appended: {ticker}')
            print(f'{count}/{numTickers} \n')
            numSuccess += 1
            count += 1
            time.sleep(wait)
        except Exception as e:
            failedTickers.append(ticker)
            print(f'Could not append: {ticker}')
            print(e)
            print(f'{count}/{numTickers} \n')
            numFail += 1
            count += 1
            time.sleep(wait)
            continue

    if numFail > 0:
        for ticker in failedTickers:
            try:
                passedTickers.append(allData(ticker))
                print(f'Appended: {ticker}')
                numSuccess += 1
                time.sleep(wait)
            except Exception as e:
                print(f'Could not append: {ticker}')
                print(e)
                time.sleep(wait)
                continue

    df = pd.DataFrame([vars(ticker) for ticker in passedTickers])
    saveDFtoExcel(df, 'all_stock_data')

    end = time.time()
    timeTaken = end - begin

    print('Done!!!')
    print(f'Number successfully appended: {numSuccess}')
    if numFail > 0:
        print(f'Check: {failedTickers}')
    print(f"Total runtime of the program is {round(timeTaken, 0)} s")

def createDataDF_AllTickers_ValueData():
    wait = getWaitTime()

    tickers    = scrapeAllASXTickers()
    numTickers = len(tickers)

    passedTickers = []
    failedTickers = []

    count      = 1
    numSuccess = 0
    numFail    = 0

    begin = time.time()

    for ticker in tickers:
        try:
            passedTickers.append(valueData(ticker))
            print(f'Appended: {ticker}')
            print(f'{count}/{numTickers} \n')
            numSuccess += 1
            count += 1
            time.sleep(wait)
        except Exception as e:
            failedTickers.append(ticker)
            print(f'Could not append: {ticker}')
            print(e)
            print(f'{count}/{numTickers} \n')
            numFail += 1
            count += 1
            time.sleep(wait)
            continue

    if numFail > 0:
        for ticker in failedTickers:
            try:
                passedTickers.append(valueData(ticker))
                print(f'Appended: {ticker}')
                numSuccess += 1
                time.sleep(wait)
            except Exception as e:
                print(f'Could not append: {ticker}')
                print(e)
                time.sleep(wait)
                continue

    df = pd.DataFrame([vars(ticker) for ticker in passedTickers])
    saveDFtoExcel(df, 'all_value_data')

    end = time.time()
    timeTaken = end - begin

    print('Done!!!')
    print(f'Number successfully appended: {numSuccess}')
    if numFail > 0:
        print(f'Check: {failedTickers}')
    print(f"Total runtime of the program is {round(timeTaken, 0)} s")

def createDataDF_WatchlistTickers_AllData():
    wait = getWaitTime()

    tickers    = readInWatchlistStocksFromExcel()
    numTickers = len(tickers)
    
    passedTickers = []
    failedTickers = []

    count      = 1
    numSuccess = 0
    numFail    = 0

    begin = time.time()

    for ticker in tickers:
        try:
            passedTickers.append(allData(ticker))
            print(f'Appended: {ticker}')
            print(f'{count}/{numTickers} \n')
            numSuccess += 1
            count += 1
            time.sleep(wait)
        except Exception as e:
            failedTickers.append(ticker)
            print(f'Could not append: {ticker}')
            print(e)
            print(f'{count}/{numTickers} \n')
            numFail += 1
            count += 1
            time.sleep(wait)
            continue

    if numFail > 0:
        for ticker in failedTickers:
            try:
                passedTickers.append(allData(ticker))
                print(f'Appended: {ticker}')
                numSuccess += 1
                time.sleep(wait)
            except Exception as e:
                print(f'Could not append: {ticker}')
                print(e)
                time.sleep(wait)
                continue

    df = pd.DataFrame([vars(ticker) for ticker in passedTickers])
    saveDFtoExcel(df, 'all_watchlist_data')

    end = time.time()
    timeTaken = end - begin

    print('Done!!!')
    print(f'Number successfully appended: {numSuccess}')
    if numFail > 0:
        print(f'Check: {failedTickers}')
    print(f"Total runtime of the program is {round(timeTaken, 0)} s")

def createDataDF_WatchlistTickers_ValueData():
    wait = getWaitTime()

    tickers    = readInWatchlistStocksFromExcel()
    numTickers = len(tickers)
    
    passedTickers = []
    failedTickers = []

    count      = 1
    numSuccess = 0
    numFail    = 0

    begin = time.time()

    for ticker in tickers:
        try:
            passedTickers.append(valueData(ticker))
            print(f'Appended: {ticker}')
            print(f'{count}/{numTickers} \n')
            numSuccess += 1
            count += 1
            time.sleep(wait)
        except Exception as e:
            failedTickers.append(ticker)
            print(f'Could not append: {ticker}')
            print(e)
            print(f'{count}/{numTickers} \n')
            numFail += 1
            count += 1
            time.sleep(wait)
            continue
    if numFail > 0:
        for ticker in failedTickers:
            try:
                passedTickers.append(valueData(ticker))
                print(f'Appended: {ticker}')
                numSuccess += 1
                time.sleep(wait)
            except Exception as e:
                print(f'Could not append: {ticker}')
                print(e)
                time.sleep(wait)
                continue

    df = pd.DataFrame([vars(ticker) for ticker in passedTickers])
    saveDFtoExcel(df, 'value_watchlist_data')

    end = time.time()
    timeTaken = end - begin

    print('Done!!!')
    print(f'Number successfully appended: {numSuccess}')
    if numFail > 0:
        print(f'Check: {failedTickers}')
    print(f"Total runtime of the program is {round(timeTaken, 0)} s")
