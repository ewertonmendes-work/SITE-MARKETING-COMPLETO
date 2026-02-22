import re
import os

pages = ['playbooks.html', 'banco-de-dados.html', 'treinamentos.html']

bg_clean = '''    <!-- Efeitos de Fundo: Profundidade e Faíscas -->
    <div class="fixed inset-0 z-[-1] overflow-hidden pointer-events-none">
        <!-- Malha de pontos -->
        <div class="absolute inset-0 opacity-[0.015]" style="background-image: radial-gradient(#fff 1px, transparent 1px); background-size: 32px 32px;"></div>
        <!-- Glow Central -->
        <div class="absolute top-1/4 right-[20%] w-[800px] h-[800px] bg-[#FFC600]/5 rounded-full blur-[150px] animate-pulse"></div>
        <!-- Faíscas -->
        <div class="spark" style="background: #FFC600; box-shadow: 0 0 10px 2px rgba(255, 198, 0, 0.8); left: 60%; top: 60%; animation: spark-fly 4s linear infinite; animation-delay: 0s;"></div>
        <div class="spark" style="background: #FFC600; box-shadow: 0 0 10px 2px rgba(255, 198, 0, 0.8); left: 65%; top: 75%; animation: spark-fly 5s linear infinite; animation-delay: 1.2s; width: 6px; height: 6px;"></div>
        <div class="spark" style="background: #FFC600; box-shadow: 0 0 10px 2px rgba(255, 198, 0, 0.8); left: 55%; top: 50%; animation: spark-fly 3.5s linear infinite; animation-delay: 0.5s;"></div>
        <div class="spark" style="background: #FFC600; box-shadow: 0 0 10px 2px rgba(255, 198, 0, 0.8); left: 80%; top: 80%; animation: spark-fly 6s linear infinite; animation-delay: 2.1s;"></div>
    </div>\n\n    '''

for page in pages:
    if os.path.exists(page):
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()

        # Regex to find everything between body tag and nav tag
        pattern = re.compile(r'(<body[^>]*>).*?(<nav\b[^>]*>)', re.DOTALL)
        
        # Replace the messy background block with the clean one
        content = pattern.sub(r'\1\n' + bg_clean + r'\2', content)
        
        with open(page, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {page}")

