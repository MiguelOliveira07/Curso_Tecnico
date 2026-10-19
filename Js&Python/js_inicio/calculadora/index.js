const display = document.getElementById('display');
const buttonsNums = document.querySelectorAll('#div_nums button');
const buttonsOps = document.querySelectorAll('#botoes button');

let currentInput = '';
let operator = '';
let previousInput = '';

function updateDisplay(value) {
    display.value = value;
}

function calculate() {
    let result;
    const prev = parseFloat(previousInput);
    const curr = parseFloat(currentInput);

    switch(operator) {
        case '+': result = prev + curr; break;
        case '-': result = prev - curr; break;
        case '*': result = prev * curr; break;
        case '/': result = curr !== 0 ? prev / curr : 'Erro'; break;
        case '%': result = prev % curr; break;
        default: return;
    }

    currentInput = result.toString();
    operator = '';
    previousInput = '';
    updateDisplay(currentInput);
}

buttonsNums.forEach(button => {
    button.addEventListener('click', () => {
        if(button.textContent === '.' && currentInput.includes('.')) return;
        currentInput += button.textContent;
        updateDisplay(currentInput);
    });
});

buttonsOps.forEach(button => {
    button.addEventListener('click', () => {
        const value = button.textContent;

        if(value === '=') {
            if(previousInput && currentInput) calculate();
            return;
        }

        if(currentInput === '') return;

        if(previousInput) {
            calculate();
        }

        operator = value;
        previousInput = currentInput;
        currentInput = '';
    });
});

document.getElementById('clear').addEventListener('click', () => {
    currentInput = '';
    previousInput = '';
    operator = '';
    updateDisplay('');
});
