import otherFunctions

sentence = "All good things come to those who wait."

words = otherFunctions.break_words(sentence)

otherFunctions.print_generic(words)

sorted_words = otherFunctions.sort_words(words)

otherFunctions.print_generic(sorted_words)


firs_word = otherFunctions.print_first_word(words)

otherFunctions.print_generic(firs_word)

last_word = otherFunctions.print_last_word(words)
otherFunctions.print_generic(last_word)

sort_sentence = otherFunctions.sort_sentence(sentence)
otherFunctions.print_generic(sort_sentence)

otherFunctions.print_first_and_last(sentence)

print("====================================================")

otherFunctions.print_first_and_last_sorted(sentence)
