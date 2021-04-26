# CovidNewsEmailer

**CovidNewsEmailer** is an automated script that web scrapes a site and automatically emails the results to the receiver's email address.

## Contains:
* **send_email.py**: automated script that sends messages from an email to another email.
    * It requires the user to input the receiver's email, and the sender's email and passpord
* **covid_news.py**: automated script that incorporates the module beautifulsoup to web scrape the website [Cp24](https://www.cp24.com/news).


## To use:
* Download the repository
* On your terminal, type the code: `python covid_news.py`
* Script will webscrape the latest local covid news in [Cp24](https://www.cp24.com/news) and send the results to the receiver's email.

![email example](https://user-images.githubusercontent.com/78524572/116009095-93298e00-a5e5-11eb-8066-a80b374147b0.png)


# Improvements that can be done:
- [ ] Have all the webscraped results from covid_news.py be sent in one email instead of individual messages.
