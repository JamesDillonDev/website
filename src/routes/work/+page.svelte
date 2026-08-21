<script>
	import './work.css';
	import missile1 from '$lib/assets/missile1.jpg';
	import missile2 from '$lib/assets/missile2.jpg';
	import missile3 from '$lib/assets/missile3.jpg';

	const missilePhotos = [
		{ src: missile1, alt: 'Mini guided missile project photo 1' },
		{ src: missile2, alt: 'Mini guided missile project photo 2' },
		{ src: missile3, alt: 'Mini guided missile project photo 3' }
	];

	let currentMissileSlide = $state(0);

	function showPreviousMissileSlide() {
		currentMissileSlide = (currentMissileSlide - 1 + missilePhotos.length) % missilePhotos.length;
	}

	function showNextMissileSlide() {
		currentMissileSlide = (currentMissileSlide + 1) % missilePhotos.length;
	}

	/** @param {number} index */
	function goToMissileSlide(index) {
		currentMissileSlide = index;
	}
</script>

<svelte:head>
	<title>James Dillon | Work</title>
	<meta name="description" content="James Dillon's professional work experience and projects." />
</svelte:head>

<section class="page work-page">
	<div class="shell stack">
		<header>
			<h1 class="page-title">Work Experience</h1>
			<p class="page-lede">
				Placements and projects where I have worked alongside professional engineering teams.
			</p>
		</header>

		<article class="role">
			<div class="entity-head role-head">
				<img
					class="entity-wordmark"
					src="https://www.mbdacareers.co.uk/application/themes/thirty_three/assets/dist/img/mbda_logo_minimal.svg"
					alt="MBDA logo"
				/>
				<div class="entity-copy">
					<p class="entity-meta">Work Experience &middot; 2026</p>
				</div>
				<a
					class="btn btn-outline btn-sm"
					href="https://www.mbda-systems.com"
					target="_blank"
					rel="noopener noreferrer"
				>
					Visit site
				</a>
			</div>

			<div class="prose role-intro">
				<p>
					During my work experience at MBDA, I had the opportunity to work across a range of teams
					and gain hands-on insight into how a world-leading defence and missile systems company
					operates:
				</p>
			</div>

			<section class="project">
				<h3 class="project-title">Miniature Guided Missile &mdash; Raspberry Pi Project</h3>
				<div class="project-body">
					<div class="project-copy">
						<div class="prose">
							<p>
								As part of a team, I helped design and program a miniature guided missile using a
								Raspberry Pi during work experience at MBDA. I contributed to coding, hardware
								integration, system testing, and troubleshooting while learning how software
								engineers collaborate on real engineering projects.
							</p>
							<p>
								I also rotated around various departments across MBDA, including systems testing and
								validation, materials, hardware-in-the-loop, electronics, production, and project
								management, which gave me a broader understanding of how large defence programmes
								are delivered from concept through to implementation.
							</p>
						</div>

						<div class="project-actions">
							<a
								class="btn btn-outline btn-sm"
								href="https://github.com/JamesDillonDev/mini-missile.git"
								target="_blank"
								rel="noopener noreferrer"
							>
								<svg class="btn-icon" viewBox="0 0 16 16" aria-hidden="true" focusable="false">
									<path
										d="M8 0C3.58 0 0 3.58 0 8a8.01 8.01 0 005.47 7.59c.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.5-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.54 7.54 0 014 0c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0016 8c0-4.42-3.58-8-8-8z"
									></path>
								</svg>
								<span>View repository</span>
							</a>
						</div>
					</div>

					<div class="carousel" aria-label="Mini missile project photos">
						<div class="carousel-frame">
							<img
								class="carousel-image"
								src={missilePhotos[currentMissileSlide].src}
								alt={missilePhotos[currentMissileSlide].alt}
							/>
						</div>
						<div class="carousel-controls">
							<button
								type="button"
								class="carousel-arrow"
								onclick={showPreviousMissileSlide}
								aria-label="Show previous MBDA project image"
							>
								<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 18l-6-6 6-6" /></svg>
							</button>
							<div class="carousel-dots" aria-label="Choose MBDA project image">
								{#each missilePhotos as _, index}
									<button
										type="button"
										class="carousel-dot"
										class:active-dot={index === currentMissileSlide}
										onclick={() => goToMissileSlide(index)}
										aria-label={`Show MBDA project image ${index + 1}`}
										aria-current={index === currentMissileSlide ? 'true' : 'false'}
									></button>
								{/each}
							</div>
							<button
								type="button"
								class="carousel-arrow"
								onclick={showNextMissileSlide}
								aria-label="Show next MBDA project image"
							>
								<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 6l6 6-6 6" /></svg>
							</button>
						</div>
					</div>
				</div>
			</section>
		</article>

		<article class="role">
			<div class="entity-head role-head">
				<img
					class="entity-wordmark"
					src="https://janustechnology.co.uk/wp-content/uploads/2023/07/Janus-Logo.png"
					alt="Janus Technology logo"
				/>
				<div class="entity-copy">
					<p class="entity-meta">Junior Software Engineer &middot; July 2025 &ndash; Aug 2025</p>
				</div>
				<a
					class="btn btn-outline btn-sm"
					href="https://janustechnology.co.uk"
					target="_blank"
					rel="noopener noreferrer"
				>
					Visit site
				</a>
			</div>

			<div class="prose role-intro">
				<p>
					During my time at Janus Technology, I worked on a range of projects, including automation
					and AI-driven support solutions:
				</p>
			</div>

			<section class="project">
				<h3 class="project-title">Support Ticket Automation Plugin &mdash; osTicket</h3>
				<div class="project-body">
					<div class="prose project-copy">
						<p>
							I developed a plugin for the open-source
							<a href="https://osticket.com/" target="_blank" rel="noopener noreferrer">osTicket</a>
							platform that uses AI to automatically generate support responses. This system analyzes
							incoming support tickets, determines the likely issue, and crafts a step-by-step
							response to help customers resolve their problems quickly and efficiently.
						</p>
						<p>
							The plugin leverages natural language processing to understand queries and provide
							relevant, actionable solutions, reducing the workload for human support agents and
							improving response times.
						</p>
					</div>
					<div class="project-media narrow">
						<img
							src="https://osticket.com/wp-content/uploads/2021/03/osticket-supsys-new-1-e1616621912452.png"
							alt="osTicket logo"
						/>
					</div>
				</div>
			</section>

			<section class="project">
				<h3 class="project-title">Stile App &mdash; AVProEdge</h3>
				<div class="project-body reverse">
					<div class="prose project-copy">
						<p>
							I contributed to the development of the
							<a
								href="https://www.avproglobal.com/pages/stile-app-avpro"
								target="_blank"
								rel="noopener noreferrer">Stile app for AVProEdge</a
							>, a drag-and-drop control application for managing multiview video sources across
							multiple displays.
						</p>
						<p>
							My main responsibility was implementing the live video preview feature for all
							draggable sources, allowing users to see real-time previews of each input before
							assigning them to a display. This made it easier for users to identify and select the
							correct source, improving the overall usability and experience of the app.
						</p>
					</div>
					<div class="project-media">
						<img
							src="https://cdn.shopify.com/s/files/1/0712/9409/1574/files/Phone_with_Tablet_-_Landscape_Home_-_2x2_fb41be4b-2670-48a2-8fed-b6e4f70d0848.png?v=1741752714"
							alt="Stile App on iPad controlling AVPro Edge multiviewer"
						/>
					</div>
				</div>
			</section>
		</article>
	</div>
</section>
