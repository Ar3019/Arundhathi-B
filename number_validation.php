# Code by Arundhathi B
# php program for validating a number.

<?php

function validateNumber($minNum, $maxNum, $disabledNumbers, $userInput) {


        if ($userInput < $minNum || $userInput > $maxNum) {
            echo "Invalid input.\n";
           return;
        }

        if (in_array($userInput, $disabledNumbers)) {
            echo "$userInput is disabled number.\n";
             $userInput++;
            
          return (validateNumber($minNum, $maxNum, $disabledNumbers, $userInput));

      
        }
        return $userInput;

}

function main() {
    $minNum = intval(readline("Enter the minimum number: "));
    $maxNum = intval(readline("Enter the maximum number: "));
    $disabledNumbersInput = readline("Enter the disabled numbers separated by space: ");
    $disabledNumbers = array_map('intval', explode(' ', $disabledNumbersInput));
    $userInput = readline("Enter a number to validate: ");

    $validatedNumber = validateNumber($minNum, $maxNum, $disabledNumbers, $userInput);
    if(!is_numeric($validatedNumber)){
        echo $validatedNumber;
        return;
    }
    echo "Validated Number: $validatedNumber";
}

main();

?>
