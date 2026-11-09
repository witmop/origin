class Solution:
    def compress(self, chars: list[str]) -> int:
        count=1
        result=""
        write=1
        result+=chars[0]
        if len(chars)>1:
            for ind,el in enumerate(chars[1:]):
                if result[-1]!=el:
                    if count>1:
                        result+=f"{count}{el}"
                        for t in str(count):
                            chars[write]=t
                            write+=1
                        chars[write]=el
                        write+=1
                    else:
                        chars[write]=el
                        write+=1
                        result+=el
                    count=0
                count+=1
            chars[write-1]=chars[-1]
            if count>1:
                for t in str(count):
                    chars[write]=t
                    write+=1
            if count>1:
                result+=str(count)
            return len(result)

 
