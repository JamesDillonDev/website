<script>
	import homeAssistantDashboard from '$lib/assets/dashboard.png';
	import homeAssistantLogo from '$lib/assets/homelogo.png';
	import homeAssistantMedia from '$lib/assets/media.png';
	import homeAssistantFloor from '$lib/assets/floor.png';

	import jellyfinLogo from '$lib/assets/jellyfinLogo.png';
	import jellyfinMedia from '$lib/assets/jellyfinMovies.png';
	import jellyfinDashboard from '$lib/assets/jellyfinDashboard.png';
	
	import './software.css';
</script>

<svelte:head>
	<title>James Dillon | Software</title>
	<meta
		name="description"
		content="Software by James Dillon including self-hosted systems, GitHub projects, and smart home automation."
	/>
</svelte:head>

<section class="software-page">
	<div class="software-shell">
		<h1>Self Hosted</h1>

		<section class="project-intro">
			<div class="project-header">
				<img
					class="project-logo"
					src={homeAssistantLogo}
					alt="Home Assistant logo"
				/>
				<div class="project-copy">
					<h2>Home Assistant Server</h2>
					<p class="project-meta">Smart home control platform</p>
				</div>
			</div>
			<div class="software-card-body">
				<div class="software-copy">
					<p>
						I rebuilt my smart home setup around Home Assistant running in Docker so it properly
						fits into my home lab and gives me more flexibility than using a standalone install.
						This time, I focused on making something that actually works for everyone in the
						house, not just me.
					</p>
					<p>
						I started with simple wins like lighting using TP-Link Tapo smart plugs, then
						expanded into things like integrating the TV with Wake-on-LAN and adding
						remote-style controls, as well as connecting my Sonos speakers for basic playback.
						It all worked well, but I started to notice the small annoyances, like setup
						friction and reliability, that made the system feel less seamless than I wanted.
					</p>
				</div>

				<div
					class="software-canvas"
					aria-label="Scrollable Home Assistant dashboard screenshot gallery"
				>
					<figure class="canvas-panel">
						<img src={homeAssistantDashboard} alt="Home Assistant dashboard overview" />
						<figcaption>Main dashboard view for my Home Assistant server.</figcaption>
					</figure>
					<figure class="canvas-panel">
						<img src={homeAssistantMedia} alt="Home Assistant media control view" />
						<figcaption>Media control view showing Sonos speakers and TV controls.</figcaption>
					</figure>
					<figure class="canvas-panel">
						<img src={homeAssistantFloor} alt="Home Assistant floor plan view" />
						<figcaption>Floor plan view showing the layout of my home and device locations.</figcaption>
					</figure>
				</div>
			</div>
		</section>

		<section class="software-card">
			<div class="software-card-body reverse-mobile">
				<div class="software-copy">
					<p>
						To improve that, I began moving over to Zigbee devices, starting with a Sonoff
						Zigbee dongle and motion sensors to create automations like hallway lights that turn
						on at night and switch off automatically.
					</p>
					<p>
						I also added a dedicated touchscreen panel powered by a Raspberry Pi 4, which
						completely changed how the system is used. Instead of relying on phones, everything
						is just there: simple, fast, and accessible. That shift made the biggest difference,
						turning the setup from something I built for myself into something the whole house
						can actually use.
					</p>
				</div>
			</div>
		</section>

		<section class="project-intro">
			<div class="project-header">
				<img
					class="project-logo"
					src={jellyfinLogo}
					alt="Jellyfin media server logo"
				/>
				<div class="project-copy">
					<h2>Jellyfin Server</h2>
					<p class="project-meta">Media streaming platform</p>
				</div>
			</div>

			<div class="software-card-body">
				<div class="software-copy">
					<p>
						I also run Jellyfin as part of my home lab, providing a fully self-hosted way to organise and stream our media from a system I control. It includes CDs my family owns that I’ve ripped and stored on the server, creating a single, centralised library for our music collection.
						Like the rest of my setup, the focus is on reliability and ease of use, so it feels like a practical family media service rather than another project that requires constant maintenance.
					</p>
				</div>

				<div class="software-canvas" aria-label="Jellyfin media server preview gallery">
					<figure class="canvas-panel">
						<img src={jellyfinMedia} alt="Media dashboard view used for Jellyfin section" />
						<figcaption>Movie and TV show library view within Jellyfin.</figcaption>
					</figure>
					<figure class="canvas-panel">
						<img src={jellyfinDashboard} alt="Media dashboard view used for Jellyfin section" />
						<figcaption>Jellyfin dashboard giving suggestions and allowing users to continue where they left off.</figcaption>
					</figure>
				</div>
			</div>
		</section>
	</div>
</section>
