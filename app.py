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
        dataframe = pd.read_csv(uploaded_file)
    except Exception:
        st.error(
            "CSV 파일을 읽지 못했습니다. "
            "UTF-8로 저장된 올바른 CSV 파일인지 확인해 주세요."
        )
    else:
        row_count, column_count = dataframe.shape

        st.success("CSV 파일을 정상적으로 읽었습니다.")
        st.write(f"전체 행 수: {row_count}")
        st.write(f"전체 열 수: {column_count}")
        st.subheader("상위 20행 미리보기")
        st.dataframe(dataframe.head(20), width="stretch")
