<script>
	import './work.css';
</script>

<svelte:head>
	<title>James Dillon | Work</title>
	<meta
		name="description"
		content="James Dillon's professional work experience and projects."
	/>
</svelte:head>

<section class="work-page">
	<div class="work-shell">
		<h1>Work Experience</h1>

		<section class="company-intro">
			<div class="company-header">
				<img
					class="company-logo"
					src="https://janustechnology.co.uk/wp-content/uploads/2023/07/Janus-Logo.png"
					alt="Janus Technology logo"
				/>
				<div class="company-copy">
					<h2>Janus Technology</h2>
					<p class="company-meta">Junior Software Engineer | July 2025 - Aug 2025</p>
				</div>
				<a
					class="visit-link"
					href="https://janustechnology.co.uk"
					target="_blank"
					rel="noopener noreferrer"
				>
					Visit Site
				</a>
			</div>

			<p class="intro-copy">
				During my time at Janus Technology, I worked on a range of projects, including
				automation and AI-driven support solutions:
			</p>
		</section>

		<section class="work-card">
			<h3>Support Ticket Automation Plugin - osTicket</h3>
			<div class="work-card-body">
				<div class="work-copy">
					<p>
						I developed a plugin for the open-source
						<a href="https://osticket.com/" target="_blank" rel="noopener noreferrer"
							>osTicket</a
						>
						platform that uses AI to automatically generate support responses. This system
						analyzes incoming support tickets, determines the likely issue, and crafts a
						step-by-step response to help customers resolve their problems quickly and
						efficiently.
					</p>
					<p>
						The plugin leverages natural language processing to understand queries and
						provide relevant, actionable solutions, reducing the workload for human support
						agents and improving response times.
					</p>
				</div>
				<img
					class="project-image small"
					src="https://osticket.com/wp-content/uploads/2021/03/osticket-supsys-new-1-e1616621912452.png"
					alt="osTicket logo"
				/>
			</div>
		</section>

		<section class="work-card">
			<h3>Stile App - AVProEdge</h3>
			<div class="work-card-body reverse-mobile">
				<img
					class="project-image large"
					src="https://cdn.shopify.com/s/files/1/0712/9409/1574/files/Phone_with_Tablet_-_Landscape_Home_-_2x2_fb41be4b-2670-48a2-8fed-b6e4f70d0848.png?v=1741752714"
					alt="Stile App on iPad controlling AVPro Edge multiviewer"
				/>
				<div class="work-copy">
					<p>
						I contributed to the development of the
						<a
							href="https://www.avproglobal.com/pages/stile-app-avpro"
							target="_blank"
							rel="noopener noreferrer"
						>
							Stile app for AVProEdge
						</a>
						, a drag-and-drop control application for managing multiview video sources
						across multiple displays.
					</p>
					<p>
						My main responsibility was implementing the live video preview feature for all
						draggable sources, allowing users to see real-time previews of each input before
						assigning them to a display. This made it easier for users to identify and select
						the correct source, improving the overall usability and experience of the app.
					</p>
				</div>
			</div>
		</section>
	</div>
</section>
