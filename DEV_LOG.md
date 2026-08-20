# TidyCSV Development Log

## Current Project

TidyCSV

## Current Stage

MVP 개발

## Completed Features

현재 Repository에서 확인된 기능:

- CSV 파일 업로드
- UTF-8 CSV 읽기
- CP949 CSV 읽기
- 전체 행 수 표시
- 전체 열 수 표시
- 상위 20행 미리보기
- 완전히 빈 행 제거
- 완전히 동일한 중복 행 제거
- 첫 번째 중복 행 유지
- 빈 행 제거와 중복 제거 동시 사용
- 문자열 값의 앞뒤 공백 제거
- 문자열 내부 공백 유지
- 숫자 값과 자료형 유지
- 앞뒤 공백이 제거된 셀 수 표시
- 빈 행, 중복 행, 앞뒤 공백 제거 동시 사용
- 빈 문자열을 pandas 결측값으로 정리
- 앞뒤 공백 제거 후 비어 있는 문자열도 결측값으로 정리
- 결측값으로 정리된 셀 수 표시
- 빈 행, 중복 행, 앞뒤 공백 제거, 빈 문자열 정리 동시 사용
- 원본 DataFrame 보존
- 작업용 DataFrame 복사본 사용

## Concepts Learned

현재까지 학습한 개념:

### uploaded_file

사용자가 업로드한 CSV 파일 자체.

### DataFrame

pandas가 CSV를 읽어 프로그램에서 다룰 수 있도록 만든 표 형태 데이터.

### dataframe

현재 프로젝트에서 원본 데이터를 담는 변수.

### cleaned_dataframe

정리 작업을 수행하기 위한 작업용 복사본.

### copy()

원본 데이터를 보존하기 위해 복사본을 만드는 기능.

### if

특정 조건이 참일 때만 코드를 실행한다.

### dropna(how="all")

한 행의 모든 값이 비어 있을 때 해당 행을 제거한다.

### drop_duplicates()

완전히 동일한 중복 행을 제거한다.

### keep="first"

중복 데이터 중 첫 번째 행은 유지하고 이후 중복 행을 제거한다.

### string

글자 형태의 데이터이며 Python에서는 `str`로 표현한다.

### strip()

문자열 내부 공백은 유지하고 앞과 뒤의 공백만 제거한다.

### isinstance(value, str)

현재 셀의 값이 문자열인지 확인하여 숫자에는 `strip()`을 적용하지 않도록 한다.

### DataFrame.map()

DataFrame의 각 셀에 같은 검사나 변환을 적용한다.

### 빈 문자열

문자열 안에 글자가 하나도 없는 `""` 값을 뜻한다.

### pd.NA

pandas에서 값이 없다는 것을 나타내는 결측값이다.

### replace()

DataFrame 안에서 특정 값을 찾아 다른 값으로 바꾼다.

## Current Understanding

사용자는 현재 다음 개념을 기본적으로 이해하고 있다.

- 원본과 복사본의 차이
- 원본을 보존하는 이유
- 중복 데이터의 의미
- 완전히 동일한 행만 중복으로 판단한다는 점
- `keep="first"`가 첫 번째 값을 남긴다는 의미
- 문자열과 숫자 데이터가 서로 다른 종류라는 점
- `strip()`이 앞뒤 공백만 제거하고 내부 공백은 유지한다는 점
- `isinstance(value, str)`가 문자열 여부를 확인한다는 점
- 공백만 있는 문자열은 `strip()` 후 빈 문자열이 될 수 있다는 점
- CSV를 읽을 때부터 비어 있던 셀은 이미 결측값일 수 있다는 점

아직 Python 문법이나 코드 전체 구조에는 익숙하지 않다.

따라서 앞으로도 개발 실력 향상을 우선한다.

## Current Tech Stack

- Python 3.11
- Streamlit
- pandas
- Git
- GitHub
- Windows

## Development Environment

프로젝트는 두 장소에서 개발한다.

- 회사 Windows PC
- 집 Windows 노트북

GitHub의 `origin/main`을 두 환경 사이의 공용 코드 기준으로 사용한다.

## Important Rule

Codex의 대화 기억을 프로젝트의 공식 기록으로 사용하지 않는다.

프로젝트의 공식 상태는 다음을 기준으로 판단한다.

1. Git Repository
2. `PROJECT_RULES.md`
3. `DEV_LOG.md`

## Next Candidate Task

다음 후보 작업은 아직 정하지 않았다.

새 기능은 사용자의 명시적인 시작 요청 전에는 구현하지 않는다.

## Current Learning Method

Understand Feature → Show Core Code → User Types Code → Review → Run → Understand Concepts → Quiz → Edit → Commit → Push

목표는 빠른 개발이 아니라, 기능 하나를 만들 때마다 코드 흐름과 핵심 개념을 이해하면서 개발 실력을 쌓는 것이다.

다음 기능부터 오늘 배우는 핵심 코드는 Codex가 위치와 코드를 안내하고 사용자가 VS Code에서 직접 입력한다.

## Last Update

2026-08-20
