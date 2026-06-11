use crate::display::{input, utils::{clear, wait}};

pub fn show_menu() {
    let menu = format!(
        "\
        {} {} {}\n\
        1 - Insert a Customer\n\
        2 - Alter a Customer\n\
        3 - Del a Customer\n\
        4 - Show Customers\n\
        0 - Exit\n\
        {}
        ",
        "=".repeat(10),
        "MENU",
        "=".repeat(10),
        "=".repeat(26)
    );
    loop {
        clear();
        println!("{}", menu);

        let option: i8 = input::read_data()
            .parse()
            .expect("Option need be a number.");
        clear();

        match option {
            1 => println!("Insert Customer."),
            2 => println!("Alter Customer."),
            3 => println!("Del Customer."),
            4 => println!("Show Customer."),
            0 => break,
            _ => println!("Invalid Option."),
        }
        wait(2);
    }
}
