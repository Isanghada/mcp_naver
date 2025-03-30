# MCP Server

Model Context Protocol을 활용한 Naver OpenAPI 사용을 위한 서버입니다.</br>
이 프로젝트는 일부 네이버 API와 상호작용을 도와줍니다!

---

- [MCP Server](#mcp-server)
  - [1. 설치](#1-설치)
  - [2. 네이버 API 등록](#2-네이버-api-등록)
  - [3. 실행](#3-실행)
  - [4. 사용 가능 API 목록](#4-사용-가능-api-목록)
    - [◼ 지역 검색](#-지역-검색)
    - [◼ 뉴스 검색](#-뉴스-검색)
    - [◼ 오타 변환](#-오타-변환)

---

### 1. 설치

- Git 레포지토리를 clone하여 프로젝트 생성

```bash
# Clone the repository
git clone https://github.com/Isanghada/mcp_naver.git

# Move project directory
cd mcp_naver

# Synchronize dependencies
uv sync --all-extras
```

---

### 2. 네이버 API 등록

- https://developers.naver.com/apps
- Application을 등록하여 API 호출을 위한 `Client ID`, `Client Secret` 발급
  ![alt text](/readme_asset/register_naver_api.png)

---

### 3. 실행

- uv를 사용하여 MCP 서버 등록
  - 발급받은 Naver Client ID, Naver Client Secret을 환경 변수로 전달

```bash
uv run mcp install server.py \
  --env-var NAVER_CLIENT_ID=<NAVER CLIENT ID> \
  --env-var NAVER_CLIENT_SECRET=<NAVER CLIENT SECRET>

uv run mcp install server.py --env-var NAVER_CLIENT_ID=<NAVER CLIENT ID> --env-var NAVER_CLIENT_SECRET=<NAVER CLIENT SECRET>
```

---

### 4. 사용 가능 API 목록

#### ◼ 지역 검색

- query 파라미터로 검색한 지역 검색 결과 반환

```python
search_local(query:str, display:int = 5, start:int = 1,sort:str = "random")

"""
query (str): Query to use for API
display (int, optional): Number of search results. Defaults to 5. Max to 5.
start (int, optional): Search Start Location. Defaults to 1. Max to 1.
sort (str, optional): Sorting Method ("random", "comment"). Defaults to "random".
"""
```

#### ◼ 뉴스 검색

- query 파라미터로 검색한 뉴스 검색 결과 반환

```python
search_news(query:str, display:int = 10, start:int = 1, sort:str = "sim")

"""
query (str): Query to use for API
display (int, optional): Number of search results. Defaults to 10. Max to 100
start (int, optional): Search Start Location. Defaults to 1. Max to 1000.
sort (str, optional): Sorting Method ("sim", "date"). Defaults to "sim".
"""
```

#### ◼ 오타 변환

- 한/영 오류로 인한 오타 query를 올바르게 변환

```python
search_typing_error_conversion(query:str)

"""
query (str): Query to use for API
"""
```
