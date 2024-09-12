def replace_word():
    str1 = input("Enter a string : ")
    word_to_replace= input("Enter the word to be replaced : ")
    if word_to_replace not in str1:
        print("The word is not present in the string")
    else:
        word_replacement = input("Enter the replacement word : ")
        print(str1. replace(word_to_replace, word_replacement))


replace_word()