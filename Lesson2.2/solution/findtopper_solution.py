
def take_input():
	"""Helper function to take input for a user"""
	name_marks = input().split()
	name = name_marks[0]
	marks = [float(x) for x in name_marks[1:]]
	return name, marks

def rank_user(users_name_list, users_score_lst):
	"""Returns a dictionary. Key is user_name and values is rank"""
	user_score = dict(zip(users_name_list, users_score_lst))
	user_score = sorted(user_score.items(), key=lambda x: x[1], reverse=True)
	
	rank_dict = {}
	rank = 0
	prev = float('-inf')

	for idx, (key, val) in enumerate(user_score):
	    if prev == val:
	        rank_dict[key] = rank
	    else:
	        rank_dict[key] = rank+1
	        rank += 1
	    prev = val
	return rank_dict

def find_topper():
	"""Rank users based on mean score."""

	# your code starts here.
	print("Enter user_name and marks (space seperated)")
	users_1, marks_1 = take_input()
	users_2, marks_2 = take_input()
	users_3, marks_3 = take_input()

	users_1_mean_score = sum(marks_1)/len(marks_1)
	users_2_mean_score = sum(marks_2)/len(marks_2)
	users_3_mean_score = sum(marks_3)/len(marks_3)

	user_lst = [users_1, users_2, users_3]
	score_lst = [users_1_mean_score, users_2_mean_score, users_3_mean_score]

	user_ranks = rank_user(user_lst, score_lst)

	for name, rank in user_ranks.items():
		print("{}: {}".format(name, rank))


if __name__ == '__main__':
	find_topper()
	



