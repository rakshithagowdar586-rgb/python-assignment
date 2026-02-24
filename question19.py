def question19():
    # 1. Count Words
    def count_words(text):
        words = text.split()
        return len(words)


    # 2. Count Vowels
    def count_vowels(text):
        vowels = "aeiouAEIOU"
        count = 0
        for char in text:
            if char in vowels:
               count += 1
        return count


    # 3. Count Consonants
    def count_consonants(text):
        vowels = "aeiouAEIOU"
        count = 0
        for char in text:
            if char.isalpha() and char not in vowels:
               count += 1
        return count


    # 4. Reverse Text
    def reverse_text(text):
        return text[::-1]


    # 5. Check Palindrome
    def is_palindrome(text):
        cleaned = text.replace(" ", "").lower()
        return cleaned == cleaned[::-1]


    # 6. Remove Vowels
    def remove_vowels(text):
        vowels = "aeiouAEIOU"
        result = ""
        for char in text:
           if char not in vowels:
            result += char
        return result
    

    # 7. Word Frequency
    def word_frequency(text):
        words = text.lower().split()
        freq = {}
        for word in words:
           freq[word] = freq.get(word, 0) + 1
        return freq


    # 8. Longest Word
    def longest_word(text):
        words = text.split()
        if not words:
           return ""
        return max(words, key=len)


    # 9. Analyze Text (Main Function)
    def analyze_text(text):
        print("\n===== TEXT ANALYSIS RESULT =====")
        print("Word Count:", count_words(text))
        print("Vowel Count:", count_vowels(text))
        print("Consonant Count:", count_consonants(text))
        print("Reversed Text:", reverse_text(text))
        print("Is Palindrome?:", is_palindrome(text))
        print("Text Without Vowels:", remove_vowels(text))
        print("Word Frequency:", word_frequency(text))
        print("Longest Word:", longest_word(text))


    # Run the program
    user_text = input("Enter some text: ")
    analyze_text(user_text)
question19()