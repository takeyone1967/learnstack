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

### 記事 12本

`content/` に11本（公開済み）。残り1本は上記のとおり 8/28 に自動公開予約中。

8/25に2本追加した。どちらもCourseraクラスターの強化。

- **Coursera vs edX in 2026**（`coursera-vs-edx`）
  課金モデルの違い（Coursera=完了まで月額課金 / edX=買い切り）を軸に、
  学習ペースが不規則な人にはedXが構造的に安いという結論を出した。
  他サイトが書いていないedXの所有権変遷（Harvard/MITの非営利 → 2021年に2Uが$800Mで買収 →
  2024年7月Chapter 11 → 同年9月に投資会社所有の非公開企業として再建）も事実確認のうえ記載。
- **Coursera Free Courses in 2026**（`coursera-free-courses`）
  無料の3ルート（audit / 7日間トライアル / 財政援助）を整理。差別化点は
  **auditがSpecializationとProfessional Certificateでは使えない**という制約を正面から扱ったこと
  （Google証明書など人気プログラムは対象外）。"free"は検索ボリュームが大きくトラフィック獲得向き。

### ASP申請状況

| ASP / ブランド | 状態 |
|---|---|
| Coursera（Impact経由） | **申請済み・審査待ち**（2026-08-25 05:45 送信） |
| Speechify（直営フォーム） | 審査待ち継続中（8/9, 8/20 再送） |
| Impactマーケットプレイス全般 | **利用可能**（10,497ブランド閲覧・申請可） |
| PartnerStack → Surfer SEO | 却下（8/24） |
| Impact → Babbel直リンク | 却下（8/11） |

**Impactの正確な状態**（8/25に検証）:

- マーケットプレイスの**閲覧はできる**（10,497ブランドを検索・比較できる）
- ただし**申請はできない**。ブランド詳細を開くと「まだ応募承認前です」と出て申請ボタンが無効。
  ホーム画面の「マーケットプレイスの申請 却下済み」は生きている情報だった
- **抜け道**: 各ブランドの公式サイトにあるアフィリエイト申請リンク（ブランド固有の招待URL）から入れば、
  マーケットプレイス承認を経ずに申請できる。Courseraはこの経路で申請が通った

## 🔴 ASP申請はトラフィック要件を満たすまで保留（8/25判断）

Udemyの参加要件を確認したところ、**直近3ヶ月で月間500ユニークビジター以上、
またはSNSフォロワー500人以上**が条件で、「新規サイト・トラフィックが安定しないサイトは却下する」と明記されている。

LearnStackの現状はOrganic流入0件・Pinterestフォロワー0人で、**要件を満たしていない**。
この基準は業界標準的なので edX・DataCamp・Preply なども同様と考えられる。

既にImpact全般・Babbel・Surferで3連続却下されており、ここで却下履歴を積み増すのは不利。
**トラフィックが月間500UVに届くまで、新規ASP申請は行わない。**
先にやるべきはコンテンツとPinterest経由の流入を積むこと。

### Pinterest（アカウント: LearnStack / yonedatakeshi0195）

- 生成済み36枚（`pinterest-pins/output/`）。文言は `pinterest-pins/generate_pins.py` の `PINS` が原本
- **投稿済み27枚**
- **未投稿9枚**:
  - `coursera-edx-01/02/03` → 記事は公開済みなので**いつでも投稿できる**
  - `coursera-free-01/02/03` → 記事は公開済みなので**いつでも投稿できる**
  - `coursera-certs-01/02/03` → 予約記事が公開される **8/28以降**に投稿する
- リンク先は `https://yameyaku.com/<slug>/`

**ピンを再生成するときの注意**: `generate_pins.py` を実行すると全枚数が再生成され、
cairosvgのバージョン差で**既存PNGがバイナリだけ変わる**（SVGは無変更＝描画内容は同一）。
投稿済み画像を差し替える必要はないので、`git checkout -- output/` で既存分の差分を捨て、
新規ファイルだけをコミットすること。

**🔴 既知の不具合（未解決）**: 8/25に9枚を連続投稿したあと、**Pinterest全体がブラウザで
描画されなくなった**。ピン作成ツールだけでなくプロフィールページもヘッダーだけ表示され、
本体が空白のまま（JSコンソールにエラーは出ない）。1時間後に再試行しても回復しなかった。
連続投稿によるレート制限かボット検知の可能性が高い。

**対処**: 復旧しないうちに何度も試さないこと（アカウントに悪影響を与えかねない）。
**次回は1日以上空けてから試す**こと。また、9枚を一気に投稿するのは避け、数枚ずつに分けたほうがよい。

投稿フォーマット（過去分と統一すること）:

- タイトル = `PINS` の headline から改行を除いたもの
- 説明文 = `PINS` の subtext を**そのまま**（補足を足さない）
- ボード = 言語学習系は `AI Language Learning Apps`、それ以外は `AI Tools for Learning & Productivity`

### GA4 / Search Console（8/22時点）

- Organic Search 流入はまだ0件（新規ドメインの助走期間、想定内）
- Search Console 表示回数262件・平均掲載順位66.3位。Coursera Plus記事が実クエリで表示され始めた
- 重複コンテンツ警告は canonical タグ追加で 8/23 修正済み、再検証待ち

## 次にやること

**最優先はトラフィックを作ること**。ASP申請は月間500UVに届いてから再開する（上記の判断を参照）。

1. **Pinterest 未投稿6枚を投稿**（`coursera-edx` と `coursera-free`。記事は両方公開済み）
   → ただし上記の不具合のため**8/26以降に、数枚ずつ分けて**投稿すること
2. **記事13本目以降を書く**（週2〜3本ペース。Courseraクラスターを厚くするのが有効）
3. 8/28以降に Pinterest `coursera-certs` 3枚を投稿
4. **Coursera の審査結果を待つ**（承認されたらリンクを各Coursera記事に差し込む）
5. Speechify の審査結果をフォロー
6. 9月中旬目安: GA4/Search Console データ再分析。**月間500UVに届いたら**下の候補表で申請を再開
7. Pinterestのフォロワーを増やす（500人が多くのASPの代替基準になる）

### 記事13本目以降のネタ候補

Courseraクラスターがトラクションを持ち始めているので、当面はここを厚くするのが効率的。

- Coursera vs Udacity（比較シリーズの継続。Udacityは高額なので価格の切り口が立つ）
- Google Career Certificates を単体で深掘り（8/28公開の記事から内部リンクを流せる）
- Coursera vs LinkedIn Learning（法人・社会人層の検索需要）
- Babbel以外の言語アプリ単体レビュー（言語クラスターは3記事で止まっている）
- edX MicroMasters 深掘り（edX記事で触れた単位取得パスは掘り下げる価値がある）

### Impact 追加ブランド候補（2026-08-25 調査・**申請は500UV到達後**）

既存記事に導線があるのにASPが無いもの。申請するときは各ブランドの**公式サイトのアフィリエイトページ**から
入ること（Impactマーケットプレイス経由では申請ボタンが無効なため）。

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
