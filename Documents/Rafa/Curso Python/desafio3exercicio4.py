#4. Crie um dicionário representando contatos (nome, telefone). Permita ao usuário procurar por um contato pelo nome.

#criando o dicionário

personagens = {
'Julio': '9898-3232',
'Alipio': '7865-9832',
'Lilica': '9863-9832',
'Lola': '8983-9832',
'Zaza': '8983-9829',
'Caco': '8983-9029',
'Mimosa': '3298-3213',
'Oriba': '1312-3234'
}

#procurando um contato pelo nome

print("Lista de Contatos Fazenda Cocoricó!")

nome = input('Digite o nome do personagem do cocoricó: ').strip()
    
print(personagens.get(nome, "contato não encontrado"))



