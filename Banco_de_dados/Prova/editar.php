<?php 
require 'Mysql_config.php';
include 'head.php';

$info = [];
        $id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);

        if($id) {
            $sql = $pdo->prepare("SELECT * FROM clientes WHERE idCliente = :id");
            $sql->bindValue('id', $id);
            $sql->execute();

            $info = $sql->fetch(PDO::FETCH_ASSOC);
            

        } else {
            header('Location: index.php');
        }

?>
<body>
    <h1>Editar Usuario <?=$info['nomeCompleto']?></h1>
    <div class="form-container">
        <form action="<?= $_SERVER['PHP_SELF'] ?>" method="post" class="form-group">
            <input type="hidden" name="id" value="<?=$info['idCliente']?>">
        
            <label for="name">Nome: </label>
            <input type="text" name="name" value="<?=$info['nomeCompleto']?>">

            <label for="phone">Telefone: </label>
            <input type="number" name="phone" value="<?=$info['telefone']?>">
            <label for="email">E-mail: </label>
            
            <input type="email" name="email" value="<?=$info['email']?>">
            <input type="submit" value="Alterar">

            <a href="index.php">
                <input type="button" value="Voltar">
            </a>
        </form>
    </div>

    <?php 
if($_SERVER["REQUEST_METHOD"] == "POST") {
    $id = filter_input(INPUT_POST, 'id', FILTER_VALIDATE_INT);
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_SPECIAL_CHARS);
    $phone = filter_input(INPUT_POST, 'phone', FILTER_VALIDATE_INT);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);

        if($name && $email && $phone) {
            $sql = $pdo->prepare("UPDATE clientes SET nomeCompleto = :name, telefone = :phone, email = :email WHERE idCliente = :id");
            $sql->bindValue(':name', $name);
            $sql->bindValue(':phone', $phone);
            $sql->bindValue(':email', $email);
            $sql->bindValue(':id', $id);
            $sql->execute();

            header('Location: index.php');
            exit;

        } else {
            header('Location: editar.php');
            exit;
        }
    } 
?>
</body>
</html>