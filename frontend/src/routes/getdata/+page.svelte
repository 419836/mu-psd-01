<!-- Frontendでの処理ロジックを記述 -->
<script>
  let title = "Data Get";
  let search; // htmlタグの方の{search}の部分と同じ変数
  let datalist = []; // htmlタグの方の{datalist}の部分と同じ変数

  async function findData() {
    // APIにアクセスする定型文
    const response = await fetch("http://localhost:5000/find/" + search);
    // 表示用変数にデータを入れると、画面も再描画される。
    datalist = await response.json();
  }
</script>

<main>
  <h1 class="title">This is sample page. {title}</h1>
  <div />
  Search:<input bind:value={search} />
  <button on:click={findData}>Get Data.</button>
  <div />
  <hr />
  <table>
    <tr>
      <th>id</th>
      <th>val</th>
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
  <a href="/">Top</a>
</main>

<!-- 画面の装飾をする -->
<style>
  /* class=titleとなっている箇所を装飾する */
  .title {
    color: blue;
    background-color: aquamarine;
  }
  th {
    color: snow;
    background-color: blue;
  }
</style>
