# stock_profit_calculator
This simple Python script returns the total profit based on company ticker, the date stock shares were bought, and the number of shares purchased on date.

# Disclaimer:
This program does not guarantee any returns in any of its products or services. Investment in markets is subject to market risk. Hence, this program is not liable for any losses in any case. All trading strategies are used at your own risk.

# Install Python 3.9.5
This program requires Python 3 to execute correctly. Downloading the latest version (3.9.5) is highly recommended. This process is not automated or included in the program, it must be completed individually by user. Here is a great website that provides instructions on how to install Python regardless of operating system: https://realpython.com/installing-python/.

# Initial Setup of Program
Download the program by selecting the green button 'Code' and selecting 'Download ZIP' from the dropdown menu. After downloading is completed, unzip the program. The unzip location does not matter, this is truly up to the user. After unzipping, the user will run one of the two scripts based on their operating system. 
For Windows users, please navigate to the program directory and double click the windows_setup file or in the Command Prompt, navigate to the program's unzipped directory and type "windows_setup.bat" without the quotation marks. You will see another Command Prompt briefly appear and disappear.
For Linux/Unix users, the process is fairly similar. After navigating to the program directory, please click linux_unix_setup or from the Command Line, navigate to the unzipped program directory and type "./linux_unix_setup.sh" without including the quotation marks. 
These 2 files install automatically the packages required to run this program and that is all. No funny business, just some quick automation.

# Running the Program
For Windows users, it is recommended to use either the Command Prompt or an appropriate IDE or Integrated Development Environment for Python like PyCharm. 
From the Command Prompt, navigate to the program directory. To run the program, type "python3 stock_return.py" without the quotation marks.
For Linux/Unix users, it is recommended to use the Command Line. Navigate to the program directory and run the program by typing "./python3 stock_return.py" without quotation marks.
After running the program, enter in the company ticker, the year the stock was purchased, the month the stock was purchased, the day the stock was purchased, and the number of shares purchased on that date. At anytime, the program can be exited by typing "exit". 

# Results
The output will be the gross profit. This is calculated by retrieving the average of the high and low stock share price of the company for the date entered then multiplying the this value by the number of shares. This is the user stock share price. Then the most recent stock share price is retrieved by calculating the average of the most recent high and low stock share price. This number is then also multiplied by number of shares to get the most recent stock share prie. Lastly, the user stock share price is subtracted from the most rcent stock share price to get the gross profit. 
