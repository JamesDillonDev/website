import { Helmet } from 'react-helmet-async';
import { FaHome } from 'react-icons/fa';
import { SiHomeassistant, SiJellyfin } from 'react-icons/si';

export default function Home() {

  return (
    <>
      <Helmet>
        <title>James Dillon | Home</title>
        <meta name="description" content="Welcome to James Dillon's portfolio. Explore projects, background, and get in touch." />
      </Helmet>
      <img
        src="/me.jpg"
        alt="James Dillon"
        style={{
          width: '100vw',
          height: 480,
          objectFit: 'cover',
          display: 'block',
          marginBottom: '1rem',
          borderRadius: 0,
          position: 'relative',
          left: '50%',
          right: '50%',
          marginLeft: '-50vw',
          marginRight: '-50vw',
          maxWidth: 'none',
        }}
      />
      <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'flex-start', maxWidth: 1200, margin: '0 auto' }}>
        {/* Fixed Quick Links Container */}
        <div style={{ position: 'fixed', top: '120px', left: 0, zIndex: 1000, display: 'flex', flexDirection: 'column', gap: '0.7rem', padding: '1.2rem 0.6rem 1rem 0.6rem', background: 'rgba(245,245,245,0.98)', borderRadius: '0 12px 12px 0', boxShadow: '0 2px 8px rgba(0,0,0,0.07)', fontFamily: 'Roboto Mono, monospace', color: '#222', minWidth: 120, maxWidth: 140 }}>
          <span style={{ fontWeight: 700, fontSize: 14, marginBottom: '0.5rem', letterSpacing: '0.02em', color: '#222' }}>Quick Links</span>
          <button
            onClick={() => window.open('https://home.jamesdillon.uk', '_blank')}
            style={{ display: 'flex', alignItems: 'center', gap: 8, color: '#3949ab', background: '#eaf0fa', border: 'none', fontWeight: 700, fontSize: 14, padding: '0.5rem 0.7rem', borderRadius: 7, cursor: 'pointer', boxShadow: '0 1px 4px rgba(0,0,0,0.07)', marginBottom: 6, transition: 'background 0.2s', width: '100%', minWidth: 80 }}
            title="Home Assistant"
          >
            <span style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', width: 22, height: 22 }}>
              <SiHomeassistant size={18} color="#3949ab" />
            </span>
            <span style={{ fontSize: 13 }}>Home Assistant</span>
          </button>
          <button
            onClick={() => window.open('https://jellyfin.jamesdillon.uk', '_blank')}
            style={{ display: 'flex', alignItems: 'center', gap: 8, color: '#3949ab', background: '#eaf0fa', border: 'none', fontWeight: 700, fontSize: 14, padding: '0.5rem 0.7rem', borderRadius: 7, cursor: 'pointer', boxShadow: '0 1px 4px rgba(0,0,0,0.07)', marginBottom: 6, transition: 'background 0.2s', width: '100%', minWidth: 80 }}
            title="Jellyfin"
          >
            <span style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', width: 22, height: 22 }}>
              <SiJellyfin size={18} color="#3949ab" />
            </span>
            <span style={{ fontSize: 13 }}>Jellyfin</span>
          </button>
        </div>
        {/* Main Content */}
        <div style={{ flex: 1, padding: '2rem 0', fontFamily: 'Roboto Mono, monospace', color: '#222', textAlign: 'left', marginLeft: 140 }}>
          <h2 style={{ fontFamily: 'Roboto Mono, monospace', fontWeight: 700, fontSize: '2.1rem', letterSpacing: '-0.02em', marginBottom: '1.2rem', marginTop: 0, color: '#222', textAlign: 'left' }}>Welcome</h2>
          <p style={{ color: '#888', fontSize: 17, marginBottom: '2rem', textAlign: 'left' }}>
            Hi, I'm James Dillon. I designed and built this website myself using React, combining my interests in both software and physical design. Here you can explore my projects, learn about my background, and get in touch.
          </p>
          <h3 style={{ fontWeight: 700, fontSize: '1.15rem', margin: '2.2rem 0 0.7rem 0', color: '#222', textAlign: 'left' }}>Personal Statement</h3>
          <p style={{ fontSize: 16, margin: '0.7em 0 0 0', color: '#888', textAlign: 'left' }}>
            I am a motivated and curious student who enjoys learning, creating, and experimenting with new ideas—especially in design and technology. My favourite subject at school is Design and Technology, where I love bringing concepts to life, whether through 3D printing, electronics, or hands-on making. I also have a strong passion for software development, building web apps and tools that solve real problems or showcase my creativity.
          </p>
          <p style={{ fontSize: 16, margin: '0.7em 0 2.2em 0', color: '#888', textAlign: 'left' }}>
            Volunteering at different organizations has helped me develop strong teamwork and communication skills. I am keen to gain experience in a professional environment and plan to pursue an apprenticeship after my A Levels, where I can continue learning and developing my skills in both design and software. Outside of school and my projects, I enjoy running (5K PB: 20:35) and am always looking for new challenges.
          </p>
          <h3 style={{ fontWeight: 700, fontSize: '1.15rem', margin: '2.2rem 0 0.7rem 0', color: '#222', textAlign: 'left' }}>Explore the site</h3>
          <ul style={{ fontSize: 16, margin: '0.7em 0 0 0', paddingLeft: '1.2em', color: '#888', textAlign: 'left' }}>
            <li><strong>About</strong> – My education, experience, and qualifications.</li>
            <li><strong>Work</strong> – My professional work experience and projects.</li>
            <li><strong>Design</strong> – Physical and 3D-printed projects, including a Children's Piano.</li>
            <li><strong>Software</strong> – Software projects with live GitHub stats.</li>
            <li><strong>Contact</strong> – Get in touch with me directly.</li>
          </ul>
        </div>
      </div>
    </>
  );
}
