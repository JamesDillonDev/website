# -*- coding: utf-8 -*-
"""Build James Dillon's software/engineering CV as a DOCX.

Usage:  python cv/build_cv.py
Deps:   pip install python-docx qrcode pillow

Layout and styling live in cv_style.py, shared with build_cv_hospitality.py.
Writes "James Dillon CV.docx" next to this script. To publish an updated CV on
the site, export it to PDF and copy that into the site:

    soffice --headless --outdir cv --convert-to pdf "cv/James Dillon CV.docx"
    cp "cv/James Dillon CV.pdf" src/lib/assets/James_Dillon_CV.pdf
"""
from cv_style import HERE, PORTFOLIO_URL, CvBuilder, build_qr

OUT_PATH = HERE / "James Dillon CV.docx"

build_qr()
cv = CvBuilder()

# =====================================================================
cv.header(
    name="James Dillon",
    tagline="Software  ·  Electronics  ·  Product Design",
    contact_line=[
        ("Letchworth, Hertfordshire", None),
        ("07821 867254", None),
        ("jamesdillon_@outlook.com", "mailto:jamesdillon_@outlook.com"),
    ],
    link_line=[
        ("linkedin.com/in/jamesdillondev", "https://www.linkedin.com/in/jamesdillondev/"),
        ("github.com/JamesDillonDev", "https://github.com/JamesDillonDev"),
    ],
    qr_caption=["Scan to view my portfolio,", "coursework and projects"],
)

# =====================================================================
cv.heading("Profile", first=True)
cv.paragraph(
    "Sixth form student studying Maths, Computer Science and Product Design, looking for a software or "
    "engineering apprenticeship. I have worked part-time as a junior software engineer at Janus Technology "
    "since July 2025, building features that went out to real customers, and spent a placement at MBDA "
    "working on a Raspberry Pi guided missile project. Outside of school I build things end to end, from a "
    "self-hosted website and home server to 3D-printed electronics projects. I am also a Sergeant in the Air "
    "Cadets, so I am used to teaching, organising and being responsible for other people.",
    before=1, line=1.05)

# =====================================================================
cv.heading("Key Skills")
cv.skill_line("Languages", "C#, Python, JavaScript")
cv.skill_line("Web & software", "SvelteKit, HTML/CSS; building web apps and plugins to a brief")
cv.skill_line("Infrastructure", "Docker, Linux, self-hosting, home networking, automated image builds and deploys")
cv.skill_line("Version control", "Git, GitHub, self-hosted GitLab")
cv.skill_line("AI tooling", "LLM-based automation, Model Context Protocol (MCP) servers, structured knowledge bases")
cv.skill_line("Hardware", "Raspberry Pi, Zigbee, sensors and smart devices, wiring and low-voltage installation, "
                          "hardware integration, testing and fault-finding")
cv.skill_line("Design", "Product and concept design, CAD, 3D printing, electronics, prototyping and iterating "
                        "from a brief (A-Level Product Design, GCSE DT grade 9)")

# =====================================================================
cv.heading("Education")

cv.role("Knights Templar School Sixth Form", "Baldock, Hertfordshire", "Sept 2024 – present")
cv.bullet([("A-Levels (predicted): ", True),
           ("Product Design A*, Computer Science A, Maths B", False)])
cv.bullet([("Extended Project Qualification — A* (50/52): ", True),
           ("designed and built an automatic pet feeder, covering the research, design, electronics and "
            "build. Full write-up on my portfolio.", False)])
cv.bullet([("GCSEs: ", True),
           ("grade 9 in Design and Technology and Computer Science; 8 in Physics and Media; 7 in Maths and "
            "Chemistry; 6 in Biology; 5 in English. Cambridge National in Enterprise and Marketing — M2 "
            "(grade A equivalent). Graded coursework is on my portfolio.", False)])

# =====================================================================
cv.heading("Work Experience")

cv.role("Janus Technology", "Junior Software Engineer (part-time)", "July 2025 – present")
cv.bullet([("Support ticket automation (osTicket) — ", True),
           ("built a plugin for the open-source osTicket helpdesk that reads an incoming ticket, works out "
            "the likely problem and drafts a step-by-step reply, so common queries get a useful first "
            "response without waiting for an agent.", False)])
cv.bullet([("Stile app for AVProEdge — ", True),
           ("added the live video preview feature to a released app that controls multiview video walls. "
            "Every draggable source now shows a real-time preview, so users can tell inputs apart before "
            "assigning them to a display.", False)])
cv.bullet([("AI knowledge base — ", True),
           ("set up a linked Obsidian vault holding API references, example projects and in-house library "
            "notes so AI tools can pull the right context instead of the team pasting docs into a chat "
            "window. Also tested several MCP servers and wrote a custom one to connect AI tools to our "
            "self-hosted GitLab.", False)])
cv.bullet("Worked to a brief on each project, mostly on my own but within a team, and iterated on feedback. "
          "Completed workplace fire warden training.")

cv.role("MBDA", "Engineering Work Experience", "2026")
_b = cv.bullet([("Miniature guided missile — ", True),
                ("worked in a team to design and program a model guided missile running on a Raspberry Pi, "
                 "helping with the code, integrating the hardware, testing the system and tracking down "
                 "faults. Code on GitHub at ", False)])
cv.hyperlink(_b, "JamesDillonDev/mini-missile",
             "https://github.com/JamesDillonDev/mini-missile", size=10, color="1A1A1A")
cv.run(_b, ".", size=10)
cv.bullet("Rotated through systems testing and validation, materials, hardware-in-the-loop, electronics, "
          "production and project management, which showed me how a large engineering programme is "
          "delivered from concept through to implementation.")

# =====================================================================
cv.heading("Projects")

cv.role("OpenHighways — Live UK Traffic Camera Map", "SvelteKit, Leaflet, Docker", "2026")
_b = cv.bullet([("openhighways.uk — ", True),
                ("a free, live map of UK traffic cameras, pulling feeds from National Highways, TfL, Traffic "
                 "Scotland, Traffic Wales and TrafficWatchNI into one place, with on-device vehicle counting "
                 "for busy roads. Code on GitHub at ", False)])
cv.hyperlink(_b, "JamesDillonDev/openhighways",
             "https://github.com/JamesDillonDev/openhighways", size=10, color="1A1A1A")
cv.run(_b, ".", size=10)
cv.bullet("Self-hosted and deployed the same way as my portfolio site, with a Docker image rebuilt and "
          "redeployed automatically on every push.")

cv.role("jamesdillon.uk — Portfolio Website", "SvelteKit, Docker, Raspberry Pi", "2025 – present")
cv.bullet("Built the site in SvelteKit and self-host it from a custom Docker image. Pushing to Git builds a "
          "new image that my server pulls and swaps in automatically, so a deploy takes nothing more than a "
          "git push.")
cv.bullet("Wrote a custom in-page PDF viewer component so my coursework can be read on the site instead of "
          "having to be downloaded first.")

cv.role("Home Assistant Smart Home", "Docker, Zigbee, Raspberry Pi", "2025 – present")
cv.bullet("Rebuilt the family smart home around Home Assistant in Docker. Started with Tapo smart plugs for "
          "lighting, then added Wake-on-LAN control for the TV and Sonos playback.")
cv.bullet("Moved over to Zigbee using a Sonoff dongle and motion sensors for automations like hallway lights "
          "that come on at night and switch themselves off, including planning cable routes and running "
          "low-voltage cabling safely and neatly.")
cv.bullet("Added a wall-mounted Raspberry Pi 4 touchscreen panel so the whole house can use the system "
          "without reaching for a phone. I diagnose and fix the hardware, network and integration problems "
          "myself.")

cv.role("Jellyfin Media Server", "Self-hosted home lab", "2025 – present")
cv.bullet("Run a Jellyfin server holding our media and the CDs I have ripped, so the family has one central "
          "library. Set up to be reliable and simple enough that everyone can use it without my help.")

# =====================================================================
cv.heading("Leadership & Volunteering")

cv.role("RAF Air Cadets, 248 Squadron", "Sergeant", "2022 – present")
cv.bullet("Promoted through four ranks to Sergeant, responsible for the training and welfare of junior "
          "cadets on weekly parade nights.")
cv.bullet("Methods of Instruction qualified, so I plan and deliver lessons to groups of 10–20 and "
          "assess cadets afterwards. Also hold the Silver Leadership award.")
cv.bullet("Qualified First Aid Instructor (St John Ambulance), able to teach and assess first aid as well as "
          "respond to incidents.")
cv.bullet("Represent the squadron at public events such as Remembrance Sunday, and competed in athletics at "
          "Wing and Regional level.")

cv.role("Scouts and Explorers", "Young Leader", "2014 – present")
cv.bullet("Help run weekly meetings at my old Scout group, planning activities, keeping sessions on track "
          "and supporting the leaders.")
cv.bullet("Help organise weekend camps and residentials: sorting equipment, giving safety briefings and "
          "running outdoor activities.")
cv.bullet("Volunteer on the BBQ and bar at Balstock and the Baldock Beer Festival, serving 100+ members of "
          "the public, handling cash and keeping a busy food station clean and safe.")

cv.role("Duke of Edinburgh’s Award", "Bronze completed, Silver in progress", "2022 – present")
cv.bullet("Expeditions in North Yorkshire and the Peak District involving route planning, navigation and "
          "teamwork, volunteering in the local community, and a cybersecurity club covering online safety "
          "and ethical hacking.")

# =====================================================================
cv.heading("Qualifications, Awards & Interests")
cv.skill_line("Qualifications", "Instructor First Aid, St John Ambulance · Methods of Instruction · "
                                "BTEC Level 2 in Teamwork and Personal Development (GCSE equivalent) · "
                                "Air Cadets Silver Leadership · Fire Warden (valid to 2027)")
cv.skill_line("Awards", "EPQ A* (50/52) · Gold medal, Wing-level athletics · GCSE grade 9 in Design "
                        "and Technology and in Computer Science")
cv.skill_line("Interests", "Running (5K PB 20:35), home lab and self-hosting, 3D printing and electronics "
                           "projects")

cv.footer_note("Full write-ups, coursework and source code: ", "jamesdillon.uk", PORTFOLIO_URL)

cv.save(OUT_PATH)
