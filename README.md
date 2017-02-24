# Tracking Web Content
Compare recent and stored snapshots of websites to determine when content at a URL has changed. Start tracking by cloning the repository, specifying URLs, and executing the script.

    git clone https://www.github.com/thoelze1/web-content-tracker.git
    vi web-content-tracker/data/urls.txt
    python track-urls.py &

## Storing Snapshots
A text file (URL log) tracks changes for each URL. Content at a URL is saved as an MD5 hash and updated regulary. Each new hash is compared to the existing hash. For each comparison, the corresponding log is timestamped and change is noted when present.

## URL Logs
Each URL log contains a series of timestamps followed by the previous MD5 hash. Below is a log for [a mirror of my website](http://bingweb.binghamton.edu/~thoelze1/).

<p align="center">
  <img src="log.jpg" width="420px" height="auto"/>
</p>

## Dangers
Saving files without sanitizing them can be dangerous.
