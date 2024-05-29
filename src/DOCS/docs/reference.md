# Referência do Conversor de Arquivo OFX

## Funções Principais

### `parse_ofx_to_dict(file)`

Esta função analisa um arquivo OFX e retorna um dicionário contendo os dados extraídos.

#### Parâmetros
- `file`: O arquivo OFX a ser processado.

#### Exemplo de Uso
```python
from transform.utils import parse_ofx_to_dict

# Ler o arquivo OFX
with open('arquivo.ofx', 'r') as file:
    data = parse_ofx_to_dict(file)
