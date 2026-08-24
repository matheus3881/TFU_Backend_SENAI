# Modulo do Treinador - API Pokedex

Este repositorio contem somente o modulo de treinador da API da Pokedex.
O modulo foi desenvolvido para trabalhar com capturas, favoritos,
comparacao e Pokédex pessoal de treinadores.

Este projeto nao e uma API de e-commerce.

## Escopo do modulo

As pastas sob responsabilidade deste modulo sao:

```text
models/treinador/
schemas/treinador/
services/treinador/
routers/treinador/
tests/treinador/
```

## O que ja foi feito

### Captura

- Model `Captura` criado com os campos da captura e Foreign Keys externas.
- Schema `CriarCaptura` com validacao de ID, local e nivel.
- Schema `CapturaResposta` para representar capturas retornadas pela API.
- `CapturaService` organizado no arquivo correto.
- Validacao independente de captura implementada.
- Testes de validacao de captura criados.
- Router com estrutura de endpoints preparada para integracao.

### Favoritos

- Model de favoritos existente em `models/treinador/favoritos.py`.
- `CriarFavorito` valida que `captura_id` seja maior que zero.
- `FavoritoResposta` define o formato da resposta.
- `FavoritoService` possui validacao independente do ID da captura.
- Router possui POST, GET e DELETE preparados.
- Testes de validacao do schema criados.

As operacoes de banco e autenticacao dos favoritos ainda nao foram
implementadas.

### Comparacao

- `CompararPokemon` recebe uma lista de IDs.
- O Schema exige entre 2 e 4 IDs positivos.
- `ComparacaoService` valida a quantidade de IDs.
- Testes cobrem quantidades validas e invalidas.
- Testes do Schema cobrem limites, IDs invalidos, tipos invalidos e IDs
   duplicados.

Atualmente a comparacao valida somente os dados de entrada. Ainda nao compara
atributos reais dos Pokemons.

### Pokedex

- `EntradaPokedex` define os dados de um Pokemon capturado.
- `PokedexResposta` define a resposta completa da Pokedex.
- Foram adicionadas validacoes independentes para IDs, nivel, totais e textos.
- `PokedexService.calcular_total_capturado()` conta os itens recebidos.
- `PokedexService.calcular_total_shiny()` conta objetos com `is_shiny=True`.
- Testes unitarios cobrem os dois metodos e os schemas.

O service recebe objetos com o atributo `is_shiny`, mas esse atributo sera
fornecido pela integracao com os Models de Pokemon.

## O que ainda falta no modulo do treinador

- Integrar os routers de captura ao usuario autenticado.
- Escolher uma unica implementacao entre os routers duplicados de captura.
- Remover os `NotImplementedError` quando banco e autenticacao estiverem
   disponiveis.
- Implementar criacao, listagem e remocao de favoritos.
- Verificar se a captura existe e pertence ao treinador.
- Definir a regra para favoritos duplicados.
- Definir quais atributos serao usados na comparacao de Pokemons.
- Criar o router da comparacao depois que o contrato da resposta for definido.
- Criar o router da Pokedex depois que a consulta de dados for definida.
- Integrar os dados de captura e Pokemon na resposta da Pokedex.
- Ampliar os testes de routers e de integracao.

## Dependencias da outra parte da equipe

Estas partes nao pertencem ao escopo deste modulo e devem ser implementadas
pelos responsaveis correspondentes:

- `database.py` deve fornecer `Base` e `SessionLocal`.
- O Model de Usuario deve fornecer a tabela `usuarios` e seu identificador.
- O Model de Pokemon deve fornecer a tabela `pokemon`, seus dados e a origem
   de `is_shiny`.
- A autenticacao deve fornecer o usuario/treinador atualmente logado.
- `main.py` deve criar a aplicacao FastAPI e registrar os routers.
- A equipe deve carregar os Models externos antes da criacao das tabelas.
- A equipe deve confirmar os nomes finais das tabelas e Foreign Keys.

Nenhuma dessas dependencias deve ser criada ou alterada dentro deste modulo.

## Rotas preparadas

```text
POST   /treinador/capturas
GET    /treinador/capturas
POST   /treinador/favoritos
GET    /treinador/favoritos
DELETE /treinador/favoritos/{favorito_id}
```

As rotas de captura e favoritos ainda aguardam integracao com banco e
autenticacao. Nao existe router de comparacao ou Pokedex neste momento.

## Testes

Os testes unitarios independentes nao dependem de banco, autenticacao ou
Models externos.

```text
tests/treinador/test_captura.py
tests/treinador/test_favorito.py
tests/treinador/test_comparacao.py
tests/treinador/test_pokedex.py
```

Foi feita validacao direta com Python. A execucao automatica pelo pytest ainda
depende da instalacao do pytest no ambiente de desenvolvimento.
