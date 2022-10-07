First, you need to install python. This [link](https://www.geeksforgeeks.org/how-to-install-python-on-windows/ "link") explains well how to do it.

2. Install pip (program for install packages):
type this in the terminal `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
then type this `python get-pip.py`

3. Install all the requirements for the program:
type this in the terminal `pip install requirements.txt`

4. Run the program on the terminal
type this in the terminal `py instagram_scraper.py`

You will get two messages:
![example](github/image.png)

Answer the respective data

Then, the terminal will prompt another message:
![example](github/image.png)

Paste the username of the account you want to scrape, and press enter.

The program will be scraping the user data, after that, will scrape information from the accounts that the user are following. The terminal will be prompt each followed account.

Note: instagram only allow to scrape 300 accounts (instagram policies), then you will need to wait 30 minutes aproximately, after that the program will continue automatically.
![example](github/image.png)
Sometimes you will get an error, this is because instagram suspects that you've been hacked, and you have to open instagram manually and fix it.

After the program runs, you will have the file .csv in your folder