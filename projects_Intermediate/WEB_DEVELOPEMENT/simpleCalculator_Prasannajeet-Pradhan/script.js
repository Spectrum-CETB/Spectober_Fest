let inputs = document.getElementById('input');
 buttons = document.querySelectorAll('button');

let inputvalue = '';
for ( item of buttons) {
    item.addEventListener('click',(e) => {
       buttontext = e.target.innerText;
        if (buttontext == 'X') {
            buttontext = '*';
            inputvalue += buttontext;
            inputs.value = inputvalue;
        }
        else if (buttontext == 'C'){
inputvalue = "";
inputs.value = inputvalue;
        }
        else if (buttontext == '='){
inputs.value = eval(inputvalue);
        }else if (buttontext == '%'){
            buttontext = '/100';
            inputvalue += buttontext;
            inputs.value = inputvalue;
        }
        else{
            inputvalue += buttontext;
            inputs.value = inputvalue;
        }
    })
}