import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

nav_match = re.search(r'<nav\b[^>]*>.*?</nav>', index_content, re.DOTALL)
new_nav = nav_match.group(0) if nav_match else ""

style_match = re.search(r'<style>(.*?)</style>', index_content, re.DOTALL)
new_style = style_match.group(0) if style_match else ""

bg_sparks = '''    <!-- Efeitos de Fundo: Profundidade e Faíscas -->
    <div class="fixed inset-0 z-[-1] overflow-hidden pointer-events-none">
        <!-- Malha de pontos -->
        <div class="absolute inset-0 opacity-[0.015]"
            style="background-image: radial-gradient(#fff 1px, transparent 1px); background-size: 32px 32px;"></div>
        <!-- Glow Central -->
        <div class="absolute top-1/4 right-[20%] w-[800px] h-[800px] bg-[#FFC600]/5 rounded-full blur-[150px] animate-pulse">
        </div>
        <!-- Faíscas -->
        <div class="spark" style="background: #FFC600; box-shadow: 0 0 10px 2px rgba(255, 198, 0, 0.8); left: 60%; top: 60%; animation: spark-fly 4s linear infinite; animation-delay: 0s;"></div>
        <div class="spark" style="background: #FFC600; box-shadow: 0 0 10px 2px rgba(255, 198, 0, 0.8); left: 65%; top: 75%; animation: spark-fly 5s linear infinite; animation-delay: 1.2s; width: 6px; height: 6px;"></div>
        <div class="spark" style="background: #FFC600; box-shadow: 0 0 10px 2px rgba(255, 198, 0, 0.8); left: 55%; top: 50%; animation: spark-fly 3.5s linear infinite; animation-delay: 0.5s;"></div>
        <div class="spark" style="background: #FFC600; box-shadow: 0 0 10px 2px rgba(255, 198, 0, 0.8); left: 80%; top: 80%; animation: spark-fly 6s linear infinite; animation-delay: 2.1s;"></div>
    </div>'''

pages = ['playbooks.html', 'banco-de-dados.html', 'treinamentos.html']

for page in pages:
    if not os.path.exists(page): continue
    with open(page, 'r+', encoding='utf-8') as f:
        content = f.read()
        
        # 1. Troca o Style
        content = re.sub(r'<style>.*?</style>', new_style, content, flags=re.DOTALL)
        
        # 2. Insere a Navbar após a tag body se não existir
        if '<nav\n' not in content and '<nav class' not in content:
            content = re.sub(r'(<body[^>]*>)', r'\1\n' + new_nav + '\n', content, count=1)
            
        # 3. Substitui o fundo antigo pelo novo com sparks
        content = re.sub(r'<div class="fixed inset-0 z-\[-1\].*?</div>', bg_sparks, content, flags=re.DOTALL)
        
        # 4. Ajustes nos Cards (remover o glass-panel antigo e usar a cara flat)
        content = re.sub(r'bg-gradient-to-br from-gray-900 to-black', 'bg-[#0D0D0D]', content)
        content = re.sub(r'border-gray-800', 'border-white/5', content)
        
        # As páginas internas tinham <main class="... max-w-6xl mx-auto space-y-12">
        # Precisamos de um mt-32 para não ficar embaixo da navbar fixa
        content = re.sub(r'<main([^>]*)>', r'<main\1 style="margin-top: 8rem;">', content)
        
        # Transforma os cards antigos
        # playbooks tem playbook-card
        content = content.replace('.playbook-card', '.module-card')
        content = content.replace('playbook-card', 'bg-[#0D0D0D] border border-white/5 border-l-4 border-l-[#FFC600] rounded-2xl p-6 relative transition-all hover:-translate-y-1 hover:shadow-2xl')
        
        # banco de dados tem db-card
        content = content.replace('.db-card', '.module-card')
        content = content.replace('db-card', 'bg-[#0D0D0D] border border-white/5 border-l-4 border-l-[#FFC600] rounded-2xl p-6 relative transition-all hover:-translate-y-1 hover:shadow-2xl')
        
        # treinamentos tem train-card
        content = content.replace('.train-card', '.module-card')
        content = content.replace('train-card', 'bg-[#0D0D0D] border border-white/5 border-l-4 border-l-[#FFC600] rounded-2xl p-6 relative transition-all hover:-translate-y-1 hover:shadow-2xl')

        f.seek(0)
        f.write(content)
        f.truncate()
        print(f"Atualizado {page}")

