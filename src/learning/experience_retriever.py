from .memory_store import ExperienceMemory

memory = ExperienceMemory()


def retrieve_past_experiences(signal):

    experiences = memory.retrieve_similar(signal)

    formatted = ""

    for i, exp in enumerate(experiences):

        formatted += f"""
Case {i+1}
Decision: {exp['decision']}
PnL: {exp['pnl']}
Lesson: {exp['lesson']}
"""

    return formatted