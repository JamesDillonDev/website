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
    "Year 13 student (Maths, Computer Science, Product Design) and part-time Junior Software Engineer with a "
    "real love of combining hardware and software, in my coursework and personal projects alike. I run a "
    "Docker-based home lab with a Home Assistant smart home (Zigbee devices and wall switches) and a Jellyfin "
    "media server, built an automated pet feeder for my EPQ, and I’m an RAF Air Cadets Sergeant with a keen "
    "interest in aviation. Seeking a software or engineering degree or higher "
    "apprenticeship starting September 2027.",
    before=1, line=1.05)

# =====================================================================
cv.heading("Key Skills")
cv.skill_line("Leadership", "Air Cadets Sergeant responsible for junior cadets; Scouts Young Leader")
cv.skill_line("Communication", "Plan and deliver lessons to groups of 10–20; Instructor First Aid")
cv.skill_line("Teamwork", "Team project on work experience at MBDA; part-time at Janus Technology; volunteer teams at events")
cv.skill_line("Languages", "C#, Python, JavaScript")
cv.skill_line("Web & software", "React, SvelteKit, HTML/CSS; building web apps and plugins to a brief")
cv.skill_line("Infrastructure", "Docker, Linux, self-hosting, home networking, automated image builds and deploys")
cv.skill_line("AI tooling", "LLM-based automation, Model Context Protocol (MCP) servers, structured knowledge bases")
cv.skill_line("Hardware", "Raspberry Pi, Zigbee, LoRa, sensors and smart devices, wiring and low-voltage installation, "
                          "hardware integration, testing and fault-finding")
cv.skill_line("Design", "Product design from brief to prototype: CAD, 3D printing and electronics "
                        "(A-Level Product Design, GCSE DT grade 9)")

# =====================================================================
cv.heading("Education")

cv.role("Knights Templar School Sixth Form", "Baldock, Hertfordshire", "Sept 2024 – present")
cv.bullet([("A-Levels (predicted): ", True),
           ("Product Design A*, Computer Science A, Maths B", False)])
cv.bullet([("Extended Project Qualification — A* (50/52): ", True),
           ("designed and built an automatic pet feeder, covering the research, design, electronics and "
            "build. Full write-up on my portfolio.", False)])
cv.bullet([("GCSEs: ", True),
           ("grade 9 in Design and Technology and Computer Science; 8 in Physics; 7 in Maths; 5 in English; "
            "plus 5 further GCSEs at grades 6–8 and a Cambridge National in Enterprise and Marketing (M2, "
            "grade A equivalent). Graded coursework is on my portfolio.", False)])

# =====================================================================
cv.heading("Work Experience")

cv.role("Janus Technology", "Junior Software Engineer (part-time)", "July 2025 – present")
cv.bullet([("Support ticket automation (osTicket) — ", True),
           ("built a plugin for the open-source osTicket helpdesk that reads each incoming ticket, works out "
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
cv.bullet("Deliver each project to a brief, mostly independently within a small team, revising it after code "
          "review and feedback from colleagues.")

cv.role("MBDA", "Engineering Work Experience", "July 2026")
_b = cv.bullet([("Miniature guided missile — ", True),
                ("in a team, designed and built a model guided missile running on a Raspberry Pi. I wrote part "
                 "of the control code, wired in the hardware, tested the system and tracked down faults. "
                 "Code on GitHub at ", False)])
cv.hyperlink(_b, "JamesDillonDev/mini-missile",
             "https://github.com/JamesDillonDev/mini-missile", size=10, color="1A1A1A")
cv.run(_b, ".", size=10)
cv.bullet("Rotated through systems testing and validation, materials, hardware-in-the-loop, electronics, "
          "production and project management, which showed me how a large engineering programme is "
          "delivered from concept through to implementation.")

# =====================================================================
cv.heading("Leadership & Volunteering")

cv.role("RAF Air Cadets, 248 Squadron", "Sergeant", "2022 – present")
cv.bullet("Promoted through four ranks to Sergeant; train and look after junior cadets every week on parade "
          "nights.")
cv.bullet("Methods of Instruction qualified: I plan and deliver lessons to groups of 10–20 and assess "
          "cadets afterwards. Hold the Silver Leadership award.")
cv.bullet("Qualified First Aid Instructor (St John Ambulance), able to teach and assess first aid as well as "
          "respond to incidents.")
cv.bullet("Represent the squadron at public events such as Remembrance Sunday, and competed in athletics at "
          "Wing and Regional level.")

cv.role("Scouts and Explorers", "Young Leader", "2014 – present")
cv.bullet("Plan and run activities at weekly meetings of my old Scout group, keeping sessions on track and "
          "supporting the leaders.")
cv.bullet("Organise kit, give safety briefings and run outdoor activities on weekend camps and residentials.")
cv.bullet("Volunteer on the BBQ and bar at Balstock and the Baldock Beer Festival, serving 100+ members of "
          "the public, handling cash and keeping a busy food station clean and safe.")

cv.role("VEX Robotics Club", "Team Member & Mentor, Knights Templar School", "Sept 2026 – present")
cv.bullet("Design and build robots for VEX competition tasks such as moving and stacking objects, competing "
          "against other school teams in head-to-head arena matches.")
cv.bullet("In the main team I help design mechanisms and parts. I also mentor younger groups, teaching the "
          "basic ideas and concepts of robot design.")

cv.role("Duke of Edinburgh’s Award", "Bronze completed, Silver in progress", "2022 – present")
cv.bullet("Expeditions in North Yorkshire and the Peak District involving route planning, navigation and "
          "teamwork, volunteering in the local community, and a cybersecurity club covering online safety "
          "and ethical hacking.")

# =====================================================================
cv.heading("Projects")

cv.role("OpenHighways — Live UK Traffic Camera Map", "React, Leaflet, Docker", "2026")
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

cv.role("Home Lab — Home Assistant Smart Home & Jellyfin", "Docker, Zigbee, Raspberry Pi", "2025 – present")
cv.bullet("Rebuilt the family smart home around Home Assistant in Docker. Started with Tapo smart plugs for "
          "lighting, then added Wake-on-LAN control for the TV and Sonos playback.")
cv.bullet("Moved over to Zigbee using a Sonoff dongle and motion sensors for automations like hallway lights "
          "that come on at night and switch themselves off, including planning cable routes and running "
          "low-voltage cabling safely and neatly.")
cv.bullet("Added a wall-mounted Raspberry Pi 4 touchscreen panel so the whole house can use the system "
          "without reaching for a phone. I diagnose and fix the hardware, network and integration problems "
          "myself.")
cv.bullet("Also run a Jellyfin media server so the family has one central library, including the CDs I have "
          "ripped, simple enough for everyone to use without my help.")

# =====================================================================
cv.heading("Qualifications & Interests")
cv.skill_line("Qualifications", "Instructor First Aid (St John Ambulance) · Methods of Instruction · "
                                "BTEC Level 2 Teamwork and Personal Development · Fire Warden")
cv.skill_line("Interests", "Aviation, running (5K PB 20:35, Wing-level athletics gold), home lab and self-hosting, "
                           "3D printing and electronics projects")

cv.footer_note("Full write-ups, coursework and source code: ", "jamesdillon.uk", PORTFOLIO_URL)

cv.save(OUT_PATH)
