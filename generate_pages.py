import os

template = """<!DOCTYPE html>
<html lang="pt-BR" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | PRONIX</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{ darkMode: 'class', theme: {{ extend: {{ fontFamily: {{ sans: ['"Inter"', 'sans-serif'], display: ['"Barlow Condensed"', 'sans-serif'] }}, colors: {{ brand: {{ yellow: '#FFD100', purple: '#6D28D9', blue: '#3b82f6', emerald: '#10b981' }} }} }} }} }}
    </script>
    <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700;800;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>body {{ background-color: #000000; color: #fff; }}</style>
</head>
<body class="min-h-screen p-6 md:p-12 max-w-4xl mx-auto">
    <a href="{back_url}" class="inline-flex items-center text-gray-400 hover:text-white transition-colors text-sm font-bold uppercase tracking-wider mb-8"><i data-lucide="arrow-left" class="w-4 h-4 mr-2"></i> Voltar</a>
    <header class="mb-12 border-b border-gray-800 pb-8 flex items-center gap-4">
        <div class="w-16 h-16 rounded-2xl bg-gray-900 flex items-center justify-center border border-gray-700"><i data-lucide="{icon}" class="w-8 h-8 text-white"></i></div>
        <div>
            <h1 class="font-display text-4xl md:text-5xl font-black uppercase text-white leading-none">{title}</h1>
            <p class="text-gray-400 font-sans mt-2">{subtitle}</p>
        </div>
    </header>
    <main class="space-y-6">
        <div class="bg-gray-900 border border-gray-800 p-12 rounded-2xl flex flex-col items-center justify-center text-center">
            <i data-lucide="construction" class="w-16 h-16 text-brand-yellow mb-4"></i>
            <h2 class="font-display text-3xl font-black uppercase text-white mb-2">Página de Template</h2>
            <p class="text-gray-400 text-lg max-w-lg">Este é um exemplo visual. O conteúdo real de {title} será preenchido aqui futuramente com textos, imagens e documentação.</p>
        </div>
    </main>
    <script>lucide.createIcons();</script>
</body>
</html>"""

pages = [
    ("playbook-lancamento.html", "Lançamento", "playbooks.html", "rocket", "Guia completo de estratégia de captação e conversão de Lançamentos."),
    ("playbook-trafego.html", "Tráfego", "playbooks.html", "mouse-pointer-click", "Estrutura de testes, hierarquia de públicos e escala."),
    ("playbook-criativos.html", "Criativos", "playbooks.html", "video", "Frameworks MCC, ganchos e retenção nos primeiros 3s."),
    ("playbook-copy.html", "Copy", "playbooks.html", "pen-tool", "Modelos de VSL e scripts comprovados."),
    ("playbook-socialmedia.html", "Social Media", "playbooks.html", "instagram", "Linha editorial e funil de stories."),
    ("playbook-landingpage.html", "Landing Page", "playbooks.html", "layout", "Anatomia da LP de alta conversão."),
    ("db-objecoes.html", "Objeções & Respostas", "banco-de-dados.html", "message-square", "Mapeamento das objeções universais e scripts de contorno."),
    ("db-calls.html", "Transcrições de Closer", "banco-de-dados.html", "headphones", "Chamadas de vendas gravadas e analisadas."),
    ("db-prompts.html", "Prompts Inteligentes", "banco-de-dados.html", "terminal", "Acervo de prompts otimizados para ChatGPT/Claude."),
    ("treinamento-clickup.html", "Como usar o ClickUp", "treinamentos.html", "play-circle", "Como operamos, abrimos cards e documentamos tarefas."),
    ("treinamento-criativos.html", "Variações de Criativos", "treinamentos.html", "play-circle", "Processo de edição para gerar R1, R2, e P2 de campeões."),
    ("galeria.html", "A Galeria Oficial", "index.html", "camera", "Fotos e bastidores dos eventos e da equipe PRONIX.")
]

dir_path = "/Users/ewertonmendes/Desktop/SITE-MARKETING-COMPLETO"

for filename, title, back_url, icon, subtitle in pages:
    filepath = os.path.join(dir_path, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(template.format(title=title, back_url=back_url, icon=icon, subtitle=subtitle))

print("Created 12 template pages.")

def replace_in_file(filepath, old, new):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    content = content.replace(old, new)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

# Update Playbooks
p_html = os.path.join(dir_path, "playbooks.html")
replace_in_file(p_html, '<div class="playbook-card rounded-2xl p-6 cursor-pointer">', '<a href="playbook-lancamento.html" class="playbook-card block rounded-2xl p-6 cursor-pointer" style="text-decoration:none;">')
# Manual string manipulation is hard when multiple are identical, so let's rewrite specific blocks

def rewrite_playbooks():
    content = open(p_html, "r", encoding="utf-8").read()
    new_grid = """<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <a href="playbook-lancamento.html" class="playbook-card block text-left rounded-2xl p-6 cursor-pointer" style="text-decoration:none;">
                <i data-lucide="rocket" class="w-6 h-6 text-brand-purple mb-4"></i>
                <h3 class="font-display text-2xl font-black uppercase mb-2">Lançamento</h3>
                <p class="text-sm text-gray-400">Estrutura de captação, CPLs, e cronograma de abertura de carrinho.</p>
            </a>
            <a href="playbook-trafego.html" class="playbook-card block text-left rounded-2xl p-6 cursor-pointer" style="text-decoration:none;">
                <i data-lucide="mouse-pointer-click" class="w-6 h-6 text-brand-purple mb-4"></i>
                <h3 class="font-display text-2xl font-black uppercase mb-2">Tráfego Pago</h3>
                <p class="text-sm text-gray-400">Estrutura de campanhas no Meta/Google, testes ABO/CBO e métricas.</p>
            </a>
            <a href="playbook-criativos.html" class="playbook-card block text-left rounded-2xl p-6 cursor-pointer" style="text-decoration:none;">
                <i data-lucide="video" class="w-6 h-6 text-brand-purple mb-4"></i>
                <h3 class="font-display text-2xl font-black uppercase mb-2">Criativos</h3>
                <p class="text-sm text-gray-400">Framework de retenção, hooks validados e formatos de alta conversão.</p>
            </a>
            <a href="playbook-copy.html" class="playbook-card block text-left rounded-2xl p-6 cursor-pointer" style="text-decoration:none;">
                <i data-lucide="pen-tool" class="w-6 h-6 text-brand-purple mb-4"></i>
                <h3 class="font-display text-2xl font-black uppercase mb-2">Copy</h3>
                <p class="text-sm text-gray-400">Modelos de VSL, e-mails de recuperação e scripts de SDR.</p>
            </a>
            <a href="playbook-socialmedia.html" class="playbook-card block text-left rounded-2xl p-6 cursor-pointer" style="text-decoration:none;">
                <i data-lucide="instagram" class="w-6 h-6 text-brand-purple mb-4"></i>
                <h3 class="font-display text-2xl font-black uppercase mb-2">Social Media</h3>
                <p class="text-sm text-gray-400">Linha editorial, reciclagem de conteúdo e engajamento via stories.</p>
            </a>
            <a href="playbook-landingpage.html" class="playbook-card block text-left rounded-2xl p-6 cursor-pointer" style="text-decoration:none;">
                <i data-lucide="layout" class="w-6 h-6 text-brand-purple mb-4"></i>
                <h3 class="font-display text-2xl font-black uppercase mb-2">Landing Pages</h3>
                <p class="text-sm text-gray-400">Estrutura Above the Fold, provas sociais e otimização de velocidade.</p>
            </a>
        </div>"""
    import re
    content = re.sub(r'<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">.*?</div>\n    </div>', new_grid + '\n    </div>', content, flags=re.DOTALL)
    open(p_html, "w", encoding="utf-8").write(content)

def rewrite_db():
    p_html = os.path.join(dir_path, "banco-de-dados.html")
    content = open(p_html, "r", encoding="utf-8").read()
    new_grid = """<div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <a href="db-objecoes.html" class="db-card block text-left rounded-2xl p-6 cursor-pointer" style="text-decoration:none;">
                <i data-lucide="message-square" class="w-6 h-6 text-brand-blue mb-4"></i>
                <h3 class="font-display text-2xl font-black uppercase mb-4">Objeções & Respostas</h3>
                <p class="text-sm text-gray-400">Mapeamento das 20 principais objeções dos leads e como contorná-las.</p>
            </a>
            <a href="db-calls.html" class="db-card block text-left rounded-2xl p-6 cursor-pointer" style="text-decoration:none;">
                <i data-lucide="headphones" class="w-6 h-6 text-brand-blue mb-4"></i>
                <h3 class="font-display text-2xl font-black uppercase mb-4">Transcrições de Closer</h3>
                <p class="text-sm text-gray-400">Calls reais de fechamento bem-sucedidas. Estude o padrão.</p>
            </a>
            <a href="db-prompts.html" class="db-card block text-left rounded-2xl p-6 cursor-pointer" style="text-decoration:none;">
                <i data-lucide="terminal" class="w-6 h-6 text-brand-blue mb-4"></i>
                <h3 class="font-display text-2xl font-black uppercase mb-4">Prompts IA</h3>
                <p class="text-sm text-gray-400">Nossa biblioteca de prompts para revisar copy e gerar variações.</p>
            </a>
        </div>"""
    import re
    content = re.sub(r'<div class="grid grid-cols-1 md:grid-cols-3 gap-6">.*?</div>\n    </div>', new_grid + '\n    </div>', content, flags=re.DOTALL)
    open(p_html, "w", encoding="utf-8").write(content)

def rewrite_trainings():
    p_html = os.path.join(dir_path, "treinamentos.html")
    content = open(p_html, "r", encoding="utf-8").read()
    new_grid = """<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <a href="treinamento-clickup.html" class="train-card block text-left rounded-2xl p-6 cursor-pointer flex gap-4" style="text-decoration:none;">
                <div class="bg-gray-800 p-3 rounded-lg self-start"><i data-lucide="play-circle" class="w-6 h-6 text-brand-emerald"></i></div>
                <div>
                    <h3 class="font-display text-2xl font-black uppercase mb-2">Como usar o ClickUp</h3>
                    <p class="text-sm text-gray-400">Aula completa de 30 min sobre como gerimos tarefas, sprints e documentamos processos.</p>
                </div>
            </a>
            <a href="treinamento-criativos.html" class="train-card block text-left rounded-2xl p-6 cursor-pointer flex gap-4" style="text-decoration:none;">
                <div class="bg-gray-800 p-3 rounded-lg self-start"><i data-lucide="play-circle" class="w-6 h-6 text-brand-emerald"></i></div>
                <div>
                    <h3 class="font-display text-2xl font-black uppercase mb-2">Criação Sub-criativos</h3>
                    <p class="text-sm text-gray-400">Como desdobrar variação R1, R2 e P2 de um mesmo criativo campeão de Tráfego.</p>
                </div>
            </a>
        </div>"""
    import re
    content = re.sub(r'<div class="grid grid-cols-1 md:grid-cols-2 gap-6">.*?</div>\n    </div>', new_grid + '\n    </div>', content, flags=re.DOTALL)
    open(p_html, "w", encoding="utf-8").write(content)

def rewrite_index():
    p_html = os.path.join(dir_path, "index.html")
    content = open(p_html, "r", encoding="utf-8").read()
    content = content.replace('<a href="#" class="module-card group">', '<a href="galeria.html" class="module-card group">')
    open(p_html, "w", encoding="utf-8").write(content)

rewrite_playbooks()
rewrite_db()
rewrite_trainings()
rewrite_index()

print("Links updated successfully!")
