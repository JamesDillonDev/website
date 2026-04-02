<script>
	import favicon from '$lib/assets/favicon.ico';
	import Header from '$lib/components/Header.svelte';
	import { fly, scale } from 'svelte/transition';
	import '../app.css';
	import './layout.css';

	let { children } = $props();
	let quickLinksOpen = $state(false);

	const serviceLinks = [
		{
			href: 'https://admin.jamesdillon.uk',
			label: 'Nginx Proxy Manager',
			shortLabel: 'NP'
		},
		{
			href: 'https://graph.jamesdillon.uk',
			label: 'Grafana',
			shortLabel: 'GR'
		},
		{
			href: 'https://home.jamesdillon.uk',
			label: 'Home Assistant',
			shortLabel: 'HA'
		},
		{
			href: 'https://jellyfin.jamesdillon.uk',
			label: 'Jellyfin Media Server',
			shortLabel: 'JF'
		},
		{
			href: 'https://vpn.jamesdillon.uk',
			label: 'WireGuard VPN',
			shortLabel: 'WG'
		},
		{
			href: 'https://mail.jamesdillon.uk',
			label: 'Roundcube Email',
			shortLabel: 'ML'
		}
	];

</script>

<svelte:head>
	<link rel="icon" href={favicon} />
	<meta name="geo.region" content="GB-HRT" />
  	<meta name="geo.placename" content="Hertfordshire" />
</svelte:head>

<Header />

<aside class:open={quickLinksOpen} class="quick-links-dock">
	{#if quickLinksOpen}
		<div
			class="quick-links-panel"
			in:fly={{ y: 26, x: -10, duration: 320, opacity: 0.2 }}
			out:scale={{ start: 0.9, duration: 180 }}
		>
			<button
				class="quick-links-close"
				type="button"
				aria-label="Collapse quick links"
				onclick={() => (quickLinksOpen = false)}
			>
				<span aria-hidden="true">×</span>
			</button>
			<p class="quick-links-eyebrow">Services</p>
			<nav aria-label="Service links">
				{#each serviceLinks as link, index}
					<a
						class="quick-link"
						style={`--quick-link-delay: ${index * 45}ms;`}
						href={link.href}
						target="_blank"
						rel="noopener noreferrer"
					>
						<span class="quick-link-badge" aria-hidden="true">{link.shortLabel}</span>
						<span>{link.label}</span>
					</a>
				{/each}
			</nav>
		</div>
	{/if}

	{#if !quickLinksOpen}
		<button
			class="quick-links-toggle"
			type="button"
			aria-expanded={quickLinksOpen}
			aria-label="Expand quick links"
			onclick={() => (quickLinksOpen = true)}
		>
			<span class="toggle-icon" aria-hidden="true">≡</span>
			<span>Links</span>
		</button>
	{/if}
</aside>

{@render children()}