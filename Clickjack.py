import os
import sys
import webbrowser
import pyfiglet
import termcolor

# Starting Banner
ascii_banner = pyfiglet.Figlet(font='slant')
print(termcolor.colored(ascii_banner.renderText('ClickJack Tester'), 'green'))

# Usage
if len(sys.argv) < 2:
    print("Invalid amount of Arguments")
    print("Syntax: python Clickjack.py <url>")
    exit(0)

# To get url
url = sys.argv[1]

# HTML code to load in iframe
html = """<html>
<head>
<title>Clickjack Test Page</title>
</head>
<body>
<h1> <center> Clickjack Test Results </center> </h1>
<h2> If the page is loaded below then the site is <em style='color:red;'> VULNERABLE </em> <br><br>
     If <mark> not </mark> then it is protected with X-frame options or Content Security Policy </h2>
<iframe src="%s" width="1200" height="500">
</iframe>
</body>
</html>""" %url

# To create HTML file in user local directory
clk = os.path.abspath("clickjack.html")

# To write HTML code into the file
with open(clk,'w') as c:
    c.write(html)

# Local URL creation
openfile = "file://" + clk

# To open the file in local directory
webbrowser.open(openfile)

print("\n [+] Test Completed!!!")