# Finding Hidden Messages

## Week 1
<p align="center"><img src="https://github.com/yeojingi/finding-hidden-messages-in-dna/blob/main/others/imgs/ori2.png" width="40%"></p>
<!-- ![ORI](https://github.com/yeojingi/finding-hidden-messages-in-dna/blob/main/others/imgs/ori2.png){: width="40%"}  -->
<p>Ori로 추정되는 DNA Sequence 추적하기. <br>
주어진 구간 안에서 존재하는 k 길이의 문자열의 발생 빈도를 찾는 함수를 만들고, 그것의 생물학적 의미를 스터디 함.</p>

### 과제 사례
|파일명|내용|결과|비고|
|------|---|---|---|
|[PatternMatching.py](https://github.com/yeojingi/finding-hidden-messages-in-dna/blob/main/week1/some-hidden-messages-are-more-surprising/PatternMatching.py)|Vibrio cholerae의 유전체에서 "CTTGATCAT" 라는 문자열이 나오는 index를 출력|60039 98409 129189 152283 152354 152411 163207 197028 200160 357976 376771 392723 532935 600085 622755 1065555|[데이터](https://github.com/yeojingi/finding-hidden-messages-in-dna/blob/main/week1/some-hidden-messages-are-more-surprising/dataset/Vibrio_cholerae.txt)|
|[EcoliFindClumps.py](https://github.com/yeojingi/finding-hidden-messages-in-dna/blob/main/week1/some-hidden-messages-are-more-surprising/EcoliFindClumps.py) |E coli의 유전체를 길이 500의 winodw로 유전체를 sliding 하며 각 window 내에서 3회 이상 나타나는 길이 9 이상의 문자열의 갯수를 출력함| 1904|[데이터](https://github.com/yeojingi/finding-hidden-messages-in-dna/blob/main/week1/some-hidden-messages-are-more-surprising/dataset/E_coli.txt)|


## Week 2 - Frequent words with mismatches
<p align="center"><img src="https://raw.githubusercontent.com/yeojingi/finding-hidden-messages-in-dna/main/others/imgs/ori3.png" width="40%"></p>
 <p><b>주어진 DNA 서열만으로 ORI의 위치를 추정할 수 있을까?</b><br>한 지점을 기준으로 3'->5'와 5'->3' 두 개의 방향으로 G, C의 개수 차이를 계산하여 비교함으로써 ORI 위치를 추정할 수 있음을 배웠다</p>
 <p>DNA 복제 과정에서 lagging strand의 경우, 단일 가닥으로 오랜 기간 노출되어 C가 T가 되는 deamination이 될 확률이 높아짐. 따라서 단일 가닥으로 존재하는 곳에서는 C의 비율이 G의 비율보다 작음.  <br>
 이 원리를 이용하여, DNA 가닥의 출발 지점부터 현재 지점까지의 G 개수 - C 개수 의 값 (<i>skew - 비대칭</i>)을 계산하고, 최소값이 나타나는 지점에 ori가 존재할 가능성이 높다는 것을 추정할 수 있음</p>
 <p>이러한 방법론은 <a href="https://pubmed.ncbi.nlm.nih.gov/8676740/">Lobry(1996)</a>에 의해 처음 제안되고, <a href="https://pubmed.ncbi.nlm.nih.gov/18660512/">Sernova and Gelfand(2008)</a>에 의해 알고리즘화 되었다고 함.</p>

### 과제 사례
|파일명|내용|결과|비고|
|------|---|---|---|
|[EcoliMininumSkew.py](https://github.com/yeojingi/finding-hidden-messages-in-dna/blob/main/week2/1.3_GC_contents/EcoliMininumSkew.py)|E coli 의 G, C 비대칭을 그래프로 만들고, 최저점이 찍히는 곳을 ori가 있는 곳이라고 추정함|![E coli](https://raw.githubusercontent.com/yeojingi/finding-hidden-messages-in-dna/main/others/imgs/ecoli_GCs.png)|[데이터](https://github.com/yeojingi/finding-hidden-messages-in-dna/blob/main/week2/1.3_GC_contents/data/E_coli.txt)|
|[FindDnaA.py](https://github.com/yeojingi/finding-hidden-messages-in-dna/blob/main/week2/1.6/FindDnaA.py)| Salmonella Enterica의 G, C 비대칭을 그래프로 만들고, 역시 최저점이 찍히는 곳을 ori가 있는 곳이라고 추정함|![Salmonella Enterica](https://raw.githubusercontent.com/yeojingi/finding-hidden-messages-in-dna/main/others/imgs/SalmonellaEnterica_GCs.png)|[데이터](https://github.com/yeojingi/finding-hidden-messages-in-dna/blob/main/week2/1.6/data/SalmonellaEnterica.txt)|
|[FrequentWordsWithMismatches(...).py](https://github.com/yeojingi/finding-hidden-messages-in-dna/blob/main/week2/1.4/FrequentWordsWithMismatchesAndReversed.py)|주어진 문자열에서 k 길이의 substring을 찾는다. 그리고 그 substring에 d 개의 오타(mismatch, 돌연변이)를 허용하여 가장 많이 등장하는 문자열을 출력함|TTTTA TAAAA|[데이터](https://github.com/yeojingi/finding-hidden-messages-in-dna/blob/main/week2/1.4/data/dataset_9_10.txt)|

## Week 3 - Frequent words with mismatches using Greedy Algorithms and Profiles

<p align="center"><img src="https://raw.githubusercontent.com/yeojingi/finding-hidden-messages-in-dna/main/others/imgs/similar.png" width="40%"></p>
<p>유전자에는 많은 돌연변이가 발생한다. 돌연변이로 인해 서로 많이 달라보이는 두 개의 서열이, 중간 지점의 서열을 찾음으로써 서로 유사하다는 것을 발견할 수도 있다.</p>
<p>위의 그림을 보면 AgAAgAAAGGttGGG 와 cAAtAAAAcGGGGcG는 hamming distance가 8로서 먼 것을 알 수 있다. <br> 그러나 AAAAAAAAGGGGGGG라는 서열을 보면 각각의 서열이 hamming distance가 각각 4, 4 인 것을 알 수 있다.</p>
<p>이를 통해 각 서열들의 비교로는 알 수 없는 frequent words가 존재할 수 있다는 것을 알 수 있다.</p>

### 과제 사례
|파일명|내용|결과|비고|
|------|---|---|---|
|[GreedyMotifSearch.py](https://github.com/yeojingi/finding-hidden-messages-in-dna/blob/main/week3/1.5/GreedyMotifSearch.py)|[Greedy motif search](https://www.mrgraeme.com/greedy-motif-search/)를 통해 서열들의 frequent words를 찾는다|||
|[GreedyMotifSearchWithPseudoCounts.py](https://github.com/yeojingi/finding-hidden-messages-in-dna/blob/main/week3/1.6/GreedyMotifSearchWithPseudoCounts.py)|Greedy motif search에 Laplace’s Rule of Succession을 추가해서 서열들의 frequent words를 찾는다|||

