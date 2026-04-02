<script>
	import './contact.css';
	import emailjs from '@emailjs/browser';

	let form = $state({
		name: '',
		email: '',
		message: ''
	});

	let alert = $state({
		show: false,
		type: '',
		message: ''
	});

	/** @type {ReturnType<typeof setTimeout> | undefined} */
	let dismissTimer;

	function hideAlertLater() {
		clearTimeout(dismissTimer);
		dismissTimer = setTimeout(() => {
			alert = { show: false, type: '', message: '' };
		}, 4000);
	}

	/** @param {Event & { currentTarget: HTMLInputElement | HTMLTextAreaElement }} event */
	function handleChange(event) {
		const { name, value } = event.currentTarget;
		form = { ...form, [name]: value };
	}

	/** @param {SubmitEvent} event */
	async function handleSubmit(event) {
		event.preventDefault();

		const SERVICE_ID = import.meta.env.VITE_EMAILJS_SERVICE_ID;
		const TEMPLATE_ID = import.meta.env.VITE_EMAILJS_TEMPLATE_ID;
		const PUBLIC_KEY = import.meta.env.VITE_EMAILJS_PUBLIC_KEY;

		if (!SERVICE_ID || !TEMPLATE_ID || !PUBLIC_KEY) {
			alert = {
				show: true,
				type: 'danger',
				message: 'Contact form is not configured yet. Missing EmailJS settings.'
			};
			hideAlertLater();
			console.error('EmailJS config missing', {
				hasServiceId: Boolean(SERVICE_ID),
				hasTemplateId: Boolean(TEMPLATE_ID),
				hasPublicKey: Boolean(PUBLIC_KEY)
			});
			return;
		}

		const templateParams = {
			from_name: form.name,
			from_email: form.email,
			message: `Sender Email: ${form.email}\n\n${form.message}`,
			to_email: 'jamesdillon_@outlook.com'
		};

		try {
			await emailjs.send(SERVICE_ID, TEMPLATE_ID, templateParams, PUBLIC_KEY);
			alert = {
				show: true,
				type: 'success',
				message: 'Thank you for contacting!'
			};
			form = { name: '', email: '', message: '' };
			hideAlertLater();
		} catch (error) {
			alert = {
				show: true,
				type: 'danger',
				message: 'Failed to send message. Please check your EmailJS setup and try again.'
			};
			hideAlertLater();
			console.error('EmailJS error:', error);
		}
	}
</script>

<svelte:head>
	<title>James Dillon | Contact</title>
	<meta name="description" content="Contact James Dillon directly via email form." />
</svelte:head>

<section class="contact-page">
	<div class="contact-shell">
		<h1>Contact</h1>
		<p class="intro-copy">Get in touch directly using the form below.</p>

		{#if alert.show}
			<div class={`alert alert-${alert.type}`} role="alert">
				{alert.message}
			</div>
		{/if}

		<form class="contact-form" onsubmit={handleSubmit}>
			<div class="field-row">
				<label for="name">Name</label>
				<input
					id="name"
					name="name"
					type="text"
					value={form.name}
					oninput={handleChange}
					required
					placeholder="John Smith"
				/>
			</div>

			<div class="field-row">
				<label for="email">Email</label>
				<input
					id="email"
					name="email"
					type="email"
					value={form.email}
					oninput={handleChange}
					required
					placeholder="example@outlook.com"
				/>
			</div>

			<div class="field-row message-row">
				<label for="message">Message</label>
				<textarea
					id="message"
					name="message"
					rows="4"
					value={form.message}
					oninput={handleChange}
					required
				></textarea>
			</div>

			<button type="submit">Contact</button>
		</form>
	</div>
</section>
