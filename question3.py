def question3 ():
   sentence = input("Enter a sentence: ")
   
   print("\n----- Sentence Details -----")

   print("Original Sentence:", sentence)
   print("Characters (with spaces):", len(sentence))
   print("Characters (without spaces):", len(sentence.replace(" ", "")))
   print("Words:", len(sentence.split()))
   print("UPPERCASE:", sentence.upper())
   print("Lowercase:", sentence.lower())
   print("Title Case:", sentence.title())

   words = sentence.split()
   print("First Word:", words[0])
   print("Last Word:", words[-1])

   print("Reversed Sentence:", "".join(reversed(sentence)))
question3()