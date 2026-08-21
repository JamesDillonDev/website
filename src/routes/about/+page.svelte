<script>
	import './about.css';
	import dofeLogo from '$lib/assets/dofe.png';
	import knightsLogo from '$lib/assets/knights.png';
	import rafacLogo from '$lib/assets/rafac.png';
	import scoutsLogo from '$lib/assets/scouts.png';

	let showCadets = $state(true);
	let showScouts = $state(true);
	let showDofE = $state(false);
	let showOtherQualifications = $state(false);

	const gcseResults = [
		{ subject: 'Maths', grade: '7', equivalent: 'A' },
		{ subject: 'English', grade: '5', equivalent: 'C' },
		{ subject: 'Physics', grade: '8', equivalent: 'A' },
		{ subject: 'Chemistry', grade: '7', equivalent: 'A' },
		{ subject: 'Biology', grade: '6', equivalent: 'B' },
		{ subject: 'Design and Technology', grade: '9', equivalent: 'A*' },
		{ subject: 'Computer Science', grade: '9', equivalent: 'A*' },
		{ subject: 'Media', grade: '8', equivalent: 'A' },
		{ subject: 'Enterprise and Marketing', grade: 'M2', equivalent: 'A' }
	];
</script>

<svelte:head>
	<title>James Dillon | About</title>
	<meta
		name="description"
		content="Learn about James Dillon's education, experience, and qualifications."
	/>
</svelte:head>

<section class="page about-page">
	<div class="shell stack">
		<header>
			<h1 class="page-title">About Me</h1>
			<p class="page-lede">
				Sixth form student in Hertfordshire, splitting my time between design, software, and
				volunteering.
			</p>
		</header>

		<section class="education">
			<div class="entity-head">
				<span class="entity-mark">
					<img src={knightsLogo} alt="Knights Templar School logo" />
				</span>
				<div class="entity-copy">
					<h2>Knights Templar School</h2>
					<p class="entity-meta">Sixth Form Student &middot; 2020&ndash;present</p>
				</div>
				<a
					class="btn btn-outline btn-sm"
					href="https://www.kts.school/"
					target="_blank"
					rel="noopener noreferrer"
				>
					Visit site
				</a>
			</div>

			<div class="prose education-body">
				<p>
					Currently studying for A-Levels in Maths, Computer Science, and Product Design at Knights
					Templar School Sixth Form. For my Extended Project Qualification (EPQ), I am designing
					and building an automatic pet dispenser/dog feeder. Below are my GCSE results:
				</p>
			</div>

			<div class="table-wrap results-wrap">
				<table class="data-table">
					<thead>
						<tr>
							<th>Subject</th>
							<th>Grade</th>
							<th>Old Grade Equivalent</th>
						</tr>
					</thead>
					<tbody>
						{#each gcseResults as result}
							<tr>
								<td>{result.subject}</td>
								<td>{result.grade}</td>
								<td>{result.equivalent}</td>
							</tr>
						{/each}
					</tbody>
				</table>
			</div>
		</section>

		<div class="accordion">
			<section class="accordion-item" class:open={showCadets}>
				<button
					class="accordion-trigger"
					type="button"
					aria-expanded={showCadets}
					onclick={() => (showCadets = !showCadets)}
				>
					<span class="accordion-label">
						Royal Air Force Air Cadets
						<span class="accordion-period">2022 &ndash; present</span>
					</span>
					<svg class="accordion-chevron" viewBox="0 0 24 24" aria-hidden="true">
						<path d="M6 9l6 6 6-6" />
					</svg>
				</button>

				{#if showCadets}
					<div class="accordion-body">
						<div class="feature-row">
							<span class="feature-badge wide">
								<img src={rafacLogo} alt="Royal Air Force Air Cadets logo" />
							</span>
							<div class="prose feature-copy">
								<p>
									I have completed the Methods of Instruction (MOI) training, which qualifies me to
									regularly teach junior cadets during parade nights. I have also achieved the
									Instructor First Aid qualification through St John Ambulance. This is a nationally
									recognised certification that is valid both within and outside of cadets. As a
									result, I am qualified to instruct and assess lower-level cadets in First Aid. In
									addition, I have achieved Silver Leadership, which has strengthened my leadership,
									communication, and organisational skills.
								</p>
								<p>
									I have progressed through the ranks and currently hold the rank of Sergeant, taking
									on increased responsibility within the squadron, particularly in relation to
									training and mentoring junior cadets. Through cadets, I have had the opportunity to
									visit RAF bases, gaining valuable insight into how the RAF operates. I have also
									participated in a range of activities, including shooting. Furthermore, I have
									represented the squadron at public events such as Remembrance Sunday and competed
									in athletics at both Wing and Regional level, achieving a Gold medal at Wing level.
								</p>
							</div>
						</div>
					</div>
				{/if}
			</section>

			<section class="accordion-item" class:open={showScouts}>
				<button
					class="accordion-trigger"
					type="button"
					aria-expanded={showScouts}
					onclick={() => (showScouts = !showScouts)}
				>
					<span class="accordion-label">
						Scouting
						<span class="accordion-period">2014 &ndash; present</span>
					</span>
					<svg class="accordion-chevron" viewBox="0 0 24 24" aria-hidden="true">
						<path d="M6 9l6 6 6-6" />
					</svg>
				</button>

				{#if showScouts}
					<div class="accordion-body">
						<div class="feature-row">
							<span class="feature-badge">
								<img src={scoutsLogo} alt="Scouts logo" />
							</span>
							<div class="prose feature-copy">
								<p>
									I have progressed through Beavers, Cubs, Scouts and now Explorers, taking part in a
									wide range of activities including cooking, pioneering, navigation, hiking and
									camping. These experiences have helped me develop teamwork, leadership and
									practical outdoor skills. I now volunteer at my former Scout group as a Young
									Leader, helping to run weekly meetings and support younger members. I also assist
									with fundraising events such as running the BBQ at Balstock and the Baldock Beer
									Festival, and help to organise and support weekend camps.
								</p>
							</div>
						</div>
					</div>
				{/if}
			</section>

			<section class="accordion-item" class:open={showDofE}>
				<button
					class="accordion-trigger"
					type="button"
					aria-expanded={showDofE}
					onclick={() => (showDofE = !showDofE)}
				>
					<span class="accordion-label">Duke of Edinburgh&rsquo;s Award</span>
					<svg class="accordion-chevron" viewBox="0 0 24 24" aria-hidden="true">
						<path d="M6 9l6 6 6-6" />
					</svg>
				</button>

				{#if showDofE}
					<div class="accordion-body">
						<div class="feature-row">
							<span class="feature-badge">
								<img src={dofeLogo} alt="Duke of Edinburgh's Award logo" />
							</span>
							<div class="prose feature-copy">
								<p>
									Currently working on Bronze, doing Silver, and planning to do Gold. For Bronze, I
									focused on improving my physical fitness by running regularly, joined a
									cybersecurity club where I learned about online safety and ethical hacking,
									volunteered in my local community, and took part in expeditions that involved
									planning, teamwork, and navigation.
								</p>
							</div>
						</div>
					</div>
				{/if}
			</section>

			<section class="accordion-item" class:open={showOtherQualifications}>
				<button
					class="accordion-trigger"
					type="button"
					aria-expanded={showOtherQualifications}
					onclick={() => (showOtherQualifications = !showOtherQualifications)}
				>
					<span class="accordion-label">Other Qualifications</span>
					<svg class="accordion-chevron" viewBox="0 0 24 24" aria-hidden="true">
						<path d="M6 9l6 6 6-6" />
					</svg>
				</button>

				{#if showOtherQualifications}
					<div class="accordion-body">
						<ul class="qualifications-list">
							<li>
								<strong>BTEC Level 2 in Teamwork and Personal Development</strong>
								<span>
									Achieved through the Air Cadets, this qualification involved developing leadership,
									communication, and problem-solving skills. It required completing a portfolio of
									evidence, practical teamwork exercises, and linking various cadet badges and
									activities to real-world scenarios, resulting in a qualification equivalent to a
									GCSE.
								</span>
							</li>
							<li>
								<strong>Fire Warden Training (valid until 2027)</strong>
								<span>
									Completed at Janus Technology. This training covered fire safety procedures,
									emergency response, and the responsibilities of a fire warden in the workplace. It
									qualifies me to act as a fire marshal, ensuring safe evacuation and fire prevention
									in a professional environment.
								</span>
							</li>
						</ul>
					</div>
				{/if}
			</section>
		</div>
	</div>
</section>
