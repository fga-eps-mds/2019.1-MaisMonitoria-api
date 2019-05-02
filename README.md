
<p align= "center"><img src="https://imgur.com/6foNNzk.png"></p>

<p align= "center">
<a><img src="https://travis-ci.org/fga-eps-mds/2019.1-MaisMonitoria-api.svg?branch=develop"></a>
<a><img src="https://codecov.io/gh/fga-eps-mds/2019.1-MaisMonitoria-api/branch/develop/graph/badge.svg"></a>
<a><img src="https://img.shields.io/badge/license-GLP--3.0-red.svg"></a>
</p>

<h1 align="center"> +Monitoria </h1>
<p align="center"> Uma aplicação para integrar alunos que desejam aprender, e os que desejam ensinar.</p>

<p align="center">
  <a href="https://fga-eps-mds.github.io/2019.1-MaisMonitoria/">Acesse o site de apresentação do +Monitoria</a>
</p>

## Contexto
Nesse repositório está localizado o código do nosso API Gateway. Responsável por gerenciar as requisições dos outros microsserviços e ser um ponto de acesso unico para o nosso frontend.

## Requisitos
Requisitos para conseguir rodar o projeto.
 - Docker
 - Docker-compose
## Desenvolvimento
1. Dê um fork do projeto
2. No [repositório de docs](https://github.com/fga-eps-mds/2019.1-MaisMonitoria) crie uma issue de acordo com  [plano de gestão e configuração](https://fga-eps-mds.github.io/2019.1-MaisMonitoria/docs/plano-gcs) 
3. Para iniciar o desenvolvimento clone o repositório.
4. Faça a build do projeto 
> sudo make build
5. Dê o run no projeto
> sudo make run
6. Acesse http://localhost:8000

### Comandos Makefile

1. Para rodar em background
> sudo make run-d
2. Para rodar os testes
> sudo make tests
3. Para entrar no container
> sudo make enter
4. Para derrubar o container
> sudo make down
5. Para parar o container
> sudo make stop
6. Para iniciar o container
> sudo make start

## Outros repositorios
* [+Monitoria DOCS](https://github.com/fga-eps-mds/2019.1-MaisMonitoria)
* [+Monitoria API Monitorias](https://github.com/fga-eps-mds/2019.1-MaisMonitoria-ApiMonitorias)
* [+Monitoria Front-End](https://github.com/fga-eps-mds/2019.1-MaisMonitoria-FrontEnd)

