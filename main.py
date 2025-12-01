"""
AI Ethics Advisor - Predictive Policing Domain

-----------------------------------------------

Propositional Variables:


    (General)

    1- sH : causes_severe_harm
    2- mH : causes_minor_harm
    3- PC : prevents_catastrophe---------------------------------------
    4- VP : violates_privacy
    5- HC : has_consent
    6- DH: deceives_human
    7- EA: has_ethics_approval
    8- EX: has_explanation
    9- PM: prevents_minor_harm

    (specific)

    1- HD: uses_historical_data
    2- BM: vhas_bias_mitigation

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


""""