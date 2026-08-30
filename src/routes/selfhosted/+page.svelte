<script>
	import homeAssistantDashboard from '$lib/assets/ha/dashboard.png';
	import homeAssistantLogo from '$lib/assets/homelogo.png';
	import homeAssistantOverview from '$lib/assets/ha/overview.png';
	import homeAssistantTravel from '$lib/assets/ha/travel.png';

	import jellyfinLogo from '$lib/assets/jellyfinLogo.png';
	import jellyfinMedia from '$lib/assets/jellyfinMovies.png';
	import jellyfinDashboard from '$lib/assets/jellyfindashboard.png';

	import './software.css';
</script>

<svelte:head>
	<title>James Dillon | Self Hosted</title>
	<meta
		name="description"
		content="Software by James Dillon including self-hosted systems, GitHub projects, and smart home automation."
	/>
</svelte:head>

<section class="page software-page">
	<div class="shell stack">
		<header>
			<h1 class="page-title">Self Hosted</h1>
			<p class="page-lede">
				The services I run at home, from smart home automation to a family media library.
			</p>
		</header>

		<article class="service">
			<div class="entity-head service-head">
				<span class="entity-mark">
					<img src={homeAssistantLogo} alt="Home Assistant logo" />
				</span>
				<div class="entity-copy">
					<h2>Home Assistant Server</h2>
					<p class="entity-meta">Smart home control platform</p>
				</div>
			</div>

			<div class="service-body">
				<div class="prose service-copy">
					<p>
						I rebuilt my smart home setup around Home Assistant running in Docker so it properly
						fits into my home lab and gives me more flexibility than using a standalone install.
						This time, I focused on making something that actually works for everyone in the house,
						not just me.
					</p>
					<p>
						I started with simple wins like lighting using TP-Link Tapo smart plugs, then expanded
						into things like integrating the TV with Wake-on-LAN and adding remote-style controls,
						as well as connecting my Sonos speakers for basic playback. It all worked well, but I
						started to notice the small annoyances, like setup friction and reliability, that made
						the system feel less seamless than I wanted.
					</p>
					<p>
						To improve that, I began moving over to Zigbee devices, starting with a Sonoff Zigbee
						dongle and motion sensors to create automations like hallway lights that turn on at
						night and switch off automatically.
					</p>
					<p>
						I also added a dedicated touchscreen panel powered by a Raspberry Pi 4, which completely
						changed how the system is used. Instead of relying on phones, everything is just there:
						simple, fast, and accessible. That shift made the biggest difference, turning the setup
						from something I built for myself into something the whole house can actually use.
					</p>
				</div>

				<div class="gallery" aria-label="Scrollable Home Assistant dashboard screenshot gallery">
					<figure class="gallery-panel">
						<img src={homeAssistantDashboard} alt="Home Assistant dashboard overview" />
						<figcaption>Main dashboard view for my Home Assistant server.</figcaption>
					</figure>
					<figure class="gallery-panel">
						<img src={homeAssistantOverview} alt="Home Assistant overview view" />
						<figcaption>Overview view showing household status at a glance.</figcaption>
					</figure>
					<figure class="gallery-panel">
						<img src={homeAssistantTravel} alt="Home Assistant travel view" />
						<figcaption>Travel view showing commute times to nearby destinations.</figcaption>
					</figure>
				</div>
			</div>
		</article>

		<article class="service">
			<div class="entity-head service-head">
				<span class="entity-mark">
					<img src={jellyfinLogo} alt="Jellyfin media server logo" />
				</span>
				<div class="entity-copy">
					<h2>Jellyfin Server</h2>
					<p class="entity-meta">Media streaming platform</p>
				</div>
			</div>

			<div class="service-body">
				<div class="prose service-copy">
					<p>
						I also run Jellyfin as part of my home lab, providing a fully self-hosted way to
						organise and stream our media from a system I control.
					</p>
					<p>
						It includes CDs my family owns that I have ripped and stored on the server, creating a
						single central library for our music collection. Like the rest of my setup, the focus is
						on reliability and ease of use, so it feels like a practical family media service rather
						than another project that needs constant maintenance.
					</p>
				</div>

				<div class="gallery" aria-label="Jellyfin media server preview gallery">
					<figure class="gallery-panel">
						<img src={jellyfinMedia} alt="Jellyfin movie and TV library view" />
						<figcaption>Movie and TV show library view within Jellyfin.</figcaption>
					</figure>
					<figure class="gallery-panel">
						<img src={jellyfinDashboard} alt="Jellyfin dashboard with suggestions" />
						<figcaption>
							Jellyfin dashboard giving suggestions and allowing users to continue where they left
							off.
						</figcaption>
					</figure>
				</div>
			</div>
		</article>
	</div>
</section>
