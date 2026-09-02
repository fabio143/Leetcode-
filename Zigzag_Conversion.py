class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        passo = 2 * numRows - 2 
        resultado = ""
        for linha in range(numRows):
            i = linha
            if linha == 0 or linha == numRows - 1: 
                while i < len(s):
                    resultado += s[i]
                    i += passo
            else: 
                passo1 = passo - 2 * linha
                passo2 = 2 * linha
                while i < len(s):
                    resultado += s[i]
                    i += passo1
                    if i < len(s):
                        resultado += s[i]
                        i += passo2
        return resultado
