"""
AI Ethics Advisor - Predictive Policing Domain

-----------------------------------------------

Propositional Variables:


    (General)

    1- sH : causes_severe_harm
    2- mH : causes_minor_harm
    3- PC : prevents_catastrophe
    4- VP : violates_privacy
    5- HC : has_consent
    6- DH: deceives_human
    7- EA: has_ethics_approval
    8- EX: has_explanation
    9- PM: prevents_minor_harm

    (specific)

    1- HD: uses_historical_data
    2- BM: has_bias_mitigation

-------------------------------

Violations:


    V1 (Non-Maleficence Violation):
    V1 := sH

    V2 (Harm-Mitigation Violation):
    V2 := mH ∧ ¬PC

    V3 (Data-Stewardship Violation):
    V3 := VP ∧ ¬HC

    V4 (Honesty Violation):
    V4 := DH ∧ ¬(PM ∧ EA)

    V5 (Accountability Violation):
        V5 := ¬EX

    V6 (Bias Governance Violation - Predictive Policing):
        V6 := HD ∧ ¬BM

---------------------------------------------------------

Overall permissibility:

    P := ¬(V1 v V2 v V3 v V4 v V5 v V6)

    Using De Morgan:

    P ≡ ¬V1 ∧ ¬V2 ∧ ¬V3 ∧ ¬V4 ∧ ¬V5 ∧ ¬V6


"""

from typing import Dict, List, Tuple


def is_rule1_violated(action: Dict[str, bool]) -> bool:
    """
    Rule 1 - Non-Maleficence:
    V1 := causes_severe_harm
    """
    return action["causes_severe_harm"]


def is_rule2_violated(action: Dict[str, bool]) -> bool:
    """
    Rule 2 - Harm-Mitigation:
    V2 := causes_minor_harm ∧ ¬prevents_catastrophe
    """
    return action["causes_minor_harm"] and not action["prevents_catastrophe"]


def is_rule3_violated(action: Dict[str, bool]) -> bool:
    """
    Rule 3 - Data-Stewardship:
    V3 := violates_privacy ∧ ¬has_consent
    """
    return action["violates_privacy"] and not action["has_consent"]


def is_rule4_violated(action: Dict[str, bool]) -> bool:
    """
    Rule 4 - Honesty:
    V4 := deceives_human ∧ ¬(prevents_minor_harm ∧ has_ethics_approval)
    """
    return action["deceives_human"] and not (
        action["prevents_minor_harm"] and action["has_ethics_approval"]
    )


def is_rule5_violated(action: Dict[str, bool]) -> bool:
    """
    Rule 5 - Accountability:
    V5 := ¬has_explanation
    """
    return not action["has_explanation"]


def is_rule6_violated(action: Dict[str, bool]) -> bool:
    """
    Rule 6 - Bias Governance (Predictive Policing):
    V6 := uses_historical_data ∧ ¬has_bias_mitigation
    """
    return action["uses_historical_data"] and not action["has_bias_mitigation"]


def is_action_permissible(action: Dict[str, bool]) -> Tuple[bool, List[str]]:
    """
     
     Main advisor function.

     It will return : ( is_premissible, violated_rules)

    """
    violated_rules: List[str] = []

    if is_rule1_violated(action):
        violated_rules.append("Rule 1: Non-Maleficence (Severe Harm)")
    if is_rule2_violated(action):
        violated_rules.append("Rule 2: Harm-Mitigation (Unjustified Minor Harm)")
    if is_rule3_violated(action):
        violated_rules.append("Rule 3: Data-Stewardship (Privacy without Consent)")
    if is_rule4_violated(action):
        violated_rules.append("Rule 4: Honesty (Unjustified Deception)")
    if is_rule5_violated(action):
        violated_rules.append("Rule 5: Accountability (No Explanation / Traceability)")
    if is_rule6_violated(action):
        violated_rules.append("Rule 6: Bias Governance (Unmitigated Historical Bias)")

    is_permissible = (len(violated_rules) == 0)
    return is_permissible, violated_rules


"""
Domain: Predictive Policing AI

1- Severe harm (causes_severe_harm):
    Wrongful arrest, physical violence, or life-changing negative consequences
    caused mainly by the AI decision (e.g., being jailed because of a risk score).

2- Minor harm (causes_minor_harm):
    Psychological stress, repeated police stops, short-term detainment, or
    uncomfortable questioning without direct physical violence.

3- Prevents catastrophe (prevents_catastrophe):
    Preventing a huge accident or event such as a mass shooting, gang retaliation,
    terrorist attack, or major loss of life.

4- Violates privacy (violates_privacy):
    Using detailed personal data (location history, online activity, communication
    metadata) beyond what people reasonably expected or agreed to.

5- Has consent (has_consent):
    There is explicit informed consent from individuals OR a clear democratic/legal
    mandate with transparency and the possibility to contest or opt out.

6- Deceives human (deceives_human):
    Citizens or officers are intentionally misled about what the system is doing
    (for example, saying “random patrols” while it is actually targeted AI prediction).

7- Has ethics approval (has_ethics_approval):
    An independent ethics board / legal committee reviewed the system and approved it
    under specific constraints.

8- Has explanation (has_explanation):
    The decisions of the AI can be explained, audited, and traced back to
    responsible humans and documented procedures.

9- Prevents minor harm (prevents_minor_harm):
    The action or deception is used to prevent “smaller-scale” harms such as
    harassment, property damage, or neighborhood-level violence.

10- uses_historical_data (uses_historical_data):
    The AI is trained mainly on historical crime / arrest data which might contain
    structural bias against certain neighborhoods or groups.

11- has_bias_mitigation (has_bias_mitigation):
    There are explicit fairness / bias mitigation techniques and regular audits
    to reduce the impact of biased historical data.
"""


# =======================
# Scenarios
# =======================

# 1- Scenario A (Obviousley Premissible):

scenario_A_description = """
Scenario A: Safer Patrol Zones with Limited Data

In this scenario, the city uses a predictive policing AI only to suggest patrol zones,
not to target specific people. The AI looks at recent anonymous incident reports and
simple factors like time of day and lighting. Police presence increases a bit in some
areas, which might annoy some residents, but the main goal is to prevent serious violence.

Key points:
- No one is directly arrested or punished just because of the AI.
- Any minor harm (extra police presence) is meant to prevent bigger dangers.
- The system does not use detailed personal data, so there is no clear privacy violation.
- The public knows that the system exists and what it roughly does.
- There is ethics approval and documentation.
- It does not rely on biased historical arrest data, and there is bias monitoring.

Because of this, I expect the action to be ethically PERMISSIBLE in this framework.
"""


scenario_A_action = {
    "causes_severe_harm": False,
    "causes_minor_harm": True,
    "prevents_catastrophe": True,
    "violates_privacy": False,
    "has_consent": True,
    "deceives_human": False,
    "has_ethics_approval": True,
    "has_explanation": True,
    "prevents_minor_harm": True,
    "uses_historical_data": False,
    "has_bias_mitigation": True,
}

scenario_A_predicted_outcome = {
    "expected_permissible": True,
    "expected_violations": [],
}


# 2- Scenario B (Obviousley Impremissible):

scenario_B_description = """
Scenario B: Hidden Risk Scores Based on Biased History

In this scenario, a police department uses an AI system that gives each person a "risk score".
The scores are mainly based on old arrest data from neighborhoods that were already heavily
policed in the past. Officers are told to stop and search people with high scores.

Key points:
- Many people with high scores get stopped again and again, and sometimes the situation
  becomes violent or leads to wrongful detainment.
- The system does not clearly prevent any specific catastrophe; it mostly supports aggressive
  "proactive" policing.
- The AI collects detailed personal data like location history and social media activity
  without explicit consent.
- The system is described dishonestly: officers and the public are told it is only a
  "scheduling tool".
- There is no independent ethics approval, no clear documentation, and no real explanation
  of how the scores are produced.
- It strongly relies on historical data that is already biased.
- There is no serious bias mitigation.

Under my rules, this scenario clearly violates multiple principles and should be IMPERMISSIBLE.
"""


scenario_B_action = {
    "causes_severe_harm": True,
    "causes_minor_harm": True,
    "prevents_catastrophe": False,
    "violates_privacy": True,
    "has_consent": False,
    "deceives_human": True,
    "has_ethics_approval": False,
    "has_explanation": False,
    "prevents_minor_harm": False,
    "uses_historical_data": True,
    "has_bias_mitigation": False,
}

scenario_B_predicted_outcome = {
    "expected_permissible": False,
    "expected_violations": [
        "Rule 1: Non-Maleficence (Severe Harm)",
        "Rule 2: Harm-Mitigation (Unjustified Minor Harm)",
        "Rule 3: Data-Stewardship (Privacy without Consent)",
        "Rule 4: Honesty (Unjustified Deception)",
        "Rule 5: Accountability (No Explanation / Traceability)",
        "Rule 6: Bias Governance (Unmitigated Historical Bias)",
    ],
}


# 3- Scenario C (Edge Case / Ambiguous):

scenario_C_description = """
Scenario C: Undercover Intervention to Prevent a Shooting

In this scenario, the AI predicts a high risk of gang retaliation at certain places and times.
The prediction uses both current intelligence and historical data that has gone through
bias mitigation and fairness checks. Based on this, the system suggests sending undercover
officers who act like ordinary civilians and try to calm down conflicts.

Key points:
- The system is designed so that officers avoid direct severe harm, and they are trained
  to de-escalate.
- There can still be minor harm, for example people feeling watched or stressed.
- The goal is to prevent a very serious event, such as a shooting.
- Some personal data is used, but there is judicial oversight and a community-level mandate,
  so consent exists at a governance level.
- There is deception (undercover work), but:
  * the deception is limited to specific times and places,
  * it has ethics and legal approval,
  * and it is meant to prevent both minor and potentially severe harms.
- The system keeps explanation logs so actions can be audited later.
- Historical data is used, but strong bias mitigation and external audits are in place.

In real life, some people might still feel uncomfortable with this scenario because of the
deception and the use of data. However, according to the logical rules I defined, this
action ends up being classified as PERMISSIBLE, which makes it an interesting edge case.
"""


scenario_C_action = {
    "causes_severe_harm": False,
    "causes_minor_harm": True,
    "prevents_catastrophe": True,
    "violates_privacy": True,
    "has_consent": True,
    "deceives_human": True,
    "has_ethics_approval": True,
    "has_explanation": True,
    "prevents_minor_harm": True,
    "uses_historical_data": True,
    "has_bias_mitigation": True,
}

scenario_C_predicted_outcome = {
    "expected_permissible": True,
    "expected_violations": [],
}


def print_scenario_result(
    label: str,
    description: str,
    predicted: Dict,
    actual: Tuple[bool, List[str]],
) -> None:
    """Pretty-print the evaluation of a scenario."""
    print(f"--- Evaluating {label} ---")
    print("Narrative:", description.strip())
    print()
    predicted_status = "PERMISSIBLE" if predicted["expected_permissible"] else "IMPERMISSIBLE"
    print(f"Predicted Outcome: {predicted_status}.")
    print(f"Expected Violations: {predicted['expected_violations']}")
    print()
    is_perm, violations = actual
    actual_status = "PERMISSIBLE" if is_perm else "IMPERMISSIBLE"
    print("Actual Output:")
    print(f"Action is {actual_status}.")
    print(f"Violated Rules: {violations}")
    print("\n" + "-" * 70 + "\n")


def main() -> None:
    """Entry point: evaluate the three scenarios."""

    # Scenario A
    result_A = is_action_permissible(scenario_A_action)
    print_scenario_result(
        "Scenario A: Location-based Patrol Optimization",
        scenario_A_description,
        scenario_A_predicted_outcome,
        result_A,
    )

    # Scenario B
    result_B = is_action_permissible(scenario_B_action)
    print_scenario_result(
        "Scenario B: Individual Risk Scoring with Secret Blacklist",
        scenario_B_description,
        scenario_B_predicted_outcome,
        result_B,
    )

    # Scenario C
    result_C = is_action_permissible(scenario_C_action)
    print_scenario_result(
        "Scenario C: Targeted Undercover Intervention",
        scenario_C_description,
        scenario_C_predicted_outcome,
        result_C,
    )


if __name__ == "__main__":
    main()


"""
Reflection & Discussion

1) Which ethical principle was hardest to formalize?

   The hardest principle to formalize was Rule 4 (Honesty). In reality, deception is not
   simply "allowed" or "forbidden". It depends on intent, context, frequency, power
   dynamics, and long-term trust. In the formal model, I compressed all of that into a
   single condition:

       V4 := DH ∧ ¬(PM ∧ EA)

   This assumes deception is acceptable whenever it prevents minor harm AND has ethics
   approval, which is a much stronger and more simplified statement than real ethical
   reasoning.

2) A real-world scenario that might break this framework:

   A predictive policing system might technically satisfy all the rules:
     - No obvious severe harm at deployment time,
     - Some form of "consent" via legal or political channels,
     - Documented bias mitigation and explainability,
   but in practice it still creates fear, over-policing, and long-term mistrust in
   certain neighborhoods. The current rules focus on direct, short-term harms and clear
   violations, but do not capture long-term social effects, historical oppression, or
   subtle coercion. So the advisor might label the system as "permissible" even when
   many people would consider it unethical.

3) Role of human oversight in real deployment:

   This AI Ethics Advisor should be treated as a structured checklist, not a final judge.
   Human oversight committees (including legal experts, ethicists, technical experts, and
   community representatives) should:
     - review the advisor's output,
     - question the truth of each boolean input (e.g., "do we REALLY have consent?"),
     - and request more evidence when the stakes are high.

   In highly sensitive cases, a negative result should trigger mandatory human review,
   and even a "PERMISSIBLE" result should not be accepted blindly without discussion.

4) Trade-offs between a simple framework and a more complex one:

   A simple, rigid framework (like this one) has clear benefits:
     - easy to explain and audit,
     - straightforward to implement in code,
     - useful as a first-line filter for obviously unacceptable actions.

   But it has drawbacks:
     - it can miss nuance,
     - it cannot fully represent social context, history, or power,
     - and it may give a false sense of security ("the logic says it's fine").

   A more complex, nuanced framework might combine formal logic with probabilistic
   reasoning, case-based analysis, and richer ethical theories. That could better match
   real-world complexity, but it would be harder to understand, verify, and maintain.

   In practice, a hybrid approach is most realistic: use a relatively simple logical core
   like this to enforce hard constraints (no severe harm, no privacy violations without
   consent, no unmitigated historical bias), and then layer human judgment and more
   nuanced analysis on top, instead of expecting the logic alone to fully solve ethics.
"""
