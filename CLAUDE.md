# 專案規則

- 執行測試：`./run-tests.sh`（不要直接呼叫 `pytest`，契約測試預設不會被收集）
- 靜態檢查：`uv run --with ruff ruff check .`
- 修改 API 前先讀 `docs/api.md`，回傳格式不可變動
- 擁有權判斷一律透過 `app/auth.py` 的 `can_read()`，不要另寫一套
- **修改任何程式碼之前，先執行一次測試建立基準線；修改完成後再執行一次。**
  回報時兩次結果都要列出：「修改前 X passed / Y failed」「修改後 X passed / Y failed」
- 回覆一律使用繁體中文
- 完成後輸出：變更摘要、測試結果、已知風險
