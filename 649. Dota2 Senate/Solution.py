class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        """
        Predict the party that will announce the victory and change the Dota2 game using queues.

        Args:
            senate (str): A string representing each senator's party belonging. 'R' for Radiant, 'D' for Dire.

        Returns:
            str: The predicted winning party, either 'Radiant' or 'Dire'.
        """

        n = len(senate)
        
        if not (1 <= n <= 10**4):
            raise ValueError("Invalid length of senate. 1 <= n <= 10^4")

        if not all(party in ('R', 'D') for party in senate):
            raise ValueError("Invalid party affiliations. Senate should consist of 'R' or 'D'.")

        radiant_queue, dire_queue = deque(), deque()

        for i, party in enumerate(senate):
            if party == 'R':
                radiant_queue.append(i)
            else:
                dire_queue.append(i)

        while radiant_queue and dire_queue:
            radiant_index, dire_index = radiant_queue.popleft(), dire_queue.popleft()

            if radiant_index < dire_index:
                radiant_queue.append(radiant_index + len(senate))
            else:
                dire_queue.append(dire_index + len(senate))

        return 'Radiant' if radiant_queue else 'Dire'