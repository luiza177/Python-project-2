import NYTimes_parser

# cd Desktop/"Python project 2"
# python NYTP_Main.py

while True:
	user = input("Enter number of titles to analyse: ")
	try:
		num = int(user)
		if num >= 1:
			break
	except ValueError:
		print("Must enter a number.")		

try:
	file = NYTimes_parser.get_XML("http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml")
	titles = NYTimes_parser.get_titles(file, num)
	NYTimes_parser.word_analysis(titles)
except NYTimes_parser.NotFound as e:
	print("RSS feed not found!")
	print(e.args[0])
except NYTimes_parser.UnexpectedError as e:
	print('An unexpected error occured!')
	print(e.args[0])