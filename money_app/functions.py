import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta


def inspect_inputs_dict():
    pass


def inspect_params_dict():
    pass


def get_income(inputs):
    income_oscar = sum(source["oscar"] for source in inputs["income"].values())
    income_rose = sum(source["rose"] for source in inputs["income"].values())
    return income_oscar, income_rose


def get_bills(inputs):
    bills_oscar = sum(source["oscar"] for source in inputs["bills"].values())
    bills_rose = sum(source["rose"] for source in inputs["bills"].values())
    return bills_oscar, bills_rose


def get_expenses(inputs):
    expenses_oscar = sum(source["oscar"] for source in inputs["expenses"].values())
    expenses_rose = sum(source["rose"] for source in inputs["expenses"].values())
    return expenses_oscar, expenses_rose


def get_investments(inputs):
    investments_oscar = sum(
        source["oscar"] for source in inputs["investments"].values()
    )
    investments_rose = sum(source["rose"] for source in inputs["investments"].values())
    return investments_oscar, investments_rose


def get_spending_total(inputs):
    return sum(get_bills(inputs)) + sum(get_expenses(inputs))


def get_spending_share(inputs, params):
    if params["split"] == "proportional_to_income":
        income_oscar, income_rose = get_income(inputs)
        split_percentage_oscar = income_oscar / (income_oscar + income_rose)
        split_percentage_rose = income_rose / (income_oscar + income_rose)
        return split_percentage_oscar, split_percentage_rose
    else:
        raise ValueError("split mode not supported")


def get_expected_spending(inputs, params):
    spending_share_oscar, spending_share_rose = get_spending_share(inputs, params)
    expected_spending_oscar = get_spending_total(inputs) * spending_share_oscar
    expected_spending_rose = get_spending_total(inputs) * spending_share_rose
    return expected_spending_oscar, expected_spending_rose


def get_actual_spending(inputs):
    actual_spending_oscar = (
        sum(source["oscar"] for source in inputs["bills"].values())
        + sum(source["oscar"] for source in inputs["expenses"].values())
        + sum(source["oscar"] for source in inputs["investments"].values())
    )
    actual_spending_rose = (
        sum(source["rose"] for source in inputs["bills"].values())
        + sum(source["rose"] for source in inputs["expenses"].values())
        + sum(source["rose"] for source in inputs["investments"].values())
    )
    return actual_spending_oscar, actual_spending_rose


def get_split_difference(inputs, params):
    expected_spending_oscar, expected_spending_rose = get_expected_spending(
        inputs, params
    )
    actual_spending_oscar, actual_spending_rose = get_actual_spending(inputs)
    split_difference_oscar = expected_spending_oscar - actual_spending_oscar
    split_difference_rose = expected_spending_rose - actual_spending_rose
    return split_difference_oscar, split_difference_rose


def get_savings_interest(inputs):
    return sum(source for source in inputs["savings_interest"].values())


def get_personal_spending(inputs):
    return sum(source for source in inputs["personal_spending"].values())


def get_savings(inputs):
    income_oscar, income_rose = get_income(inputs)
    actual_spending_oscar, actual_spending_rose = get_actual_spending(inputs)
    savings_oscar = income_oscar - actual_spending_oscar
    savings_rose = income_rose - actual_spending_rose
    return savings_oscar, savings_rose


def get_saving_pots(params):
    return list(params["saving_pots_shares"].keys())


def get_saving_pots_contribution(inputs, params):
    savings_total = (
        sum(get_savings(inputs))
        + get_savings_interest(inputs)
        - get_personal_spending(inputs)
    )
    saving_pots_contributions = {}
    for pot in get_saving_pots(params):
        saving_pots_contributions[pot] = (
            savings_total * params["saving_pots_shares"][pot]
        )
    return saving_pots_contributions


def get_saving_pots_contribution_per_account(inputs, params):
    saving_pots_contribution = get_saving_pots_contribution(inputs, params)
    return {
        "easy_access_account": sum(
            [
                saving_pots_contribution[pot]
                for pot in saving_pots_contribution
                if pot in params["easy_access_pots"]
            ]
        ),
        "high_yield_account": sum(
            [
                saving_pots_contribution[pot]
                for pot in saving_pots_contribution
                if pot in params["high_yield_pots"]
            ]
        ),
    }


def get_saving_pots_projection_df(inputs, params, date, months=12):
    saving_pots_projection_df = pd.DataFrame(
        columns=["month"] + get_saving_pots(params)
    )
    saving_pots_projection_df.loc[0] = {
        **{"month": datetime.strptime(date, "%Y-%m-%d").strftime("%b %y")},
        **inputs["current_savings"],
    }
    start_date = datetime.strptime(date, "%Y-%m-%d")
    saving_pots_contribution = get_saving_pots_contribution(inputs, params)
    for i in range(1, months + 1):
        saving_pots_projection_df.loc[i] = {
            **{
                "month": (start_date + relativedelta(months=i)).strftime("%b %y"),
            },
            **{
                pot: (
                    saving_pots_projection_df.loc[i - 1][pot]
                    + saving_pots_contribution[pot]
                )
                for pot in get_saving_pots(params)
            },
        }
    return saving_pots_projection_df
