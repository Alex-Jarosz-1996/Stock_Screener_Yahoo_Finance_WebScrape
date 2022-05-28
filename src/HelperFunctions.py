from joblib import PrintTime
import pandas as pd
import os
import shutil
import random

from requests import delete
from YahooFinanceMethods import *

def getWaitTime():
    return random.randint(9, 15)

def saveDFtoExcel(df, excelFileName):
    removeSingleExcelFile(excelFileName)
    currentPath = str(os.path.abspath(os.getcwd()))
    desiredPath = currentPath.replace('python_run_scripts', 'ASX')
    df.to_excel(f'{desiredPath}/{excelFileName}.xlsx')
    removeCache()

def removeSingleExcelFile(excelFileName): 
    currentPath = str(os.path.abspath(os.getcwd()))
    desiredPath = currentPath.replace('python_run_scripts', 'ASX')
    filePath = f'{desiredPath}\{excelFileName}.xlsx'
    if os.path.exists(filePath):
        os.remove(filePath)
        print(f'Deleted old {excelFileName}.')
    
def removeCache():
    currentPath = str(os.path.abspath(os.getcwd()))
    desiredPath = currentPath.replace('python_run_scripts', 'src')
    cachePath = f'{desiredPath}\__pycache__'
    shutil.rmtree(cachePath)
    print('Removed Cache.')

def scrapeAllASXTickers():
    url = 'https://www.fnarena.com/index/ALL-ORDS/'
    df = pd.read_html(url)
    return df[0].SYMBOL

def readInWatchlistStocksFromExcel():
    currentPath = str(os.path.abspath(os.getcwd()))
    desiredPath = currentPath.replace('python_run_scripts', 'ASX')
    df = pd.read_excel(f'{desiredPath}\watchlist.xlsx')
    return df['Desired Stocks'].tolist()

def getAllStockDataFiles():
    currentPath = str(os.path.abspath(os.getcwd()))
    desiredPath = currentPath.replace('python_run_scripts', 'ASX')
    return os.listdir(desiredPath)

def deleteAllStockDataFiles():
    currentPath = str(os.path.abspath(os.getcwd()))
    desiredPath = currentPath.replace('python_run_scripts', 'ASX')    
    
    files = getAllStockDataFiles()
    
    for f in files:
        if f != 'watchlist.xlsx':
            os.remove(f'{desiredPath}\{f}')
            print(f'Deleted: {f}')
    
    removeCache()

