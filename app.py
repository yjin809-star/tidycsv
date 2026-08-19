import pandas as pd
import streamlit as st


st.set_page_config(page_title="TidyCSV")

st.title("TidyCSV")
st.write("CSV 파일을 업로드하면 상위 20행을 미리 볼 수 있습니다.")

uploaded_file = st.file_uploader(
    "CSV 파일 업로드",
    type=["csv"],
    accept_multiple_files=False,
)

if uploaded_file is None:
    st.info("미리 볼 CSV 파일을 업로드해 주세요.")
else:
    try:
        dataframe = pd.read_csv(
            uploaded_file,
            encoding="utf-8-sig",
            skip_blank_lines=False,
        )
    except UnicodeDecodeError:
        uploaded_file.seek(0)

        try:
            dataframe = pd.read_csv(
                uploaded_file,
                encoding="cp949",
                skip_blank_lines=False,
            )
        except Exception:
            dataframe = None
    except Exception:
        dataframe = None

    if dataframe is None:
        st.error(
            "CSV 파일을 읽지 못했습니다. "
            "UTF-8 또는 CP949로 저장된 올바른 CSV 파일인지 확인해 주세요."
        )
    else:
        row_count, column_count = dataframe.shape

        st.success("CSV 파일을 정상적으로 읽었습니다.")
        st.write(f"전체 행 수: {row_count}")
        st.write(f"전체 열 수: {column_count}")
        st.subheader("원본 데이터 상위 20행")
        st.dataframe(dataframe.head(20), width="stretch")

        remove_empty_rows = st.checkbox("빈 행 제거")
        remove_duplicate_rows = st.checkbox("중복 행 제거")
        remove_surrounding_whitespace = st.checkbox("앞뒤 공백 제거")

        cleaned_dataframe = dataframe.copy()

        if remove_empty_rows:
            cleaned_dataframe = cleaned_dataframe.dropna(how="all")

        removed_empty_row_count = row_count - len(cleaned_dataframe)

        row_count_before_duplicate_removal = len(cleaned_dataframe)

        if remove_duplicate_rows:
            cleaned_dataframe = cleaned_dataframe.drop_duplicates(keep="first")

        trimmed_cell_count = 0

        if remove_surrounding_whitespace:
            cells_with_surrounding_whitespace = cleaned_dataframe.map(
                lambda value: isinstance(value, str) and value != value.strip()
            )
            trimmed_cell_count = int(cells_with_surrounding_whitespace.sum().sum())
            cleaned_dataframe = cleaned_dataframe.map(
                lambda value: value.strip() if isinstance(value, str) else value
            )

        cleaned_row_count = len(cleaned_dataframe)
        removed_duplicate_row_count = (
            row_count_before_duplicate_removal - cleaned_row_count
        )

        st.subheader("정리 결과")
        st.write(f"정리 전 행 수: {row_count}")
        st.write(f"정리 후 행 수: {cleaned_row_count}")
        st.write(f"제거된 빈 행 수: {removed_empty_row_count}")
        st.write(f"제거된 중복 행 수: {removed_duplicate_row_count}")
        st.write(f"앞뒤 공백이 제거된 셀 수: {trimmed_cell_count}")
        st.subheader("데이터 정리 상위 20행")
        st.dataframe(cleaned_dataframe.head(20), width="stretch")
