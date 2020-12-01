import csv


def find(message_text):
	with open("db_users.csv") as users_only:
		csv_reader = csv.reader(users_only)
		for row in csv_reader:
			if message_text == row[0]:
				return True
		return False
