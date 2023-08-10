# AutoScoringTask
과제를 오토로 채점하는 시대가 올까요?
해당 스크립트는 과제를 오토로 채점하기 위한 파일 입니다.

0. make_output.sh [ C / Python ]
은 input에 있는 .c 혹은 .py 파일을 output에 출력해줍니다.
해당 입력 범위는 기본으로 50까지 이며, 이는 수정 가능합니다.
answer.c 혹은 answer.py를 이용해 정답을 넣어주세요.

1. check_cases.py
는 output에 있는 모든 케이스들에 대해 answer와 비교하여 ./result 디렉터리에 {case_name}.txt 를 생성합니다.
해당 txt에는 몇개 맞았고, 몇퍼센트 인지 그리고 어디서 틀렸는지도 포함하여 출력됩니다.
