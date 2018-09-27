## Fortify
*Requires*
* Python 2.7.10
* pip 9.0.1

*Setup*
Install Python
Install pip

```
pip install requests
```
```
pip install beautifulsoup4
```

*Scoring*
This code scores each review based on 3 different categories:
* The use of specific words with point values
* The ratio of positive words to length of the review
* The rating the reviewer left the dealership

The point values are as follows:
Words:
wonderful - 3
painless - 2
fantastic - 3
thank you - 5
perfect - 4
hassle free - 2
pleasure - 3
appreciate - 4
knowledgable - 3
patient - 2

Ratio:
ratio > 50 - 5
40-49 - 4
30-39 - 3
10-29 1

Rating:
0-29 - 0
30-40 - 1
41-45 - 4
46-47 - 5
48-50 - 7

*Running*
Access the directory from the command line
Run:
```
python dealerrater.py
```
