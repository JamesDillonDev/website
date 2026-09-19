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
				I am a motivated and curious student who enjoys learning, creating, and experimenting with
				new ideas—especially in design and technology. My favourite subject at school is Design and
				Technology, where I love bringing concepts to life, whether through 3D printing,
				electronics, or hands-on making. I also have a strong passion for software development,
				building web apps and tools that solve real problems or showcase my creativity.
			</p>
			<p>
				Volunteering at different organizations has helped me develop strong teamwork and
				communication skills. I am keen to gain experience in a professional environment and plan to
				pursue an apprenticeship after my A Levels, where I can continue learning and developing my
				skills in both design and software. Outside of school and my projects, I enjoy running (5K
				PB: 20:35) and am always looking for new challenges.
			</p>
		</div>
	</div>
</section>
