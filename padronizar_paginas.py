import os
import re

# Lendo o index.html para extrair o novo estilo da Home
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extrair a tag <style> completa da Home
style_match = re.search(r'<style>(.*?)</style>', index_content, re.DOTALL)
if style_match:
    new_style = style_match.group(1)
else:
    print("Nenhum slice de estilo encontrado")
    exit(1)

# Extrair as faíscas dinâmicas (se quiser manter nas internas, senao só a classe .spark do css)
# Vamos extrair a nova <nav>
nav_match = re.search(r'<nav\b[^>]*>.*?</nav>', index_content, re.DOTALL)
if nav_match:
    new_nav = nav_match.group(0)
    # Adaptar os links se necessário, ou usar direto
else:
    print("Nova Navbar não encontrada")
    exit(1)

# Páginas a serem padronizadas
pages = ['playbooks.html', 'banco-de-dados.html', 'treinamentos.html']

for page in pages:
    if os.path.exists(page):
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Substitui todo o bloco <style> pelo da Home
        content = re.sub(r'<style>.*?</style>', f'<style>{new_style}</style>', content, flags=re.DOTALL)
        
        # Adicionar o padding mt-32 no main igual a home
        content = re.sub(r'<main([^>]*)>', r'<main\1 class="w-full max-w-5xl mx-auto space-y-12 relative z-10 flex-grow mt-32 px-4 md:px-0">', content)
        # Limpar o class="w-full max-w-5xl..." duplicado caso exista
        content = re.sub(r'class="w-full max-w-6xl mx-auto space-y-12 relative z-10 flex-grow" class="w-full max-w-5xl.*?"', r'class="w-full max-w-5xl mx-auto space-y-12 relative z-10 flex-grow mt-32 px-4 md:px-0"', content)

        # Atualizar a Navbar / Header:
        # Nas subpaginas, geralmente tem um <header class="mb-12...">
        # Vamos inserir o <nav> logo apos a div fixed inset-0 (background)
        # Primeiro, remover o 'header' atual e o botão Voltar, e colocar a Navbar
        
        # Como o header e voltar variam, mais seguro injetar a navbar logo após a abertura do <body> e remover o antigo
        
        if '<nav>' not in content:
            content = re.sub(r'(<body[^>]*>.*?)(<div[ \n\t]+class="fixed inset-0[^>]*>.*?</div>)', r'\1\2\n' + new_nav.replace('\\', '\\\\'), content, flags=re.DOTALL, count=1)
        
        # Atualizar o visual do background div
        bg_new = '''<div class="fixed inset-0 z-[-1] overflow-hidden pointer-events-none">

        <!-- Malha de pontos sutil (opcional, mantido para textura) -->
        <div class="absolute inset-0 opacity-[0.015]"
            style="background-image: radial-gradient(#fff 1px, transparent 1px); background-size: 32px 32px;"></div>

        <!-- Glow Central focado atrás do logo/texto principal -->
        <div
            class="absolute top-1/4 right-[20%] w-[800px] h-[800px] bg-[#FFC600]/5 rounded-full blur-[150px] animate-pulse">
        </div>
    </div>'''
        content = re.sub(r'<div class="fixed inset-0 z-\[-1\] overflow-hidden pointer-events-none">.*?</div>', bg_new, content, flags=re.DOTALL)
        
        # Padronizar o glass-panel das subpáginas
        content = re.sub(r'\.class-das-subpaginas', r'', content) # (Se precisar aplicar em cards específicos)
        content = content.replace('border-t-2 border-t-brand-purple', 'border border-white/5 border-l-4 border-l-[#FFC600]')
        content = content.replace('border-t-2 border-t-brand-blue', 'border border-white/5 border-l-4 border-l-[#FFC600]')
        content = content.replace('border-t-2 border-t-brand-emerald', 'border border-white/5 border-l-4 border-l-[#FFC600]')
        content = content.replace('glass-panel', 'bg-[#0D0D0D] border border-white/5 rounded-2xl')

        
        with open(page, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Atualizado {page}")

print("Pronto. Faltam refinamentos nos cards se ficarem muito quebrados.")
