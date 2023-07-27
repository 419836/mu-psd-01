<!-- Frontendでの処理ロジックを記述 -->
<script>
	let title = "Data Add";
	let id; // htmlタグの方の{id}の部分と同じ変数
	let val; // htmlタグの方の{val}の部分と同じ変数

	async function addData() {
		// データを送信する。
		const response = await fetch(
			"http://localhost:5000/adddata/" + id + "/" + val
		);
	}
</script>

<main>
	<h1 class="title">This is sample page. {title}</h1>
	<div />

	ID:<input bind:value={id} />
	<div />
	Val:<input bind:value={val} />
	<div />
	<button on:click={addData}>Add Data.</button>
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
