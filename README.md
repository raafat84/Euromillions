Euromillions
============

Open source script for Python which connects to a [Euromillions lottery public Web Service](http://resultsservice.lottery.ie/ResultsService.asmx?WSDL) and informs to a list of people if their ticket is a winner one.

Setup
=====

* Install [Suds](https://fedorahosted.org/suds/) to handle Web Services easily.
* Get a Gmail account (Why don't you have it already?!).
* Get this project files.
* Create a database with [SQLite3] (http://www.sqlite.org/), named euromillions.db, in the lib directory and create a new table on it named draws as shown below:
```
~/euromillions/lib $ sqlite3 euromillions.db
```
```
sqlite> CREATE TABLE draws (_id INTEGER PRIMARY KEY, date DATETIME, numbers VARCHAR(14), stars VARCHAR(5), prize REAL);
```
* In Euromillions.py, set numbers and stars to play.
* Set the email list too to notify potential prizes.
* Run it!.

Usage
=====
```python
python Euromillions.py -u <GmailAccount> -p <GmailPassword>
Or
python Euromillions.py --user <GmailAccount> --password <GmailPassword>
```
