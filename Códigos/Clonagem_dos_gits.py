import git
import os
from pathlib import Path

class GitClone():
    def __init__(self, links: list[str] = []) -> None:
        self.links = [link.replace('\n', '') for link in links if link]
        self.base_dir = Path(__file__).parent.absolute().joinpath("gits_clonados/")
    
    def clone(self):
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir, exist_ok=True)

        for link in self.links:
            nome_pasta = link.split('/')[-1]
            dir_clone = self.base_dir.joinpath(nome_pasta)
            if os.path.exists(dir_clone):
                print(f'O repositório {link} já existe')
                continue
            print(f'Clonando {link} para a pasta {dir_clone}\n')
            git.Repo.clone_from(link, dir_clone)

if __name__ == "__main__":
    with open('links.txt', 'r') as txt:
        links = txt.readlines()
    
    try:
        gitclone = GitClone(links)
        gitclone.clone()
    except:
        pass
