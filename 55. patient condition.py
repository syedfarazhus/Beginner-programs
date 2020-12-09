from typing import List
from typing import Dict

patients = {
"Alice Liddel": {"bed": 1, "ward": "psych", "condition": "poor"},
"Bob Vance": {"bed": 2, "ward": "cancer", "condition": "good"},
"Charlie Andrews": {"bed": 3, "ward": "paediatrics", "condition": "good"}
}

def attend(patients: Dict[str, Dict], condition: str) -> List[str]:
    """Return a list of all patients with the input condition.
    Given patients structured as from slide 3.
    >>> attend(patients, ‘good’)
    [‘Charlie Andrews’, ‘Bob Vance’]
    """
    cond = []

    for key in patients.keys():
        if patients[key]["condition"] == condition:
            cond.append(key)
    return cond
            
    
    
