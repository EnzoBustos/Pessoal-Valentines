# Pessoal-Valentines

Landing page romantica desenvolvida em Next.js/React para compartilhar mensagens especiais de Valentine's Day. O foco e oferecer uma experiencia leve, responsiva e cheia de animacoes para encantar quem receber o link.

## Visao geral
Este repositorio concentra todo o front-end da aplicacao, com rotas criadas pelo App Router do Next.js, componentes reutilizaveis e estilos controlados via Tailwind CSS. O conjunto de efeitos com Framer Motion e `@fireworks-js/react` adiciona o clima festivo do Dia dos Namorados.

## Funcionalidades
- Hero animado com transicoes suaves e chamadas afetuosas.
- Efeitos de fogos de artificio responsivos ao scroll e a interacoes.
- Layout 100% responsivo seguindo abordagem mobile-first.
- Componentes isolados para textos, botoes e secoes tematicas.

## Tecnologias
- [Next.js 16](https://nextjs.org/) com App Router e Turbopack.
- [React 19](https://react.dev/) e [TypeScript](https://www.typescriptlang.org/).
- [Tailwind CSS 3](https://tailwindcss.com/) para estilizar com utilitarios.
- [Framer Motion 12](https://www.framer.com/motion/) para animacoes.
- [`@fireworks-js/react`](https://fireworks.js.org/) para particulas e fireworks.
- ESLint com configuracoes oficiais do Next para manter padroes consistentes.

## Como rodar localmente
Requisitos: Node.js 20+ e npm (ou pnpm/yarn equivalente).

```bash
git clone https://github.com/EnzoBustos/Pessoal-Valentines.git
cd Pessoal-Valentines
npm install
npm run dev
```

A pagina ficara disponivel em `http://localhost:3000` com recarregamento instantaneo.

## Scripts npm
- `npm run dev` — inicia o servidor Next com Turbopack.
- `npm run build` — gera a versao otima para producao.
- `npm run start` — sobe o build produzido em modo producao.
- `npm run lint` — executa o ESLint com a configuracao do Next.

## Estrutura do projeto
```
src/
  app/          # rotas, layouts e entrypoints
  components/   # componentes reutilizaveis
public/         # assets estaticos (imagens, favicon etc.)
```

## Deploy e personalizacao
- Deploy recomendado na [Vercel](https://vercel.com/) para aproveitar a integracao nativa com Next.js.
- Ajuste textos, imagens e cores diretamente nos componentes em `src/components`.
- Crie novas secoes romanticas adicionando rotas ou layouts na pasta `src/app`.

Contribuicoes e sugestoes sao bem-vindas! Abra um issue ou envie um pull request com ideias para deixar a experiencia ainda mais memoravel.
