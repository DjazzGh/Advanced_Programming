unique_words = set()  
total_words = 0  

while True:
        word = input("Enter a word: ").strip().lower()  
        total_words += 1  

        if word in unique_words: 
            print(f"You typed {len(unique_words)} unique words.")
            break  
        else:
            unique_words.add(word)  


