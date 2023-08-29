<!-- Frontendでの処理ロジックを記述 -->
<script>
  let title = "Data Add";
  let id; // htmlタグの方の{id}の部分と同じ変数
  let val; // htmlタグの方の{val}の部分と同じ変数
  let msg = ""; // メッセージ表示用変数
  let date = new Date();
  let year = date.getFullYear();
  let month = ("0"+(date.getMonth()+1)).slice(-2);
  let day = ("0"+date.getDate()).slice(-2);
  let hour = date.getHours();
  let minite = date.getMinutes();
  let second = date.getSeconds();
  let today = `${year}年${month}月${day}日${hour}時${minite}分${second}秒`;

  async function addData() {
    // データを送信する。
    const response = await fetch(
      "http://localhost:5000/adddata/" + today + "/" + val
    );
    val = ""; // 登録したら入力内容クリア
    msg = "Data added.";
  }
</script>

<main>
  <h1 class="title">投稿する</h1>
  <div />
  内容:<input bind:value={val} />
  <div />
  <button on:click={addData}>Add Data.</button>
  <div />
  <div>{msg}</div>
  <div />
  <hr />
  <a href="/">Top</a>
</main>

<!-- 画面の装飾をする -->
<style>
  /* class=titleとなっている箇所を装飾する */
  .title {
    color: green;
    background-color: lime;
  }
</style>
