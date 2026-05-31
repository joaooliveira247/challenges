use std::io;

fn main() {
    loop {
        let options: &str = r#"
Chose an option:
1 - Language Name
2 - Current Year
3 - Country
0 - Exit
            "#;

        println!("{}", options);

        let mut user_option = String::new();

        io::stdin()
            .read_line(&mut user_option)
            .expect("Failed to read line");

        let option = user_option
            .trim()
            .parse()
            .expect(format!("Expected an integer Got: {}", user_option).as_str());

        match option {
            1 => println!("Rust"),
            2 => println!("2026"),
            3 => println!("Brasil 🇧🇷"),
            0 => break,
            _ => {
                println!("Invalid Option, try again")
            }
        }
    }
}
