class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
        The extraCandies will be given to kids so that their total number of candies
        will be the greatest.
        
        Args:
            candies(List of int):the number of candies for each kid.
            extraCandies(int): the number of extra candies I can give out.
        
        Returns: 
            result(boolean array of length = len(candies)):true if the new number of 
            candies will be the greatest and false if not.
        """ 

        #Validate the number of candies and extra candies
        if not(1 <= extraCandies <= 50):
            raise ValueError("The number of extra candies should be between 1 and 50")

        for candy in candies:
            if not(1 <= candy <= 100):
                raise ValueError("Number of candies per kid should be between 1 and 100")


        #Find the kid with the maximum number of candies
        max_candies = max(candies)

        #Check for each kid if they will have the greatest number of candies
        result = [candy + extraCandies >= max_candies for candy in candies]

        # Validate the size of the resulting array
        if not (2 <= len(result) <= 100 and len(result) == len(candies)):
            raise ValueError("Invalid result size")

        return result

