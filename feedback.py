class Feedback:
    def guess(self,guess,answer):
        feedback = [0] * 5
        remaining = {}
        # green check
        for letter in range(5):
            if guess[letter] == answer[letter]:
                feedback[letter] = 2
            else:
                remaining[answer[letter]] = remaining.get(answer[letter], 0) + 1
        # yellow check
        for letter in range(5):
            if feedback[letter]==0:
                if remaining.get(guess[letter],0) > 0:
                    feedback[letter] = 1
                    remaining[guess[letter]] -= 1
        return feedback