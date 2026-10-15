# Agent Harness Lab

> A tiny Python order service used to practise **harness engineering** for coding agents:
> project rules, tool permissions, and verification loops. Three branches let you compare a
> bare repo with one that has a harness configured. All credentials in this repo are fake.

一個很小的 Python 訂單服務，用來練習 **Harness Engineering**——不是練寫程式，是練「怎麼把 agent 的工作環境設對」：規範檔、工具權限、驗證回路。

## 三個 branch

| Branch | 內容 | 用途 |
|---|---|---|
| `main` | **裸版**。只有程式與測試，沒有 `CLAUDE.md`、沒有 `.claude/` | 你的起點 |
| `harness` | **設定好的版本**＝ `main` ＋ 規範檔 ＋ 權限規則 ＋ hook ＋ skill（`/plan-first`）＋ 子代理（`reviewer`） | 對照組與參考答案 |
| `workshop` | **實戰版**＝ `harness` ＋ 更多模組、更多歷史包袱，Harness 已設好 | 實戰班：在既有系統上完成一次可交接的交付 |

看這兩版差在哪，一行就夠：

```bash
git diff main..harness
```

## 跑起來

需要 [uv](https://docs.astral.sh/uv/)。

```bash
git clone <this repo> && cd agent-harness-lab
./run-tests.sh
```

第一次在這個目錄開 Claude Code 時，**要接受信任對話框**，否則 `.claude/settings.json` 的 `allow` 規則會被忽略，每個指令都會跳出詢問。（`deny` 規則不受影響，未信任時照樣生效。）

在 `main` 與 `harness` 預期會看到 **3 failed, 5 passed**（共 8 個測試）——`app/orders.py` 有一個刻意留下的權限缺陷（`get_order()` 沒有檢查呼叫者是不是訂單擁有者），三個失敗的測試就是在抓它。在 `workshop` 這個缺陷已修好，測試全綠；任務另外發。

## 為什麼 `.env` 在版控裡

這不是意外，**請不要把它加進 `.gitignore`**。它是教材的一部分，內容全是假值（沒有任何一個是真實憑證）。把它拿掉，練習就做不了了。

## 練習

- 進階班（把裸版變成 Harness 版）：`harness` branch 的 `EXERCISES.md`。
- 實戰班（從 Issue 到可交付的 PR）：本分支的 [workshop/TASK.md](workshop/TASK.md)，另附 [審查分工卡](workshop/REVIEW_CARD.md) 與 [資安檢核表](workshop/SECURITY_CHECKLIST.md)。

## 授權

MIT，見 [LICENSE](LICENSE)。歡迎 fork 自己玩。
