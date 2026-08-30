<script>
	import './coursework.css';
	import PdfViewer from '$lib/components/PdfViewer.svelte';
	import dtCoursework from '$lib/assets/coursework/GCSE_DT_Coursework.pdf';
	import epqCoursework from '$lib/assets/coursework/17401_3044_DILLON_ Essay.pdf';

	const courseworkItems = [
		{
			title: 'GCSE Design and Technology Coursework',
			subject: 'Design and Technology',
			grade: '9',
			file: dtCoursework,
			fileName: 'GCSE_DT_Coursework.pdf'
		},
		{
			title: 'EPQ: Creating an Automatic Pet Feeder',
			subject: 'Extended Project Qualification',
			grade: 'A* (50/52)',
			file: epqCoursework,
			fileName: 'EPQ_Automatic_Pet_Feeder.pdf'
		}
	];
</script>

<svelte:head>
	<title>James Dillon | Coursework</title>
	<meta
		name="description"
		content="James Dillon's GCSE and A-Level coursework, including PowerPoints and Word documents embedded as PDFs."
	/>
</svelte:head>

<section class="page coursework-page">
	<div class="shell stack">
		<header>
			<h1 class="page-title">Coursework</h1>
			<p class="page-lede">
				PowerPoints and Word documents from my coursework, converted to PDF so they can be viewed
				directly here.
			</p>
		</header>

		{#each courseworkItems as item}
			<article class="coursework-item">
				<div class="entity-head coursework-head">
					<div class="entity-copy">
						<h2>{item.title}</h2>
						<p class="entity-meta">{item.subject} &middot; Grade {item.grade}</p>
					</div>
					<a
						class="btn btn-outline btn-sm"
						href={item.file}
						target="_blank"
						rel="noopener noreferrer"
						download={item.fileName}
					>
						Download
					</a>
				</div>

				<div class="pdf-frame">
					<PdfViewer src={item.file} title={item.title} />
				</div>
			</article>
		{/each}
	</div>
</section>
