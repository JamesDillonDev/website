<script>
	import heroImage from '$lib/assets/me.jpg';
	import openHighwaysPreview from '$lib/assets/openhighway.png';
	import './home.css';

	const heroSlides = [
		{
			image: heroImage,
			alt: 'Portrait of James Dillon',
			heading: 'Welcome',
			body: 'Find out more about me and my work.'
		},
		{
			image: openHighwaysPreview,
			alt: 'OpenHighways — a live map of UK traffic cameras',
			heading: 'Check out my new project: OpenHighways',
			body: 'A free, live map of UK traffic cameras — pulling feeds from National Highways, TfL, Traffic Scotland, Traffic Wales and TrafficWatchNI into one place, with on-device vehicle counting for busy roads.',
			cta: { label: 'Visit openhighways.uk', href: 'https://openhighways.uk' },
			secondaryCta: {
				label: 'GitHub',
				href: 'https://github.com/JamesDillonDev/openhighways'
			}
		}
	];

	let currentHeroSlide = $state(0);

	function goToHeroSlide(index) {
		currentHeroSlide = index;
	}

	function showNextHeroSlide() {
		currentHeroSlide = (currentHeroSlide + 1) % heroSlides.length;
	}

	function showPreviousHeroSlide() {
		currentHeroSlide = (currentHeroSlide - 1 + heroSlides.length) % heroSlides.length;
	}

	// Auto-advance, but pause the timer while the tab isn't visible/focused
	// isn't worth the complexity here - just re-arm on every slide change.
	$effect(() => {
		currentHeroSlide;
		const timer = setInterval(showNextHeroSlide, 7000);
		return () => clearInterval(timer);
	});
</script>

<svelte:head>
	<title>James Dillon | Home</title>
	<meta
		name="description"
		content="Welcome to James Dillon's personal website. Explore his projects, work experience, and contact information."
	/>
</svelte:head>

<section class="hero">
	{#each heroSlides as slide, index (slide.heading)}
		<div class="hero-slide" class:hero-slide-active={index === currentHeroSlide}>
			<img class="hero-image" src={slide.image} alt={slide.alt} />
			<div class="hero-overlay">
				<div class="hero-inner">
					<h1>{slide.heading}</h1>
					<p>{slide.body}</p>
					{#if slide.cta}
						<div class="hero-cta-row">
							<a
								class="btn hero-cta"
								href={slide.cta.href}
								target="_blank"
								rel="noopener noreferrer"
							>
								{slide.cta.label}
							</a>
							{#if slide.secondaryCta}
								<a
									class="btn hero-cta hero-cta-secondary"
									href={slide.secondaryCta.href}
									target="_blank"
									rel="noopener noreferrer"
								>
									{slide.secondaryCta.label}
								</a>
							{/if}
						</div>
					{/if}
				</div>
			</div>
		</div>
	{/each}

	<div class="hero-controls">
		<button
			type="button"
			class="carousel-arrow hero-arrow"
			onclick={showPreviousHeroSlide}
			aria-label="Show previous hero slide"
		>
			<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 18l-6-6 6-6" /></svg>
		</button>
		<div class="carousel-dots hero-dots" aria-label="Choose hero slide">
			{#each heroSlides as _, index}
				<button
					type="button"
					class="carousel-dot"
					class:active-dot={index === currentHeroSlide}
					onclick={() => goToHeroSlide(index)}
					aria-label={`Show hero slide ${index + 1}`}
					aria-current={index === currentHeroSlide ? 'true' : 'false'}
				></button>
			{/each}
		</div>
		<button
			type="button"
			class="carousel-arrow hero-arrow"
			onclick={showNextHeroSlide}
			aria-label="Show next hero slide"
		>
			<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 6l6 6-6 6" /></svg>
		</button>
	</div>
</section>

<section class="page">
	<div class="shell">
		<h2 class="page-title">Personal Statement</h2>
		<div class="prose statement">
			<p>
				I'm a sixth form student who likes turning ideas into things that actually work — a
				3D-printed pet feeder, a smart home rebuilt from scratch, a live map of UK traffic cameras
				used by real people. Design and Technology is my favourite subject at school, but I spend
				just as much time writing code, from a part-time software engineering job to my own
				self-hosted projects.
			</p>
			<p>
				Volunteering with the Air Cadets and Scouts has given me plenty of practice teaching,
				organising and taking responsibility for others, and I'm looking to build on that with an
				apprenticeship after my A Levels. Outside of all that I run competitively (5K PB: 20:35) and
				I'm always looking for the next thing to build or improve.
			</p>
		</div>
	</div>
</section>
