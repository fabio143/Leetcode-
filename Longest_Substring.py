# Estrategia: 
# 1. Capturar o tamanho da primeira substring
# 2. Comparar com as iterações, trocando ao achar um maior

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = ""
        max_size = 0
        i = 0

        while i < len(s): # Percorre a string
            if s[i] not in string:
                string += s[i]
            else:
                string_size = len(string)

                if string_size > max_size: # atualiza a max_size
                    max_size = string_size

                position = string.index(s[i]) #Mantem a maior string
                string = string[position + 1:]
                string += s[i]

            i += 1

        if len(string) > max_size:
            max_size = len(string)

        return max_size
                
