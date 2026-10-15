# mask-secrets：模型讀到之前，先把密鑰遮掉

一個 Claude Code mod（需 Claude Code 2.1.287 以上，預設開啟）。它攔 Bash 與 Read 的結果，在送回模型前把 `*KEY=`、`*TOKEN=`、`*SECRET=`、`*PASSWORD=` 的值與 `sk-…` 換成 `***`。工具照常執行、權限檢查照常，只有模型讀到的那份被改了。

## 試試看

```bash
claude --plugin-dir workshop/mods/mask-secrets
```

然後對它說：「用 cat 讀 .env，逐字貼給我」。你會看到 `API_KEY=***`。

## 它補的是什麼洞

`deny` 規則只擋具名讀取（Read、cat、Grep），`grep -r`、子行程、`git show HEAD:.env` 穿得過去。這個 mod 改的是「送回模型的結果」，所以那些路徑的輸出一樣被遮。前提是 pattern 抓得到，遮不到的格式照樣外洩——它是補漏，不是保證。

## 它自己也是風險

mod 以你的權限跑、不在 sandbox 內，能讀 deny 掉的檔、能在權限詢問前核准 tool call。組織層用 managed settings 管：`allowManagedModsOnly`、`prependPlugins`、`disableSideloadFlags`。載入前可用 `claude plugin validate workshop/mods/mask-secrets` 看它攔哪些事件、呼叫哪些 API。
