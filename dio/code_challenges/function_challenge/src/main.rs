use std::io;

fn sum(x: i32, y: i32) -> i32 {
    x + y
}

fn sub(x: i32, y: i32) -> i32 {
    x - y
}

fn multiplication_table(number: i32) -> String {
    let mut results: Vec<String> = Vec::new();

    for n in 1..11 {
        results.push(format!("{} x {} = {}", number, n, n * number));
    }

    results.join("\n")
}

fn main() {
    loop {
        println!(
            r#"
Chose an option:
1 - Sum
2 - Sub
3 - Multiplication Table
0 - Exit
            "#
        );

        let mut user_option = String::new();

        io::stdin()
            .read_line(&mut user_option)
            .expect("Failed to read line");

        let option: i32 = user_option
            .trim()
            .parse()
            .expect(format!("Expected integer got: {}", user_option).as_str());

        match option {
            1 => {
                println!("Type numbers to sum\nEx: 10 50");

                let mut user_input = String::new();

                io::stdin()
                    .read_line(&mut user_input)
                    .expect("Failed to read line");

                let mut nums = user_input.split_whitespace();

                let x: i32 = nums.next().unwrap().parse().expect("Expected integer");

                let y: i32 = nums.next().unwrap().parse().expect("Expected integer");

                println!("{}", sum(x, y))
            }
            2 => {
                println!("Type numbers to sub\nEx: 10 50");

                let mut user_input = String::new();

                io::stdin()
                    .read_line(&mut user_input)
                    .expect("Failed to read line");

                let mut nums = user_input.split_whitespace();

                let x: i32 = nums.next().unwrap().parse().expect("Expected integer");

                let y: i32 = nums.next().unwrap().parse().expect("Expected integer");

                println!("{}", sub(x, y))
            }
            3 => {
                println!("Type numbers to generate the multiplication table");

                let mut user_input = String::new();

                io::stdin()
                    .read_line(&mut user_input)
                    .expect("Failed to read line");

                let number: i32 = user_input.trim().parse().expect("Expected integer");

                println!("{}", multiplication_table(number))
            }
            0 => break,
            _ => println!("Invalid option"),
        }
    }
}
