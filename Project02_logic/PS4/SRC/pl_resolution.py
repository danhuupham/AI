from utilities import *


def pl_resolve(first_clause: list, second_clause: list) -> list:
    """Resolve two clauses and return the result."""

    result_clause = []

    for first_literal in first_clause:
        for second_literal in second_clause:
            if first_literal == to_negative(second_literal):
                result_clause = first_clause + second_clause

                result_clause.remove(first_literal)
                result_clause.remove(second_literal)

                result_clause = standardize(result_clause)

                for i in range(len(result_clause) - 1):
                    if is_inverse(result_clause[i], result_clause[i + 1]):
                        return None

                return result_clause

    return None


def pl_resolution(knowledge_base: list, alpha: str, output_path: str) -> bool:
    """Perform PL-Resolution on a knowledge base and a sentence alpha."""

    output_file = open(output_path, 'w')

    clauses = knowledge_base + [[to_negative(literal)] for literal in alpha]

    new_clauses = []
    output_clauses = []
    has_solution = False

    while True:
        new_clauses = []
        output_clauses = []

        for i in range(len(clauses) - 1):
            for j in range(i + 1, len(clauses)):
                result_clause = pl_resolve(clauses[i], clauses[j])

                if result_clause is not None and result_clause not in clauses and result_clause not in new_clauses:
                    new_clauses.append(result_clause)

        for clause in new_clauses:
            if clause not in clauses:
                clauses.append(clause)
                output_clauses.append(clause)

        output_file.write(str(len(output_clauses)) + '\n')

        if new_clauses == []:
            output_file.write('NO')
            return False

        for clause in output_clauses:
            if clause:
                output_file.write(to_cnf_string(clause) + '\n')
            else:
                output_file.write('{}\n')
                has_solution = True

        if has_solution:
            output_file.write('YES')
            return True
