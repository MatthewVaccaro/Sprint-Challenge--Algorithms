'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word, count=0, inc=0):

    if len(word) == count:
        return inc

    if word[count: count + 2] == 'th':
        count += 1
        inc += 1

        return count_th(word, count, inc)

    else:
        count += 1
        return count_th(word, count, inc)
