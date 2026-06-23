import pandas as pd
import matplotlib.pyplot as plt

# 1. Dados simulados (CRM + Transações)
dados = {
    'Nome': ['Jean Dupont (LuxFunds)', 'Maria Silva (Retalho Privado)', 'Alpha Management'],
    'Segmento': ['Institucional', 'Retalho', 'Institucional'],
    'Ultimo_Contacto_Dias':,
    'Total_Movimentado_Recente': [750000, -100000, 1000000]
}

df = pd.DataFrame(dados)

# 2. Lógica do Pensamento Analítico
def calcular_risco(linha):
    if linha['Ultimo_Contacto_Dias'] > 60 and linha['Total_Movimentado_Recente'] < 0:
        return 'CRITICO: Risco de Churn'
    elif linha['Ultimo_Contacto_Dias'] > 45:
        return 'ATENCAO: Ligar Urgente'
    else:
        return 'SEGURO: Saudavel'

df['Status_Risco'] = df.apply(calcular_risco, axis=1)

# 3. Exibir relatórios no terminal
print("--- TABELA GLOBAL ---")
print(df.to_string())

clientes_criticos = df[df['Status_Risco'] == 'CRITICO: Risco de Churn']
capital_em_risco = clientes_criticos['Total_Movimentado_Recente'].sum()

print("\n--- IMPACTO NO FUNDO ---")
print(f"Total de Capital em Risco de Saída: {abs(capital_em_risco):,} EUR\n")

# 4. Gráfico Visual (Sem emojis para evitar avisos de fonte)
resumo_financeiro = df.groupby('Status_Risco')['Total_Movimentado_Recente'].sum().reset_index()
resumo_financeiro['Total_Movimentado_Recente'] = resumo_financeiro['Total_Movimentado_Recente'].abs()

plt.figure(figsize=(8, 5))
cores = ['red' if 'CRITICO' in x else 'green' for x in resumo_financeiro['Status_Risco']]

plt.bar(resumo_financeiro['Status_Risco'], resumo_financeiro['Total_Movimentado_Recente'], color=cores)
plt.title('Analise de Risco de Capital no Fundo de Investimento', fontsize=14, fontweight='bold')
plt.ylabel('Volume de Capital (EUR)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('analise_risco.png') # Guarda o gráfico como imagem para o GitHub
plt.show()
