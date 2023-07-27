<!-- Frontendでの処理ロジックを記述 -->
<script>
	let title = "Data Get";
	let id; // htmlタグの方の{id}の部分と同じ変数
	let val; // htmlタグの方の{val}の部分と同じ変数

	async function getData() {
		// APIにアクセスする定型文
		const response = await fetch("http://localhost:5000/getdata/" + id);
		const text = await response.text();
		const json = JSON.parse(text);
		// 値を取得して画面の変数に入れると、画面描画も変わる。
		val = json.value;
	}
</script>

<main>
	<h1 class="title">This is sample page. {title}</h1>
	<div />
	ID:<input bind:value={id} />
	<button on:click={getData}>Get Data.</button>
	<div />
	<hr />
	Val:<input bind:value={val} />
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
</style>
