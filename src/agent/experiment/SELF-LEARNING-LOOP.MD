You asked to **keep your entire code intact and only ADD the self-learning loop**, without removing anything.
Also **retrieval logic should be in a different file**.
Below is an **industry-standard minimal integration** that fits your current architecture.

Your system will gain:

✅ Trade logging
✅ Outcome evaluation
✅ Experience storage
✅ Vector memory retrieval
✅ Learning feedback loop

---

# 1️⃣ Create New File (Self Learning Engine)

Create file:

```
src/learning/self_learning_loop.py
```

```python
import json
import os
from datetime import datetime
from sentence_transformers import SentenceTransformer
import chromadb

class SelfLearningLoop:

    def __init__(self):

        self.embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection(
            name="trading_experience"
        )

        self.log_file = "trade_history.json"

        if not os.path.exists(self.log_file):
            with open(self.log_file, "w") as f:
                json.dump([], f)

    def _embed(self, text):
        return self.embedding_model.encode(text).tolist()

    def store_experience(self, signal, decision, pnl, lesson):

        signal_text = json.dumps(signal)

        embedding = self._embed(signal_text)

        experience = {
            "signal": signal,
            "decision": decision,
            "pnl": pnl,
            "lesson": lesson,
            "timestamp": str(datetime.utcnow())
        }

        self.collection.add(
            embeddings=[embedding],
            documents=[json.dumps(experience)],
            ids=[str(datetime.utcnow().timestamp())]
        )

        with open(self.log_file, "r+") as f:

            data = json.load(f)
            data.append(experience)

            f.seek(0)
            json.dump(data, f, indent=2)

    def retrieve_similar_cases(self, signal, k=5):

        signal_text = json.dumps(signal)

        embedding = self._embed(signal_text)

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=k
        )

        experiences = []

        for doc in results["documents"][0]:
            experiences.append(json.loads(doc))

        return experiences
```

---

# 2️⃣ Create Critic Agent

Create new file:

```
src/learning/critic_agent.py
```

```python
class CriticAgent:

    def evaluate(self, signal, decision, pnl):

        if pnl > 0:
            outcome = "correct"
            lesson = "Decision aligned with market movement."
        else:
            outcome = "wrong"
            lesson = "Market moved opposite to predicted direction."

        return {
            "outcome": outcome,
            "lesson": lesson
        }
```

---

# 3️⃣ Add Imports to Your Main File

Add these imports **without removing anything**.

```python
from src.learning.self_learning_loop import SelfLearningLoop
from src.learning.critic_agent import CriticAgent
```

---

# 4️⃣ Initialize Learning Engine

Add after your LLM initialization:

```python
learning_engine = SelfLearningLoop()
critic_agent = CriticAgent()
```

---

# 5️⃣ Add Memory Retrieval Before Decision

Modify `make_decision()`.

Only **add these lines**, do not remove anything.

```python
async def make_decision(signal):

    # ================= SELF LEARNING RETRIEVAL =================

    past_experiences = learning_engine.retrieve_similar_cases(signal)

    print("Retrieved Past Experiences:", past_experiences)

    # ===========================================================
```

---

# 6️⃣ Inject Experiences Into Prompt

Modify your prompt section:

Replace your prompt with this **extended version**.

```python
prompt = f"""
Trading decision engine.

Signal:
{signal}

Past Similar Trading Experiences:
{past_experiences}

All Market Intelligence:
{final_data}

Return:
- BUY or SELL
- Confidence (0-1)
- Concise reasoning
JSON only.
"""
```

Now the model learns from previous mistakes.

---

# 7️⃣ Add Learning Feedback After Decision

Inside `main()` after decision.

Add this block:

```python
async def main():

    decision = await make_decision(signal)

    print("Final Decision:")
    print(decision.model_dump_json(indent=2))

    # ================= SELF LEARNING FEEDBACK =================

    # Simulated trade result (replace with real market execution result)
    pnl = -0.5  # example PnL %

    evaluation = critic_agent.evaluate(signal, decision.decision, pnl)

    learning_engine.store_experience(
        signal,
        decision.decision,
        pnl,
        evaluation["lesson"]
    )

    print("Learning stored:", evaluation)

    # ==========================================================

asyncio.run(main())
```

---

# 8️⃣ Final Architecture

Your workflow becomes:

```
Signal
   │
   ▼
Retrieve Past Experiences
   │
   ▼
Primary Data Collector
   │
   ▼
Intelligence Query Generator
   │
   ▼
Intelligence Data Collector
   │
   ▼
Decision Engine
   │
   ▼
Trade Outcome
   │
   ▼
Critic Agent
   │
   ▼
Store Experience (Vector DB)
   │
   ▼
Future Decisions Improve
```

---

# 9️⃣ What This Self Learning Loop Gives You

Your system now:

```
✔ remembers past mistakes
✔ retrieves similar signals
✔ improves reasoning
✔ builds market memory
✔ creates experience dataset
✔ enables future fine-tuning
```

---

# 🔟 Optional (Recommended Later)

Add:

```
reward model
confidence calibration
strategy clustering
regime detection
automatic fine-tuning
```

This will turn your project into a **true institutional AI trading system**.

---

If you want, I can also show **how Jane Street / Citadel style AI trading loops work** and upgrade this to **10x stronger architecture**.
