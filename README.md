## MySQL CSV

Este repositório tem como objetivo demonstrar o processo de extração de dados de um banco de dados MariaDB utilizando a IDE HeidiSQL para análise das queries, juntamente com Python para realizar a extração e a transformação prévia, além do ajuste do Excel para a transformação completa dos dados, finalizando com a importação no PowerBI para a análise de dados.

### MariaDB

MariaDB é um gerenciador de dados open source que visa gerir dados de forma rápida e fácil para o armazenamento de dados relacionais. Desenvolvido pelos criadores do MySQL, ambas as ferramentas possuem plataformas de trabalho idênticas.

### HeidiSQL

HeidiSQL é um IDE de gerenciamento de banco de dados, um dos principais no mercado, que possui uma grande variedade de bibliotecas de bancos que podem ser conectados e gerenciados.

### SQL e extração

1. Realizar a conexão com o banco utilizando o HeidiSQL
  
https://github.com/CarlosJuncher03/MySQL-CSV/assets/145303814/18333ea9-8d3b-406e-9d48-31738c5b3b0e
   
4. Após isso, escolher o banco de dados e realizar análise e consulta

https://github.com/CarlosJuncher03/MySQL-CSV/assets/145303814/7ab7c6d8-c00a-4534-8818-5fa5cc5fe539

#### Querys usadas:

```sql
SELECT v.Codigo, v.`Data`, v.Hora, v.FormaParcelamento, v.TotalPedido
FROM vendas v
WHERE v.Status = "f" AND v.Cancelada IS NULL AND v.Tipo = "vp";

SELECT vp.CodigoVenda, vp.CodigoProduto, vp.Descricao, vp.Quantidade, vp.ValorUnitario, vp.ValorTotal
FROM vendasprodutos vp
INNER JOIN vendas v ON v.Codigo = vp.CodigoVenda
WHERE vp.Cancelada IS NULL AND v.`Status` = "f" AND v.Tipo = "vp";
```
# Extração dos arquivos CSV usando Python

Após realizar as consultas SQL no banco de dados, os dados são extraídos e armazenados em arquivos CSV utilizando Python.

Para visualizar um exemplo de como realizar essa extração, assista ao vídeo

https://github.com/CarlosJuncher03/MySQL-CSV/assets/145303814/9219b956-1130-42de-a733-4d8f86b5c705

# Importação dos dados para o Excel e transformações finais

Após a extração dos dados em arquivos CSV, é possível importá-los para o Excel e realizar as transformações necessárias para análise.

Assista a um exemplo de importação dos dados e realização de transformações finais no Excel

https://github.com/CarlosJuncher03/MySQL-CSV/assets/145303814/1b5b0f80-4be4-47e8-abfd-cc44657d358f

# Análise dos dados em Dashboards usando PowerBI

Por fim, os dados transformados podem ser analisados e visualizados em Dashboards utilizando o PowerBI.

Assista ao processo de análise dos dados em Dashboards no PowerBI 

https://github.com/CarlosJuncher03/MySQL-CSV/assets/145303814/349f9ae8-9a8b-4a17-b8b8-e33f472c13be

# Conclusão

Este repositório apresentou um processo completo de extração e análise de dados de um banco de dados MariaDB. Utilizando a IDE HeidiSQL para análise das queries SQL, Python para extração dos dados em arquivos CSV, Excel para transformações finais e o PowerBI para análise e visualização dos dados em Dashboards.

Ao seguir os passos descritos neste README, você poderá entender como extrair dados de um banco de dados relacional, transformá-los e analisá-los de maneira eficiente. Além disso, os vídeos fornecidos demonstram cada etapa do processo, tornando mais fácil a compreensão e aplicação do mesmo em seus projetos.

Sinta-se à vontade para explorar o conteúdo deste repositório e adaptar o processo às suas necessidades específicas. Qualquer dúvida ou sugestão, não hesite em entrar em contato.

Obrigado por visitar este repositório!

