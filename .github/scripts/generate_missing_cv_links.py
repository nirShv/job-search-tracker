from pathlib import Path

OUT=Path('Applications'); OUT.mkdir(exist_ok=True)
CONTACT='Tel Aviv-Yafo, Israel | 055-689-5816 | nir1shv@gmail.com | LinkedIn'
COMMON=[
('CallApp | Product Manager, Branded & Verified Caller Identity | March 2023 - August 2026',[
'Owned strategy, roadmap and end-to-end delivery for a B2B SaaS product from discovery and business goals through requirements, launch, KPI tracking and continuous improvement.',
'Translated customer, Support, Sales, business and operational input into PRDs, user stories, UX flows, acceptance criteria, business rules, edge cases and prioritized development tasks.',
'Led API integrations with invoicing, payment and CRM systems, reading technical documentation, mapping dependencies and validating end-to-end behavior.',
'Used GA4, Firebase, customer feedback, product-admin data, defects and support signals to identify friction and prioritize improvements.',
'Used Cursor, Claude, ChatGPT and Codex for discovery, research, requirements, UX exploration, working prototypes and technical feasibility validation.'
]),
('Tapuhi | Founder, Product & Operations Manager | January 2017 - December 2022',[
'Founded and led a D2C eCommerce product from zero, owning the platform, customer journey, pricing, payments, operations, suppliers, staffing, budget and go-to-market execution.',
'Acted as product owner for an external development company, leading discovery, requirements, UX planning, delivery reviews, acceptance testing, launch, issue resolution and post-launch changes.',
'Used customer feedback, user behavior, sales, service and operational data to improve product priorities, workflows and the end-to-end customer journey.'
]),
('HP (HPE) | Business Analyst | January 2015 - December 2016',[
'Gathered business requirements, modeled operational data and translated stakeholder input into workflows, analytical tools, reporting solutions and process improvements for HP Indigo.'
]),
('HP (HPE) | Material Planner Analyst | January 2013 - December 2014',[
'Managed supply-chain planning across six operational divisions, including inventory monitoring, supplier coordination, exception handling and VMI oversight.'
]),
('SAP WIN | Project Manager | February 2012 - January 2013',[
'Managed a year-long, on-site SAP R/3 implementation across Production and Accounting modules, leading requirements, work planning, developer-user coordination, testing, training, Go-Live and post-launch support.'
])]

JOBS={
'Nir_Shvarchberg_CV_morning_Green_Invoice_Product_Manager.pdf':('PRODUCT MANAGER | B2B SAAS, SMB, ANALYTICS & COMMERCIAL OWNERSHIP','Product Manager with 5+ years of relevant experience across B2B SaaS and B2C digital products. Combines end-to-end SaaS ownership with founder-level SMB experience, payments, analytics and commercial decision-making. Experienced in discovery, requirements, roadmap, launch and optimization using GA4 and Firebase, without overstating advanced querying or unit-economics ownership.','B2B SaaS | SMB | Discovery | Roadmap | PRDs | Payments | GA4 | Firebase | Jira | Figma | APIs | Cursor'),
'Nir_Shvarchberg_CV_BiltOn_Senior_Product_Manager.pdf':('SENIOR PRODUCT MANAGER | B2B SAAS, E2E OWNERSHIP & AI-ASSISTED EXECUTION','Senior-level Product Manager with 5+ years of relevant product experience across B2B SaaS and B2C products. Strong in E2E ownership, PRDs, UX flows, APIs, R&D collaboration and Cursor-assisted prototyping. Technical fluency is grounded in integrations, documentation and Full-Stack training, without claiming deep system-architecture or construction-domain expertise.','B2B SaaS | E2E Product Ownership | PRDs | UX | APIs | R&D Collaboration | Jira | Figma | Cursor'),
'Nir_Shvarchberg_CV_Meta_Product_Manager_Growth.pdf':('PRODUCT MANAGER | B2C & B2B, GROWTH, ANALYTICS & CROSS-FUNCTIONAL EXECUTION','Product Manager with 5+ years of relevant experience across B2C and B2B digital products. Owns user and business problems from discovery through roadmap, requirements, launch and optimization, using quantitative data and customer insight to guide prioritization. Uses AI-assisted tools in product work without claiming Meta-scale consumer, A/B testing or AI-product ownership.','B2C | B2B SaaS | Growth | User Needs | Roadmap | Requirements | GA4 | Firebase | Cross-functional Execution'),
'Nir_Shvarchberg_CV_IDX_Product_Manager.pdf':('PRODUCT MANAGER | B2B SAAS, APIS, PRDS & DATA-INFORMED EXECUTION','Product Manager with 5+ years of relevant experience owning B2B SaaS and B2C digital products end to end. Strong in API documentation, PRDs, Jira, analytics and AI-assisted execution with Cursor. Experienced translating business and customer needs into clear requirements, releases and measurable improvements without claiming AdTech or SQL experience.','B2B SaaS | E2E Ownership | APIs | Technical Documentation | PRDs | Jira | GA4 | Firebase | Cursor'),
'Nir_Shvarchberg_CV_Glow_Senior_Product_Manager.pdf':('SENIOR PRODUCT MANAGER | B2B SAAS, TECHNICAL PRODUCT, ANALYTICS & GTM','Senior-level Product Manager with 5+ years of relevant experience across B2B SaaS and B2C products, with E2E ownership, technical product work, APIs, integrations, analytics and GTM collaboration. Tapuhi adds 0-to-1 founder experience. Does not claim cybersecurity, enterprise-customer depth or AI/data-product ownership beyond verified experience.','B2B SaaS | Technical Product | APIs | Integrations | Analytics | GTM | 0-to-1 | Jira | Figma | Cursor'),
'Nir_Shvarchberg_CV_Afeka_Information_Systems_Project_Manager.pdf':('INFORMATION SYSTEMS PROJECT MANAGER | IMPLEMENTATION, REQUIREMENTS & GO-LIVE','Project and Product Manager with extensive experience leading information-systems, ERP and digital initiatives from requirements and planning through implementation, testing, training, Go-Live and support. Combines SAP R/3 implementation, business analysis, vendor coordination and cross-functional delivery.','Information Systems | ERP | SAP R/3 | Requirements | Planning | Testing | Training | Go-Live | Vendors | Jira'),
'Nir_Shvarchberg_CV_Delek_Israel_PMO.pdf':('PMO / PROJECT MANAGER | PORTFOLIO GOVERNANCE, PROCESS DIGITALIZATION & DELIVERY','Project and operations leader with extensive experience coordinating complex technology and business initiatives across SaaS, ERP, industrial operations and vendors. Strong in work planning, dependencies, budgets, reporting, process improvement and cross-functional delivery, without claiming formal PMO tenure or Monday expertise not verified in the CV.','PMO | Portfolio Governance | Work Plans | Budgets | Risks | Dependencies | Process Improvement | Digitalization | Cross-functional Delivery'),
'Nir_Shvarchberg_CV_Papaya_Global_Product_Manager.pdf':('PRODUCT MANAGER | B2B SAAS, E2E PRODUCT OWNERSHIP & INTEGRATIONS','Product Manager with 5+ years of relevant experience across B2B SaaS and B2C digital products. Experienced in discovery, requirements, roadmap, UX, API integrations, analytics, launch and continuous improvement, with founder-level 0-to-1 experience and strong cross-functional execution.','B2B SaaS | Discovery | Roadmap | PRDs | UX | APIs | Integrations | GA4 | Firebase | Jira | Figma')
}

def clean(s):
    return s.replace('–','-').replace('—','-').replace('→','->').replace('’',"'").encode('ascii','ignore').decode('ascii')

def esc(s):
    return s.replace('\\','\\\\').replace('(','\\(').replace(')','\\)')

def wrap(text,n):
    words=text.split(); out=[]; cur=''
    for w in words:
        if len(cur)+(1 if cur else 0)+len(w)<=n: cur=(cur+' '+w).strip()
        else:
            if cur: out.append(cur)
            cur=w
    if cur: out.append(cur)
    return out

def pdf(path, headline, summary, skills):
    y=812; items=[]
    def add(text,size=8,bold=False,before=0,after=0,indent=0):
        nonlocal y
        y-=before; maxchars=max(28,int((520-indent)/(size*.52)))
        for line in wrap(clean(text),maxchars):
            items.append((38+indent,y,size,bold,line)); y-=size*1.2
        y-=after
    add('NIR SHVARCHBERG',18,True,after=2); add(CONTACT,8.7,after=5); add(headline,11.5,True,after=5)
    add('PROFESSIONAL SUMMARY',10,True,before=3,after=1); add(summary,7.8,indent=8,after=2)
    add('PROFESSIONAL EXPERIENCE',10,True,before=3,after=1)
    for role,bullets in COMMON:
        add(role,8.7,True,before=2,after=1)
        for b in bullets: add('- '+b,7.25,indent=8,after=.5)
    add('EDUCATION',10,True,before=3,after=1)
    add('B.Sc. Industrial Engineering & Management | Ben-Gurion University | 2008-2012',7.5)
    add('Full-Stack & Frontend Development | Coding Academy Israel | Jul-Nov 2022',7.5,after=2)
    add('SKILLS & TOOLS',10,True,before=3,after=1); add(skills,7.2)
    stream=['BT']
    for x,yy,size,bold,text in items:
        stream += [f'/F{2 if bold else 1} {size:.2f} Tf',f'1 0 0 1 {x:.1f} {yy:.1f} Tm',f'({esc(text)}) Tj']
    stream.append('ET'); data='\n'.join(stream).encode('latin1')
    objs=[]
    objs.append(b'<< /Type /Catalog /Pages 2 0 R >>')
    objs.append(b'<< /Type /Pages /Kids [3 0 R] /Count 1 >>')
    objs.append(b'<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Resources << /Font << /F1 5 0 R /F2 6 0 R >> >> /Contents 4 0 R >>')
    objs.append(b'<< /Length '+str(len(data)).encode()+b' >>\nstream\n'+data+b'\nendstream')
    objs.append(b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>')
    objs.append(b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>')
    out=b'%PDF-1.4\n'; offsets=[0]
    for i,o in enumerate(objs,1):
        offsets.append(len(out)); out += f'{i} 0 obj\n'.encode()+o+b'\nendobj\n'
    xref=len(out); out += f'xref\n0 {len(objs)+1}\n0000000000 65535 f \n'.encode()
    for off in offsets[1:]: out += f'{off:010d} 00000 n \n'.encode()
    out += f'trailer\n<< /Size {len(objs)+1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n'.encode()
    path.write_bytes(out)

for fn,(headline,summary,skills) in JOBS.items():
    pdf(OUT/fn,headline,summary,skills)
    print('generated',fn)
