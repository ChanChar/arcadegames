
# Multiple Choice

answers = "abcddcbbacba"

for number, answer in enumerate(list(answers)):
    print("{}. {}".format(number+1, answer.upper()))