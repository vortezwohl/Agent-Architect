<div align="center">

# Agent Architect

**面向程式設計智能體的架構護欄。**

*你的智能體已經在作出架構決策。<br />
不要讓它悄無聲息地作出這些決定。*

[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-agent--architect-111827?style=flat-square)](https://github.com/vortezwohl/Agent-Architect/tree/main/skills/agent-architect)
[![MIT License](https://img.shields.io/badge/License-MIT-22c55e?style=flat-square)](https://github.com/vortezwohl/Agent-Architect/blob/main/LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/vortezwohl/Agent-Architect?style=flat-square&label=Stars)](https://github.com/vortezwohl/Agent-Architect/stargazers)

<br />

> <strong>不讓架構偶然產生。</strong><br />
> <strong>不讓抽象源於臆測。</strong>

[安裝](#安裝) &middot; [問題所在](#問題所在) &middot; [對比差異](#對比差異) &middot; [決策協議](#決策協議)

</div>

<h4 align="center">
  <p>
    <a href="https://github.com/vortezwohl/Agent-Architect/blob/main/README.md">English</a> |
    <b>繁體中文</b> |
    <a href="https://github.com/vortezwohl/Agent-Architect/blob/main/i18n/README_zh-hans.md">简体中文</a> |
    <a href="https://github.com/vortezwohl/Agent-Architect/blob/main/i18n/README_ja-jp.md">日本語</a>
  </p>
</h4>

---

## 問題所在

大多數使用者並不會要求智能體作出架構決策。

他們要求它完成一般工作：

```text
新增一個用於下載發票的端點。
建立一個設定頁面。
將此服務接入新的提供者。
重構這個模組。
讓此功能具備可擴充性。
```

智能體寫下第一行程式碼之前，就已經開始決定：

- 哪個模組擁有該行為與狀態。
- 哪些相依性會跨越邊界。
- 哪些失敗路徑會成為公開行為。
- 直接實作、抽象或框架擴充是否有充分理由。
- 這項改動將如何演進、遷移、回滾與驗證。

這些都是架構決策。

沒有明確協議時，智能體通常會以三種方式失敗：

<table>
<tr>
<th align="left">失敗方式</th>
<th align="left">會發生什麼</th>
</tr>
<tr>
<td><strong>偶然架構</strong></td>
<td>智能體把功能直接寫進最近的檔案。還沒有人為邊界命名，相依性、狀態和錯誤路徑就已經擴散。</td>
</tr>
<tr>
<td><strong>臆測抽象</strong></td>
<td>智能體看見一個可能的未來，在真正的變化出現前就建立介面、工廠、登錄表、事件或繼承體系。</td>
</tr>
<tr>
<td><strong>斷言式驗證</strong></td>
<td>智能體沒有證明行為、相容性、失敗處理或剩餘風險，便宣稱重構乾淨或已完成。</td>
</tr>
</table>

**Agent Architect** 是非平凡程式設計請求與結構複雜度之間的護欄。

它促使智能體檢視現實、選擇理由最充分的最小設計，並在複雜度擴散前報告證據。

---

## 對比差異

### 使用 Agent Architect 前

```text
使用者：「新增一個用於下載發票的端點。」

智能體：寫一個處理器，直接存取持久化層並呼叫儲存，
內聯加入授權，再為「未來格式」建立 ExportFactory，
然後報告該端點已完成。
```

### 使用 Agent Architect 後

```text
使用者：「新增一個用於下載發票的端點。」

智能體：
1. 檢查現有發票歸屬、授權、儲存、呼叫端、
   錯誤處理和測試。
2. 說明實際改動：為一個現有發票產物新增一個 HTTP 入口。
3. 對比直接呼叫應用服務與新增匯出層。
4. 當只有一種格式和一條儲存路徑時，保留直接設計。
5. 記錄擷取觸發條件：同一應用操作背後有多個獨立變化的匯出
   格式或儲存提供者。
6. 驗證授權、發票缺失、儲存失敗和既有發票流程。
```

結果並不是更少的工程工作。

而是**具有明確決策、更小影響範圍和驗證路徑的工程工作**。

---

## 決策協議

```text
收到一項非平凡的程式設計請求
      |
      v
檢查儲存庫和目前行為
      |
      v
說明已證實的改動、穩定核心、約束與失敗路徑
      |
      +-- 沒有獨立變化的證據？
      |     `-- 保留直接設計，並記錄擷取觸發條件。
      |
      v
將最小直接方案與候選結構進行比較
      |
      v
拒絕不必要的介面、工廠、包裝器、事件和繼承
      |
      v
檢查所有權、生命週期、API 方向、交易、並行、
回滾、可觀測性和框架慣例
      |
      v
實作一個最小且已驗證的切片
      |
      v
報告證據、決策、已執行驗證和剩餘風險
```

### 不可妥協的規則

- 在說明哪些內容獨立變化、哪些內容保持穩定之前，不要產生結構。
- 未說明它隔離的具體變化及增加的成本前，不要引入介面、工廠、包裝器、事件、繼承層級、全域物件或框架層。
- 不要把不確定性轉化為臆測式抽象。
- 沒有傳遞語義時，不要把事件稱為非同步設計。
- 不要用 Singleton 規避相依性注入。
- 當組合、回呼或直接函式更清楚時，不要使用繼承。
- 不要把未經驗證的實作或重構稱為完成。

---

## 智能體會產出什麼

對於每項非平凡功能、整合、設計或重構，Agent Architect 都會產生可稽核記錄：

```text
01. 設計診斷
    目標、非目標、儲存庫證據、呼叫端、穩定核心、
    變化點、異味和約束。

02. 備選方案
    最小直接設計、候選結構、
    被拒絕的備選方案和持續性的結構成本。

03. 決策
    選定設計、公開 API 與相依性影響、
    遷移與回滾影響，或經過充分理由支持的不使用模式的決定。

04. 驗證
    正常、邊界、失敗、整合和運行檢查；
    實際執行的驗證；以及剩餘不確定性或風險。
```

---

## 何時使用

在**實作或審查任何非平凡改動之前**使用 Agent Architect，包括：

- 跨越模組、層或服務的新功能。
- 改變相依性、所有權、狀態或生命週期的重構。
- 第三方整合和遺留系統調適。
- 非同步、事件、交易、重試、快取或授權工作。
- 要求讓系統「乾淨」「可擴充」「可延展」或「面向未來」的請求。
- 程式碼看似合理、但其結構決策是隱含的 PR 審查。

> [!TIP]
> 不要等使用者提出架構問題。請將此技能加入處理功能工作和結構性改動的智能體工作流程。

---

## 安裝

### Codex

```text
$skill-installer install https://github.com/vortezwohl/Agent-Architect/tree/main/skills/agent-architect
```

安裝後重新啟動 Codex。

### 其他相容 Agent Skills 的工具

將 `skills/agent-architect/` 複製到工具支援的技能目錄，然後呼叫：

```text
agent-architect
```

> [!IMPORTANT]
> 安裝技能前請先閱讀。技能是可執行的智能體指引：請檢查其說明、隨附參考資料、指令碼和信任邊界。

---

## 使用方法

向你的程式設計智能體提出：

```text
在實作或審查這項非平凡改動之前使用 $agent-architect。
檢查儲存庫，選擇理由最充分的最小設計，
然後實作並驗證它。
```

範例：

```text
在新增此付款提供者之前使用 $agent-architect。

使用 $agent-architect 審查此功能，尋找偶然架構
和臆測抽象。

在重構此服務邊界之前使用 $agent-architect。
保持行為不變，並報告遷移和回滾影響。

使用 $agent-architect 判定此整合是否需要調適器、
直接相依性或框架擴充。
```

---

## 模式是工具，而非產品

Agent Architect 涵蓋全部 23 種 GoF 模式，但它並不從模式目錄開始。

它從證據開始：**什麼會變化、誰擁有它、什麼會失敗，以及什麼必須保持穩定。**

<details>
<summary><b>建立型決策</b></summary>

- Factory Method
- Abstract Factory
- Builder
- Prototype
- Singleton scope

</details>

<details>
<summary><b>結構型決策</b></summary>

- Adapter
- Bridge
- Composite
- Decorator
- Facade
- Flyweight
- Proxy

</details>

<details>
<summary><b>行為型決策</b></summary>

- Chain of Responsibility
- Command
- Interpreter
- Iterator
- Mediator
- Memento
- Observer
- State
- Strategy
- Template Method
- Visitor

</details>

<details>
<summary><b>關鍵模式邊界</b></summary>

| 不要混淆 | 與 |
| --- | --- |
| Decorator | Proxy 或 Adapter |
| Facade | Mediator |
| Factory Method | Abstract Factory、Builder 或 Prototype |
| Strategy | State 或 Template Method |
| Observer | Chain of Responsibility 或 Command |
| Composite | Decorator |

模式應按**意圖、協作者、生命週期、變化和失敗行為**選擇——絕不能只依據類別圖。

</details>

---

## 此技能不是什麼

| 不是這個 | 而是這個 |
| --- | --- |
| 模式百科全書 | 面向程式設計智能體的架構決策協議 |
| 儀式產生器 | 防止偶然複雜度的護欄 |
| 預設採用「乾淨架構」 | 明確分析邊界、相依性和生命週期 |
| 增加層級的理由 | 沒有證據時保留直接設計的許可 |
| 工程所有權的替代品 | 讓智能體產出結構可稽核、可驗證的方法 |

---

## 儲存庫結構

```text
skills/
`-- agent-architect/
    |-- SKILL.md
    |-- agents/
    |   `-- openai.yaml
    `-- references/
        |-- decision-protocol.md
        |-- gof-patterns.md
        `-- source-article.md
```

- `SKILL.md` - 運行規則和必需的設計記錄
- `decision-protocol.md` - 具有約束力的診斷、選擇、重構和審查關卡
- `gof-patterns.md` - 模式意圖、權衡、誤用情境和驗證指南
- `source-article.md` - AI 程式設計時代的架構原則

---

## 標準

功能並不會因為能編譯就算完成。

重構並不會因為程式碼看起來更乾淨就算完成。

架構決策只有能回答下列問題時才算完成：

```text
什麼證據證明此結構合理？
為什麼直接替代方案不足？
什麼會獨立變化？
我們拒絕了什麼，為什麼？
行為如何得到驗證？
還剩下什麼風險？
```

> **為下一次經過驗證的改動設計——而不是為某個模式名稱設計。**

---

## 貢獻

貢獻應改進**判斷力**，而不是增加儀式。

有價值的貢獻包括：

- 面向真實功能與架構決策的證據關卡。
- 更清楚的模式邊界和拒絕條件。
- 可重現的偶然架構與臆測抽象範例。
- 面向生命週期、並行、交易、遷移和回滾的驗證指南。
- 能讓智能體更不容易擴散結構複雜度的修正。

在發起改動前，請先問：

```text
這是否改進了智能體在程式碼擴散前可作出的決策？
這項改進能否驗證？
它是否在不增加臆測流程的情況下提供指引？
```

---

## 授權條款

MIT。請參閱 [LICENSE](../LICENSE)。

---

<div align="center">

### 不要讓你的程式設計智能體悄無聲息地設計你的系統。

<strong>點個 Star。Fork 它。在下一次非平凡改動前加入它。</strong>

</div>