import os


def compare_results(case_name, total_cases):
    answer = 0

    for i in range(1, total_cases + 1):
        result_file = f'./output/{case_name}/result_{i}.txt'
        answer_file = f'./output/answer/result_{i}.txt'

        with open(result_file, 'r') as r_file, open(answer_file, 'r') as a_file:
            result_content = r_file.read().strip()
            answer_content = a_file.read().strip()

            if result_content == answer_content:
                answer += 1

    percentage = (answer / total_cases) * 100
    summary = f"{answer} / {total_cases}\n{percentage:.2f}%\n"

    with open(f'./result/{case_name}.txt', 'w') as result_file:
        result_file.write(summary)


def get_case_names():
    output_path = './output'
    case_names = []

    for entry in os.scandir(output_path):
        if entry.is_dir() and entry.name != 'answer':
            case_names.append(entry.name)

    return case_names


def count_txt_files(path):
    txt_count = 0

    for entry in os.scandir(path):
        if entry.is_file() and entry.name.endswith('.txt'):
            txt_count += 1

    return txt_count


case_names = get_case_names()
    
for case_name in case_names:
    total_cases = count_txt_files('./output/answer')
    compare_results(case_name, total_cases)

