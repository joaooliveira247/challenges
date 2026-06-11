use std::io;

pub fn read_data() -> String {
    let mut data = String::new();

    io::stdin().read_line(&mut data).expect("Failed read data.");

    data.trim().to_string()
}