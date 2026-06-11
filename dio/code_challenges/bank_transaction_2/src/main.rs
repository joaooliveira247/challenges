use std::io;

fn main() {
    // Lê a linha de entrada do usuário
    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Erro ao ler entrada");

    // Divide a entrada em partes e remove espaços extras
    let parts: Vec<&str> = input.trim().split_whitespace().collect();

    let (account_1, account_2) = (parts[0], parts[1]);

    let value: u32 = parts[2].parse().expect("Expect Integer");

    if account_1 == account_2 || account_1.len() != account_2.len() || value < 1 {
        println!("REJEITADA")
    } else {
        println!("APROVADA")
    }

    // TODO: Verifique se as regras de validação da transferência são atendidas
    // - As contas devem ter 6 dígitos, ser diferentes e o valor deve ser inteiro positivo (>0)
    // Dica: Use métodos como len(), chars().all(), parse::<i32>() e comparações para validar.

    // Exemplo de saída (substitua pela lógica de validação):
}
