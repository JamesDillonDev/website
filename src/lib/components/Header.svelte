<script>
	import { page } from '$app/state';
	import { goto } from '$app/navigation';
	import { onMount, tick } from 'svelte';
	import './Header.css';

	const links = [
		{ href: '/', label: 'Home' },
		{ href: '/about', label: 'About' },
		{ href: '/work', label: 'Work' },
		{ href: '/coursework', label: 'Coursework' },
		{ href: '/selfhosted', label: 'Projects' },
		{ href: '/contact', label: 'Contact' }
	];

	/** @param {string} href */
	function isActive(href) {
		return href === '/' ? page.url.pathname === '/' : page.url.pathname.startsWith(href);
	}

	/** @type {HTMLElement | undefined} */
	let nav = $state();
	let pill = $state({ x: 0, w: 0, visible: false, ready: false });

	async function movePill() {
		await tick();
		const el = nav?.querySelector('.nav-link.active');
		if (!nav || !(el instanceof HTMLElement)) {
			pill.visible = false;
			return;
		}
		pill.x = el.offsetLeft;
		pill.w = el.offsetWidth;
		pill.visible = true;
		el.scrollIntoView({ inline: 'nearest', block: 'nearest' });
	}

	// Drag the highlight along the nav; on release it snaps to the nearest link and navigates
	let dragging = $state(false);
	let moved = false;
	let startX = 0;
	let startPillX = 0;

	/** @param {PointerEvent} e */
	function dragStart(e) {
		const el = nav?.querySelector('.nav-link.active');
		if (!nav || !(el instanceof HTMLElement) || e.button !== 0) return;
		if (!(e.target instanceof Node) || !el.contains(e.target)) return;
		startX = e.clientX;
		startPillX = pill.x;
		moved = false;
		dragging = true;
		nav.setPointerCapture(e.pointerId);
	}

	/** @param {PointerEvent} e */
	function dragMove(e) {
		if (!dragging || !nav) return;
		const dx = e.clientX - startX;
		if (Math.abs(dx) > 4) moved = true;
		if (!moved) return;
		const last = /** @type {HTMLElement} */ (nav.lastElementChild);
		const max = last.offsetLeft + last.offsetWidth - pill.w;
		const min = /** @type {HTMLElement} */ (nav.querySelector('.nav-link')).offsetLeft;
		pill.x = Math.min(max, Math.max(min, startPillX + dx));
	}

	/** @param {PointerEvent} e */
	async function dragEnd(e) {
		if (!dragging || !nav) return;
		dragging = false;
		nav.releasePointerCapture?.(e.pointerId);
		if (!moved) return;
		const center = pill.x + pill.w / 2;
		const els = /** @type {HTMLAnchorElement[]} */ ([...nav.querySelectorAll('.nav-link')]);
		const nearest = els.reduce((best, el) =>
			Math.abs(el.offsetLeft + el.offsetWidth / 2 - center) <
			Math.abs(best.offsetLeft + best.offsetWidth / 2 - center)
				? el
				: best
		);
		if (nearest.classList.contains('active')) return movePill();
		pill.x = nearest.offsetLeft;
		pill.w = nearest.offsetWidth;
		await goto(nearest.getAttribute('href') ?? '/');
	}

	/** @param {MouseEvent} e */
	function swallowClick(e) {
		if (moved) {
			e.preventDefault();
			moved = false;
		}
	}

	$effect(() => {
		page.url.pathname;
		movePill();
	});

	onMount(() => {
		movePill().then(() => requestAnimationFrame(() => (pill.ready = true)));
		window.addEventListener('resize', movePill);
		document.fonts?.ready.then(movePill);
		return () => window.removeEventListener('resize', movePill);
	});
</script>

<header class="site-header">
	<div class="site-header-inner">
		<a class="site-title" href="/">James Dillon</a>

		<nav
			class="site-nav"
			class:dragging
			aria-label="Primary"
			bind:this={nav}
			onpointerdown={dragStart}
			onpointermove={dragMove}
			onpointerup={dragEnd}
			onpointercancel={dragEnd}
			onclickcapture={swallowClick}
			ondragstart={(e) => e.preventDefault()}
		>
			<span
				class="nav-pill"
				class:ready={pill.ready}
				aria-hidden="true"
				style:transform="translateX({pill.x}px)"
				style:width="{pill.w}px"
				style:opacity={pill.visible ? 1 : 0}
			></span>
			{#each links as link}
				<a
					class="nav-link"
					draggable="false"
					class:active={isActive(link.href)}
					aria-current={isActive(link.href) ? 'page' : undefined}
					href={link.href}>{link.label}</a
				>
			{/each}
		</nav>

		<div class="site-social">
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
			<a class="cv-button" class:active={isActive('/cv')} href="/cv">CV</a>
		</div>
	</div>
</header>
