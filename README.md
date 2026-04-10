# Ecocondução — Análise Exploratória de Dados
 
Análise exploratória de um dataset com 30.000 registros de comportamentos de condução, com foco na identificação de padrões que influenciam a eficiência energética de veículos.

Acesse o relatório completo em: https://drive.google.com/file/d/1l6mS914LKtM93lGlHOHi2bXzy1G9T9S2/view?usp=sharing
 
---
 
## Visão geral
 
O projeto investiga como diferentes hábitos ao volante — variação de rotação do motor, frenagens bruscas, tempo em marcha lenta, suavidade das acelerações e consumo de combustível — se correlacionam com uma pontuação de ecocondução (eco_score). A partir dessas correlações, os motoristas são segmentados em categorias e comparados entre si.
 
---
 
## Estrutura do dataset
 
| Coluna | Descrição |
|--------|-----------|
| `rpm_variation` | Grau de variação da rotação do motor |
| `harsh_braking_count` | Número de eventos de frenagem brusca |
| `idling_time` | Tempo total em marcha lenta |
| `fuel_consumption` | Consumo de combustível no período |
| `acceleration_smoothness` | Suavidade nas acelerações |
| `eco_score` | Pontuação de eficiência (0–100) |
 
---
 
## Principais resultados
 
- O hábito mais prejudicial à ecocondução é a **frenagem brusca** (correlação de −0,74 com o eco_score).
- A **suavidade nas acelerações** é o fator mais positivo (correlação de +0,48).
- Motoristas classificados como **Bom** consomem, em média, **33,6% menos combustível** do que os classificados como **Ruim**.
 
| Categoria | Eco Score | Consumo médio (L) |
|-----------|-----------|-------------------|
| Bom | 70–100 | 6,18 |
| Mediano | 40–70 | 7,67 |
| Ruim | 0–40 | 9,31 |
 
---
 
## Tecnologias utilizadas
 
- **Linguagem:** Python 3
- **Ambiente:** Jupyter Notebook
- **Visualização:** Matplotlib, Seaborn
- **Manipulação de dados:** Pandas
- **Dashboard interativo:** Streamlit
- **Versionamento:** Git
 
---

## Licença
 
Distribuído sob a licença MIT.
