#!/bin/bash
# 改完檔就自動跑測試，並把結果送進 Claude 的 context。
#
# 兩個關鍵：
#   1. 純文字 stdout 不會進到 context，只會寫進 debug log。必須用 JSON 的
#      hookSpecificOutput.additionalContext。
#   2. additionalContext 的值是「字串」。
# 輸出超過 10,000 字元會被改寫成檔案路徑＋預覽，所以先 tail 過。

cd "$CLAUDE_PROJECT_DIR" 2>/dev/null || cd "$(dirname "$0")/.."

OUT=$(./run-tests.sh 2>&1 | tail -5)

python3 - "$OUT" <<'PY'
import json
import sys

print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "PostToolUse",
        "additionalContext": "自動測試結果（由 hook 執行）：\n" + sys.argv[1],
    }
}))
PY
