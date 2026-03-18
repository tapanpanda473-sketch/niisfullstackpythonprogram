s = input("Enter a string: ")

char_count = len(s)
alpha_count = 0
upper_count = 0
lower_count = 0
vowel_count = 0
consonant_count = 0
space_count = 0
digit_count = 0
symbol_count = 0

vowels = "aeiouAEIOU"

for ch in s:
    if ch.isalpha():
        alpha_count += 1
        
        if ch.isupper():
            upper_count += 1
        elif ch.islower():
            lower_count += 1
            
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

    elif ch.isdigit():
        digit_count += 1

    elif ch.isspace():
        space_count += 1

    else:
        symbol_count += 1

words = len(s.split())
print("Total characters:", char_count)
print("Alphabets:", alpha_count)
print("Uppercase:", upper_count)
print("Lowercase:", lower_count)
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
print("Spaces:", space_count)
print("Digits:", digit_count)
print("Symbols:", symbol_count)
print("Words:", words)