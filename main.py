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
    Scenario A: Location-based Patrol Optimization with Oversight

    A city deploys a predictive policing AI that only suggests patrol zones (not specific people)
    based on recent anonymous incident reports and environmental factors (lighting, time of day).
    Police presence increases slightly in some areas, which may cause minor inconvenience,
    but the main goal is to prevent serious violent incidents.

    The system:
    - does NOT directly cause severe harm,
    - may cause minor harm (increased presence) but is justified to prevent catastrophe,
    - does NOT use invasive personal data (no privacy violation),
    - is NOT deceptive (citizens are informed about the system),
    - has ethics approval and clear documentation,
    - does NOT rely on biased historical arrest data,
    - and still has bias monitoring in place as a safeguard.
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
    Scenario B: Individual Risk Scoring with Secret Blacklist

    A police department deploys an AI system that assigns "risk scores" to individual citizens
    using mainly historical arrest and stop-and-frisk data from heavily policed neighborhoods.
    Officers are instructed to stop and search people with high scores.

    The system:
    - has led to repeated wrongful stops and occasional violent escalations,
    - does NOT clearly prevent a specific catastrophe, it mainly supports aggressive policing,
    - collects detailed location history and social media data without explicit consent,
    - is not honestly described (officers and public are told it is just a 'scheduling tool'),
    - has no independent ethics approval, no documentation, and no real explanation of scores,
    - strongly relies on biased historical data,
    - and there is no bias mitigation in place.

    This scenario is clearly impermissible under the EGF.
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
    Scenario C: Targeted Undercover Intervention with Strong Safeguards

    An AI system predicts a high risk of gang retaliation at specific locations and times.
    It uses a combination of current intelligence and carefully debiased historical data.
    The system recommends deploying undercover officers who appear as ordinary civilians
    to quietly de-escalate conflicts and interrupt potential violence.

    The system:
    - does NOT directly cause severe harm (officers are trained to avoid escalation),
    - may cause minor harm (some people may feel watched or briefly questioned),
    - is aimed at preventing a likely shooting (a serious catastrophe),
    - uses limited personal data with judicial oversight and community-level consent,
    - involves deception (undercover work), but:
        * the deception is narrowly scoped,
        * it has ethics and legal approval,
        * and it is intended to prevent minor and potentially severe harms,
    - keeps full internal explanations and logs for later audit,
    - uses historical data but only with strong bias mitigation and fairness audits.

    This scenario is ethically ambiguous in real life, but under the current formal rules,
    it is classified as permissible because every rule's logical condition is satisfied.
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