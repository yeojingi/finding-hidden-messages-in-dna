# Finding Hidden Messages

## Week 1
Ori로 추정되는 DNA Sequence 추적하기  

주어진 구간 안에서 존재하는 k 길이의 문자열의 발생 빈도를 찾는 함수를 만들고, 그것의 생물학적 의미를 스터디 함.

### 과제 사례
Vibrio cholerae 의 유전체에서 
|파일명|내용|결과|데이터 파일|
|------|---|---|---|
|PatternMatching.py|Vibrio cholerae의 유전체에서 "CTTGATCAT" 라는 문자열이 나오는 index를 출력|60039 98409 129189 152283 152354 152411 163207 197028 200160 357976 376771 392723 532935 600085 622755 1065555|week1/some-hidden-messages-are-more-surprising/dataset/Vibrio_cholerae.txt|
|EcoliFindClumps.py|E coli의 유전체를 길이 500의 winodw로 유전체를 sliding 하며 각 window 내에서 3회 이상 나타나는 길이 9 이상의 문자열의 갯수를 출력함| 1904|week1/some-hidden-messages-are-more-surprising/dataset/E_coli.txt|