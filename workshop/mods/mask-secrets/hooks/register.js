// mask-secrets：Bash／Read 的結果送回模型前，把像密鑰的值換成 ***
// 這是「什麼離開了這台機器」的第三層機制：模型根本沒看到原值
const SECRET_LINE = /\b([A-Z0-9_]*(KEY|TOKEN|SECRET|PASSWORD|PASSWD))\s*=\s*\S+/g
const SK_TOKEN = /\bsk-[A-Za-z0-9_-]{8,}/g

function mask(text) {
  if (typeof text !== 'string') return { text, hits: 0 }
  let hits = 0
  const out = text
    .replace(SECRET_LINE, (m, key) => { hits += 1; return key + '=***' })
    .replace(SK_TOKEN, () => { hits += 1; return 'sk-***' })
  return { text: out, hits }
}

export function register(on) {
  on('tool.call', { tool: ['Bash', 'Read'] }, async ($, e, next) => {
    const r = await next(e)                      // 先讓工具照常跑（權限檢查也照常）
    if (r.deny || r.isError || !r.result) return r
    let hits = 0
    let result = r.result
    if (e.tool === 'Bash') {
      const m = mask(result.stdout); hits = m.hits
      result = { ...result, stdout: m.text }
    } else if (result.type === 'text' && result.file) {
      const m = mask(result.file.content); hits = m.hits
      result = { ...result, file: { ...result.file, content: m.text } }
    }
    if (hits > 0) $.ui.log('mask-secrets: 遮掉 ' + hits + ' 個值，模型沒看到原文')
    return { ...r, result }                      // 模型讀到的是遮罩後的版本
  })
}
