DATE = "2023-12-01"

INPUTS = {
    "current_savings": {
        "new_house": 6720.0,
        "car": 15120.0,
        "current_house": 11760.0,
        "holidays": 0,
        "wedding": 0,
        "children": 0,
        "family": 0,
    },
    "income": {
        "salary": {"oscar": 4900, "rose": 2542},
        "freelance": {"oscar": 0, "rose": 0},
    },
    "savings_interest": {
        "ulster_bank": 10.68,
        "hampshire_trust_bank": 0,
    },
    "bills": {
        "mortgage": {"oscar": 1973.17, "rose": 0},
        "electricity": {"oscar": 0, "rose": 150},
        "gas": {"oscar": 0, "rose": 168.72},
        "water": {"oscar": 0, "rose": 78.87},
        "council_tax": {"oscar": 0, "rose": 188.00},
        "internet": {"oscar": 60, "rose": 0},
        "home_insurance": {"oscar": 0, "rose": 22.37},
    },
    "expenses": {
        "shopping": {"oscar": 95.09, "rose": 260.03},
        "freya": {"oscar": 97.19, "rose": 9.15},
        "cleaning": {"oscar": 101.4, "rose": 0},
        "fertility": {"oscar": 0, "rose": 0},
    },
    "investments": {
        "comcast_shares": {"oscar": 0, "rose": 0},
    },
    "personal_spending": {"oscar": 0, "rose": 0},
}

PARAMS = {
    "saving_pots_shares": {
        "new_house": 0.3,
        "car": 0.2,
        "current_house": 0.15,
        "holidays": 0.15,
        "wedding": 0.10,
        "children": 0.05,
        "family": 0.05,
    },
    "split": "proportional_to_income",
    "savings_interest_rates": {
        "ulster_bank": 0.052,
        "hampshire_trust_bank": 0.0551,
    },
    "easy_access_pots": ["current_house", "wedding", "holidays", "family"],
    "high_yield_pots": ["new_house", "car", "children"],
}
