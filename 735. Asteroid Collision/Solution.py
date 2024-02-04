class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Simulate the state of asteroids after collisions.

        Handle collisions between asteroids where the smaller one explodes.
        Return the state of asteroids after all collisions.

        Args:
            asteroids (List[int]): Integers representing asteroids.

        Returns:
            List[int]: State of asteroids after collisions.
        """

        if not(2 <= len(asteroids) <= 10**4):
            raise ValueError("The length of asteroids should be between 2 and 10^4")

        if not(all(-1000 <= asteroid <= 1000 for asteroid in asteroids)):
            raise ValueError("Each element in asteroids should be between -1000 and 1000")

        if any(asteroid == 0 for asteroid in asteroids):
            raise ValueError("Each element in asteroids should not be zero")

        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                # Collision occurs
                if stack[-1] < -asteroid:
                    # The top asteroid in the stack explodes
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    # Both asteroids explode
                    stack.pop()
                break
            else:
                # No collision, or the asteroid is moving in the same direction
                stack.append(asteroid)

        return stack        