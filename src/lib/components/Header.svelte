<script>
	import { page } from '$app/state';
	import './Header.css';

	const links = [
		{ href: '/', label: 'Home' },
		{ href: '/about', label: 'About' },
		{ href: '/work', label: 'Work' },
		{ href: '/coursework', label: 'Coursework' },
		{ href: '/selfhosted', label: 'Self Hosted' },
		{ href: '/contact', label: 'Contact' }
	];

	/** @param {string} href */
	function isActive(href) {
		return href === '/' ? page.url.pathname === '/' : page.url.pathname.startsWith(href);
	}
</script>

<header class="site-header">
	<div class="site-header-inner">
		<a class="site-title" href="/">James Dillon</a>

		<nav class="site-nav" aria-label="Primary">
			{#each links as link}
				<a
					class="nav-link"
					class:active={isActive(link.href)}
					aria-current={isActive(link.href) ? 'page' : undefined}
					href={link.href}>{link.label}</a
				>
			{/each}
		</nav>

		<div class="site-social">
			<a
				class="social-link"
				href="https://www.instagram.com/james.dillon15/"
				target="_blank"
				rel="noopener"
				aria-label="Instagram"
			>
				<svg viewBox="0 0 24 24" aria-hidden="true">
					<path d="M7.75 2C4.575 2 2 4.575 2 7.75v8.5C2 19.425 4.575 22 7.75 22h8.5C19.425 22 22 19.425 22 16.25v-8.5C22 4.575 19.425 2 16.25 2zm0 1.8h8.5c2.181 0 3.95 1.769 3.95 3.95v8.5c0 2.181-1.769 3.95-3.95 3.95h-8.5A3.95 3.95 0 0 1 3.8 16.25v-8.5A3.95 3.95 0 0 1 7.75 3.8m8.95 1.35a1.15 1.15 0 1 0 0 2.3 1.15 1.15 0 0 0 0-2.3M12 6.8A5.2 5.2 0 1 0 17.2 12 5.206 5.206 0 0 0 12 6.8m0 1.8A3.4 3.4 0 1 1 8.6 12 3.406 3.406 0 0 1 12 8.6" />
				</svg>
			</a>
			<a
				class="social-link"
				href="https://www.linkedin.com/in/jamesdillondev/"
				target="_blank"
				rel="noopener"
				aria-label="LinkedIn"
			>
				<svg viewBox="0 0 24 24" aria-hidden="true">
					<path d="M20.447 20.452H16.89V14.87c0-1.33-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.68H9.345V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455zM5.337 7.433a2.063 2.063 0 1 1 0-4.126 2.063 2.063 0 0 1 0 4.126M7.119 20.452H3.555V9h3.564zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0z" />
				</svg>
			</a>
			<a
				class="social-link"
				href="https://github.com/JamesDillonDev"
				target="_blank"
				rel="noopener"
				aria-label="GitHub"
			>
				<svg viewBox="0 0 24 24" aria-hidden="true">
					<path d="M12 .297a12 12 0 0 0-3.794 23.39c.6.111.82-.261.82-.577v-2.234c-3.338.726-4.042-1.416-4.042-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.744.083-.729.083-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.834 2.809 1.304 3.495.997.108-.776.419-1.305.762-1.605-2.665-.303-5.467-1.334-5.467-5.932 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.47 11.47 0 0 1 12 6.11c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.119 3.176.77.84 1.235 1.91 1.235 3.221 0 4.609-2.807 5.625-5.479 5.921.431.372.815 1.103.815 2.222v3.293c0 .319.216.694.825.576A12 12 0 0 0 12 .297" />
				</svg>
			</a>
		</div>
	</div>
</header>
