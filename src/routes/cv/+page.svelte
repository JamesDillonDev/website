<script>
	import './cv.css';
	import PdfViewer from '$lib/components/PdfViewer.svelte';
	import cvPdf from '$lib/assets/James_Dillon_CV.pdf';
</script>

<svelte:head>
	<title>James Dillon | CV</title>
	<meta
		name="description"
		content="James Dillon's CV — education, work experience at Janus Technology and MBDA, projects, technical skills and leadership experience."
	/>
</svelte:head>

<section class="page cv-page">
	<div class="shell stack">
		<header>
			<h1 class="page-title">CV</h1>
			<p class="page-lede">
				A two-page summary of everything on this site. The rest of the site has the detail behind
				it, including project write-ups and graded coursework.
			</p>
		</header>

		<article class="cv-item">
			<div class="entity-head cv-head">
				<div class="entity-copy">
					<h2>James Dillon &mdash; CV</h2>
					<p class="entity-meta">Updated September 2026 &middot; 2 pages</p>
				</div>
				<a
					class="btn btn-outline btn-sm"
					href={cvPdf}
					target="_blank"
					rel="noopener noreferrer"
					download="James_Dillon_CV.pdf"
				>
					Download PDF
				</a>
			</div>

			<div class="pdf-frame">
				<PdfViewer src={cvPdf} title="James Dillon CV" />
			</div>
		</article>
	</div>
</section>
