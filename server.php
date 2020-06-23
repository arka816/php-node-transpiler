<?php

//namespace App;

//use Illuminate\Database\Eloquent\Model;

$x = 10;

while($x >= 2&&"4" <= "5" or ($x == "#" and $x != "%")) {
  echo "The number is: $x <br>";
  $x++;
}

/*
if ($t < "20") {
  echo "Have a good day!";
} 
else {
  echo "Have a good night!";
}

switch ($favcolor) {
  case "red":
    echo "Your favorite color is red!";
    break;
  case "blue":
    echo "Your favorite color is blue!";
    break;
  case "green":
    echo "Your favorite color is green!";
    break;
  default:
    echo "Your favorite color is neither red, blue, nor green!";
}
do {
  echo "The number is: $x <br>";
  $x++;
} while ($x <= 5);

for ($x = 0; $x <= 10; $x++) {
  echo "The number is: $x <br>";
}

foreach ($colors as $value) {
  echo "$value <br>";
}

class UserGenre extends Model
{
    protected $table = 'user_genres';

    protected $guarded = ['id'];

    public function users() {
    	return $this->belongsTo('App\User');
    }

    public function genres(){
    	return $this->belongsTo('App\Genres');
    }
}
*/
