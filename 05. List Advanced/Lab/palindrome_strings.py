words = input().split()
palindrome = input()
final_list = []

for word in words:
    reversed_word = ''.join(reversed(word))
    if word == reversed_word:
        final_list.append(word)
print(final_list)
print(f'Found palindrome {final_list.count(palindrome)} times')