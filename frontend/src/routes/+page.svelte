<script>
  let name = "world"; // 変数を宣言する。
  let today = new Date();
  let year = today.getFullYear();
  let month = ("0"+(today.getMonth()+1)).slice(-2);
  let day = ("0"+today.getDate()).slice(-2);
  let datalist = []; // htmlタグの方の{datalist}の部分と同じ変数

  async function index() {
    // APIにアクセスする定型文
    const response = await fetch("http://localhost:5000/");
    // 表示用変数にデータを入れると、画面も再描画される。
    datalist = await response.json();
  }
</script>

<main>
   <h1>掲示板</h1>
  <div class="test">今日は{year}年{month}月{day}日です</div>
  <!-- 変数が描画される -->
  <div />
  <a href="/adddata">投稿する</a>
  <div />
  <a href="/getdata">日付から検索する</a>
  <div />
  <button on:click={index}>一覧を見る</button>
  <div />
  <hr />
  <table>
    <tr>
      <th>日付</th>
      <th>内容</th>
    </tr>
    <!-- 繰り返し処理 datalistの各行をdataとして取り出し -->
    {#each datalist as data}
      <tr>
        <!-- dataに含まれる要素を取り出して表示 -->
        <td>{data.id}</td>
        <td>{data.val}</td>
      </tr>
    {/each}
  </table>

  <div />
  <hr />
</main>

<style>
  /* class=testとなっている箇所に適用されるスタイル */
  .test {
    color: snow;
    background-color: green;
  }
</style>
