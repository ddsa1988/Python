def print_models(unprinted_designs: list[str], completed_models: list[str]) -> None:
    while (len(unprinted_designs)) > 0:
        current_design = unprinted_designs.pop()
        completed_models.append(current_design)

        print(f"Printing model: {current_design}")


def show_completed_models(completed_models: list[str]) -> None:
    print("\nThe following models gave been printed:")

    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

print()

print(unprinted_designs)
