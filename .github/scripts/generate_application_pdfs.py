from pathlib import Path
import re

OUT = Path('Applications')
OUT.mkdir(exist_ok=True)

CONTACT = 'Tel Aviv-Yafo, Israel | 055-689-5816 | nir1shv@gmail.com | LinkedIn'

COMMON = {
'product': [
('CallApp | Product Manager, Branded & Verified Caller Identity | March 2023 - August 2026', [
'Owned strategy, roadmap, and end-to-end delivery for a B2B SaaS product, from discovery and business goals through requirements, launch, KPI tracking, and continuous improvement.',
'Translated customer, Support, Sales, business, and operational input into PRDs, user stories, UX flows, acceptance criteria, business rules, edge cases, and prioritized development tasks.',
'Led product workstreams across onboarding, business profiles, verification, activation, subscriptions, payments, analytics, and post-signup experience.',
'Aligned Engineering, UX, QA, Data, Marketing, Support, Sales, leadership, and vendors on scope, tradeoffs, priorities, release readiness, rollout, and follow-up using Jira and Figma.',
'Led API integrations with invoicing, payment, and CRM systems, reading technical documentation, defining requirements, mapping dependencies, and validating end-to-end behavior.',
'Used GA4, Firebase, customer feedback, product-admin data, defects, and support signals to identify friction and prioritize improvements; mobile traffic share increased from 10% to 60% following mobile UX and campaign-flow changes.',
'Used Cursor, Claude, ChatGPT, and Codex for discovery, research, requirements, UX exploration, working prototypes, and technical feasibility validation.'
]),
('Tapuhi | Founder, Product & Operations Manager | January 2017 - December 2022', [
'Founded and led a D2C eCommerce product from zero, owning the platform, customer journey, pricing, payments, operations, suppliers, staffing, budget, and go-to-market execution.',
'Acted as product owner for an external development company, leading discovery, requirements, UX planning, delivery reviews, acceptance testing, launch, issue resolution, and post-launch changes.',
'Used customer feedback, user behavior, sales, service, and operational data to improve product priorities, workflows, and the end-to-end customer journey.',
'Managed parallel workstreams and vendors across technology, marketing, logistics, packaging, payment processing, and customer operations.'
]),
('HP (HPE) | Business Analyst | January 2015 - December 2016', [
"Gathered business requirements, modeled operational data, and translated complex stakeholder input into workflows, analytical tools, reporting solutions, and process improvements for HP Indigo's industrial product line.",
'Coordinated operations, planning, business, and technical stakeholders to improve performance visibility, decision-making, process consistency, and cost efficiency.'
]),
('HP (HPE) | Material Planner Analyst | January 2013 - December 2014', [
'Managed supply-chain planning across six operational divisions, including inventory monitoring, supplier coordination, exception handling, and VMI oversight; wrote work manuals and trained four logistics specialists.'
]),
('SAP WIN | Project Manager | February 2012 - January 2013', [
'Managed a year-long, on-site SAP R/3 implementation across Production and Accounting modules, leading requirements, work planning, developer-user coordination, testing, training, Go-Live, and post-launch support.'
])],
'project': [
('CallApp | Product Manager, Branded & Verified Caller Identity | March 2023 - August 2026', [
'Led end-to-end delivery of B2B SaaS initiatives from business and customer requirements through specifications, development, QA, release readiness, launch, and follow-up.',
'Translated customer, Support, Sales, business, and operational needs into PRDs, user stories, acceptance criteria, business rules, edge cases, UX flows, and prioritized implementation tasks.',
'Led API integrations with invoicing, payment, and CRM systems, reading technical documentation, mapping data flows and dependencies, defining expected behavior, and validating end-to-end flows.',
'Coordinated Engineering, UX, QA, Data, Support, Sales, Operations, leadership, and external providers on scope, timelines, dependencies, issue resolution, and release readiness using Jira and Figma.',
'Used GA4, Firebase, product-admin data, defects, and support signals to validate behavior, identify friction, and prioritize corrective and improvement work.',
'Used Claude, ChatGPT, Cursor, and Codex for research, requirements, documentation, prototypes, and technical feasibility validation.'
]),
('Tapuhi | Founder, Product & Operations Manager | January 2017 - December 2022', [
'Founded and operated a D2C eCommerce business, managing the digital platform, suppliers, staffing, logistics, payments, budget, customer service, and day-to-day operations.',
'Managed an external development company from requirements and UX planning through delivery reviews, acceptance testing, launch, issue resolution, and post-launch changes.',
'Coordinated technology, logistics, packaging, payment, credit-card, and marketing vendors across multiple parallel workstreams and operational dependencies.',
'Built working procedures and used customer, sales, service, and operational data to improve workflows, exception handling, and service delivery.'
]),
('HP (HPE) | Business Analyst | January 2015 - December 2016', [
"Gathered business requirements, modeled operational data, and translated complex stakeholder input into workflows, analytical tools, reporting solutions, and process improvements for HP Indigo's industrial product line.",
'Coordinated operations, planning, business, and technical stakeholders to improve performance visibility, decision-making, process consistency, and cost efficiency.'
]),
('HP (HPE) | Material Planner Analyst | January 2013 - December 2014', [
'Managed supply-chain planning across six operational divisions, including inventory monitoring, supplier coordination, exception handling, and VMI oversight; wrote work manuals and trained four logistics specialists.'
]),
('SAP WIN | Project Manager | February 2012 - January 2013', [
'Managed a year-long, on-site SAP R/3 implementation across Production and Accounting modules, leading requirements, work planning, developer-user coordination, testing, training, Go-Live, and post-launch support.'
])]
}

JOBS = {
'Nir_Shvarchberg_CV_Partnerize_Senior_Product_Manager.pdf': ('product','SENIOR PRODUCT MANAGER | B2B SAAS, STRATEGY, DISCOVERY & GTM','Product Manager with 5+ years of experience owning B2B SaaS and B2C digital products from discovery through launch, adoption, and iteration. Turns customer, business, and operational insights into product strategy, roadmaps, clear requirements, prioritized delivery plans, and measurable outcomes. Experienced aligning Engineering, UX, Data, Marketing, Support, Sales, and external partners across complex initiatives, with hands-on use of analytics and AI-assisted tools to accelerate product work.','Product Strategy & Delivery: Discovery, roadmaps, PRDs, user stories, prioritization, launch, adoption, GTM, Agile/Scrum, Jira, Figma | Data, Technical & AI: KPIs, GA4, Firebase, funnel analysis, APIs, integrations, basic SQL, Cursor, Claude, ChatGPT, Codex'),
'Nir_Shvarchberg_CV_FIBI_Product_Manager_Digital_Unit.pdf': ('product','PRODUCT MANAGER | DIGITAL PRODUCTS, B2C/B2B SAAS & DATA-DRIVEN DELIVERY','Product Manager with 5+ years of experience owning B2C and B2B digital products across the full lifecycle, from discovery and strategy through requirements, UX, development, launch, analytics, and optimization. Combines consumer eCommerce ownership with B2B SaaS experience, payments and API integrations, and data-informed decision-making using GA4 and Firebase. Strong at translating business needs and user behavior into clear product priorities and cross-functional execution.','Digital Product: Strategy, discovery, roadmaps, requirements, UX, user journeys, onboarding, activation, subscriptions, payments, launch and iteration | Data & Technical: GA4, Firebase, KPIs, APIs, integrations, Jira, Figma, Cursor'),
'Nir_Shvarchberg_CV_Tenable_Product_Manager_AI_Exposure.pdf': ('product','PRODUCT MANAGER | B2B SAAS, DISCOVERY, ROADMAPS & TECHNICAL DELIVERY','Product Manager with 5+ years of relevant experience across B2B SaaS and B2C digital products, owning discovery, roadmaps, requirements, cross-functional delivery, launch, and iteration. Technically fluent in APIs and integrations, experienced translating customer and business needs into product decisions, and comfortable working with Engineering, UX, Sales, Support, and Marketing. Uses data and AI-assisted tools to accelerate product work without overstating AI product ownership.','B2B SaaS Product: Discovery, roadmaps, customer requirements, PRDs, prioritization, launch, GTM and iteration | Technical & Data: APIs, integrations, GA4, Firebase, Jira, Figma, Cursor, Claude, ChatGPT, Codex'),
'Nir_Shvarchberg_CV_Wix_Product_Manager_Premium_Growth.pdf': ('product','PRODUCT MANAGER | GROWTH, SELF-SERVE, MONETIZATION & B2C ECOMMERCE','Product Manager with 5+ years of experience across B2B SaaS and B2C digital products, with hands-on ownership of self-serve journeys, onboarding, activation, subscriptions, payments, funnels, UX, launch, and optimization. Combines CallApp product ownership with founder-level B2C eCommerce experience at Tapuhi and uses GA4, Firebase, Cursor, and AI-assisted prototyping to improve product and monetization flows.','Growth & Monetization: Self-serve, funnels, KPIs, onboarding, activation, subscriptions, payments, pricing and eCommerce | Data & Technical: GA4, Firebase, APIs, integrations, Cursor, AI-assisted prototyping, Jira and Figma'),
'Nir_Shvarchberg_CV_Silverfort_Product_Manager.pdf': ('product','PRODUCT MANAGER | B2B SAAS, PLATFORM OWNERSHIP, UX & INTEGRATIONS','Product Manager with 5+ years of relevant experience owning B2B SaaS and B2C digital products from discovery through roadmap, requirements, UX, launch, analytics, and iteration. Strong in platform workflows, API integrations, user journeys, technical collaboration, and data-informed prioritization, with hands-on use of AI-assisted tools for research, specifications, prototyping, and feasibility validation.','B2B SaaS & Platform: Strategy, roadmaps, PRDs, UX flows, user journeys, launch and iteration | Technical & Data: APIs, integrations, GA4, Firebase, Jira, Figma, Cursor and AI-assisted tools'),
'Nir_Shvarchberg_CV_Fordefi_Technical_Product_Manager.pdf': ('product','TECHNICAL PRODUCT MANAGER | B2B SAAS, APIS, INTEGRATIONS & UX','Technical Product Manager with 5+ years of relevant product experience across B2B SaaS and B2C digital products. Experienced in customer discovery, technical requirements, API integrations, UX flows, delivery, launch, and data-informed iteration. Combines product ownership with Full-Stack training and hands-on work with technical documentation, payments, CRM, invoicing, analytics, and AI-assisted prototyping.','Technical Product: APIs, integrations, technical requirements, data flows, UX, roadmaps, launch and iteration | Tools: GA4, Firebase, Jira, Figma, Cursor, Claude, ChatGPT, Codex, basic SQL'),
'Nir_Shvarchberg_CV_Primis_McCann_Product_Manager.pdf': ('product','PRODUCT MANAGER | B2B SAAS, API PLATFORM & CLIENT-FACING EXECUTION','Product Manager with 5+ years of relevant experience owning B2B SaaS and B2C digital products from customer needs through requirements, UX, delivery, launch, analytics, and iteration. Strong in APIs and integrations, client-facing discovery, platform workflows, cross-functional execution, and AI-assisted prototyping, with founder-level 0-to-1 business ownership from Tapuhi.','B2B Platform Product: Customer discovery, requirements, PRDs, UX, APIs, integrations, launch and iteration | Execution: Jira, Figma, GA4, Firebase, Cursor, Claude, ChatGPT, Codex'),
'Nir_Shvarchberg_CV_Opmed_AI_Product_Manager.pdf': ('product','PRODUCT MANAGER | END-TO-END EXECUTION, PROTOTYPING & DATA-INFORMED DELIVERY','Hands-on Product Manager with 5+ years of experience owning B2B SaaS and B2C digital products from problem definition through requirements, design, development, launch, and continuous improvement. Strong in PRDs, UX flows, Agile execution, analytics, API integrations, and cross-functional alignment. Uses Cursor, Claude, ChatGPT, and Codex to accelerate discovery, specifications, prototyping, and technical feasibility validation while keeping product decisions grounded in user, business, and operational needs.','Product Delivery: Discovery, roadmaps, PRDs, UX flows, acceptance criteria, prioritization, Agile/Scrum, launch and iteration | Data & AI: GA4, Firebase, APIs, integrations, Cursor, Claude, ChatGPT, Codex'),
'Nir_Shvarchberg_CV_Scytale_Senior_Product_Manager.pdf': ('product','SENIOR PRODUCT MANAGER | B2B SAAS, CORE PRODUCT, UX & KPI OWNERSHIP','Product Manager with 5+ years of relevant experience owning B2B SaaS and B2C digital products from discovery and strategy through roadmap, execution, launch, KPIs, and iteration. Strong in translating customer and business needs into prioritized backlogs, PRDs, UX flows, and measurable product improvements. Experienced partnering with Engineering, Design, Data, Sales, Support, and Marketing in fast-moving environments and using analytics and AI-assisted tools to accelerate product work.','B2B SaaS Product: Strategy, discovery, roadmaps, prioritization, PRDs, UX flows, backlog, launch, KPIs and iteration | Data & Technical: GA4, Firebase, APIs, integrations, payments, CRM, Jira, Figma, Cursor'),
'Nir_Shvarchberg_CV_Nayax_Project_Manager_Retail.pdf': ('project','PROJECT MANAGER | ERP, SOFTWARE IMPLEMENTATION, INTEGRATIONS & GO-LIVE','Project and Product Manager with extensive experience leading software, ERP, and digital initiatives from requirements and planning through implementation, UAT, Go-Live, and post-launch support. Combines hands-on SAP R/3 implementation experience with B2B SaaS, API integrations, customer and operational requirements, vendor coordination, and cross-functional delivery. Uses Jira, Figma, analytics, and AI-assisted tools to clarify requirements, accelerate documentation, and support execution.','Project & Implementation: Requirements, work planning, dependencies, UAT, QA, Go-Live, stakeholder/vendor management | ERP & Technical: SAP R/3, APIs, integrations, payments, CRM, invoicing, Jira, Figma, AI-assisted tools'),
'Nir_Shvarchberg_CV_Applied_Materials_Integration_Manager.pdf': ('project','INTEGRATION / PROJECT MANAGER | PLANNING, OPERATIONS & CROSS-FUNCTIONAL EXECUTION','Project and operations leader with extensive experience coordinating complex, cross-functional initiatives across technology, industrial operations, SaaS, ERP, vendors, and business teams. Strong in work planning, requirements, dependencies, risks, reporting, process improvement, implementation, and Go-Live. Combines an Industrial Engineering & Management degree with hands-on experience in HP Indigo operations and supply-chain planning, SAP R/3 implementation, and digital product delivery.','Project & Integration: Work planning, requirements, dependencies, risks, reporting, process improvement, delivery, Go-Live, stakeholder/vendor management | Industrial & Technical: HP Indigo operations, supply-chain planning, SAP R/3, APIs, integrations, analytics, Jira, Figma')
}

def clean(s):
    return s.replace('–','-').replace('—','-').replace('‑','-').replace('’',"'").replace('→','->').encode('ascii','ignore').decode('ascii')

def esc(s):
    return s.replace('\\','\\\\').replace('(','\\(').replace(')','\\)')

def wrap(text, maxchars):
    words=text.split(); lines=[]; cur=''
    for w in words:
        if len(cur)+(1 if cur else 0)+len(w) <= maxchars: cur=(cur+' '+w).strip()
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines

def make_pdf(filename, kind, headline, summary, skills):
    items=[]; y=812; left=38; right=557
    def add(text,size=8,bold=False,leading=None,indent=0,before=0,after=0):
        nonlocal y
        y-=before; leading=leading or size*1.18
        maxchars=max(30,int((right-left-indent)/(size*.52)))
        for line in wrap(clean(text),maxchars):
            items.append((left+indent,y,size,bold,line)); y-=leading
        y-=after
    add('NIR SHVARCHBERG',18,True,21,after=2)
    add(CONTACT,8.8,False,10.5,after=4)
    add(headline,11.5,True,13.5,after=6)
    add('PROFESSIONAL SUMMARY',10,True,11.5,before=4,after=2)
    add('- '+summary,7.8,False,9.3,indent=10,after=1)
    add('PROFESSIONAL EXPERIENCE',10,True,11.5,before=4,after=2)
    for role, bullets in COMMON[kind]:
        add(role,9,True,10.5,before=3,after=1)
        for b in bullets: add('- '+b,7.8,False,9.3,indent=10,after=1)
    add('EDUCATION',10,True,11.5,before=4,after=2)
    add('Ben-Gurion University of the Negev | B.Sc. in Industrial Engineering & Management | 2008 - 2012',8.3,False,10,after=1)
    add('Coding Academy Israel | Full-Stack & Frontend Development | July - November 2022',8.3,False,10,after=1)
    add('SKILLS & TOOLS',10,True,11.5,before=4,after=2)
    add(skills,7.8,False,9.3,indent=10,after=1)
    add('Languages: Hebrew: Native | English: Fluent',8,False,9.5)
    top=max(v[1] for v in items); bottom=min(v[1] for v in items); target=62
    factor=min(1.38,(top-target)/(top-bottom)) if bottom>target else 1
    items=[(x,top-(top-yy)*factor,sz,b,t) for x,yy,sz,b,t in items]
    stream=['q','0 0 0 rg']
    for x,yy,sz,bold,text in items:
        stream += ['BT',f"/{'F2' if bold else 'F1'} {sz:.2f} Tf",f'1 0 0 1 {x:.2f} {yy:.2f} Tm',f'({esc(text)}) Tj','ET']
    stream += ['Q']; data=('\n'.join(stream)+'\n').encode('ascii')
    objs=[b'<< /Type /Catalog /Pages 2 0 R >>',b'<< /Type /Pages /Kids [3 0 R] /Count 1 >>',b'<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Resources << /Font << /F1 5 0 R /F2 6 0 R >> >> /Contents 4 0 R >>',b'<< /Length '+str(len(data)).encode()+b' >>\nstream\n'+data+b'endstream',b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>',b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>']
    out=bytearray(b'%PDF-1.4\n'); offs=[0]
    for i,obj in enumerate(objs,1): offs.append(len(out)); out+=f'{i} 0 obj\n'.encode()+obj+b'\nendobj\n'
    xref=len(out); out+=f'xref\n0 {len(objs)+1}\n'.encode()+b'0000000000 65535 f \n'
    for off in offs[1:]: out+=f'{off:010d} 00000 n \n'.encode()
    out+=f'trailer\n<< /Size {len(objs)+1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n'.encode()
    (OUT/filename).write_bytes(out)

for filename, spec in JOBS.items():
    make_pdf(filename,*spec)
print(f'Generated {len(JOBS)} application PDFs')
