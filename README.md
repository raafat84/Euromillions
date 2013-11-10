Euromillions
============

Open source script for Python which connects to a [Euromillions lottery public Web Service](http://resultsservice.lottery.ie/ResultsService.asmx?WSDL) and informs to a list of people if their ticket is a winner one.

Setup
=====

* Install [Suds](https://fedorahosted.org/suds/) to handle Web Services easily.
* Get an Gmail account (Why don't you have it already?!).
* Get this script.
* Set numbers and stars to play.
* Set the email list to notify potential prizes.
* Run it!.

Usage
=====
```python
python Euromillions.py -u <GmailAccount> -p <GmailPassword>
Or
python Euromillions.py --user <GmailAccount> --password <GmailPassword>
```
