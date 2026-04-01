<script>
	import heroImage from '$lib/assets/me.jpg';
	import './home.css';
</script>

<svelte:head>
	<title>James Dillon</title>
	<meta
		name="description"
		content="Welcome to James Dillon's personal website. Explore his projects, work experience, and contact information."
	/>
	
</svelte:head>

<section class="hero-banner">
	<img class="hero-image" src={heroImage} alt="Portrait of James Dillon" />
	<div class="hero-overlay">
		<h1>Welcome</h1>
		<p>Find out more about me and my work.</p>
	</div>
</section>

<section class="page-copy">
	<h2>Personal Statement</h2>
	<p>
		I am a motivated and curious student who enjoys learning, creating, and experimenting with new ideas—especially in design and technology. My favourite subject at school is Design and Technology, where I love bringing concepts to life, whether through 3D printing, electronics, or hands-on making. I also have a strong passion for software development, building web apps and tools that solve real problems or showcase my creativity.
	</p>
	<p>   
		Volunteering at different organizations has helped me develop strong teamwork and communication skills. I am keen to gain experience in a professional environment and plan to pursue an apprenticeship after my A Levels, where I can continue learning and developing my skills in both design and software. Outside of school and my projects, I enjoy running (5K PB: 20:35) and am always looking for new challenges.
	</p>
</section>