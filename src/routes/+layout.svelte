<script>
	import favicon from '$lib/assets/favicon.svg';
	import Header from '$lib/components/Header.svelte';
	import '../app.css';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
	<meta name="geo.region" content="GB-HRT" />
  	<meta name="geo.placename" content="Hertfordshire" />
</svelte:head>

<Header />

{@render children()}
