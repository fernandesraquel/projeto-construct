# Documento de Visão

## Descrição do Projeto
**CONSTRUCT** é um sistema de gestão para lojas de materiais de construção que visa o bom atendimento ao cliente, a gestão do estoque e o controle dos pedidos, fornecedores e finanças, além da emissão de notas fiscais e relatórios gerenciais.

## Histórico de Revisões 

| Data       | Versão  | Descrição                                   | Autor(es)                |
| ---------- | ------- | ------------------------------------------- | ------------------------ |
| 08/04/2021 | 1.0.0   | Documento Inicial                           | Raquel Lima Fernandes    |
| 03/05/2021 | 1.1.0   | Inclusão de atores e atualização dos RF     | Raquel Lima Fernandes    |

## Equipe e Definição de Papéis

| Membro       | Papel                                      | E-mail                       | GitHub                                           |
| ------------ | ------------------------------------------ | ---------------------------- | ------------------------------------------------ |
| Annielly     | Gerente, Analista, Testador, Desenvolvedor | anniefs2021@gmail.com        |[Link](https://github.com/Anniellyfs)      |
| José Cláudio | Gerente, Analista, Testador, Desenvolvedor | zeclaudio_jr@yahoo.com.br    |[Link](https://github.com/ZeClaudio-Jr)    |
| Maicon       | Gerente, Analista, Testador, Desenvolvedor | marc.douglas630@gmail.com    |[Link](https://github.com/wanessabezerra)  |
| Raquel       | Gerente, Analista, Testador, Desenvolvedor | fernandeslimaraquel@gmail.com|[Link](https://github.com/fernandesraquel) |
| Renata       | Gerente, Analista, Testador, Desenvolvedor | renata.k.a@hotmail.com       |[Link](https://github.com/renatak12)       |



## Matriz de Competências

| Membro       | Competências                                                                                                      |
| ------------ | ----------------------------------------------------------------------------------------------------------------- |
| Annielly     | Desenvolvedora JavaScript, Python                                                                                 |
| José Cláudio | Desenvolvedor Javascript, Python                                                                                  |
| Maicon       | Desenvolvedor Python, Django, JavaScript                                                                          |
| Raquel       | Desenvolvedora Javascript, React, Nexjtjs, Python, C, PostgreSQL                                                  |  
| Renata       | Desenvolvedora Javascript, Python, Django                                                                         |

## Perfis dos Usuários

O sistema poderá ser utilizado por usuários. Temos os seguintes perfis/atores:

| Perfil        | Descrição                                                                                                                                                      |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gerente       | Este usuário precisará de acesso a todas as funcionalidades da aplicação, incluindo gestão de estoque, controle de vendas, gerenciamento de fornecedores e usuários, e relatórios gerenciais.                                  |
| Vendedor   | Este usuário precisará usar a aplicação para realizar suas atividades diárias. Ele precisará de acesso a funcionalidades como registro de vendas, gestão de estoque, preços e promoções. |
| Fornecedor  | Este usuário não terá acesso a nenhuma das funcionalidades da aplicação. |
| Cliente  | Este usuário não terá acesso a nenhuma das funcionalidades da aplicação. |

## Lista de Requisitos Funcionais

| Requisito                                      | Descrição                                                                   | Ator(es)     |
| ---------------------------------------------- | ---------------------------------------------------------------- | -------- |
| RF001 - Efetuar Login    | funcionalidade realizada por todos os usuários, para obter acesso ao sistema. | Gerente, Vendedor |
| RF002 - Recuperar senha  | funcionalidade realizada pelos usuários, ao perder a senha, tem a possibilidade de recupará-la pelo e-mail cadastrado. | Gerente, Vendedor |
| RF003 - Controlar Permissões | Esta funcionalidade permite definir níveis de acesso para diferentes usuários, com base em funções e responsabilidades. | Gerente |
| RF004 - Manter Vendedor  | Esta funconalidade permite cadastrar, editar, excluir e visualisar usuários tipo 'vendedor'. | Gerente |
| RF005 - Manter Fornecedor | Esta funconalidade permite cadastrar, editar, excluir e visualisar os fornecedores da loja. | Gerente |
| RF006 - Manter Cliente | Esta funconalidade permite cadastrar, editar, excluir e visualisar os clientes da loja. | Gerente, Vendedor |
| RF007 - Manter Produto | Esta funconalidade permite cadastrar, editar, excluir e visualisar produtos do estoque. | Gerente, Vendedor |
| RF008 - Vender Produto | Esta funcionalidade efetua a exclusão do produto vendido do estoque. | Gerente, Vendedor |
| RF009 - Gerar Nota     | Esta funcionalidade permite após a venda de produtos é gerado uma nota fiscal eletrônica. | Gerente, Vendedor |
| RF010 - Emitir Relatórios | Esta funcionalidade permite gerar relatórios personalizados de vendas, estoque e desenpenho financeiro. | Gerente |


## Lista de Requisitos Não-Funcionais

| Requisito                                    | Descrição                                                                                    |
| -------------------------------------------- | -------------------------------------------------------------------------------------------- |
| RNF001  |**Usabilidade**: a aplicação deve ser fácil de usar e intuitiva, com design responsivo e acessibilidade.                                       |
| RNF002  | **Performance**: a aplicação deve ser capaz de lidar com grande volume de dados e usuários simultâneos, com tempos de resposta rápidos e sem tempo de inatividade. |
| RNF003 | **Segurança**: a aplicação deve ter medidas de segurança adequadas, como criptografia, autenticação de usuário e controle de acesso baseado em função. |
| RNF004 | **Manutenção**: a aplicação deve ser fácil de manter e atualizar, com documentação clara e suporte técnico disponível. |
| RN005  | **Escalabilidade**: a aplicação deve ser escalável para acomodar o crescimento do negócio, sem necessidade de reformulação ou retrabalho. |

## Riscos

Tabela com o mapeamento dos riscos do projeto, as possíveis soluções e os responsáveis.

| Data       | Risco                                                                  | Prioridade | Responsável | Status  | Providência/Solução                                            |
| ---------- | ---------------------------------------------------------------------- | ---------- | ----------- | ------- | -------------------------------------------------------------- |
| 08/04/2023 | Não aprendizado das ferramentas utilizadas pelos componentes da equipe | Alta       | Gerente     | Vigente | Reforçar estudos sobre as ferramentas.                         |
| 08/04/2023 | Ausência por qualquer membro da equipe                                 | Média      | Gerente     | Vigente | Planejar o cronograma tendo em base a agenda dos membros.      |
| 08/04/2023 | Divisão de tarefas mal sucedida                                        | Baixa      | Gerente     | Vigente | Acompanhar de perto o desenvolvimento de cada membro da equipe |

## Modelo Conceitual 