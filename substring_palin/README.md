# Longest Palindrom Substring


## Idea

To detect the longest palindrom substring you need to consider each caracter of the string as a center logical as the string : zabatrsn contains the palindrom aba which is not centered around the string. That's why a simple 2 pointers solution isn't possible and that you need to loop over each caracter.

## Note

My first idea of using only 2 pointers similar to the simpler problem of checking wheter a string s is a palindrome or not was not the correct approach, i did not consider not-centered palindrom in my first approach which was a mistake
