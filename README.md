# MHTML_Cleanup — Premise
To use Python scripts to extract the names of the categories and subcategories from the McMaster-Carr website.

_As a disclaimer, I'm a bit out of touch with Python development, so some of the names and implementations probably look more appropriate for JavaScript._

## Why I went this route
I wanted to get a list of all categories and subcategories of products on the McMaster-Carr website. Unfortunately, I couldn't find an easy way of doing that.
I tried using some basic web-scraping techniques, but found that McMaster's site live-loads data, which means that it can't be scraped without using a 
headless browser (at least, that's how it seems with my current knowledge). 

However, I discovered that if I were to save the main page as an .mhtml file, all the populated text was there. This was not the end of the problem. The mhtml file was messy,
and for some reason, there were line breaks in weird places. Enter Python. I'm attempting to use Python to fix the weird line breaks and extract the information I need.

## Install Info and Dependencies

Currently using Python 3.9.1. 

Currently, the main file is `customizedScrape.py`. 
