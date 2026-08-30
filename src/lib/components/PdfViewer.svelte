<script>
	import { onMount } from 'svelte';
	import './PdfViewer.css';

	let { src, title = '' } = $props();

	/** @type {HTMLDivElement} */
	let container;
	/** @type {HTMLCanvasElement} */
	let canvas;

	let pageNum = $state(1);
	let numPages = $state(0);
	let isFullscreen = $state(false);
	let loading = $state(true);
	let errorMessage = $state('');

	/** @type {any} */
	let pdfDoc;
	/** @type {any} */
	let loadingTask;
	/** @type {any} */
	let renderTask;

	onMount(() => {
		let cancelled = false;

		(async () => {
			try {
				const pdfjsLib = await import('pdfjs-dist');
				const workerUrl = (await import('pdfjs-dist/build/pdf.worker.mjs?url')).default;
				pdfjsLib.GlobalWorkerOptions.workerSrc = workerUrl;

				loadingTask = pdfjsLib.getDocument({ url: src });
				const doc = await loadingTask.promise;
				if (cancelled) return;

				pdfDoc = doc;
				numPages = doc.numPages;
				loading = false;
				await renderPage(pageNum);
			} catch (err) {
				console.error('Failed to load PDF', err);
				errorMessage = 'Unable to load this document.';
				loading = false;
			}
		})();

		document.addEventListener('fullscreenchange', handleFullscreenChange);
		window.addEventListener('resize', handleResize);

		return () => {
			cancelled = true;
			document.removeEventListener('fullscreenchange', handleFullscreenChange);
			window.removeEventListener('resize', handleResize);
			renderTask?.cancel();
			loadingTask?.destroy();
		};
	});

	function handleFullscreenChange() {
		isFullscreen = document.fullscreenElement === container;
		renderPage(pageNum);
	}

	function handleResize() {
		if (pdfDoc) renderPage(pageNum);
	}

	/** @param {number} num */
	async function renderPage(num) {
		if (!pdfDoc || !canvas) return;

		const page = await pdfDoc.getPage(num);
		const baseViewport = page.getViewport({ scale: 1 });

		// Fit the page into whatever space the viewer currently has, like a slide.
		const fitScale = Math.min(
			container.clientWidth / baseViewport.width,
			container.clientHeight / baseViewport.height
		);
		const pixelRatio = window.devicePixelRatio || 1;
		const viewport = page.getViewport({ scale: fitScale * pixelRatio });

		canvas.width = viewport.width;
		canvas.height = viewport.height;
		canvas.style.width = `${viewport.width / pixelRatio}px`;
		canvas.style.height = `${viewport.height / pixelRatio}px`;

		renderTask?.cancel();
		const context = canvas.getContext('2d');
		renderTask = page.render({ canvasContext: context, viewport });

		try {
			await renderTask.promise;
		} catch (/** @type {any} */ err) {
			if (err?.name !== 'RenderingCancelledException') throw err;
		}
	}

	/** @param {number} num */
	function goToPage(num) {
		if (!pdfDoc) return;
		const clamped = Math.min(Math.max(num, 1), numPages);
		if (clamped === pageNum) return;
		pageNum = clamped;
		renderPage(pageNum);
	}

	function nextPage() {
		goToPage(pageNum + 1);
	}

	function previousPage() {
		goToPage(pageNum - 1);
	}

	function firstPage() {
		goToPage(1);
	}

	function lastPage() {
		goToPage(numPages);
	}

	function toggleFullscreen() {
		if (document.fullscreenElement) {
			document.exitFullscreen();
		} else {
			container.requestFullscreen?.();
		}
	}

	/** @param {KeyboardEvent} event */
	function handleKeydown(event) {
		if (event.key === 'ArrowRight' || event.key === 'PageDown') {
			event.preventDefault();
			nextPage();
		} else if (event.key === 'ArrowLeft' || event.key === 'PageUp') {
			event.preventDefault();
			previousPage();
		} else if (event.key === 'Home') {
			event.preventDefault();
			firstPage();
		} else if (event.key === 'End') {
			event.preventDefault();
			lastPage();
		} else if (event.key === 'Escape' && isFullscreen) {
			document.exitFullscreen();
		}
	}
</script>

<!-- svelte-ignore a11y_no_noninteractive_tabindex -->
<!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
<div
	class="pdf-viewer"
	class:pdf-viewer-fullscreen={isFullscreen}
	bind:this={container}
	role="group"
	aria-label={title}
	tabindex="0"
	onkeydown={handleKeydown}
>
	<div class="pdf-viewer-stage">
		{#if loading}
			<p class="pdf-viewer-status">Loading document&hellip;</p>
		{:else if errorMessage}
			<p class="pdf-viewer-status">{errorMessage}</p>
		{/if}
		<canvas
			bind:this={canvas}
			class="pdf-viewer-canvas"
			class:is-hidden={loading || errorMessage}
		></canvas>
	</div>

	{#if !loading && !errorMessage}
		<div class="pdf-viewer-controls">
			<button
				type="button"
				class="pdf-viewer-arrow"
				onclick={firstPage}
				disabled={pageNum <= 1}
				aria-label="First page"
			>
				<svg viewBox="0 0 24 24" aria-hidden="true">
					<path d="M11 18l-6-6 6-6" />
					<path d="M18 18l-6-6 6-6" />
				</svg>
			</button>

			<button
				type="button"
				class="pdf-viewer-arrow"
				onclick={previousPage}
				disabled={pageNum <= 1}
				aria-label="Previous page"
			>
				<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 18l-6-6 6-6" /></svg>
			</button>

			<span class="pdf-viewer-page">Page {pageNum} of {numPages}</span>

			<button
				type="button"
				class="pdf-viewer-arrow"
				onclick={nextPage}
				disabled={pageNum >= numPages}
				aria-label="Next page"
			>
				<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 6l6 6-6 6" /></svg>
			</button>

			<button
				type="button"
				class="pdf-viewer-arrow"
				onclick={lastPage}
				disabled={pageNum >= numPages}
				aria-label="Last page"
			>
				<svg viewBox="0 0 24 24" aria-hidden="true">
					<path d="M6 6l6 6-6 6" />
					<path d="M13 6l6 6-6 6" />
				</svg>
			</button>

			<button
				type="button"
				class="pdf-viewer-fullscreen-toggle"
				onclick={toggleFullscreen}
				aria-label={isFullscreen ? 'Exit fullscreen' : 'View fullscreen'}
			>
				{#if isFullscreen}
					<svg viewBox="0 0 24 24" aria-hidden="true">
						<path d="M8 3v3a2 2 0 01-2 2H3" />
						<path d="M21 8h-3a2 2 0 01-2-2V3" />
						<path d="M3 16h3a2 2 0 012 2v3" />
						<path d="M16 21v-3a2 2 0 012-2h3" />
					</svg>
				{:else}
					<svg viewBox="0 0 24 24" aria-hidden="true">
						<path d="M8 3H5a2 2 0 00-2 2v3" />
						<path d="M21 8V5a2 2 0 00-2-2h-3" />
						<path d="M3 16v3a2 2 0 002 2h3" />
						<path d="M16 21h3a2 2 0 002-2v-3" />
					</svg>
				{/if}
			</button>
		</div>
	{/if}
</div>
