class CriticAgent:

    def evaluate(self, decision, pnl):

        if pnl > 0:
            lesson = "Decision aligned with market movement."
            outcome = "correct"
        else:
            lesson = "Market moved opposite to the predicted direction."
            outcome = "wrong"

        return {
            "outcome": outcome,
            "lesson": lesson
        }