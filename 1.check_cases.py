import os

def compare_results(case_name, total_cases):
    answer = 0
    error_cases = []

    result_file = f'./output/{case_name}.txt'
    answer_file = f'./output/answer.txt'

    with open(result_file, 'r') as r_file, open(answer_file, 'r') as a_file:
        lines = r_file.readlines()
        answer_lines = a_file.readlines()

        for i in range(1, total_cases + 1):
            result_content = lines[(i - 1) * 2 + 1].strip()
            answer_content = answer_lines[(i - 1) * 2 + 1].strip()

            if result_content == answer_content:
                answer += 1
            else:
                error_cases.append(i)

    percentage = (answer / total_cases) * 100
    summary = f"{answer}/{total_cases}\n{percentage:.2f}%\n\/ error cases : {error_cases}\n"

    with open(f'./result/{case_name}.txt', 'w') as result_file:
        result_file.write(summary)


def get_case_names():
    output_path = './output'
    case_names = []

    for entry in os.scandir(output_path):
        if entry.is_file() and entry.name.endswith('.txt'):
            case_names.append(entry.name[:-4])

    return case_names


def count_cases_in_txt(path):
    case_count = 0

    with open(path, 'r') as f:
        for line in f:
            if '<<<' in line and 'case >>>' in line:
                case_count += 1

    return case_count


case_names = get_case_names()

for case_name in case_names:
    total_cases = count_cases_in_txt('./output/answer.txt')
    compare_results(case_name, total_cases)

