use std::io;

fn main() {
    // Lê a linha de entrada do usuário
    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Erro ao ler entrada");

    // Divide a entrada em partes e faz o parse dos valores
    let parts: Vec<&str> = input.trim().split_whitespace().collect();

    let balance: i32 = parts[0].parse().expect("Expect Integer");
    let value: i32 = parts[2].parse().expect("Expect Integer");

    // TODO: Verifique se a entrada possui exatamente 3 partes (saldo, operação, valor)
    match parts[1] {
        "deposit" => println!("{}", balance + value),
        "withdraw" => {
            if balance < value {
                println!("Insufficient funds")
            } else {
                println!("{}", balance - value)
            }
        }
        _ => println!("Operação invalida"),
    }

    // Dica: Use match para tratar as operações "deposit" e "withdraw"
    // Se for "deposit", some o valor ao saldo e imprima o resultado
    // Se for "withdraw", verifique se há saldo suficiente antes de subtrair e imprimir
    // Caso contrário, imprima "Insufficient funds"
}
