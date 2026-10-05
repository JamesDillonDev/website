# -*- coding: utf-8 -*-
"""Build James Dillon's cover letter template as a DOCX.

Usage:  python cv/build_cover_letter.py
Deps:   pip install python-docx qrcode pillow

Uses the same header and styling as the CV (cv_style.py). Anything in
[square brackets] is a placeholder: it is highlighted yellow in the output so
it is obvious what still needs filling in or deleting before sending.
"""
import re

from docx.enum.text import WD_COLOR_INDEX

from cv_style import HERE, CvBuilder, build_qr

OUT_PATH = HERE / "James Dillon Cover Letter Template.docx"

build_qr()
cv = CvBuilder()


def para(text, before=0, after=9, size=10.5, line=1.15, bold=False):
    """Paragraph where [bracketed] text is highlighted as a placeholder."""
    p = cv.set_spacing(cv.doc.add_paragraph(), before=before, after=after, line=line)
    for chunk in re.split(r"(\[[^\]]*\])", text):
        if not chunk:
            continue
        r = cv.run(p, chunk, size=size, bold=bold)
        if chunk.startswith("["):
            r.font.highlight_color = WD_COLOR_INDEX.YELLOW
    return p


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

para("[Date]", before=8, after=9)

para("[Hiring manager name, or “Hiring Manager”]", after=0)
para("[Company name]", after=0)
para("[Company address]", after=12)

para("Dear [Mr/Ms Surname / Hiring Manager],", after=9)

para("Re: Application for [apprenticeship / role title] ([reference number, if any])",
     after=9, bold=True)

# Opening: who, what, why this company
para("I am a Year 13 student at Knights Templar School Sixth Form studying Maths, Computer Science and "
     "Product Design, and I am writing to apply for the [role title] at [company]. I am drawn to [company] "
     "because [one specific reason: a product, project, value or something you read about them], and I "
     "would like to build my career in [software / electronics / engineering] with a team that [what "
     "attracted you to them].")

# Experience: software
para("I already work as a part-time Junior Software Engineer at Janus Technology, where I built a plugin "
     "for the osTicket helpdesk that reads an incoming ticket and drafts a step-by-step reply, added a "
     "live video preview feature to a released app that controls multiview video walls, and set up an AI "
     "knowledge base and a custom MCP server for the team. That has taught me to work to a brief, "
     "iterate on feedback and ship something people actually use. [Tie this to a specific need in the "
     "job advert.]")

# Experience: hardware / engineering
para("What I enjoy most is combining software with hardware. At MBDA I worked in a team to design and "
     "program a miniature guided missile on a Raspberry Pi, helping with the code, integrating the "
     "hardware and tracking down faults, and I saw how a large engineering programme is delivered from "
     "concept to implementation. At home I run a Home Assistant smart home on Zigbee, built an automatic "
     "pet feeder for my Extended Project Qualification (A*), and created OpenHighways, a live map of UK "
     "traffic cameras that I self-host with automated Docker deploys. [Pick the one or two most relevant "
     "to this role and cut the rest.]")

# Character: leadership / teamwork
para("Outside of study I am a Sergeant in the RAF Air Cadets, where I plan and deliver lessons to groups "
     "of 10–20 and am responsible for the training and welfare of junior cadets. I am also a Scouts Young "
     "Leader and a qualified First Aid Instructor. These have given me the confidence to lead, communicate "
     "clearly and stay calm and organised in a team. [Optional: link this to the company’s culture.]")

# Close
para("I would welcome the chance to discuss how I could contribute to [company]. My CV is attached, and my "
     "coursework, projects and source code are available at jamesdillon.uk. Thank you for your time and "
     "consideration.")

para("Yours sincerely,   [or “Yours faithfully,” if you used “Dear Hiring Manager”]", before=2, after=26)

para("James Dillon", after=0, bold=True)

cv.footer_note("Full write-ups, coursework and source code: ", "jamesdillon.uk", "https://jamesdillon.uk",
               before=14)

cv.save(OUT_PATH)
