import requests
import xml.dom.minidom
import re

class NotFound(Exception):
	pass

class UnexpectedError(Exception):
	pass

""" Downloads RSS feed, but does not save to file. """
def get_XML(url):
	response = requests.get(url)
	if response.status_code == 200:
		doc = xml.dom.minidom.parseString(response.text)
		return doc
	elif response.status_code == 404:
		raise NotFound(response.text)
	else:
		raise UnexpectedError(response.text)

""" Opens local *.xml file. """
def get_local_XML(file):
	open(file, "r")
	return file.read()

""" Downloads and saves to *.xml file. """
def download_XML(url):
	response = requests.get(url)
	if response.status_code == 200:
		file = open("NYT_front_page.xml", "w")
		file.write(response.text)
		file.close()
		doc = xml.dom.minidom.parse("NYT_front_page.xml")
		return doc
	elif response.status_code == 404:
		raise NotFound(response.text)
	else:
		raise UnexpectedError(response.text)

""" Returns list of strings with all RSS titles. """
def get_titles(doc):
	titles = []
	for element in doc.getElementsByTagName("item"):
		title = element.getElementsByTagName('title')[0].firstChild.nodeValue
		titles.append(title)
	return titles

""" Returns list of strings with a specfied number of RSS titles. """
def get_titles(doc, num):
	titles = []
	counter = 0
	for element in doc.getElementsByTagName("item"):
		title = element.getElementsByTagName('title')[0].firstChild.nodeValue
		counter += 1
		titles.append(title)
		if counter == num:
			break
	return titles

""" Creates sorted list of lower-case words from title. """
def prepare_for_analysis(title):
	title_words = title.split()
	for word_id in range(len(title_words)):
		title_words[word_id] = title_words[word_id].lower()
		title_words[word_id] = re.sub(r'\W+', '', title_words[word_id]) # Removes non-alphanum
	title_words.sort()
	return title_words

""" Prints full word analysis. """
def word_analysis(title):
	for ti in title:
		print(ti)
		words = prepare_for_analysis(ti)
		text_length = len(words)
		print("Word count: {}".format(text_length))
		print()
		word_dict = {}
		for word in words: # dict creation
			count = words.count(word) # counts occurances of word in the words/title (list)
			if word not in word_dict:
				word_dict[word] = count
		for word in word_dict: # analyzes dict
			percent = round(100 * word_dict[word] / text_length, 2)
			print("Word '{0}' appears {1} times and consists of {2} percent of text".format(word, count, percent))
		print("\n")		