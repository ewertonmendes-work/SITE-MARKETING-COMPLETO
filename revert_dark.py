import re

with open('onboarding.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Trocar cor de fundo do body e cor principal
content = content.replace(
    'background-color: #050505;',
    'background-color: var(--pronix-white);' 
)
content = content.replace(
    'color: #ffffff;', 
    'color: var(--pronix-black);'
)

# Textos
content = content.replace(
    'h1,\n        h2,\n        h3,\n        h4,\n        h5,\n        h6 {\n            color: #ffffff;',
    'h1,\n        h2,\n        h3,\n        h4,\n        h5,\n        h6 {\n            color: var(--pronix-black);' 
)
content = content.replace(
    'p,\n        li {\n            margin-bottom: 1rem;\n            color: #aaa;',
    'p,\n        li {\n            margin-bottom: 1rem;\n            color: #333;' 
)
content = content.replace(
    'background-image: radial-gradient(rgba(255,255,255,0.02) 1px, transparent 1px);',
    'background-image: radial-gradient(#e5e5e5 1px, transparent 1px);'
)

# Sidebar
content = content.replace(
    'border-right: 1px solid rgba(255,255,255,0.05);',
    'border-right: 4px solid var(--pronix-yellow);'
)

# Principios List
content = content.replace(
    '.principles-list li {\n            background: rgba(20,20,20,0.8);',
    '.principles-list li {\n            background: white;'
)
content = content.replace(
    'border: 1px solid rgba(255,255,255,0.05);',
    'border: 1px solid #ddd;'
)
content = content.replace(
    'color: #ffffff;\n            font-size: 1.5rem;',
    'color: var(--pronix-black);\n            font-size: 1.5rem;'
)

# Funnel Cards
content = content.replace(
    '.funnel-card {\n            background: rgba(20,20,20,0.8);',
    '.funnel-card {\n            background: white;'
)
content = content.replace(
    '.funnel-card.performance {\n            border-color: var(--pronix-yellow);\n            background: rgba(20,20,20,0.9);',
    '.funnel-card.performance {\n            border-color: var(--pronix-yellow);\n            background: #fff;'
)
content = content.replace(
    '.funnel-card.pap {\n            border-color: var(--pronix-purple);\n            background: rgba(20,20,20,0.9);',
    '.funnel-card.pap {\n            border-color: var(--pronix-purple);\n            background: #fff;'
)
content = content.replace(
    '.funnel-card.club {\n            border-color: rgba(255,255,255,0.1);\n            background: rgba(20,20,20,0.9);',
    '.funnel-card.club {\n            border-color: var(--pronix-black);\n            background: #fff;'
)
content = content.replace(
    '.funnel-card.club .funnel-header {\n            border-bottom: 2px solid rgba(255,255,255,0.1);',
    '.funnel-card.club .funnel-header {\n            border-bottom: 2px solid var(--pronix-black);'
)
content = content.replace(
    '.funnel-card.club .funnel-title {\n            color: #fff;',
    '.funnel-card.club .funnel-title {\n            color: var(--pronix-black);'
)
content = content.replace(
    'border: 2px solid rgba(255,255,255,0.05);',
    'border: 2px solid #ddd;'
)

# Processos específicos
content = content.replace('background: rgba(20,20,20,0.8);', 'background: white;')
content = content.replace('background: rgba(25,25,25,0.8);', 'background: #eee;')
content = content.replace('background: rgba(15,15,15,0.8);', 'background: #fdfdfd;')

# Summary Cards adjustments
content = content.replace(
    '.summary-card {\n            background: rgba(255, 209, 0, 0.9);\n            padding: 1.5rem;\n            color: var(--pronix-black);',
    '.summary-card {\n            background: var(--pronix-yellow);\n            padding: 1.5rem;\n            color: var(--pronix-black);'
)
content = content.replace(
    'border: 1px solid rgba(255,255,255,0.1);',
    'border: 2px solid var(--pronix-black);'
)

# Removendo o grid diagonal
content = content.replace(
    '<body class="min-h-screen flex flex-col items-center">\n    <div class="fixed inset-0 z-[-1] overflow-hidden pointer-events-none">\n        <div class="absolute inset-0 opacity-[0.02]" style="background-image: radial-gradient(#fff 1px, transparent 1px); background-size: 24px 24px;"></div>\n        <div class="absolute top-1/2 right-1/4 w-[400px] h-[400px] bg-brand-yellow/5 rounded-full blur-[100px] animate-pulse"></div>\n        <div class="absolute top-1/4 left-1/4 w-[500px] h-[500px] bg-brand-purple/5 rounded-full blur-[120px] animate-pulse" style="animation-delay: 2s;"></div>\n        <div class="absolute top-[80%] left-[-20%] w-[150%] h-[1px] bg-gradient-to-r from-transparent via-brand-purple/10 to-transparent rotate-[35deg] transform"></div>\n    </div>',
    '<body class="min-h-screen flex flex-col items-center">'
)

with open('onboarding.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Onboarding reverted.")
