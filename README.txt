Background:
- The purpose of this project is to allow a user to collect data of 500 ASX companies for analysis.
- All scripts are ran in the python_run_scripts folder
- Approximate run times are as follows:
    - All data all data         : 2.5 - 3 hrs.
    - All data value data       : 2 - 2.5 hrs.
    - Watchlist data all data   : Dependent on number of tickers specified in the watchlist excel file.
    - Watchlist data value data : Dependent on number of tickers specified in the watchlist excel file.
- NOTE: Multithreading has not been utilsed for this project since the Yahoo Finance website throttles requests. Waiting
times have been deliberately inserted within the code to account for this.

How to run:
- Navigate to the 'program_run_scripts' folder of this project
- Select:
    - All_Tickers_All_Data         : To get all Data parameters for all ASX stocks
    - All_Tickers_Value_Data       : To get only the value parameters for all ASX stocks
    - Delete_All_Stock_Data_Files  : To delete all Stock data fields (NOTE: this does not delete the 'Watchlist' file)
    - Watchlist_Tickers_All_Data   : To get all Data parameters for your selected stocks 
    - Watchlist_Tickers_Value_Data : To get only the value parameters for your selected stocks
- When running either All_Tickers_All_Data, All_Tickers_Value_Data, Watchlist_Tickers_All_Data or Watchlist_Tickers_Value_Data, 
the program outputs a tally of how many stocks has been appended out of how many total stocks to append (ex: 25/500)

How to create your custom Watchlist:
- Navigate to the 'ASX' folder of this project
- Open the 'watchlist' excel file
- Enter all stocks you are interested in (vertically) in column 'A'.




