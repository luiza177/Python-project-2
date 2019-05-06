import NYTimes_parser

# cd Desktop/"Python project 2"
# python NYTP_Main.py

while True:
	user = input("Enter number of titles to analyse, or type 'all': ")
	if not user.isdigit():
		user = user.lower()
		if user == 'all':
			num = -1
			break
	try:
		num = int(user)
		if num >= 1:
			break
	except ValueError:
		print("Must enter a number or 'all'")		

try:
	# file = NYTimes_parser.get_XML("http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml")
	file = NYTimes_parser.get_local_XML("NYT_front_page.xml")
	titles = NYTimes_parser.get_titles(file, num)
	NYTimes_parser.word_analysis(titles)
except NYTimes_parser.NotFound as e:
	print("RSS feed not found!")
	print(e.args[0])
except NYTimes_parser.UnexpectedError as e:
	print('An unexpected error occured!')
	print(e.args[0])
except FileNotFoundError as e:
	print("File not found!")
	print(e.args[0])