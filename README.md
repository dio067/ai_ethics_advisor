# AI Ethics Advisor – Predictive Policing Domain

This project is a simple logic-based system that checks whether an AI action is
ethically acceptable or not. The whole idea is to translate ethical rules into
clear propositional logic, then implement these rules in Python.

I chose the “Predictive Policing” domain because it has a lot of real-world
ethical problems like biased data, privacy issues, and the risk of harming
communities. This makes it a good fit for testing the logic.

---

## How the System Works

Each AI action is represented as a set of True/False values.  
Example:

- Does it cause severe harm?
- Does it violate privacy?
- Does it use biased historical data?
- Does it have ethics approval?  
  …and so on.

The system has 6 rules:

1. No severe harm
2. Minor harm must prevent a catastrophe
3. No privacy violation without consent
4. No deception unless it prevents minor harm and has ethics approval
5. The action must have an explanation
6. Historical data must have bias mitigation

If any rule is violated → the action becomes **IMPERMISSIBLE**.  
If all rules pass → the action is **PERMISSIBLE**.

---

## What’s Implemented

- All rules are translated into propositional logic (V1 to V6).
- A Python function for each rule checks if it is violated.
- A main advisor function returns:
  - Whether the action is permissible
  - Which rules were violated (if any)

I also created 3 scenarios for testing:

- **Scenario A:** Clearly permissible
- **Scenario B:** Clearly impermissible
- **Scenario C:** Edge case (ambiguous but ends up permissible under the rules)

Each scenario has:

- A short story description
- Predicted outcome
- Actual output printed by the program

---

## How to Run

Make sure you have Python installed.  
Then run:

```bash
python ai_ethics_advisor.py
```
