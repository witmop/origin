class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        from string import ascii_lowercase
        morse_code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result=set()
        for el in words:
            temp=""
            for lett in el:
                temp+=morse_code[ascii_lowercase.find(lett)]
            result.add(temp)
        return len(result)