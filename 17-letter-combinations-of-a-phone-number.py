class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        if len(digits)==1:
            if digits=='2':
                return ['a','b','c']
            if digits=='3':
                return ['d','e','f']
            if digits=='4':
                return ['g','h','i']
            if digits=='5':
                return ['j','k','l']
            if digits=='6':
                return ['m','n','o']
            if digits=='7':
                return ['p','q','r','s']
            if digits=='8':
                return ['t','u','v']
            if digits=='9':
                return ['w','x','y','z']
            else:
                return []
        res=[]
        head=self.letterCombinations(digits[0])
        tail=self.letterCombinations(digits[1:])
        for h in head:
            for t in tail:
                res.append(h+t)
        return res