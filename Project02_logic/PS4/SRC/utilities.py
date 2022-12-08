def to_negative(literal: str) -> str:
    """Return the negative of a literal."""

    return literal[1] if literal[0] == '-' else '-' + literal


def is_inverse(first_literal: str, second_literal: str) -> bool:
    """Check if two literals are inverse of each other."""

    return first_literal == to_negative(second_literal)


def standardize(clause: list) -> list:
    """Standardize literals in a clause."""

    return sorted(list(set(clause)), key=lambda literal: literal[-1])


def to_cnf_string(clause: list) -> str:
    """Convert a clause to a string in CNF format."""

    return ' OR '.join(clause)


def read_input(input_path: str) -> tuple:
    """Read the input file and return the knowledge base and the sentence alpha."""

    input_file = open(input_path, 'r')

    alpha = input_file.readline().strip().split(' OR ')

    number_of_clauses = int(input_file.readline().strip())

    knowledge_base = []

    for _ in range(number_of_clauses):
        knowledge_base.append(input_file.readline().strip().split(' OR '))

    input_file.close()

    return knowledge_base, alpha
