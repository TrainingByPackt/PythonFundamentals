
def take_input():
	"""Helper function to take input for a user"""
	name_marks = input().split()
	name = name_marks[0]
	marks = [float(x) for x in name_marks[1:]]
	return name, marks

def rank_user(users_name_list, users_score_lst):
	"""Returns a dictionary. Key is user_name and values is rank

	Arguments:
		users_name_list : list of strings (user names)
		user_score_lst : list of numbers (mean score)
	"""
	# your code starts here.

	return #dictionary of name and rank.

def find_topper():
	"""Rank users based on mean score."""

	# your code starts here.
	print("Enter user_name and marks (space seperated)")
	users_1, marks_1 = take_input()
	users_2, marks_2 = take_input()
	users_3, marks_3 = take_input()

	users_1_mean_score = # mean score for user_1
	users_2_mean_score = # mean score for user_2
	users_3_mean_score = # mean score for user_3

	user_lst = [users_1, users_2, users_3]
	score_lst = [users_1_mean_score, users_2_mean_score, users_3_mean_score]

	user_ranks = rank_user(user_lst, score_lst)

	for name, rank in user_ranks.items():
		print("{}: {}".format(name, rank))


if __name__ == '__main__':
	find_topper()
	



