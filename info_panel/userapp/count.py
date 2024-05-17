import json

def get_count():
    with open('simulations.json') as file:
        simulations = json.load(file)["simulations"]

    with open('users.json') as file:
        users = json.load(file)["users"]

    simulation_count = {}

    for user in users:
        simulation_id = user["simulation_id"]
        if simulation_id in simulation_count:
            simulation_count[simulation_id] += 1
        else:
            simulation_count[simulation_id] = 1

    company_count = {}

    for simulation in simulations:
        company_id = simulation["company_id"]
        simulation_id = simulation["simulation_id"]
        if company_id in company_count:
            company_count[company_id] += simulation_count[simulation_id]
        else:
            company_count[company_id] = simulation_count[simulation_id]

    company_id_to_name = {simulation["company_id"]: simulation["company_name"] for simulation in simulations}

    return [{"company_name": company_id_to_name[company_id], "count": count} for company_id, count in company_count.items()]
