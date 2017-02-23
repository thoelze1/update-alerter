# Tracking Web Content
I use Python to compare recent and stored snapshots of websites to determine when content at a URL has changed.

## Storing Snapshots
A text file (URL log) tracks changes for each URL. Content at a URL is saved as an MD5 hash and updated regulary. Each new hash is compared to the existing hash. For each comparison, the corresponding log is timestamped and change is noted when present.

## URL Logs
Each URL log contains a series of timestamps followed by the previous MD5 hash. Below is a log for (a mirror of my website)[http://bingweb.binghamton.edu/~thoelze1/].

<p align="center">
  <img src="log.jpg">
</p>

## Dangers
Saving files without sanitizing them can be dangerous.
