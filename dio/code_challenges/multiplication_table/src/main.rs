use std::io;

fn main() {
    println!("Type a number:");

    let mut input = String::new();

    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read line.");

    let number: i32 = input
        .trim()
        .parse()
        .expect(format!("Expected integer got: {}", input).as_str());

    let mut results: Vec<String> = Vec::new();

    for n in 1..11 {
        results.push(format!("{} x {} = {}", number, n, n * number));
    }

    println!("{}", results.join("\n"))
}
