<?php 
require 'Mysql_config.php';

$lista = [];
$sql = $pdo->query("SELECT * FROM clientes");
if($sql->rowCount() > 0) {
    $lista = $sql->fetchAll(PDO::FETCH_ASSOC);
}

include 'head.php';
?>
<body>
    <a href="create.php">
        ADICIONAR USÚARIO
        <i class="fa-solid fa-circle-plus"></i>  
    </a>
    <table border="1" width="100%">
        <th>ID</th>
        <th>NOME</th>
        <th>TELEFONE</th>
        <th>EMAIL</th>
        <th>DATA DE CADASTRO</th>
        <th>AÇÕES</th>
        <?php foreach($lista as $users): ?>
            <tr>
                <td><?= $users['idCliente'] ?></td>
                <td><?= $users['nomeCompleto'] ?></td>
                <td><?= $users['telefone'] ?></td>
                <td><?= $users['email'] ?></td>
                <td><?= $users['dataCadastro'] ?></td>
                <td align="center">
                    <a href="editar.php?id=<?=$users['idCliente']?>">
                        <i class="fa-solid fa-pen-to-square"></i>
                    </a>
                    <a href="deletar.php?id=<?=$users['idCliente']?>" onclick="return confirm('Tem certeza que deseja excluir o usúario <?=$users['nomeCompleto']?>?')">
                        <i class="fa-solid fa-trash"></i>
                    </a>
            
                </td>
            </tr>
        <?php endforeach;?>
    </table>    
</body>
</html>
