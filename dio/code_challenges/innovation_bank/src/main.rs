use std::io;

fn main() {
    // Lê uma linha da entrada padrão
    let mut input = String::new();
    if io::stdin().read_line(&mut input).is_ok() {
        let trimmed = input.trim();
        let parts: Vec<&str> = trimmed.split_whitespace().collect();

        // TODO: Se houver exatamente dois elementos, imprima a mensagem personalizada.
        // Caso contrário, imprima "Invalid input."
        if parts.len() != 2 {
            println!("Invalid input.");
            return;
        }
        println!("Welcome, {}! Your account type is {}.", parts[0], parts[1])
    }
}
