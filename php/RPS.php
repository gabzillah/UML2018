<?php



class RPS {
  public $result;
  // an array dictionary to be able to call various keys to get the winner message
  private $engine = [
    "rock" => [
      "scissors" => "Rock crushes scissors!!!",
      "lizard" => "Rock crushes lizard!!!"
    ],
    "paper" => [
      "rock" => "Paper covers rock!!!",
      "spock" => "Paper disproves Spock!!!"
    ],
    "scissors" => [
      "paper" => "Scissors cut paper!!!",
      "lizard" => "Scissors decapiate lizard!!!"
    ],
    "lizard" => [
      "spock" => "Lizard poisons Spock!!!",
      "paper" => "Lizard eats paper!!!"
    ],
    "spock" => [
      "scissors" => "Spock smashes scissors!!!",
      "rock" => "Spock vaporizes rock!!!"
    ]
  ];

  // a private function to determine the outcome of each game played then return a specified message based on that outcome

  private function game($human, $computer) {
    if ($human == $computer) { // first check for a tie then output the result
      return "<p id='result'>{$human} against {$computer}: It's a tie! </p>";
    }

    // if the loser is computer output the winning move and specificed message
    $loser = $this->engine[$human];
    if(isset($loser[$computer])) {
      $message = $loser[$computer];
      return "<p id='result'>{$human} against {$computer}: The Human wins! {$message} </p>";
    }

    // if the loser is human then output the winning move and specificed message
    $human_loser = $this->engine[$computer];
    if(isset($human_loser[$human])) {
      $message = $human_loser[$human];
      return "<p id='result'>{$human} against {$computer}: The Borg wins! {$message} </p>";
    }

    // a check for unspecificed input -> if someone added an new option without defining it
    return "You must select rock, paper, scissors, lizard, or spock";
  }


  // a public function to take in the input from the form, randomize a computer play and then run the game fuction

  public function handle($data) {
    //var_dump($data["attack"]); <-- used to check outcome of the results
    $human = $_POST["attack"];
    $plays = array("rock", "paper", "scissors", "lizard", "spock");
    $computer = $plays[array_rand($plays)];
    $this->result = $this->game($human, $computer);


  }

}
