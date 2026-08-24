# LearnStack (yameyaku.com) — 引き継ぎメモ

英語圏向けの学習ツールレビューサイト。海外アフィリエイトで収益化する。

- 公開URL: https://yameyaku.com
- リポジトリ: https://github.com/takeyone1967/learnstack （`main`ブランチ、`docs/`をGitHub Pagesで公開）
- ローカル: `C:\claude-test\yameyaku`

## 🔴 触ってはいけないもの

`drafts/coursera-career-certificates-2026.md`（記事10本目）は
**2026-08-28 00:00 UTC に別のクラウドセッション（session_01BJSeXi2UFGQdQddiTUKJeQ）が
自動で `content/` へ移動・ビルド・push する設定**になっている。
ローカル側で先に公開したり `drafts/` から動かしたりしないこと（クラウド側のトリガーと衝突する）。
状況確認が必要ならクラウドセッションにメッセージを送って聞く。

## 編集方針（README の Editorial policy と同じ）

- 虚偽の体験談は書かない。事実は裏取りしてから書く
- 全記事の冒頭にアフィリエイト開示を入れる
- 長所と短所を必ず併記する
- 公開ペースは週2〜3本

## 現在の状態（2026-08-25 時点）

### 公開済み記事 10本
`content/` に9本。10本目は上記のとおり 8/28 に自動公開予約中。

### ASP申請状況

| ASP / ブランド | 状態 |
|---|---|
| Coursera（Impact経由） | **申請済み・審査待ち**（2026-08-25 05:45 送信） |
| Speechify（直営フォーム） | 審査待ち継続中（8/9, 8/20 再送） |
| Impactマーケットプレイス全般 | **利用可能**（10,497ブランド閲覧・申請可） |
| PartnerStack → Surfer SEO | 却下（8/24） |
| Impact → Babbel直リンク | 却下（8/11） |

**注意**: Impactのホーム画面には「マーケットプレイスの申請 却下済み」というカードが今も残っているが、
実際にはマーケットプレイスもブランド申請も使える。このカードの表示だけで「使えない」と判断しないこと。

### Pinterest（アカウント: LearnStack / yonedatakeshi0195）

- 生成済み30枚（`pinterest-pins/output/`）。文言は `pinterest-pins/generate_pins.py` の `PINS` が原本
- **投稿済み27枚**
- **未投稿は coursera-certs-01/02/03 の3枚のみ**。記事10本目が公開される **8/28以降** に投稿する
- リンク先は `https://yameyaku.com/<slug>/`

投稿フォーマット（過去分と統一すること）:

- タイトル = `PINS` の headline から改行を除いたもの
- 説明文 = `PINS` の subtext を**そのまま**（補足を足さない）
- ボード = 言語学習系は `AI Language Learning Apps`、それ以外は `AI Tools for Learning & Productivity`

### GA4 / Search Console（8/22時点）

- Organic Search 流入はまだ0件（新規ドメインの助走期間、想定内）
- Search Console 表示回数262件・平均掲載順位66.3位。Coursera Plus記事が実クエリで表示され始めた
- 重複コンテンツ警告は canonical タグ追加で 8/23 修正済み、再検証待ち

## 次にやること

1. **Coursera の審査結果を待つ**（承認されたらリンクを各Coursera記事に差し込む）
2. **Impact の追加ブランド申請を検討**（下の候補表。ユーザー判断待ち）
3. Speechify の審査結果をフォロー
4. 8/28以降に Pinterest 残り3枚（coursera-certs系）を投稿
5. 9月中旬目安: GA4/Search Console データ再分析、次戦略を判断
6. 記事11本目以降の企画

### Impact 追加ブランド候補（2026-08-25 調査）

既存記事に導線があるのにASPが無いものを優先。

| ブランド | 報酬 | 該当記事 |
|---|---|---|
| **Udemy** | Course 10% / Sub 10-20% | AWS認定記事で「$12のUdemyコース」を主題に紹介済み。最優先 |
| mindhub™ by Pearson | 10% | AWS/IT認定の試験バウチャー |
| edX | 8% | Coursera比較記事の自然な相手 |
| DataCamp | 7.5-15% | Coursera vs Pluralsight（データ/テック系） |
| Educative | 20% | Pluralsight の代替（Pluralsight自体はImpactに無い） |
| **Preply** | 新規トライアル $10 / サブスク $50 | 言語学習3記事向け。単価が突出して高い |
| italki Global | $18/購入 | 同上 |
| British Council English Online | 10% | 英語学習 |
| Transkriptor / HappyScribe | 30% | 音声書き起こし。TTS記事に追記すれば導線になる |

**申請しないほうがよいもの**: EssayDone（AI Writer & Humanizer, 50%）。
報酬は高いが学術不正を助長するツールで、当サイトの編集方針と衝突する。

## ビルド手順

```bash
python3 build.py
```

`docs/` が再生成される。コミットして push すれば GitHub Pages に反映される。
