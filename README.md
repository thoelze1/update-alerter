# Tracking Web Content
I use Python to compare recent and stored snapshots of websites to determine when content at a URL has changed.

## Storing Snapshots
A text file track changes for each URL. Content at a URL is saved as an MD5 hash and updated regulary. Each new hash is compared to the existing hash. For each omparison, the corresponding textfile is timestamped to reflect change.

## Dangers
Saving files without sanitizing them can be dangerous.
