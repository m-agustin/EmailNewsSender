# CovidNewsEmailer

**CovidNewsEmailer** is an automated script programmed with python3 containing _send_email.py_ and _covid_news.py_.

* send_email.py: automated script that sends messages from an email to another email.
    * It requires the user to input the receiver's email, and the sender's email and passpord

* covid_news.py: automated script that incorporates the module beautifulsoup to webscrape the website [Cp24](https://www.cp24.com/news).


*To use:*
* Download the repository
* On your terminal, type the code below:
    `python covid_news.py`
Script will webscrape the latest local covid news in [Cp24](https://www.cp24.com/news) and send the results to the receiver's email.


# Improvements that can be done:
- [ ] Have all the webscraped results from covid_news.py be sent in one email instead of individual messages.