# -*- coding: utf-8 -*-

import os
import requests
import json

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
print BASE_DIR
EMOTICONS_DIR = os.path.join(BASE_DIR, 'emoticons')


def download_emoticon(url, file_name):
	r = requests.get(url)
	with open(file_name, 'wb') as fd:
		for chunk in r.iter_content():
			fd.write(chunk)


def load_data(json_file):
	with file(json_file) as f:
		return json.load(f)


if __name__ == '__main__':
	json_file = os.path.join(BASE_DIR, 'emoticons.json')
	print 'Load emoticons list from {} ......'.format(json_file)
	data_list = load_data(json_file)

	counter = 1
	for data in data_list:
		print 'Downloading[{}/{}]: {} ......'.format(counter, len(data_list), data['url'])
		emoticon_file_name = os.path.join(EMOTICONS_DIR, '{}.gif'.format(data['md5']))
		download_emoticon(data['url'], emoticon_file_name)
		print 'Download[{}/{}]: {} success.'.format(counter, len(data_list), data['url'])
		counter += 1
