from typing import List

def kidsWithCandies( candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        result = []
        for i in range(len(candies)):
            if candies[i]+extraCandies >= maxCandies:
                result.append(True)
            else:
                result.append(False)
        return result


list=[3,7,4,9,2,1]
candies_extra=4
print(kidsWithCandies(list,candies_extra))