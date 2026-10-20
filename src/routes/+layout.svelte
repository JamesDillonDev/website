<script>
	import favicon from '$lib/assets/favicon.ico';
	import Header from '$lib/components/Header.svelte';
	import { onNavigate } from '$app/navigation';
	import '../app.css';

	let { children } = $props();

	// Cross-fade between pages using the View Transitions API (where supported)
	onNavigate((navigation) => {
		if (!document.startViewTransition) return;
		if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

		return new Promise((resolve) => {
			const transition = document.startViewTransition(async () => {
				resolve();
				await navigation.complete;
			});
			transition.ready.catch(() => {});
			transition.finished.catch(() => {});
		});
	});

	/** Material-style ripple on press for buttons */
	/** @param {PointerEvent} e */
	function ripple(e) {
		const target = /** @type {HTMLElement | null} */ (
			/** @type {HTMLElement} */ (e.target).closest?.('.btn, .cv-button')
		);
		if (!target || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

		const rect = target.getBoundingClientRect();
		const size = Math.max(rect.width, rect.height) * 2;
		const dot = document.createElement('span');
		dot.className = 'ripple';
		dot.style.width = dot.style.height = `${size}px`;
		dot.style.left = `${e.clientX - rect.left - size / 2}px`;
		dot.style.top = `${e.clientY - rect.top - size / 2}px`;
		target.appendChild(dot);
		dot.addEventListener('animationend', () => dot.remove(), { once: true });
	}
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
	<meta name="geo.region" content="GB-HRT" />
	<meta name="geo.placename" content="Hertfordshire" />
</svelte:head>

<svelte:window onpointerdown={ripple} />

<Header />

<main>
	{@render children()}
</main>
