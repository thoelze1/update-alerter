# Track Website Changes with SMS
Compare current and stored snapshots of websites to determine when content at a URL has changed. Get a text message the moment a web page changes!

## How to Use
Clone the repository and specify URLs to track (data/urls.txt). You'll need a Twilio API key and a Twilio phone number to send texts. Add your Twilio details and your personal phone number to config.py. Now you can run the script!

    git clone https://www.github.com/thoelze1/web-content-tracker.git
    nano web-content-tracker/data/urls.txt
    nano web-content-tracker/config.py
    python track-urls.py &

## How to Download Dependencies 

Download Python and pip as described [here](http://thelazylog.com/install-python-as-local-user-on-linux/). Then use pip to install Flask and the Twilio library for Python.

    pip install Flask
    pip install twilio

## Input URLs
The script expects each line of data/urls.txt to contain exactly one URL and nothing else.

## Storing Snapshots
A text file (URL log) tracks changes for each URL. Content at a URL is saved as an MD5 hash and updated regulary. Each new hash is compared to the existing hash. For each comparison, the corresponding log is timestamped and change is noted when present.

## URL Logs
Each URL log contains a series of timestamps followed by the previous MD5 hash. Below is a log for [a mirror of my website](http://bingweb.binghamton.edu/~thoelze1/).

<p align="center">
  <img src="log.jpg" width="420px" height="auto"/>
</p>

## Dangers
Saving files without sanitizing them can be dangerous.
