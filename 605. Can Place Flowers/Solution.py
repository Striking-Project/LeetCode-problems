class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Check if n flowers can be planted in a non-adjacent way in the flower bed.

        Args:
            flowerbed(list[int]): list of plant plots, empty is (0), not empty is (1)
            n(int): number of plants to be planted

        Returns:
            true if it's possible and false if not
        """
        length = len(flowerbed)
        count = 0

        for i in range(length):
            if (flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0)):
                # Plant a flower and reduce the count of remaining flowers
                flowerbed[i] = 1
                n -= 1

        return n <= 0