<?php

require(__DIR__.'/RPS.php');
if (!empty($_POST)) {
  $rps = new RPS;
  $rps->handle($_POST);
}


?>

<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>RPS</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss/dist/tailwind.min.css" rel="stylesheet">

  </head>
  <body class="h-screen">
  <?php
  if (isset($rps)) { // else show game results ?>
    <div class="flex justify-center text-center items-center h-screen">
      <div class="w-full max-w-lg flex-no-grow">
        <form class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4" >
        <label class="block text-grey-darker text-sm font-bold mb-2" for="result" action="index.php" method="post"> <!-- for="username"-->
        <?=$rps->result;?>
        </label>
        <br>
    <div class="flex justify-center items-center">
      <a href="index.php" class="button bg-blue hover:bg-blue-dark text-white font-bold py-2 px-4 rounded">Play Again</a>
    </div>
      </form>
    </div>
    </div>
  <?php } else {?>
    <div class="flex justify-center items-center h-screen">
      <div class="w-full max-w-lg flex-no-grow">
      <form class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4" action="index.php" method="post">
        <div class="mb-4">
          <label class="block text-grey-darker text-sm font-bold mb-2" for="attack"> <!-- for="username"-->
            Resistance is Futile!! Choose your attack:
            <br>
            <br>
            <input type="radio" name="attack" value="rock"> Rock<br>
            <input type="radio" name="attack" value="paper"> Paper<br>
            <input type="radio" name="attack" value="scissors"> Scissors<br>
            <input type="radio" name="attack" value="lizard"> Lizard<br>
            <input type="radio" name="attack" value="spock"> Spock<br>


          </label>
        </div>

        <div class="flex items-center justify-between">
          <button class="bg-blue hover:bg-blue-dark text-white font-bold py-2 px-4 rounded" type="submit">
            Play!
          </button>

        </div>
      </form>
    </div></div>
    <?php } ?>
  </body>
</html>
