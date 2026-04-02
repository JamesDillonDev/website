<script>
	import './about.css';

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

<section class="about-page">
	<div class="about-shell">
		<h1>About Me</h1>

		<section class="education-card">
			<div class="education-header">
				<img src="/src/lib/assets/knights.png" alt="Knights Templar School logo" style="width: 3.375rem; height: 3.375rem; object-fit: contain; border-radius: 0.5rem;" />
				<div class="education-copy">
					<h2>Knights Templar School</h2>
					<p class="education-meta">Sixth Form Student | 2020-present</p>
				</div>
				<a
					class="visit-link"
					href="https://www.kts.school/"
					target="_blank"
					rel="noopener noreferrer"
				>
					Visit
				</a>
			</div>

			<p class="section-copy">
				Currently studying for A-Levels in Maths, Computer Science, and Product Design at
				Knights Templar School Sixth Form. For my Extended Project Qualification (EPQ), I am
				designing and building an automatic pet dispenser/dog feeder. Below are my GCSE
				results:
			</p>

			<table class="results-table">
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
		</section>

		<section class="accordion-section">
			<button class="accordion-trigger" type="button" onclick={() => (showCadets = !showCadets)}>
				<span>Royal Air Force Air Cadets</span>
				<span class="accordion-icon">{showCadets ? '▼' : '►'}</span>
			</button>

			{#if showCadets}
				<div class="accordion-body">
					<p class="period">(2022 to present)</p>
					<div class="feature-row">
						<div class="feature-badge raf-badge" aria-hidden="true">
							<img src="/src/lib/assets/rafac.png" alt="Royal Air Force Air Cadets logo" style="width: 12.5rem; height: 7.5rem; object-fit: contain; border-radius: 0.5rem;" />
						</div>
						<div class="feature-copy">
							<p>
								I have completed the Methods of Instruction (MOI) training, which qualifies
								me to regularly teach junior cadets during parade nights. I have also
								achieved the Instructor First Aid qualification through St John Ambulance.
								This is a nationally recognised certification that is valid both within and
								outside of cadets. As a result, I am qualified to instruct and assess
								lower-level cadets in First Aid. In addition, I have achieved Silver
								Leadership, which has strengthened my leadership, communication, and
								organisational skills.
							</p>
							<p>
								I have progressed through the ranks and currently hold the rank of Sergeant,
								taking on increased responsibility within the squadron, particularly in
								relation to training and mentoring junior cadets. Through cadets, I have had
								the opportunity to visit RAF bases, gaining valuable insight into how the RAF
								operates. I have also participated in a range of activities, including
								shooting. Furthermore, I have represented the squadron at public events such
								as Remembrance Sunday and competed in athletics at both Wing and Regional
								level, achieving a Gold medal at Wing level.
							</p>
						</div>
					</div>
				</div>
			{/if}
		</section>

		<section class="accordion-section">
			<button class="accordion-trigger" type="button" onclick={() => (showScouts = !showScouts)}>
				<span>Scouting</span>
				<span class="accordion-icon">{showScouts ? '▼' : '►'}</span>
			</button>

			{#if showScouts}
				<div class="accordion-body">
					<p class="period">(2014 to present)</p>
					<div class="feature-row reverse">
						<div class="feature-badge scouts-badge" aria-hidden="true">
							<img src="/src/lib/assets/scouts.png" alt="Scouts logo" style="width: 7.5rem; height: 7.5rem; object-fit: contain; border-radius: 0.5rem;" />
						</div>
						<div class="feature-copy">
							<p>
								I have progressed through Beavers, Cubs, Scouts and now Explorers, taking part
								in a wide range of activities including cooking, pioneering, navigation,
								hiking and camping. These experiences have helped me develop teamwork,
								leadership and practical outdoor skills. I now volunteer at my former Scout
								group as a Young Leader, helping to run weekly meetings and support younger
								members. I also assist with fundraising events such as running the BBQ at
								Balstock and the Baldock Beer Festival, and help to organise and support
								weekend camps.
							</p>
						</div>
					</div>
				</div>
			{/if}
		</section>

		<section class="accordion-section">
			<button class="accordion-trigger" type="button" onclick={() => (showDofE = !showDofE)}>
				<span>Duke of Edinburgh's Award</span>
				<span class="accordion-icon">{showDofE ? '▼' : '►'}</span>
			</button>

			{#if showDofE}
				<div class="accordion-body">
					<div class="feature-row">
						   <div class="feature-badge dofe-badge" aria-hidden="true">
							   <img src="/src/lib/assets/dofe.png" alt="Duke of Edinburgh's Award logo" style="width: 7.5rem; height: 7.5rem; object-fit: contain; border-radius: 0.5rem;" />
						   </div>
						<div class="feature-copy">
							<p>
								Currently working on Bronze, doing Silver, and planning to do Gold.
								For Bronze, I focused on improving my physical fitness by running regularly,
								joined a cybersecurity club where I learned about online safety and ethical
								hacking, volunteered in my local community, and took part in expeditions that
								involved planning, teamwork, and navigation.
							</p>
						</div>
					</div>
				</div>
			{/if}
		</section>

		<section class="accordion-section">
			<button
				class="accordion-trigger"
				type="button"
				onclick={() => (showOtherQualifications = !showOtherQualifications)}
			>
				<span>Other Qualifications</span>
				<span class="accordion-icon">{showOtherQualifications ? '▼' : '►'}</span>
			</button>

			{#if showOtherQualifications}
				<div class="accordion-body">
					<ul class="qualifications-list">
						<li>
							<strong>BTEC Level 2 in Teamwork and Personal Development</strong>
							<span>
								Achieved through the Air Cadets, this qualification involved developing
								leadership, communication, and problem-solving skills. It required completing
								a portfolio of evidence, practical teamwork exercises, and linking various
								cadet badges and activities to real-world scenarios, resulting in a
								qualification equivalent to a GCSE.
							</span>
						</li>
						<li>
							<strong>Fire Warden Training (valid until 2027)</strong>
							<span>
								Completed at Janus Technology. This training covered fire safety procedures, emergency
								response, and the responsibilities of a fire warden in the workplace. It
								qualifies me to act as a fire marshal, ensuring safe evacuation and fire
								prevention in a professional environment.
							</span>
						</li>
					</ul>
				</div>
			{/if}
		</section>
	</div>
</section>