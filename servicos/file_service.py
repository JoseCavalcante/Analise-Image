from pathlib import Path
import tempfile

def criar_pasta_temporaria() -> Path:
    """
    Cria uma pasta temporária onde os arquivos de imagem 
    podem ser analisados sem poluir o sistema de arquivos principal.
    Retorna o objeto Path apontando para o diretório.
    """
    temp_dir = tempfile.mkdtemp(prefix="analise_img_")
    return Path(temp_dir)

def garantir_pasta_persistente(nome_pasta: str = "upload_img_enviadas") -> Path:
    """
    Garante que uma pasta específica exista no diretório do projeto.
    Por padrão cria/retorna a pasta 'upload_img_enviadas'.
    """
    caminho = Path(nome_pasta)
    caminho.mkdir(parents=True, exist_ok=True)
    return caminho
